"""Worker types for ResoniteLink data model.

This module contains the Worker base class and its derived types including
Slot and Component.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

from .fields import FieldBool, FieldFloat3, FieldFloatQ, FieldLong, FieldString
from .members import Member, Reference

if TYPE_CHECKING:
    # protocols imports this module.
    from . import protocols


@dataclass
class Worker:
    """Base class for workers.

    Workers are objects that can be referenced by their unique ID.
    """

    id: str | None = None
    isReferenceOnly: bool = False


@dataclass
class Component(Worker):
    """A component attached to a slot.

    Components contain typed data through their members dictionary.
    """

    componentType: str | None = None
    members: dict[str, Member] = field(default_factory=dict[str, Member])


@dataclass
class Slot(Worker):
    """A slot in the scene hierarchy.

    Slots are the primary building blocks of the scene graph, containing
    transform data, components, and child slots.
    """

    # A class constant, so that it isn't a dataclass field that gets encoded.
    ROOT_SLOT_ID: ClassVar[str] = "Root"

    parent: Reference | None = None
    position: FieldFloat3 | None = None
    rotation: FieldFloatQ | None = None
    scale: FieldFloat3 | None = None
    isActive: FieldBool | None = None
    isPersistent: FieldBool | None = None
    name: FieldString | None = None
    tag: FieldString | None = None
    orderOffset: FieldLong | None = None
    components: list[Component] = field(default_factory=list[Component])
    children: list["Slot"] = field(default_factory=list["Slot"])

    async def remove_children_named(
        self, resolink: "protocols.ResoniteLinkClient", name: str,
    ) -> list[str]:
        """Removes each child of this slot that has a given name, with its descendants.

        Scripts that add a slot under a fixed name call this first, so that
        running them again replaces the slot instead of adding a second one.
        Only direct children are removed, and the name must match exactly.
        The children are read from the server, so this slot's children
        field may be empty or out of date. Only the slot's id is used.

            root = workers.Slot(id=workers.Slot.ROOT_SLOT_ID)
            await root.remove_children_named(resolink, "Example")

        Args:
            resolink (protocols.ResoniteLinkClient): The connected client.
            name (str): The name of the children to remove.

        Returns:
            The IDs of the removed slots.
        """
        assert self.id is not None, "The slot has no ID."
        data = (await resolink.get_slot(self.id, depth=1)).data
        assert data is not None
        removed: list[str] = []
        for child in data.children:
            if child.name is not None and child.name.value == name:
                assert child.id is not None
                await resolink.remove_slot(child)
                removed.append(child.id)
        return removed
