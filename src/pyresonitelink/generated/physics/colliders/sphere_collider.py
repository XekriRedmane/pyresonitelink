"""Generated component: SphereCollider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.collider_type import ColliderType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ihighlightable import IHighlightable
from pyresonitelink.generated._types.isweepable_collider import ISweepableCollider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class SphereCollider(GeneratedComponent, IHighlightable, ISweepableCollider, ICustomInspector):
    """The SphereCollider generates a spherical collision shape based on an inputted radius.

    Category: Physics/Colliders
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SphereCollider"

    def __init__(self, offset: primitives.Float3 | None = None, type_: ColliderType | str | None = None, mass: primitives.Float | None = None, character_collider: primitives.Bool | None = None, ignore_raycasts: primitives.Bool | None = None, radius: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            type_: Initial value for Type.
            mass: Initial value for Mass.
            character_collider: Initial value for CharacterCollider.
            ignore_raycasts: Initial value for IgnoreRaycasts.
            radius: Initial value for Radius.
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
        if radius is not None:
            self.radius = radius

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
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
    def radius(self) -> primitives.Float | None:
        """How big the sphere is from center to outside edge."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    async def set_from_local_bounds(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetFromLocalBounds sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetFromLocalBounds", {}, debug,
        )

    async def set_from_global_bounds(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetFromGlobalBounds sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetFromGlobalBounds", {}, debug,
        )

    async def set_from_precise_bounds(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetFromPreciseBounds sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetFromPreciseBounds", {}, debug,
        )

