"""A fake client that serves a slot hierarchy and world transforms, for unit tests."""

import math
from typing import Any

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import transforms
from pyresonitelink.data import workers


def make_slot(
    slot_id: str,
    name: str,
    component_types: tuple[str, ...] = (),
    children: tuple[workers.Slot, ...] = (),
) -> workers.Slot:
    """Returns slot data with a name, components of the given types, and children."""
    return workers.Slot(
        id=slot_id,
        name=fields.FieldString(value=name),
        components=[workers.Component(componentType=t) for t in component_types],
        children=list(children),
    )


class FakeClient:
    """Serves a fixed slot hierarchy and world transforms, and records changes.

    Attributes:
        slots (dict[str, workers.Slot]): The slot data that get_slot
            returns, by slot ID.
        world (dict[str, transforms.Transform]): The world transform of
            each slot, by slot ID.
        added (list[dict[str, Any]]): The keyword arguments of each
            add_slot call.
        removed (list[str]): The IDs of the removed slots, in order.
    """

    def __init__(self, root_children: tuple[workers.Slot, ...] = ()) -> None:
        root = make_slot(workers.Slot.ROOT_SLOT_ID, "Root", children=root_children)
        self.slots: dict[str, workers.Slot] = {workers.Slot.ROOT_SLOT_ID: root}
        for child in root_children:
            assert child.id is not None
            self.slots[child.id] = child
            for grandchild in child.children:
                assert grandchild.id is not None
                self.slots[grandchild.id] = grandchild
        self.world: dict[str, transforms.Transform] = {
            workers.Slot.ROOT_SLOT_ID: transforms.Transform(),
        }
        self.added: list[dict[str, Any]] = []
        self.removed: list[str] = []

    @staticmethod
    def _id(slot: str | workers.Slot) -> str:
        """Returns a slot's ID."""
        slot_id = slot if isinstance(slot, str) else slot.id
        assert slot_id is not None
        return slot_id

    async def get_slot(self, slot: str | workers.Slot, depth: int = 0) -> responses.SlotData:
        """Returns the stored data of a slot."""
        return responses.SlotData(success=True, data=self.slots[self._id(slot)])

    async def get_global_transform(self, slot: str | workers.Slot) -> transforms.Transform:
        """Returns the stored world transform of a slot."""
        return self.world[self._id(slot)]

    async def add_slot(self, **kwargs: Any) -> workers.Slot:
        """Records the arguments and returns a new slot."""
        self.added.append(kwargs)
        return workers.Slot(id=f"new-{len(self.added)}")

    async def remove_slot(self, slot: str | workers.Slot) -> responses.Response:
        """Records the removal."""
        self.removed.append(self._id(slot))
        return responses.Response(success=True)


def close(a: primitives.Float3, b: tuple[float, float, float]) -> bool:
    """Tells whether a vector equals a tuple to within float32 rounding."""
    return all(math.isclose(float(x), y, abs_tol=1e-5) for x, y in zip((a.x, a.y, a.z), b))
