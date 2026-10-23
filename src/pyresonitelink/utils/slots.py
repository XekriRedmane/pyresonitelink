"""Adds slots at places given in world space.

A slot's position, rotation, and scale are relative to its parent, so a
slot that has to end up at a given place in the world needs that place
re-expressed in its parent's space. add_slot_at does that with the parent's
world transform, which it reads from the server, because the parent's
transform, and each of its ancestors', can change in every engine update.

    world = transforms.Transform(primitives.Float3(0, 1.5, 2))
    slot = await slots.add_slot_at(resolink, world, name="Example", parent=table)
"""

from pyresonitelink import client
from pyresonitelink.data import transforms
from pyresonitelink.data import workers


async def add_slot_at(
    resolink: client.Client,
    world: transforms.Transform,
    *,
    name: str,
    parent: str | workers.Slot = workers.Slot.ROOT_SLOT_ID,
) -> workers.Slot:
    """Adds a slot whose world position, rotation, and scale are those of a transform.

    Args:
        resolink (client.Client): The connected client.
        world (transforms.Transform): Where the slot goes, in world space.
        name (str): The new slot's name.
        parent (str | workers.Slot): The new slot's parent, as an ID or a
            Slot. The default is Root.

    Returns:
        The new slot.

    Raises:
        ValueError: The parent's world scale has a zero component, so no
            local transform puts the slot at world.
    """
    local = transforms.relative_to(await resolink.get_global_transform(parent), world)
    return await resolink.add_slot(
        parent=parent,
        name=name,
        position=local.position,
        rotation=local.rotation,
        scale=local.scale,
    )
