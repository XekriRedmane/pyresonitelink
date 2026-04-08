"""Generated component: CylinderCollider."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ihighlightable import IHighlightable
from pyresonitelink.generated._types.isweepable_collider import ISweepableCollider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class CylinderCollider(GeneratedComponent, IHighlightable, ISweepableCollider, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.CylinderCollider.

    Category: Physics/Colliders
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CylinderCollider"

    def __init__(self, offset: primitives.Float3 | None = None, mass: np.float32 | None = None, character_collider: bool | None = None, ignore_raycasts: bool | None = None, height: np.float32 | None = None, radius: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            mass: Initial value for Mass.
            character_collider: Initial value for CharacterCollider.
            ignore_raycasts: Initial value for IgnoreRaycasts.
            height: Initial value for Height.
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset
        if mass is not None:
            self.mass = mass
        if character_collider is not None:
            self.character_collider = character_collider
        if ignore_raycasts is not None:
            self.ignore_raycasts = ignore_raycasts
        if height is not None:
            self.height = height
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
    def type_(self) -> members.FieldEnum | None:
        """The Type member."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @type_.setter
    def type_(self, value: members.FieldEnum) -> None:
        """Set the Type member."""
        self.set_member("Type", value)

    @property
    def mass(self) -> np.float32 | None:
        """The Mass field value."""
        member = self.get_member("Mass")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mass.setter
    def mass(self, value: np.float32) -> None:
        """Set the Mass field value."""
        member = self.get_member("Mass")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mass", fields.FieldFloat(value=value)
            )

    @property
    def character_collider(self) -> bool | None:
        """The CharacterCollider field value."""
        member = self.get_member("CharacterCollider")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @character_collider.setter
    def character_collider(self, value: bool) -> None:
        """Set the CharacterCollider field value."""
        member = self.get_member("CharacterCollider")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CharacterCollider", fields.FieldBool(value=value)
            )

    @property
    def ignore_raycasts(self) -> bool | None:
        """The IgnoreRaycasts field value."""
        member = self.get_member("IgnoreRaycasts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_raycasts.setter
    def ignore_raycasts(self, value: bool) -> None:
        """Set the IgnoreRaycasts field value."""
        member = self.get_member("IgnoreRaycasts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreRaycasts", fields.FieldBool(value=value)
            )

    @property
    def height(self) -> np.float32 | None:
        """The Height field value."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: np.float32) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    async def set_from_precise_bounds(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetFromPreciseBounds sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetFromPreciseBounds", {}, debug,
        )

