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
