"""Worker types for ResoniteLink data model.

This module contains the Worker base class and its derived types including
Slot and Component.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass, field
from typing import ClassVar

from .fields import FieldBool, FieldFloat3, FieldFloatQ, FieldLong, FieldString
from .members import Member, Reference


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
