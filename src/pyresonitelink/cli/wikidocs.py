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


_WIKI_COMPONENT_URL = (
    "https://wiki.resonite.com/index.php"
    "?title=Component:{name}&action=raw"
)
_WIKI_PROTOFLUX_URL = (
    "https://wiki.resonite.com/index.php"
    "?title=ProtoFlux:{name}&action=raw"
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
    # Strip [[Category:...]] before general wiki link stripping
    text = re.sub(r"\[\[Category:[^\]]*\]\]", "", text)
    text = _strip_wiki_links(text)
    # Strip bold/italic markup
    text = re.sub(r"'{2,3}", "", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<code>(.*?)</code>", r"``\1``", text)
    text = re.sub(r"<[^>]+>", "", text)
    # Collapse multiple spaces (but preserve newlines)
    text = re.sub(r"[^\S\n]+", " ", text)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
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

    # Extract the long description: all body text between the last
    # template/infobox and the first == section heading.  This includes
    # paragraphs, bullet lists, etc.
    # Track template nesting depth to skip multi-line templates like
    # {{#Invoke:ProtoFlux|GenerateUI ... |}}
    body_lines: list[str] = []
    in_body = False
    template_depth = 0
    for line in wikitext.split("\n"):
        stripped = line.strip()
        if stripped.startswith("==") and template_depth == 0:
            break  # hit a section heading, stop
        # Track template nesting
        template_depth += line.count("{{") - line.count("}}")
        if template_depth < 0:
            template_depth = 0
        if template_depth > 0:
            continue  # inside a template, skip
        if in_body:
            body_lines.append(line)
        elif (
            stripped
            and not stripped.startswith("{{")
            and not stripped.startswith("}}")
            and not stripped.startswith("<!--")
            and not stripped.startswith("|")
            and not stripped.startswith("<languages")
            and not stripped.startswith("<translate")
            and not stripped.startswith("</translate")
            and not stripped.startswith("[")
            and not stripped.startswith("]")
        ):
            in_body = True
            body_lines.append(line)

    long_desc = _clean_text("\n".join(body_lines))

    # Convert wiki bullet lists to plain text
    # * Item -> - Item
    long_desc = re.sub(r"^\* ", "- ", long_desc, flags=re.MULTILINE)
    long_desc = re.sub(r"^\*\* ", "  - ", long_desc, flags=re.MULTILINE)

    if long_desc:
        doc["description"] = long_desc
    else:
        # Fall back to SHORTDESC if no body text
        shortdesc = re.search(r"\{\{SHORTDESC:(.*?)\}\}", wikitext)
        if shortdesc:
            doc["description"] = _clean_text(shortdesc.group(1))

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


# Cache of component names known to have no wiki page.
_no_wiki_page: set[str] = set()

_WIKI_TIMEOUT = 5  # seconds


def fetch_wiki_docs(
    component_name: str,
    prefer_protoflux: bool = False,
) -> dict | None:
    """Fetch and parse documentation for a component from the wiki.

    Tries ``ProtoFlux:<name>`` first for ProtoFlux nodes, otherwise
    ``Component:<name>`` first.  Falls back to the other prefix if the
    preferred one returns 404.

    Results are cached: components known to have no wiki page are
    not fetched again within the same process.

    Args:
        component_name: Component name as it appears in the wiki URL
            (e.g. "AudioOutput", "FireOnTrue").
        prefer_protoflux: If True, try ``ProtoFlux:`` prefix first.

    Returns:
        Parsed documentation dict, or None if the page doesn't exist.
    """
    if component_name in _no_wiki_page:
        return None

    # Build list of URLs to try, in priority order.
    # For ProtoFlux nodes, also try with Value/Object prefix stripped
    # since the wiki often uses shorter names (ValueAdd -> Add,
    # ObjectConstant -> Constant).
    names = [component_name]
    for prefix in ("Value", "Object"):
        if component_name.startswith(prefix) and len(component_name) > len(prefix):
            names.append(component_name[len(prefix):])

    urls: list[str] = []
    if prefer_protoflux:
        for n in names:
            urls.append(_WIKI_PROTOFLUX_URL.format(name=n))
        urls.append(_WIKI_COMPONENT_URL.format(name=component_name))
    else:
        urls.append(_WIKI_COMPONENT_URL.format(name=component_name))
        for n in names:
            urls.append(_WIKI_PROTOFLUX_URL.format(name=n))

    wikitext = None
    for url in urls:
        try:
            with request.urlopen(url, timeout=_WIKI_TIMEOUT) as resp:
                if resp.status == 200:
                    text = resp.read().decode("utf-8")
                    if text and "There is currently no text in this page" not in text:
                        wikitext = text
                        break
        except Exception:
            continue

    if wikitext is None:
        _no_wiki_page.add(component_name)
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

    # Place in a category subfolder if available.
    # Wiki categories use colons for subcategories (e.g. "UIX:Graphics")
    # — take the last segment as the folder name.
    category = docs.get("category", "")
    if category:
        # Use the most specific (last) subcategory
        leaf_cat = category.rsplit(":", 1)[-1]
        cat_dir = _to_snake_case(leaf_cat)
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
