"""Example that places a textured card from a glTF file in front of the user.

The card is TexturedCard.glb, next to this script, which
make_textured_card.py writes. It is a printed order form, a paper box with
decals just in front of it, most of which have transparent backgrounds.
The script reads it with pyresonitelink.utils.glb, leaves out the nodes
that the file marks hidden, and uploads the mesh and its textures. Each
submesh gets an unlit material, because the card is printed artwork, and
its colors look as drawn without lighting. The card is placed 1.5 m in
front of the user's head, facing them. Each run deletes the card from the
previous run.

Usage:
    python examples/textured_card.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import os
import sys
from typing import Any

import numpy as np
import trimesh

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated.assets import static_texture_2d
from pyresonitelink.generated.assets.materials.unlit import unlit_material
from pyresonitelink.utils import glb
from pyresonitelink.utils import placement
from pyresonitelink.utils import rendering
from pyresonitelink.utils import slots

GLB_PATH = os.path.join(os.path.dirname(__file__), "TexturedCard.glb")
SLOT_NAME = "Textured Card Example"
CARD_NODE = "TexturedCard"
DISTANCE = 1.5  # meters in front of the head
# The card in the file is 0.22 m wide. This makes it 0.66 m.
CARD_SCALE = 3.0

# The Resonite blend mode for each glTF alphaMode. A material without an
# alphaMode is opaque.
BLEND_MODES = {"OPAQUE": "Opaque", "MASK": "Cutout", "BLEND": "Alpha"}


def is_hidden(name: str, extras: dict[str, Any]) -> bool:
    """Tells whether the card file marks a node hidden.

    Args:
        name (str): The node's name.
        extras (dict[str, Any]): The node's glTF extras.

    Returns:
        True if the extras have "hidden": true.
    """
    return extras.get("hidden") is True


def load_card(path: str) -> glb.Mesh:
    """Reads the visible parts of the card from a glTF file.

    Args:
        path (str): The .glb file.

    Returns:
        The card in Resonite's coordinates, with its front facing +Z, and
        one submesh for each visible part.

    Raises:
        LookupError: The file has no node named CARD_NODE.
    """
    scene = glb.load(path)
    return glb.to_resonite(glb.read_node(scene, CARD_NODE, skip=is_hidden))


async def add_material(
    resolink: client.Client,
    slot: workers.Slot,
    material: trimesh.visual.material.Material | None,
) -> unlit_material.UnlitMaterial:
    """Adds an unlit material, and its texture if it has one, to a slot.

    Args:
        resolink (client.Client): The connected client.
        slot (workers.Slot): The slot to add the components to.
        material (trimesh.visual.material.Material | None): The material
            that trimesh read from the file, or None for plain white.

    Returns:
        The material component.
    """
    if not isinstance(material, trimesh.visual.material.PBRMaterial):
        unlit = unlit_material.UnlitMaterial()
        await unlit.add_to_slot(resolink, slot)
        return unlit
    texture = None
    if material.baseColorTexture is not None:
        # Row 0 of the pixel array is the top of the image, the same as in
        # the PIL image.
        pixels = np.asarray(material.baseColorTexture.convert("RGBA"))
        asset = await resolink.import_texture_2d_raw_data(pixels)
        # Clamping keeps a decal's edge from blending in its opposite edge
        # when the texture is filtered.
        texture = static_texture_2d.StaticTexture2D(
            url=asset.assetURL, wrap_mode_u="Clamp", wrap_mode_v="Clamp",
        )
        await texture.add_to_slot(resolink, slot)
    # trimesh gives the color factor as 0 to 255. glTF color factors are
    # linear.
    factor = material.baseColorFactor
    r, g, b, a = (1.0,) * 4 if factor is None else (float(c) / 255 for c in factor)
    unlit = unlit_material.UnlitMaterial(
        tint_color=primitives.ColorX(r, g, b, a, "Linear"),
        texture=texture,
        blend_mode=BLEND_MODES[material.alphaMode or "OPAQUE"],
    )
    await unlit.add_to_slot(resolink, slot)
    return unlit


async def place_card(resolink: client.Client, slot_name: str) -> workers.Slot:
    """Places the card 1.5 m in front of the user's head, facing them.

    A slot under Root named slot_name, from a previous run, is deleted
    first.

    Args:
        resolink (client.Client): The connected client.
        slot_name (str): The name of the slot under Root that holds the
            card.

    Returns:
        The card's slot.
    """
    card = load_card(GLB_PATH)
    print(f"Read {len(card.submeshes)} parts from {GLB_PATH}: {', '.join(card.nodes)}.")

    for old in await workers.Slot(id=workers.Slot.ROOT_SLOT_ID).remove_children_named(
        resolink, slot_name,
    ):
        print(f"Deleted old slot {old}.")

    # Half a turn turns the card's front, +Z, toward the head.
    world = await placement.in_front_of_head(
        resolink, DISTANCE, turn=placement.HALF_TURN, scale=CARD_SCALE,
    )
    slot = await slots.add_slot_at(resolink, world, name=slot_name)
    print(f"Created slot {slot.id}.")

    # Parts that share a material in the file share one here.
    added: dict[int, unlit_material.UnlitMaterial] = {}
    for material in card.materials:
        if id(material) not in added:
            added[id(material)] = await add_material(resolink, slot, material)
    await rendering.add_mesh(
        resolink, slot, card, [added[id(material)] for material in card.materials],
    )
    return slot


async def main(port: int | None) -> None:
    """Places the textured card in front of the user's head.

    Args:
        port (int | None): The ResoniteLink port, or None to find the
            session from its LAN announcement.
    """
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)
    await place_card(resolink, SLOT_NAME)
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
