"""Member types for ResoniteLink data model.

This module contains the Member base class and its derived types including
Reference, SyncList, SyncObject, EmptyElement, and FieldEnum.
"""

# pylint: disable=invalid-name

import uuid
from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


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
class Reference(Member, Generic[T]):
    """A typed reference to another member or worker.

    References point to other elements in the data model by their ID.
    The type parameter ``T`` is a phantom type used only for static
    type checking — it does not affect runtime behavior.

    ``Reference[Slot]`` means a reference that targets a Slot.
    Unparameterized ``Reference`` is equivalent to ``Reference[Any]``.
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
class FieldNullableEnum(FieldEnum):
    """A field containing an optional enum value represented as a string.

    It has its own wire type, "enum?". The server can't cast between the
    two, so sending "enum?" to a non-nullable enum field fails with an
    InvalidCastException, and the other way around presumably too.
    """


@dataclass
class DataReference:
    """A reference passed as an argument to a sync method.

    Sync method arguments use ResoniteLink's ``Data`` types rather than
    members. A primitive argument is encoded the same way as its field,
    such as ``FieldInt``, but a reference argument has its own wire form,
    ``{"$type": "reference", "targetID": ...}``. Note the capital ``ID``,
    which differs from the ``targetId`` of a ``Reference`` member.

    This class is only ever encoded. The codec decodes ``"reference"`` as
    a ``Reference`` member.
    """

    targetID: str | None = None


def tag_method_arguments(
    arguments: dict[str, object] | None,
) -> dict[str, "Member | DataReference"]:
    """Returns sync method arguments in the $type-tagged form the server parses.

    A Member, such as FieldInt(value=2), and a DataReference are passed as
    they are. Anything else with an ``id`` attribute, such as a component
    or a slot, becomes a DataReference to it.

    Args:
        arguments: Parameter names mapped to values, or None.

    Returns:
        The arguments, ready for CallSyncMethod or CallStaticSyncMethod.

    Raises:
        TypeError: An argument is neither tagged nor something with an ID.
            A bare value such as 2 can't be sent, because the server needs
            its type.
    """
    tagged: dict[str, Member | DataReference] = {}
    for name, value in (arguments or {}).items():
        if isinstance(value, (Member, DataReference)):
            tagged[name] = value
        elif getattr(value, "id", None) is not None:
            tagged[name] = DataReference(targetID=getattr(value, "id"))
        else:
            raise TypeError(
                f"Argument {name}={value!r} needs a type. Pass a field "
                f"instance such as fields.FieldInt(value=2), or a "
                f"members.DataReference."
            )
    return tagged


@dataclass
class Type(Member):
    """A field containing a Resonite type value (assembly-qualified name)."""

    value: str | None = None


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
