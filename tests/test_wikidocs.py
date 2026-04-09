"""Tests for the wiki documentation scraper."""

import json
from pathlib import Path

from pyresonitelink.cli.wikidocs import parse_wikitext

_FIXTURES_DIR = Path(__file__).parent / "wiki_fixtures"


def _load_fixture(name: str) -> tuple[str, dict]:
    """Load a wikitext fixture and its expected output.

    Args:
        name: Fixture base name (e.g. "impulse_display").

    Returns:
        Tuple of (raw wikitext, expected parsed dict).
    """
    wikitext_path = _FIXTURES_DIR / f"{name}.wikitext"
    expected_path = _FIXTURES_DIR / f"{name}_expected.json"
    wikitext = wikitext_path.read_text(encoding="utf-8")
    with open(expected_path, encoding="utf-8") as f:
        expected = json.load(f)
    return wikitext, expected


class TestParseImpulseDisplay:
    """Tests for parsing the ImpulseDisplay ProtoFlux node wiki page."""

    def test_description(self) -> None:
        wikitext, expected = _load_fixture("impulse_display")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]

    def test_description_includes_bullet_list(self) -> None:
        wikitext, _ = _load_fixture("impulse_display")
        result = parse_wikitext(wikitext)
        assert "- The User that owns the impulse" in result["description"]
        assert "  - Indices are only tracked" in result["description"]

    def test_description_includes_full_text(self) -> None:
        wikitext, _ = _load_fixture("impulse_display")
        result = parse_wikitext(wikitext)
        assert "ProtoFlux Tool" in result["description"]
        assert result["description"].endswith("pressing secondary.")

    def test_no_wiki_markup_in_description(self) -> None:
        wikitext, _ = _load_fixture("impulse_display")
        result = parse_wikitext(wikitext)
        assert "'''" not in result["description"]
        assert "''" not in result["description"]
        assert "[[" not in result["description"]
        assert "]]" not in result["description"]
        assert "Category:" not in result["description"]

    def test_no_fields(self) -> None:
        wikitext, expected = _load_fixture("impulse_display")
        result = parse_wikitext(wikitext)
        assert result["fields"] == expected["fields"]

    def test_no_methods(self) -> None:
        wikitext, expected = _load_fixture("impulse_display")
        result = parse_wikitext(wikitext)
        assert result["methods"] == expected["methods"]


class TestParseAudioOutput:
    """Tests for parsing the AudioOutput component wiki page."""

    def test_description(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]

    def test_category(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["category"] == expected["category"]

    def test_field_count(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert len(result["fields"]) == len(expected["fields"])

    def test_field_volume(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["fields"]["Volume"] == expected["fields"]["Volume"]

    def test_field_source(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["fields"]["Source"] == expected["fields"]["Source"]

    def test_field_excluded_users(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["fields"]["excludedUsers"] == expected["fields"]["excludedUsers"]

    def test_all_fields_match(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["fields"] == expected["fields"]

    def test_method_count(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert len(result["methods"]) == len(expected["methods"])

    def test_method_exlude_user(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["methods"]["ExludeUser"] == expected["methods"]["ExludeUser"]

    def test_all_methods_match(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["methods"] == expected["methods"]

    def test_usage(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert result["usage"] == expected["usage"]

    def test_notes(self) -> None:
        wikitext, expected = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        assert len(result["notes"]) == len(expected["notes"])
        assert result["notes"][0]["title"] == expected["notes"][0]["title"]
        assert result["notes"][0]["text"] == expected["notes"][0]["text"]

    def test_no_wiki_markup_in_fields(self) -> None:
        wikitext, _ = _load_fixture("audio_output")
        result = parse_wikitext(wikitext)
        for value in result["fields"].values():
            assert "[[" not in value
            assert "]]" not in value
            assert "{{" not in value
            assert "}}" not in value


class TestParseValueField:
    """Tests for parsing the ValueField component wiki page.

    Covers: <translate> tags, <!--T:--> comments, bold type in field,
    generic component with usage section.
    """

    def test_description(self) -> None:
        wikitext, expected = _load_fixture("value_field")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]

    def test_no_translate_tags_in_description(self) -> None:
        wikitext, _ = _load_fixture("value_field")
        result = parse_wikitext(wikitext)
        assert "<translate" not in result["description"]
        assert "<!--T:" not in result["description"]

    def test_field_value(self) -> None:
        wikitext, expected = _load_fixture("value_field")
        result = parse_wikitext(wikitext)
        assert result["fields"] == expected["fields"]

    def test_usage(self) -> None:
        wikitext, expected = _load_fixture("value_field")
        result = parse_wikitext(wikitext)
        assert result["usage"] == expected["usage"]

    def test_category(self) -> None:
        wikitext, expected = _load_fixture("value_field")
        result = parse_wikitext(wikitext)
        assert result["category"] == expected["category"]


class TestParseWrite:
    """Tests for parsing the Write ProtoFlux node wiki page.

    Covers: {{#Invoke:ProtoFlux|GenerateUI}} multi-line template,
    multiple == sections for inputs/outputs/globals.
    """

    def test_description_skips_template_content(self) -> None:
        wikitext, expected = _load_fixture("write")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]
        # Should NOT contain JSON from the GenerateUI template
        assert '{"Name"' not in result["description"]
        assert "|Outputs=" not in result["description"]

    def test_description_starts_with_body_text(self) -> None:
        wikitext, _ = _load_fixture("write")
        result = parse_wikitext(wikitext)
        assert result["description"].startswith("Writes take Variable")

    def test_notes_include_optimizations(self) -> None:
        wikitext, expected = _load_fixture("write")
        result = parse_wikitext(wikitext)
        titles = [n["title"] for n in result["notes"]]
        assert any("Optimizations" in t for t in titles)


class TestParseLocal:
    """Tests for parsing the Local ProtoFlux node wiki page.

    Covers: stub page with body text after {{Stub}} template,
    SHORTDESC not preferred when body exists.
    """

    def test_description_includes_body_text(self) -> None:
        wikitext, expected = _load_fixture("local")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]
        assert "Local Nodes will have the default value" in result["description"]

    def test_description_not_just_shortdesc(self) -> None:
        wikitext, _ = _load_fixture("local")
        result = parse_wikitext(wikitext)
        # Should have more than just the SHORTDESC
        assert len(result["description"]) > 200

    def test_notes_include_scoped_variables(self) -> None:
        wikitext, expected = _load_fixture("local")
        result = parse_wikitext(wikitext)
        titles = [n["title"] for n in result["notes"]]
        assert any("Scoped Variables" in t for t in titles)


class TestSyntheticDefensive:
    """Tests using synthetic wikitext to exercise defensive code paths.

    These are fake documents specifically designed to test edge cases
    that don't occur in well-formed wiki pages but are handled
    defensively in the parser.
    """

    def test_shortdesc_fallback_when_no_body(self) -> None:
        """SHORTDESC is used when there is no body text before == heading."""
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]

    def test_non_pipe_line_skipped_in_fields(self) -> None:
        """Lines not starting with | in the fields block are skipped."""
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        assert "FieldA" in result["fields"]
        # The "This line does not start with |" is skipped

    def test_too_few_parts_skipped_in_fields(self) -> None:
        """Field lines with <4 pipe-separated parts are skipped."""
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        # |B|Int has only 3 parts — should be skipped
        assert "B" not in result["fields"]

    def test_template_placeholder_in_type_column(self) -> None:
        """Fields with {{RootFieldType}} get __TPL__ in type column."""
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        assert result["fields"]["FieldD"] == expected["fields"]["FieldD"]
        assert "__TPL__" not in result["fields"]["FieldD"]

    def test_non_pipe_line_skipped_in_triggers(self) -> None:
        """Lines not starting with | in the triggers block are skipped."""
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        assert "MethodA" in result["methods"]

    def test_too_few_parts_skipped_in_triggers(self) -> None:
        """Trigger lines with <5 pipe-separated parts are skipped."""
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        # |Too|Few|Parts has only 4 parts — should be skipped
        assert "Too" not in result["methods"]

    def test_all_fields_match(self) -> None:
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        assert result["fields"] == expected["fields"]

    def test_all_methods_match(self) -> None:
        wikitext, expected = _load_fixture("synthetic_defensive")
        result = parse_wikitext(wikitext)
        assert result["methods"] == expected["methods"]


class TestSyntheticShortDescOnly:
    """Tests using a synthetic page that has only SHORTDESC and no body."""

    def test_shortdesc_used_as_description(self) -> None:
        wikitext, expected = _load_fixture("synthetic_shortdesc_only")
        result = parse_wikitext(wikitext)
        assert result["description"] == expected["description"]

    def test_fields_still_parsed(self) -> None:
        wikitext, expected = _load_fixture("synthetic_shortdesc_only")
        result = parse_wikitext(wikitext)
        assert result["fields"] == expected["fields"]


class TestStripTemplatesDefensive:
    """Test _strip_templates with malformed input."""

    def test_unclosed_template_does_not_loop(self) -> None:
        """Malformed unclosed {{ should not cause infinite loop."""
        from pyresonitelink.cli.wikidocs import _strip_templates
        result = _strip_templates("normal {{unclosed text")
        assert "{{unclosed" in result  # left as-is


class TestDefensiveGuards:
    """Synthetic inputs that exercise every defensive guard in parse_wikitext.

    These are crafted strings, not real wiki pages.
    """

    def test_stray_closing_braces_before_body(self) -> None:
        """Stray }} before body text should not crash."""
        wikitext = (
            "{{SHORTDESC:test}}\n"
            "}}\n"
            "}}\n"
            "Body text after stray braces.\n"
            "== Section ==\n"
        )
        result = parse_wikitext(wikitext)
        assert result["description"] == "Body text after stray braces."

    def test_malformed_template_in_fields_block(self) -> None:
        """Template with inner braces that regex can't strip.

        {{a{b}} contains a bare { inside, which [^{}]* won't match,
        so the iterative stripping gets stuck and breaks. The brace-depth
        parser sees {{ and }} balancing at the outer level, so the field
        text is extracted — but the inner stripping can't resolve it.
        """
        wikitext = (
            "== Fields ==\n"
            "{{Table ComponentFields\n"
            "|Good|Int| A good field.\n"
            "|Bad|Int| Has {{a{b}} in description.\n"
            "}}\n"
        )
        result = parse_wikitext(wikitext)
        assert "Good" in result["fields"]

    def test_template_placeholder_in_description_parts(self) -> None:
        """__TPL__ in description position (part 3+) is skipped."""
        wikitext = (
            "== Fields ==\n"
            "{{Table ComponentFields\n"
            "|MyField|Int|{{SomeTemplate}}| The real description.\n"
            "}}\n"
        )
        result = parse_wikitext(wikitext)
        assert result["fields"]["MyField"] == "The real description."

    def test_nested_template_in_triggers_block(self) -> None:
        """Nested {{...}} inside triggers block is handled correctly."""
        wikitext = (
            "== Sync Delegates ==\n"
            "{{Table ComponentTriggers\n"
            "|Method:{{Type|Action}}|{{Type|Action}}|false| Does something.\n"
            "}}\n"
        )
        result = parse_wikitext(wikitext)
        assert result["methods"]["Method"] == "Does something."
