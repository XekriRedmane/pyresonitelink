"""Builds static scenery in batches, with IDs chosen before anything is sent.

Adding a slot or a component one request at a time costs a round trip
each, and a scene of a few hundred boxes takes minutes. A SceneBatch
collects the additions instead, gives every slot and component an ID of
its own choosing, so that a later addition can refer to an earlier one,
and sends them in a few data_model_operation_batch messages, each of
which the server runs within one engine update.

    batch = batches.SceneBatch(resolink)
    box = batch.add_slot(parent, "Box", position=(0, 0.5, 0))
    mesh = batch.add_component(box, box_mesh.BoxMesh(size=primitives.Float3(1, 1, 1)))
    batch.add_renderer(box, mesh, [material.id])
    await batch.flush()

NEVER add ProtoFlux nodes this way. A node wired in the same engine
update that created it can have every reference in place and still never
run.
"""

import math
import uuid
from collections.abc import Sequence

from pyresonitelink import client
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import messages
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated.rendering import mesh_renderer

# How many operations go into one message. 200 additions took 0.02 s to
# run on 23 Oct 2026, so a message of this size holds up an engine update
# only briefly.
MAX_OPERATIONS = 400


def new_id() -> str:
    """Returns a new ID for a slot, a component, or a member."""
    return str(uuid.uuid4())


def euler(x: float = 0.0, y: float = 0.0, z: float = 0.0) -> primitives.FloatQ:
    """Returns the rotation of Euler angles in degrees, as Resonite's floatQ.Euler composes them.

    The rotation turns about Z first, then X, then Y, the order of
    floatQ.Euler (Y * X * Z).
    """
    def axis(ax: float, ay: float, az: float, degrees: float) -> tuple[float, float, float, float]:
        half = math.radians(degrees) / 2
        s = math.sin(half)
        return ax * s, ay * s, az * s, math.cos(half)

    def multiply(a: tuple[float, float, float, float],
                 b: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
        ax, ay, az, aw = a
        bx, by, bz, bw = b
        return (
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw,
            aw * bw - ax * bx - ay * by - az * bz,
        )

    q = multiply(multiply(axis(0, 1, 0, y), axis(1, 0, 0, x)), axis(0, 0, 1, z))
    return primitives.FloatQ(*q)


class SceneBatch:
    """Collects slot and component additions and sends them in batches.

    Attributes:
        operations (list[messages.Message]): The additions not sent yet.
    """

    def __init__(self, resolink: client.Client) -> None:
        self._resolink = resolink
        self.operations: list[messages.Message] = []

    def add_slot(
        self,
        parent: str | workers.Slot,
        name: str,
        *,
        position: Sequence[float] = (0.0, 0.0, 0.0),
        rotation: primitives.FloatQ | None = None,
        scale: Sequence[float] | None = None,
        active: bool = True,
    ) -> str:
        """Adds a slot, and returns its ID.

        Args:
            parent: The parent, as an ID or a Slot. It may be a slot added
                earlier in this batch.
            name: The slot's name.
            position: The position in the parent's space.
            rotation: The rotation in the parent's space, or None for none.
            scale: The scale, or None for 1.
            active: Whether the slot is active.
        """
        slot_id = new_id()
        parent_id = parent if isinstance(parent, str) else parent.id
        slot = workers.Slot(
            id=slot_id,
            parent=members.Reference(targetId=parent_id),
            name=fields.FieldString(value=name),
            position=fields.FieldFloat3(value=primitives.Float3(*position)),
            isActive=fields.FieldBool(value=active),
        )
        if rotation is not None:
            slot.rotation = fields.FieldFloatQ(value=rotation)
        if scale is not None:
            slot.scale = fields.FieldFloat3(value=primitives.Float3(*scale))
        self.operations.append(messages.AddSlot(data=slot))
        return slot_id

    def add_component(self, slot: str | workers.Slot, component: GeneratedComponent) -> str:
        """Adds a component to a slot, and returns its ID.

        The component's id is set to that ID, so that it can be refreshed
        from the server after the batch is sent, which gives its members
        the IDs the server knows them by.

        Args:
            slot: The slot, as an ID or a Slot. It may be a slot added
                earlier in this batch.
            component: The component, with its members' values set.
        """
        component_id = new_id()
        component.id = component_id
        slot_id = slot if isinstance(slot, str) else slot.id
        self.operations.append(messages.AddComponent(
            containerSlotId=slot_id, data=component.component,
        ))
        return component_id

    def add_renderer(
        self, slot: str | workers.Slot, mesh: str, materials: Sequence[str],
    ) -> str:
        """Adds a MeshRenderer that draws a mesh with a material per submesh, and returns its ID.

        Args:
            slot: The slot, as an ID or a Slot.
            mesh: The ID of the mesh component, such as a BoxMesh.
            materials: The IDs of the materials, in submesh order.
        """
        renderer = mesh_renderer.MeshRenderer(mesh=mesh)
        renderer.component.members["Materials"] = members.SyncList(
            id=new_id(),
            elements=[members.Reference(id=new_id(), targetId=m) for m in materials],
        )
        return self.add_component(slot, renderer)

    async def flush(self) -> None:
        """Sends the collected additions, in order, in messages of up to MAX_OPERATIONS.

        Raises:
            RuntimeError: The server refused an addition. The additions
                before it in its message, and the messages before that,
                are in the world.
        """
        operations, self.operations = self.operations, []
        for start in range(0, len(operations), MAX_OPERATIONS):
            chunk = operations[start:start + MAX_OPERATIONS]
            resp = await self._resolink.data_model_operation_batch(chunk)
            failures = [
                (op, r) for op, r in zip(chunk, resp.responses or []) if not r.success
            ]
            if failures:
                op, r = failures[0]
                raise RuntimeError(
                    f"{len(failures)} of {len(chunk)} additions failed. The first, "
                    f"{type(op).__name__}, failed with: {r.errorInfo}"
                )
