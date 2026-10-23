"""Reads values that only ProtoFlux can compute, through fields that nodes drive.

ViewProbe reads where the local user's view is, which is the camera's pose
in desktop mode and the headset's in VR. ResoniteLink reads the values of
the Resonite instance it is connected to, so the local user is the one
running that instance. In desktop mode the camera isn't where the avatar's
Head slot points, which is about 3 degrees off, and the user's "View" slot
isn't driven at all (measured 23 Oct 2026), so a script that has to know
where the screen center points uses the probe.

    probe = await probes.ViewProbe.create(resolink)
    view = await probe.read(resolink)  # a transforms.Transform
    forward = transforms.rotate(view.rotation, primitives.Float3(0, 0, 1))
    await probe.remove(resolink)

The probe is a slot with two ValueFields, which ValueFieldDrives drive from
the ViewPosition and ViewRotation nodes in every engine update. A
ValueDisplay can't take a ValueFieldDrive's place here, since it wrote its
field once, when it was wired, and never again. The fields start at random
sentinel values, and create returns once the drives have replaced both,
since a read before then returns the fields' starting values.
"""

import asyncio
import random

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.generated.data import value_field
from pyresonitelink.generated.protoflux.runtimes.execution.nodes.users.local_output import (
    view_position,
)
from pyresonitelink.generated.protoflux.runtimes.execution.nodes.users.local_output import (
    view_rotation,
)
from pyresonitelink.utils import wiring

# The magnitude bound of each component of the sentinel values. A driven
# rotation is a unit quaternion, so the rotation's sentinel, which isn't
# one, can't be mistaken for it.
_SENTINEL_RANGE = 1e4
# Seconds between reads while create waits for the drives.
_POLL_INTERVAL = 0.02


class ViewProbe:
    """Represents a slot whose fields hold the local user's view in world space.

    Attributes:
        slot (workers.Slot): The probe's slot.
        position (value_field.ValueField): The field that holds the view's
            position.
        rotation (value_field.ValueField): The field that holds the view's
            rotation.
    """

    def __init__(
        self,
        slot: workers.Slot,
        position: value_field.ValueField,
        rotation: value_field.ValueField,
    ) -> None:
        self.slot = slot
        self.position = position
        self.rotation = rotation

    @classmethod
    async def create(
        cls,
        resolink: client.Client,
        parent: str | workers.Slot = workers.Slot.ROOT_SLOT_ID,
        *,
        name: str = "View Probe",
        timeout: float = 5.0,
    ) -> "ViewProbe":
        """Adds a probe slot, its fields, and the nodes that drive them.

        Args:
            resolink (client.Client): The connected client.
            parent (str | workers.Slot): The slot to add the probe under.
                The default is Root.
            name (str): The probe slot's name.
            timeout (float): How long to wait for the drives, in seconds.

        Returns:
            The probe, whose fields hold the view.

        Raises:
            TimeoutError: The fields weren't driven within timeout seconds.
                The probe's slot is removed first.
        """
        slot = await resolink.add_slot(parent=parent, name=name)
        position_sentinel = primitives.Float3(*_random(3))
        rotation_sentinel = primitives.FloatQ(*_random(4))
        position = value_field.ValueField[primitives.Float3](position_sentinel)
        rotation = value_field.ValueField[primitives.FloatQ](rotation_sentinel)
        await position.add_to_slot(resolink, slot)
        await rotation.add_to_slot(resolink, slot)
        for node, field, value_type in (
            (view_position.ViewPosition(), position, primitives.Float3),
            (view_rotation.ViewRotation(), rotation, primitives.FloatQ),
        ):
            await wiring.add_node(resolink, slot, node)
            member = field.get_member("Value")
            assert member is not None and member.id is not None
            await wiring.drive_from(resolink, slot, node, member.id, value_type)
        probe = cls(slot, position, rotation)
        deadline = asyncio.get_running_loop().time() + timeout
        while True:
            view = await probe.read(resolink)
            if view.position != position_sentinel and view.rotation != rotation_sentinel:
                return probe
            if asyncio.get_running_loop().time() > deadline:
                await probe.remove(resolink)
                raise TimeoutError(f"The view probe {slot.id} wasn't driven within {timeout} s.")
            await asyncio.sleep(_POLL_INTERVAL)

    async def read(self, resolink: client.Client) -> transforms.Transform:
        """Reads the view's pose in world space, with a scale of 1.

        Args:
            resolink (client.Client): The connected client.

        Returns:
            The view's position and rotation.
        """
        await self.position.refresh(resolink)
        await self.rotation.refresh(resolink)
        position = self.position.value
        rotation = self.rotation.value
        assert isinstance(position, primitives.Float3)
        assert isinstance(rotation, primitives.FloatQ)
        return transforms.Transform(
            position=position, rotation=rotation, scale=primitives.Float3(1, 1, 1),
        )

    async def remove(self, resolink: client.Client) -> None:
        """Removes the probe's slot, with its fields and nodes.

        Args:
            resolink (client.Client): The connected client.
        """
        assert self.slot.id is not None
        await resolink.remove_slot(self.slot.id)


def _random(count: int) -> list[float]:
    """Returns count numbers, each uniform in +/-_SENTINEL_RANGE."""
    return [random.uniform(-_SENTINEL_RANGE, _SENTINEL_RANGE) for _ in range(count)]
