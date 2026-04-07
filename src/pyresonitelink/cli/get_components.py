"""CLI tool for listing and inspecting Resonite component types."""

import argparse
import asyncio
import json

from pyresonitelink import client
from pyresonitelink.data import messages


async def get_component_types(port: int, host: str, category: str) -> None:
    """Connect to Resonite and print the component type list."""
    uri = f"ws://{host}:{port}"

    print(f"Connecting to {uri}...")
    resolink = client.Client()
    await resolink.connect(port, host)
    print(f"Connected. Requesting component types for category '{category}'...")

    response = await resolink.get_component_type_list(
        messages.GetComponentTypeList(categoryPath=category)
    )

    if not response.success:
        print(f"Error: {response.errorInfo}")
        return

    print(f"\nTotal component count: {response.totalComponentCount}")

    if response.subcategories:
        print(f"\nSubcategories ({len(response.subcategories)}):")
        for subcategory in response.subcategories:
            print(f"  {subcategory}")

    if response.componentTypes:
        print(f"\nComponent types ({len(response.componentTypes)}):")
        for component_type in response.componentTypes:
            print(f"  {component_type}")


async def get_component_definition(
    port: int, host: str, component_type: str, flattened: bool
) -> None:
    """Connect to Resonite and print a component's definition."""
    uri = f"ws://{host}:{port}"

    print(f"Connecting to {uri}...")
    resolink = client.Client()
    await resolink.connect(port, host)
    print(
        f"Connected. Requesting definition for '{component_type}'"
        f" (flattened={flattened})..."
    )

    json_response = await resolink.request_json(
        messages.GetComponentDefinition(
            componentType=component_type, flattened=flattened
        )
    )

    if not json_response.get("success", False):
        error_info = json_response.get("errorInfo", "Unknown error")
        print(f"Error: {error_info}")
        return

    definition = json_response.get("definition")
    if definition is None:
        print("No definition returned.")
        return

    print(json.dumps(definition, indent=2, ensure_ascii=False))


def main() -> None:
    """Run the get components CLI tool."""
    parser = argparse.ArgumentParser(
        description="List or inspect Resonite component types"
    )
    parser.add_argument(
        "port", type=int, help="Port number for ResoniteLink connection"
    )
    parser.add_argument(
        "--host", default="localhost", help="Host address (default: localhost)"
    )
    parser.add_argument(
        "--category",
        default="/",
        help="Category path to list (default: /)",
    )
    parser.add_argument(
        "--component",
        default=None,
        help="Fully qualified component type name to get its definition",
    )
    parser.add_argument(
        "--no-flatten",
        action="store_true",
        help="Don't include inherited members (default: include them)",
    )

    args = parser.parse_args()

    if args.component:
        asyncio.run(
            get_component_definition(
                args.port, args.host, args.component, not args.no_flatten
            )
        )
    else:
        asyncio.run(get_component_types(args.port, args.host, args.category))


if __name__ == "__main__":
    main()
