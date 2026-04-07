"""Member types for ResoniteLink data model.

This module contains the Member base class and its derived types including
Reference, SyncList, SyncObject, EmptyElement, and FieldEnum.
"""

# pylint: disable=invalid-name

import uuid
from dataclasses import dataclass, field


def _generate_uuid() -> str:
    """Generate a random UUID v4 string.

    Returns:
        A new random UUID v4 as a string.
    """
    return str(uuid.uuid4())


@dataclass
class Member:
    """Base class for all member types.

    Members are elements that belong to components or sync objects and can be
    referenced by their unique ID. When constructed directly (not through
    deserialization), the id is automatically set to a random UUID v4.
    """

    id: str = field(default_factory=_generate_uuid)


@dataclass
class Reference(Member):
    """A reference to another member or worker.

    References point to other elements in the data model by their ID.
    """

    targetId: str | None = None
    targetType: str | None = None


@dataclass
class SyncList(Member):
    """A synchronized list of members."""

    elements: list[Member] = field(default_factory=list[Member])


@dataclass
class SyncObject(Member):
    """A synchronized object containing named members."""

    members: dict[str, Member] = field(default_factory=dict[str, Member])


@dataclass
class EmptyElement(Member):
    """An empty placeholder element in a list."""


@dataclass
class FieldEnum(Member):
    """A field containing an enum value represented as a string."""

    value: str | None = None
    enumType: str | None = None


@dataclass
class SyncPlayback(Member):
    """A playback state member with transport controls."""

    play: bool = False
    loop: bool = False
    position: float = 0.0
    speed: float = 1.0


@dataclass
class SyncDictionary(Member):
    """A synchronized dictionary member.

    Keys are typically enum values (as strings). Values are decoded
    members stored in the elements dict.
    """

    enumType: str | None = None
    elements: dict[str, Member] = field(default_factory=dict[str, Member])
