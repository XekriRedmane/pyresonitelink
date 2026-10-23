"""Adds colliders that fit meshes.

A collider is what a laser hits and what a hand's grab finds, so a mesh
without one can't be pointed at or grabbed. A Grabber looks for a grabbable
component on the collider's slot and then on its ancestors
(Grabber.FindGrabbableInParents), so a collider on a small child slot, such
as a handle, makes only that part of an object grabbable.

add_bounding_box adds a slot at the center of a mesh's bounds, with a
BoxCollider the size of the bounds.

    part, position = glb.read_part(scene, "Wheel Handle")
    await colliders.add_bounding_box(resolink, wheel, part, name="Handle")
"""

import numpy as np

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated.physics.colliders import box_collider
from pyresonitelink.utils import glb


async def add_bounding_box(
    resolink: client.Client,
    parent: str | workers.Slot,
    m: glb.Mesh,
    *,
    name: str,
) -> workers.Slot:
    """Adds a slot with a BoxCollider that just encloses a mesh.

    The box is aligned with the parent's axes, so it encloses the mesh
    tightly only when the mesh's sides are too.

    Args:
        resolink (client.Client): The connected client.
        parent (str | workers.Slot): The slot to add the new slot under, as
            an ID or a Slot. The mesh's positions are in its space.
        m (glb.Mesh): The mesh.
        name (str): The new slot's name.

    Returns:
        The new slot, at the center of the mesh's bounds, which holds the
        collider.

    Raises:
        ValueError: The mesh has no vertices.
    """
    if len(m.positions) == 0:
        raise ValueError("A mesh with no vertices has no bounds.")
    lower = m.positions.min(axis=0).astype(np.float64)
    upper = m.positions.max(axis=0).astype(np.float64)
    slot = await resolink.add_slot(parent=parent, name=name, position=(lower + upper) / 2)
    await box_collider.BoxCollider(
        size=primitives.Float3(*(upper - lower).tolist()),
    ).add_to_slot(resolink, slot)
    return slot
