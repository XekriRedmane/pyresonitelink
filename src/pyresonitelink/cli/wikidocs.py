"""Fetch and parse component documentation from the Resonite wiki.

Fetches raw wikitext from wiki.resonite.com, parses it into
structured documentation, and saves it as a JSON file that the
code generator can merge into generated component docstrings.

Usage:
    python -m pyresonitelink.cli.wikidocs <component_name> [--output-dir DIR]

Example:
    python -m pyresonitelink.cli.wikidocs AudioOutput
    python -m pyresonitelink.cli.wikidocs AudioClipPlayer
"""

import argparse
import json
import re
from pathlib import Path
from urllib import request


_WIKI_RAW_URL = (
    "https://wiki.resonite.com/index.php"
    "?title=Component:{name}&action=raw"
)

_DOCS_DIR = (
    Path(__file__).resolve().parent.parent / "scraped_docs"
)


def _strip_wiki_links(text: str) -> str:
    """Remove wikitext link markup, keeping display text.

    ``[[Foo (Bar)|Baz]]`` → ``Baz``.
    ``[[Foo|Bar]]`` → ``Bar``.
    ``[[Foo]]`` → ``Foo``.
    ``[[#Section|Display]]`` → ``Display``.
    ``[[Type:User|User]]`` → ``User``.
    """
    # [[Page|Display]] → Display (handles [[#anchor|text]] too)
    text = re.sub(r"\[\[[^|\]]*\|([^\]]+)\]\]", r"\1", text)
    # [[Page]] → Page, but strip namespace prefixes like Type:
    text = re.sub(
        r"\[\[(?:[A-Za-z]+:)?([^\]]+)\]\]", r"\1", text,
    )
    # Strip external links [url text]
    text = re.sub(r"\[https?://\S+\s+([^\]]+)\]", r"\1", text)
    return text.strip()


def _strip_templates(text: str) -> str:
    """Remove wikitext template calls like {{...}}.

    Handles nested templates by stripping innermost first.
    """
    # Iteratively strip innermost {{ }} until none remain
    while "{{" in text:
        new = re.sub(r"\{\{[^{}]*\}\}", "", text)
        if new == text:
            break  # avoid infinite loop on malformed input
        text = new
    return text.strip()


def _clean_text(text: str) -> str:
    """Clean wikitext into plain text."""
    # Strip HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = _strip_templates(text)
    text = _strip_wiki_links(text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<code>(.*?)</code>", r"``\1``", text)
    text = re.sub(r"<[^>]+>", "", text)
    # Collapse multiple spaces
    text = re.sub(r"  +", " ", text)
    text = text.strip()
    return text


def parse_wikitext(wikitext: str) -> dict:
    """Parse component wikitext into structured documentation.

    Args:
        wikitext: Raw wikitext from the Resonite wiki.

    Returns:
        Dict with keys: description, fields, methods, usage, notes.
    """
    doc: dict = {
        "description": "",
        "category": "",
        "fields": {},
        "methods": {},
        "usage": "",
        "notes": [],
    }

    # Extract description from SHORTDESC or first paragraph
    shortdesc = re.search(r"\{\{SHORTDESC:(.*?)\}\}", wikitext)
    if shortdesc:
        doc["description"] = _clean_text(shortdesc.group(1))
    else:
        # First non-template, non-empty line after the infobox
        lines = wikitext.split("\n")
        for line in lines:
            line = line.strip()
            if (
                line
                and not line.startswith("{{")
                and not line.startswith("<!--")
                and not line.startswith("==")
                and not line.startswith("|")
            ):
                doc["description"] = _clean_text(line)
                break

    # Parse fields from {{Table ComponentFields ... }}
    # Can't use simple regex because inner templates also use }}.
    # Find the matching }} by counting brace depth.
    fields_match = re.search(
        r"\{\{Table ComponentFields\s*\n", wikitext,
    )
    field_text = ""
    if fields_match:
        start = fields_match.end()
        depth = 1
        i = start
        while i < len(wikitext) - 1 and depth > 0:
            if wikitext[i:i+2] == "{{":
                depth += 1
                i += 2
            elif wikitext[i:i+2] == "}}":
                depth -= 1
                if depth == 0:
                    field_text = wikitext[start:i]
                    break
                i += 2
            else:
                i += 1
    if field_text:
        # Pre-clean the entire block: replace template calls
        # with a placeholder so their internal pipes don't
        # interfere with field splitting.  Use iterative stripping
        # to handle nested templates/links.
        cleaned_block = field_text
        while "{{" in cleaned_block:
            new = re.sub(r"\{\{[^{}]*\}\}", "__TPL__", cleaned_block)
            if new == cleaned_block:
                break
            cleaned_block = new
        # Also replace wiki links with just the display text
        cleaned_block = re.sub(
            r"\[\[[^|\]]*\|([^\]]+)\]\]", r"\1", cleaned_block,
        )
        cleaned_block = re.sub(r"\[\[([^\]]+)\]\]", r"\1", cleaned_block)
        for line in cleaned_block.strip().split("\n"):
            line = line.strip()
            if not line.startswith("|"):
                continue
            parts = line.split("|")
            # parts[0] is empty, parts[1] is name, parts[2] is type
            if len(parts) < 4:
                continue
            name = parts[1].strip()
            # Description: last parts that aren't key=value or placeholders
            desc_parts = []
            for p in parts[3:]:
                p = p.strip()
                if not p or p == "__TPL__":
                    continue
                if re.match(r"^\w+=", p):
                    continue  # skip key=value like TypeAdv14=true
                desc_parts.append(p)
            desc = _clean_text(" ".join(desc_parts))
            if name and desc:
                doc["fields"][name] = desc

    # Parse methods from {{Table ComponentTriggers ... }}
    triggers_match = re.search(
        r"\{\{Table ComponentTriggers\s*\n", wikitext,
    )
    trigger_text = ""
    if triggers_match:
        start = triggers_match.end()
        depth = 1
        i = start
        while i < len(wikitext) - 1 and depth > 0:
            if wikitext[i:i+2] == "{{":
                depth += 1
                i += 2
            elif wikitext[i:i+2] == "}}":
                depth -= 1
                if depth == 0:
                    trigger_text = wikitext[start:i]
                    break
                i += 2
            else:
                i += 1
    if trigger_text:
        # Each line: |MethodName:Type|Type|bool| Description
        # Split on lines starting with | and parse the last field
        for line in trigger_text.strip().split("\n"):
            line = line.strip()
            if not line.startswith("|"):
                continue
            parts = line.split("|")
            # parts[0] is empty (before first |)
            # parts[1] is "MethodName:Type"
            # parts[-1] is the description (last field)
            if len(parts) < 5:
                continue
            method_part = parts[1].strip()
            method_name = method_part.split(":")[0].strip()
            desc = _clean_text(parts[-1])
            if method_name and desc:
                doc["methods"][method_name] = desc

    # Extract usage section
    usage_match = re.search(
        r"== Usage ==.*?\n(.*?)(?=\n==|\Z)",
        wikitext,
        re.DOTALL,
    )
    if usage_match:
        doc["usage"] = _clean_text(usage_match.group(1))

    # Extract any extra sections as notes (skip standard sections)
    _skip_sections = {
        "Fields", "Sync Delegates", "Usage", "Examples", "See Also",
    }
    for section_match in re.finditer(
        r"^== ([^=]+) ==.*?\n(.*?)(?=\n==|\Z)",
        wikitext,
        re.MULTILINE | re.DOTALL,
    ):
        title = section_match.group(1).strip()
        # Remove HTML comments from title
        title = re.sub(r"<!--.*?-->", "", title).strip()
        if title in _skip_sections or not title:
            continue
        body = _clean_text(section_match.group(2))
        if body:
            doc["notes"].append({"title": title, "text": body})

    # Extract the most specific category from [[Category:...]] tags.
    # e.g. [[Category:Components:Audio{{#translation:}}|Audio Output]]
    # → "Audio"
    categories: list[str] = []
    for cat_match in re.finditer(
        r"\[\[Category:Components:?([^|\]{}]*)", wikitext,
    ):
        cat = cat_match.group(1).strip()
        if cat:
            categories.append(cat)
    if categories:
        # Pick the most specific (longest) category
        doc["category"] = max(categories, key=len)

    return doc


def fetch_wiki_docs(component_name: str) -> dict | None:
    """Fetch and parse documentation for a component from the wiki.

    Args:
        component_name: Component name as it appears in the wiki URL
            (e.g. "AudioOutput", "AudioClipPlayer").

    Returns:
        Parsed documentation dict, or None if the page doesn't exist.
    """
    url = _WIKI_RAW_URL.format(name=component_name)
    try:
        with request.urlopen(url) as resp:
            if resp.status != 200:
                return None
            wikitext = resp.read().decode("utf-8")
    except Exception:
        return None

    if not wikitext or "There is currently no text in this page" in wikitext:
        return None

    return parse_wikitext(wikitext)


def save_docs(component_name: str, docs: dict, output_dir: Path | None = None) -> Path:
    """Save parsed documentation to a JSON file.

    Args:
        component_name: Component name.
        docs: Parsed documentation dict.
        output_dir: Directory to save to. Defaults to generated/docs/.

    Returns:
        Path to the saved file.
    """
    if output_dir is None:
        output_dir = _DOCS_DIR
    from pyresonitelink.generated._generator import _to_snake_case

    # Place in a category subfolder if available
    category = docs.get("category", "")
    if category:
        cat_dir = _to_snake_case(category)
        output_dir = output_dir / cat_dir

    output_dir.mkdir(parents=True, exist_ok=True)

    # Use snake_case filename matching the generated module
    filename = _to_snake_case(component_name) + ".json"
    path = output_dir / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)
    return path


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch component docs from the Resonite wiki",
    )
    parser.add_argument(
        "component",
        help="Component name (e.g. AudioOutput, AudioClipPlayer)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: generated/docs/)",
    )
    args = parser.parse_args()

    print(f"Fetching docs for {args.component}...")
    docs = fetch_wiki_docs(args.component)
    if docs is None:
        print(f"No wiki page found for {args.component}")
        return

    path = save_docs(args.component, docs, args.output_dir)
    print(f"Saved to {path}")
    print(f"  description: {docs['description'][:80]}...")
    print(f"  fields: {len(docs['fields'])}")
    print(f"  methods: {len(docs['methods'])}")
    if docs["usage"]:
        print(f"  usage: {docs['usage'][:80]}...")
    if docs["notes"]:
        print(f"  notes: {len(docs['notes'])}")


if __name__ == "__main__":
    main()
