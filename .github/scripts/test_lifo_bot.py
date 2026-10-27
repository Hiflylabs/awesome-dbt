import unittest

from lifo_bot import MARKER, find_problems, parse, report

BASE = """\
# Awesome dbt

## Contents
- [Testing](#testing)
- [Utilities](#utilities)

## Testing

Tests and checks.

- [dbt-expectations](https://github.com/calogica/dbt-expectations) - Great Expectations style tests.
- [Elementary](https://github.com/elementary-data/elementary) - Anomaly detection as dbt tests.

## Utilities

- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - SQL linter.
- dbt on AWS - A series of posts.
  - [Part 1](https://example.com/part-1)
"""


def check(head: str, base: str = BASE) -> dict[str, list]:
    return find_problems(parse(base), parse(head))


def add(after: str, line: str, base: str = BASE) -> str:
    return base.replace(after, after + line + "\n", 1)


NEW = "- [dbt-score](https://github.com/PicnicSupermarket/dbt-score) - Linter for dbt metadata."


class LifoTest(unittest.TestCase):
    def test_unchanged_readme_passes(self):
        self.assertFalse(any(check(BASE).values()))

    def test_new_entry_on_top_passes(self):
        head = add("Tests and checks.\n\n", NEW)
        self.assertFalse(any(check(head).values()))

    def test_several_new_entries_on_top_pass(self):
        head = add("Tests and checks.\n\n", NEW + "\n" + NEW.replace("dbt-score", "dbt-bouncer"))
        self.assertFalse(any(check(head).values()))

    def test_new_entry_at_the_bottom_is_misplaced(self):
        head = add("Anomaly detection as dbt tests.\n", NEW)
        misplaced = check(head)["misplaced"]
        self.assertEqual(len(misplaced), 1)
        new, first = misplaced[0]
        self.assertEqual(new.name, "dbt-score")
        self.assertEqual(first.name, "dbt-expectations")

    def test_new_entry_in_the_middle_is_misplaced(self):
        head = add("Great Expectations style tests.\n", NEW)
        self.assertEqual(len(check(head)["misplaced"]), 1)

    def test_moving_an_existing_entry_is_not_an_addition(self):
        elementary = "- [Elementary](https://github.com/elementary-data/elementary) - Anomaly detection as dbt tests.\n"
        head = add("- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - SQL linter.\n", elementary, BASE.replace(elementary, ""))
        self.assertFalse(any(check(head).values()))

    def test_fixing_a_link_or_description_is_not_an_addition(self):
        head = BASE.replace("calogica/dbt-expectations) - Great", "metaplane/dbt-expectations) - Maintained fork of Great")
        self.assertFalse(any(check(head).values()))

    def test_swapping_a_dead_entry_for_its_successor_is_an_edit(self):
        head = BASE.replace(
            "- [Elementary](https://github.com/elementary-data/elementary) - Anomaly detection as dbt tests.",
            "- [Sentinel](https://github.com/example/sentinel) - Successor of a dead project.",
        )
        self.assertFalse(any(check(head).values()))

    def test_a_swap_does_not_hide_an_addition_elsewhere(self):
        head = BASE.replace(
            "- [Elementary](https://github.com/elementary-data/elementary) - Anomaly detection as dbt tests.",
            "- [Sentinel](https://github.com/example/sentinel) - Successor of a dead project.",
        )
        head = add("- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - SQL linter.\n", NEW, head)
        self.assertEqual([new.name for new, _ in check(head)["misplaced"]], ["dbt-score"])

    def test_new_section_passes(self):
        head = BASE + "\n## AI\n\n" + NEW + "\n"
        self.assertFalse(any(check(head).values()))

    def test_sections_with_the_same_title_are_separate(self):
        base = "## A\n### Tools\n- [x](https://x.io) - X.\n## B\n### Tools\n- [y](https://y.io) - Y.\n"
        head = base.replace("### Tools\n- [y]", "### Tools\n- [z](https://z.io) - Z.\n- [y]")
        self.assertFalse(any(check(head, base).values()))

    def test_table_of_contents_and_nested_items_are_ignored(self):
        head = BASE.replace("- [Utilities](#utilities)\n", "- [Utilities](#utilities)\n- [AI](#ai)\n")
        head = head.replace("  - [Part 1](https://example.com/part-1)\n", "  - [Part 1](https://example.com/part-1)\n  - [Part 2](https://example.com/part-2)\n")
        self.assertFalse(any(check(head).values()))

    def test_duplicate_of_an_existing_entry_is_reported(self):
        head = add("## Utilities\n\n", "- [Elementary](https://github.com/elementary-data/elementary/) - Again.")
        duplicates = check(head)["duplicates"]
        self.assertEqual(len(duplicates), 1)
        self.assertEqual({e.section for e in duplicates[0]}, {"Testing", "Utilities"})

    def test_existing_duplicates_are_not_blamed_on_the_pr(self):
        base = add("## Utilities\n\n", "- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - Again.")
        self.assertFalse(any(check(base, base).values()))

    def test_format_issues_of_new_entries(self):
        cases = {
            "- [a](https://a.io) Missing dash.": "` - `",
            "- [b](https://b.io) - No period": "period",
            "- [c](www.c.io) - Relative link.": "https://",
            "- Plain text entry.": "start the entry with a link",
        }
        for line, expected in cases.items():
            with self.subTest(line=line):
                issues = check(add("Tests and checks.\n\n", line))["format"]
                self.assertEqual(len(issues), 1)
                self.assertIn(expected, issues[0][1])


class ReportTest(unittest.TestCase):
    def test_report_starts_with_the_marker(self):
        self.assertTrue(report(check(BASE)).startswith(MARKER))
        self.assertIn("✅", report(check(BASE)))

    def test_report_explains_where_to_move_the_entry(self):
        text = report(check(add("Anomaly detection as dbt tests.\n", NEW)))
        self.assertIn("`dbt-score`", text)
        self.assertIn("`dbt-expectations`", text)
        self.assertIn("+ - [dbt-score]", text)

    def test_untrusted_text_cannot_ping_or_break_out(self):
        evil = "- [@everyone `x` | y](https://evil.io) - ```\nboom."
        text = report(check(add("Anomaly detection as dbt tests.\n", evil)))
        self.assertIn("`@everyone 'x' \\| y`", text)
        self.assertNotIn("```\nboom", text)


if __name__ == "__main__":
    unittest.main()
