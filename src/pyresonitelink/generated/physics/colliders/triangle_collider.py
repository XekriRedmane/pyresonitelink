"""Generated component: TriangleCollider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.collider_type import ColliderType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isweepable_collider import ISweepableCollider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class TriangleCollider(GeneratedComponent, ISweepableCollider, ICustomInspector):
    """Triangle collider is a component that acts as a single polygon version of a Mesh Collider

    Category: Physics/Colliders
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TriangleCollider"

    def __init__(self, offset: primitives.Float3 | None = None, type_: ColliderType | str | None = None, mass: primitives.Float | None = None, character_collider: primitives.Bool | None = None, ignore_raycasts: primitives.Bool | None = None, a: primitives.Float3 | None = None, b: primitives.Float3 | None = None, c: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            type_: Initial value for Type.
            mass: Initial value for Mass.
            character_collider: Initial value for CharacterCollider.
            ignore_raycasts: Initial value for IgnoreRaycasts.
            a: Initial value for A.
            b: Initial value for B.
            c: Initial value for C.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset
        if type_ is not None:
            self.type_ = type_
        if mass is not None:
            self.mass = mass
        if character_collider is not None:
            self.character_collider = character_collider
        if ignore_raycasts is not None:
            self.ignore_raycasts = ignore_raycasts
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if c is not None:
            self.c = c

    @property
    def offset(self) -> primitives.Float3 | None:
        """how much to add to points ``A``, ``B``, and ``C``."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def type_(self) -> ColliderType | None:
        """The Type enum value."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColliderType(member.value)
        return None

    @type_.setter
    def type_(self, value: ColliderType | str) -> None:
        """Set the Type enum value."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Type",
                members.FieldEnum(value=str(value)),
            )

    @property
    def mass(self) -> primitives.Float | None:
        """The Mass field value."""
        member = self.get_member("Mass")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mass.setter
    def mass(self, value: primitives.Float) -> None:
        """Set the Mass field value."""
        member = self.get_member("Mass")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mass", fields.FieldFloat(value=value)
            )

    @property
    def character_collider(self) -> primitives.Bool | None:
        """The CharacterCollider field value."""
        member = self.get_member("CharacterCollider")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @character_collider.setter
    def character_collider(self, value: primitives.Bool) -> None:
        """Set the CharacterCollider field value."""
        member = self.get_member("CharacterCollider")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CharacterCollider", fields.FieldBool(value=value)
            )

    @property
    def ignore_raycasts(self) -> primitives.Bool | None:
        """The IgnoreRaycasts field value."""
        member = self.get_member("IgnoreRaycasts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_raycasts.setter
    def ignore_raycasts(self, value: primitives.Bool) -> None:
        """Set the IgnoreRaycasts field value."""
        member = self.get_member("IgnoreRaycasts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreRaycasts", fields.FieldBool(value=value)
            )

    @property
    def a(self) -> primitives.Float3 | None:
        """The position of the first vertex of the triangle."""
        member = self.get_member("A")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @a.setter
    def a(self, value: primitives.Float3) -> None:
        """Set the A field value."""
        member = self.get_member("A")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "A", fields.FieldFloat3(value=value)
            )

    @property
    def b(self) -> primitives.Float3 | None:
        """The position of the second vertex of the triangle."""
        member = self.get_member("B")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @b.setter
    def b(self, value: primitives.Float3) -> None:
        """Set the B field value."""
        member = self.get_member("B")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "B", fields.FieldFloat3(value=value)
            )

    @property
    def c(self) -> primitives.Float3 | None:
        """The position of the third vertex of the triangle."""
        member = self.get_member("C")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @c.setter
    def c(self, value: primitives.Float3) -> None:
        """Set the C field value."""
        member = self.get_member("C")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "C", fields.FieldFloat3(value=value)
            )

