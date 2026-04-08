"""Generated component: LegacyGlowingSphereToggle."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyGlowingSphereToggle(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyGlowingSphereToggle.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyGlowingSphereToggle"

    def __init__(self, target_field: str | IField[bool] | None = None, fade_speed: np.float32 | None = None, cooldown_time: np.float32 | None = None, radius: np.float32 | None = None, glow_color: primitives.ColorX | None = None, emissive_color: str | IField[primitives.ColorX] | None = None, rim_color: str | IField[primitives.ColorX] | None = None, sphere_radius: str | IField[np.float32] | None = None, sphere_extrude: str | IField[np.float32] | None = None, collider_radius: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_field: Initial value for TargetField.
            fade_speed: Initial value for FadeSpeed.
            cooldown_time: Initial value for CooldownTime.
            radius: Initial value for Radius.
            glow_color: Initial value for GlowColor.
            emissive_color: Initial value for _emissiveColor.
            rim_color: Initial value for _rimColor.
            sphere_radius: Initial value for _sphereRadius.
            sphere_extrude: Initial value for _sphereExtrude.
            collider_radius: Initial value for _colliderRadius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_field is not None:
            self.target_field = target_field
        if fade_speed is not None:
            self.fade_speed = fade_speed
        if cooldown_time is not None:
            self.cooldown_time = cooldown_time
        if radius is not None:
            self.radius = radius
        if glow_color is not None:
            self.glow_color = glow_color
        if emissive_color is not None:
            self.emissive_color = emissive_color
        if rim_color is not None:
            self.rim_color = rim_color
        if sphere_radius is not None:
            self.sphere_radius = sphere_radius
        if sphere_extrude is not None:
            self.sphere_extrude = sphere_extrude
        if collider_radius is not None:
            self.collider_radius = collider_radius

    @property
    def target_field(self) -> str | None:
        """Target ID of the TargetField reference (targets IField[bool])."""
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField[bool] | None) -> None:
        """Set the TargetField reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def fade_speed(self) -> np.float32 | None:
        """The FadeSpeed field value."""
        member = self.get_member("FadeSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fade_speed.setter
    def fade_speed(self, value: np.float32) -> None:
        """Set the FadeSpeed field value."""
        member = self.get_member("FadeSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FadeSpeed", fields.FieldFloat(value=value)
            )

    @property
    def cooldown_time(self) -> np.float32 | None:
        """The CooldownTime field value."""
        member = self.get_member("CooldownTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cooldown_time.setter
    def cooldown_time(self, value: np.float32) -> None:
        """Set the CooldownTime field value."""
        member = self.get_member("CooldownTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CooldownTime", fields.FieldFloat(value=value)
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

    @property
    def glow_color(self) -> primitives.ColorX | None:
        """The GlowColor field value."""
        member = self.get_member("GlowColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @glow_color.setter
    def glow_color(self, value: primitives.ColorX) -> None:
        """Set the GlowColor field value."""
        member = self.get_member("GlowColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlowColor", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color(self) -> str | None:
        """Target ID of the _emissiveColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_emissiveColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_color.setter
    def emissive_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _emissiveColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_emissiveColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_emissiveColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def rim_color(self) -> str | None:
        """Target ID of the _rimColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_rimColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rim_color.setter
    def rim_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _rimColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rimColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rimColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def sphere_radius(self) -> str | None:
        """Target ID of the _sphereRadius reference (targets IField[np.float32])."""
        member = self.get_member("_sphereRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sphere_radius.setter
    def sphere_radius(self, target: str | IField[np.float32] | None) -> None:
        """Set the _sphereRadius reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sphereRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sphereRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def sphere_extrude(self) -> str | None:
        """Target ID of the _sphereExtrude reference (targets IField[np.float32])."""
        member = self.get_member("_sphereExtrude")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sphere_extrude.setter
    def sphere_extrude(self, target: str | IField[np.float32] | None) -> None:
        """Set the _sphereExtrude reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sphereExtrude")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sphereExtrude",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def collider_radius(self) -> str | None:
        """Target ID of the _colliderRadius reference (targets IField[np.float32])."""
        member = self.get_member("_colliderRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_radius.setter
    def collider_radius(self, target: str | IField[np.float32] | None) -> None:
        """Set the _colliderRadius reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

