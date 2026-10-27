#!/usr/bin/env python3
"""LIFO bot: check that a pull request adds new entries at the top of their section.

The README asks contributors to add new entries on the top of their section (LIFO), so
the freshest resources stay visible. This script compares the README before and after a
pull request and reports:

- new entries placed below an existing entry of the same section,
- entries that are already listed elsewhere,
- new entries that don't follow the `- [Name](https://link) - Description.` format.

Usage:
    python3 lifo_bot.py BASE_README HEAD_README

Prints a Markdown report (used as the PR comment) and exits with 1 when it finds
problems, 0 otherwise. Standard library only, so it runs on a bare runner.
"""

import os
import re
import sys
from collections import Counter
from dataclasses import dataclass

MARKER = "<!-- lifo-bot -->"
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
ITEM = re.compile(r"^[-*+]\s+(.*\S)\s*$")  # top-level only: nested items belong to their parent
LINK = re.compile(r"^\[([^\]]+)\]\(\s*([^)\s]+)\s*\)")
ENDS_WITH_PUNCTUATION = (".", "!", "?", "…")


@dataclass
class Entry:
    section: str
    section_id: int
    line: int
    text: str
    name: str | None = None
    url: str | None = None

    @property
    def keys(self) -> set[str]:
        """Identities that mark this entry as already listed: its URL, name and raw text.

        Matching on any of them means editing a description, fixing a link or moving an
        entry to another section doesn't count as adding a new one.
        """
        keys = {"text:" + self.text.lower()}
        if self.url:
            keys.add("url:" + normalize_url(self.url))
        if self.name:
            keys.add("name:" + self.name.strip().lower())
        return keys


def normalize_url(url: str) -> str:
    url = url.strip().lower().split("#", 1)[0]
    url = re.sub(r"^https?://(www\.)?", "", url)
    return url.rstrip("/")


def parse(markdown: str) -> list[Entry]:
    """Return the top-level list entries of a README, skipping the table of contents."""
    entries = []
    section, section_id, in_code = "", 0, False
    for number, line in enumerate(markdown.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        heading = HEADING.match(line)
        if heading:
            section, section_id = heading.group(2), section_id + 1
            continue
        item = ITEM.match(line)
        if not item:
            continue
        text = item.group(1)
        link = LINK.match(text)
        name, url = link.groups() if link else (None, None)
        if url and url.startswith("#"):
            continue  # table of contents
        entries.append(Entry(section, section_id, number, text, name, url))
    return entries


def find_problems(base: list[Entry], head: list[Entry]) -> dict[str, list]:
    base_keys = set().union(*(entry.keys for entry in base))
    added = [entry for entry in head if not entry.keys & base_keys]
    added_lines = {entry.line for entry in added}

    misplaced = []
    first_existing: dict[int, Entry] = {}
    for entry in head:
        if entry.line not in added_lines:
            first_existing.setdefault(entry.section_id, entry)
        elif entry.section_id in first_existing:
            misplaced.append((entry, first_existing[entry.section_id]))

    base_urls = Counter(normalize_url(e.url) for e in base if e.url)
    head_urls = Counter(normalize_url(e.url) for e in head if e.url)
    duplicates = []
    for url, count in head_urls.items():
        if count > 1 and count > base_urls[url]:
            duplicates.append([e for e in head if e.url and normalize_url(e.url) == url])

    badly_formatted = [(entry, issue) for entry in added if (issue := format_issue(entry))]
    return {"misplaced": misplaced, "duplicates": duplicates, "format": badly_formatted}


def format_issue(entry: Entry) -> str | None:
    if not entry.url:
        return "start the entry with a link: `- [Name](https://link) - Description.`"
    if not entry.url.startswith(("https://", "http://")):
        return "use a full `https://` link"
    description = entry.text[LINK.match(entry.text).end():]
    if not description.startswith(" - ") or not description[3:].strip():
        return "separate the link and the description with ` - `"
    if not description.endswith(ENDS_WITH_PUNCTUATION):
        return "end the description with a period"
    return None


def code(text: str | None, limit: int = 80) -> str:
    """Render untrusted README text inertly: inline code can't mention anyone or inject markup."""
    text = re.sub(r"\s+", " ", text or "").replace("`", "'").replace("|", "\\|")
    return f"`{text[:limit] + '…' if len(text) > limit else text}`"


def label(entry: Entry) -> str:
    return code(entry.name or entry.text)


def section_name(entry: Entry) -> str:
    return re.sub(r"[^\w &/.,+'-]", "", entry.section).strip() or "(top of the file)"


def suggestion(misplaced: list[tuple[Entry, Entry]]) -> str:
    """A paste-ready view of where the misplaced entries belong."""
    by_section: dict[int, list[tuple[Entry, Entry]]] = {}
    for new, first in misplaced:
        by_section.setdefault(new.section_id, []).append((new, first))
    blocks = []
    for pairs in by_section.values():
        lines = [f"## {section_name(pairs[0][0])}", ""]
        lines += [f"+ - {new.text}" for new, _ in pairs]
        lines += [f"  - {pairs[0][1].text}", "  ..."]
        blocks.append("\n".join(re.sub("`{3,}", "``", line) for line in lines))
    return "````diff\n" + "\n\n".join(blocks) + "\n````"


def report(problems: dict[str, list]) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "Hiflylabs/awesome-dbt")
    guidelines = f"https://github.com/{repo}/blob/main/contributing.md"
    out = [MARKER, "### 🤖 LIFO bot", ""]

    if not any(problems.values()):
        out.append("✅ All new entries are at the top of their sections. Thanks for contributing!")
        return "\n".join(out) + "\n"

    out += ["Thanks for contributing to Awesome dbt! A few things need a fix before this can be merged.", ""]

    if problems["misplaced"]:
        out += [
            "**New entries go at the top of their section (LIFO)**, so the freshest resources stay visible.",
            "",
            "| Entry | Section | Move it above |",
            "| --- | --- | --- |",
        ]
        out += [
            f"| {label(new)} (line {new.line}) | {section_name(new)} | {label(first)} (line {first.line}) |"
            for new, first in problems["misplaced"]
        ]
        out += ["", "<details><summary>Where it should go</summary>", "", suggestion(problems["misplaced"]), "", "</details>", ""]

    if problems["duplicates"]:
        out += ["**Already listed**", ""]
        for entries in problems["duplicates"]:
            where = ", ".join(f"{section_name(e)} (line {e.line})" for e in entries)
            out.append(f"- {label(entries[0])} appears {len(entries)} times: {where}. Keep one.")
        out.append("")

    if problems["format"]:
        out += ["**Format**: entries look like `- [Name](https://link) - Description.`", ""]
        out += [f"- {label(entry)} (line {entry.line}): {issue}." for entry, issue in problems["format"]]
        out.append("")

    out.append(f"Push a fix to this branch and I'll check again. See the [contribution guidelines]({guidelines}).")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as base, open(argv[2], encoding="utf-8") as head:
        problems = find_problems(parse(base.read()), parse(head.read()))
    print(report(problems), end="")
    return 1 if any(problems.values()) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
