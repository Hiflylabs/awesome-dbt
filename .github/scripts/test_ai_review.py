import json
import os
import tempfile
import unittest
from pathlib import Path

from unittest import mock

from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart
from pydantic_ai.models.function import AgentInfo, FunctionModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

import ai_review

BASE = """\
# Awesome dbt

## Contents

- [Testing](#testing)

## Testing & Data Quality

Test your models.

### Testing

- [dbt-expectations](https://github.com/metaplane/dbt-expectations) - Great Expectations-style tests.

### Data Observability

- [Elementary](https://github.com/elementary-data/elementary) - Data observability for dbt.

## CI/CD

- [dbt-ci-cd](https://github.com/bruno-szdl/dbt-ci-cd) - Example CI/CD setup.

## Contributors

- [Someone](https://github.com/someone)
"""

NEW_LINE = "- [New Tool](https://example.com/new-tool) - Checks dbt models in CI."


def with_new_entry(markdown: str, after: str, line: str = NEW_LINE) -> str:
    return markdown.replace(after, after + "\n" + line, 1)


def verdict(**overrides) -> dict:
    answer = {
        "summary": "A CI checker for dbt.",
        "dbt_reason": "It parses manifest.json.",
        "dbt_related": "yes",
        "section_reason": "It runs in CI.",
        "best_section": "CI/CD",
        "description_ok": True,
        "suggested_description": "",
        "flags": [],
    }
    return answer | overrides


def model_answering(answer: dict, seen: list | None = None) -> FunctionModel:
    """A fake model that records what it was sent and answers with `answer`."""

    def respond(messages, info: AgentInfo) -> ModelResponse:
        if seen is not None:
            seen.append((messages, info))
        if info.output_tools:  # tool output, the default
            return ModelResponse(parts=[ToolCallPart(info.output_tools[0].name, answer)])
        return ModelResponse(parts=[TextPart(json.dumps(answer))])

    return FunctionModel(respond)


def no_fetch(url):
    return "Title: New Tool"


class SectionTests(unittest.TestCase):
    def test_sections_are_leaves_in_readme_order(self):
        self.assertEqual(ai_review.sections(BASE), ["Testing & Data Quality > Testing", "Testing & Data Quality > Data Observability", "CI/CD"])

    def test_section_of_a_line(self):
        head = with_new_entry(BASE, "## CI/CD\n")
        line = head.splitlines().index(NEW_LINE) + 1
        self.assertEqual(ai_review.section_of(head, line), "CI/CD")
        line = head.splitlines().index("- [Elementary](https://github.com/elementary-data/elementary) - Data observability for dbt.") + 1
        self.assertEqual(ai_review.section_of(head, line), "Testing & Data Quality > Data Observability")


class NewEntryTests(unittest.TestCase):
    def names(self, head: str) -> list[str]:
        return [e.name for e in ai_review.new_entries(BASE, head)]

    def test_new_link(self):
        self.assertEqual(self.names(with_new_entry(BASE, "## CI/CD\n")), ["New Tool"])

    def test_moved_or_edited_entries_are_not_new(self):
        moved = BASE.replace("- [dbt-ci-cd](https://github.com/bruno-szdl/dbt-ci-cd) - Example CI/CD setup.\n", "")
        moved = moved.replace("### Testing\n", "### Testing\n\n- [dbt-ci-cd](https://github.com/bruno-szdl/dbt-ci-cd) - Reworded.\n")
        self.assertEqual(self.names(moved), [])

    def test_link_swapped_in_place_is_new(self):
        swapped = BASE.replace("https://github.com/bruno-szdl/dbt-ci-cd", "https://github.com/someone/successor")
        self.assertEqual(self.names(swapped), ["dbt-ci-cd"])


class ReviewTests(unittest.TestCase):
    def run_review(self, answer: dict, head: str | None = None, seen: list | None = None):
        head = head or with_new_entry(BASE, "## CI/CD\n")
        return ai_review.review(BASE, head, "Guidelines.", model_answering(answer, seen), pr_body="I built this.", pr_author="octocat", fetch=no_fetch, log=lambda _: None)

    def test_clean_entry(self):
        [item] = self.run_review(verdict())
        self.assertEqual(item.section, "CI/CD")
        self.assertFalse(item.needs_look)
        text = ai_review.report([item])
        self.assertIn("✅ The new entry follows the [contribution guidelines]", text)
        self.assertIn("<details><summary>New Tool</summary>", text)
        self.assertIn("- **Section:** fits CI/CD. It runs in CI.", text)

    def test_prompt_and_schema(self):
        seen = []
        self.run_review(verdict(), seen=seen)
        messages, info = seen[0]
        sent = str(messages)
        for expected in (NEW_LINE[2:], "<current_section>CI/CD</current_section>", 'author="octocat"', "I built this.", "Title: New Tool"):
            self.assertIn(expected, sent)
        self.assertIn("<readme>", info.instructions)
        schema = json.dumps(info.output_tools[0].parameters_json_schema)
        for section in ai_review.sections(BASE):
            self.assertIn(section, schema)
        for reason in ai_review.OFF_TOPIC:
            self.assertIn(reason, schema)
            self.assertIn(reason, info.instructions)

    def test_reasoning_effort(self):
        sections = ai_review.sections(BASE)
        thinking_model = FunctionModel(lambda m, i: None, profile={"supports_thinking": True})
        self.assertEqual(ai_review.make_agent(thinking_model, sections, "").model_settings, {"thinking": "low"})
        # OpenAI-compatible endpoints such as LiteLLM get it as reasoning_effort.
        gpt_oss = OpenAIChatModel("gpt-oss-120b", provider=OpenAIProvider(base_url="http://litellm.invalid/v1", api_key="x"))
        self.assertEqual(ai_review.make_agent(gpt_oss, sections, "").model_settings, {"openai_reasoning_effort": "low"})
        with mock.patch.dict(os.environ, {"AI_REVIEW_THINKING": ""}):
            self.assertIsNone(ai_review.make_agent(gpt_oss, sections, "").model_settings)

    def test_native_output(self):
        seen = []
        with mock.patch.dict(os.environ, {"AI_REVIEW_OUTPUT": "native"}):
            [item] = self.run_review(verdict(), seen=seen)
        self.assertFalse(item.needs_look)
        info = seen[0][1]
        self.assertEqual(info.output_tools, [])
        self.assertIn("CI/CD", json.dumps(info.model_request_parameters.output_object.json_schema))

    def test_answer_outside_the_schema_is_reported_not_raised(self):
        [item] = self.run_review(verdict(best_section="Not a section"))
        self.assertTrue(item.needs_look)
        self.assertIn("review unavailable", ai_review.report([item]))

    def test_needs_look(self):
        for overrides in ({"dbt_related": "unclear"}, {"best_section": "Testing & Data Quality > Testing"}, {"description_ok": False}, {"flags": [{"kind": "marketing_language", "evidence": "best ever"}]}):
            with self.subTest(overrides=overrides):
                [item] = self.run_review(verdict(**overrides))
                self.assertTrue(item.needs_look)


class ReportTests(unittest.TestCase):
    def review_of(self, **overrides) -> ai_review.Review:
        entry = ai_review.new_entries(BASE, with_new_entry(BASE, "## CI/CD\n"))[0]
        return ai_review.Review(entry, "CI/CD", verdict(**overrides))

    def test_report_explains_the_flags(self):
        text = ai_review.report(
            [
                self.review_of(
                    dbt_related="unclear",
                    best_section="Testing & Data Quality > Testing",
                    description_ok=False,
                    suggested_description="Runs dbt tests in CI.",
                    flags=[{"kind": "undisclosed_affiliation", "evidence": "The author owns the repository."}],
                )
            ],
            "bedrock:eu.anthropic.claude-haiku-5-5",
        )
        self.assertTrue(text.startswith(ai_review.MARKER))
        for expected in ("❔ unclear", "➡️ Testing & Data Quality \\> Testing", "✏️ rewrite", "Looks affiliated, not disclosed", "`Runs dbt tests in CI.`", "### 🤖 Review bot", "Automatic review of the new entries against the [contribution guidelines](https://github.com/", "<sub>Model: `eu.anthropic.claude-haiku-5-5`</sub>"):
            self.assertIn(expected, text)

    def test_off_topic_entry_gets_no_section_or_description_verdict(self):
        text = ai_review.report([self.review_of(dbt_related="no_dbt_integration", dbt_reason="A generic database.", description_ok=False, suggested_description="A database.", flags=[{"kind": "marketing_language", "evidence": "the best choice ever!"}])])
        self.assertIn("| `New Tool` | ❌ no | – | – | No dbt integration, Marketing language |", text)
        self.assertIn("- **No dbt integration:** A generic database.", text)
        for unexpected in ("**About dbt:**", "**Section:**", "**Suggested description:**", "**Description:**"):
            self.assertNotIn(unexpected, text)

    def test_every_entry_gets_details(self):
        clean, flagged = self.review_of(), self.review_of(dbt_related="unclear")
        text = ai_review.report([clean, flagged])
        self.assertEqual(text.count("<details><summary>New Tool</summary>"), 2)
        self.assertIn("- **About dbt:** yes. It parses manifest.json.", text)

    def test_model_text_cannot_mention_link_or_inject_markup(self):
        injected = "Ping @octocat, see [this](https://evil.example) <img src=x> | ``` `"
        text = ai_review.report([self.review_of(dbt_related="unclear", dbt_reason=injected, flags=[{"kind": "other", "evidence": injected}])])
        self.assertNotIn("@octocat", text)
        self.assertNotIn("https://evil.example", text)
        self.assertNotRegex(text, r"(?<!\\)<img")  # an escaped \<img renders as text
        self.assertNotIn("```", text)

    def test_unavailable_review(self):
        entry = self.review_of().entry
        text = ai_review.report([ai_review.Review(entry, "CI/CD", error="ModelHTTPError: status_code: 403")])
        self.assertIn("review unavailable", text)
        self.assertIn("AI review unavailable: ModelHTTPError", text)


class EnvironmentTests(unittest.TestCase):
    def test_env_file_does_not_override_and_empty_secrets_are_dropped(self):
        names = ("AI_REVIEW_TEST_A", "AI_REVIEW_TEST_B", "ANTHROPIC_API_KEY")
        saved = {name: os.environ.get(name) for name in names}
        try:
            os.environ["AI_REVIEW_TEST_A"] = "from-environment"
            os.environ["ANTHROPIC_API_KEY"] = ""
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / ".env"
                path.write_text("# comment\nAI_REVIEW_TEST_A=from-file\nAI_REVIEW_TEST_B='quoted'\n", encoding="utf-8")
                ai_review.load_env(path)
            self.assertEqual(os.environ["AI_REVIEW_TEST_A"], "from-environment")
            self.assertEqual(os.environ["AI_REVIEW_TEST_B"], "quoted")
            ai_review.prepare_environment()
            self.assertNotIn("ANTHROPIC_API_KEY", os.environ)
        finally:
            for name, value in saved.items():
                if value is None:
                    os.environ.pop(name, None)
                else:
                    os.environ[name] = value


class ModelNameTests(unittest.TestCase):
    def test_provider_prefix(self):
        for name in ("bedrock:openai.gpt-oss-120b-1:0", "openai-chat:gpt-oss-120b", "anthropic:claude-haiku-5-5"):
            self.assertTrue(ai_review.PROVIDER_PREFIX.match(name), name)
        for name in ("openai.gpt-oss-120b-1:0", "gpt-oss-120b"):  # LiteLLM names: sent to OPENAI_BASE_URL
            self.assertFalse(ai_review.PROVIDER_PREFIX.match(name), name)


class FetchTests(unittest.TestCase):
    def test_github_repository_urls(self):
        match = ai_review.GITHUB_REPO.match
        self.assertEqual(match("https://github.com/dbt-labs/dbt-mcp/tree/main").groups(), ("dbt-labs", "dbt-mcp"))
        self.assertEqual(match("https://github.com/owner/repo.git").groups(), ("owner", "repo"))
        self.assertIsNone(match("https://gist.github.com/owner/abc"))

    def test_page_text(self):
        title, description, text = ai_review.page_text(
            '<html><head><title>Cube &amp; dbt</title><meta name="description" content="Sync dbt models."><style>x{}</style></head>'
            "<body><script>alert(1)</script><p>Every dbt model becomes a cube.</p></body></html>"
        )
        self.assertEqual((title, description), ("Cube & dbt", "Sync dbt models."))
        self.assertEqual(text, "Cube & dbt Every dbt model becomes a cube.")

    def test_non_http_links_are_not_fetched(self):
        self.assertEqual(ai_review.fetch_resource("ftp://example.com"), "No fetchable link.")


if __name__ == "__main__":
    unittest.main()
