"""Generated component: LegacyGlowCircle."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyGlowCircle(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyGlowCircle.

    Category: Rendering/Visuals
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyGlowCircle"

    def __init__(self, radius: np.float32 | None = None, height: np.float32 | None = None, color: primitives.ColorX | None = None, cylinder_offset: str | IField[primitives.Float3] | None = None, cylinder_radius: str | IField[np.float32] | None = None, cylinder_height: str | IField[np.float32] | None = None, circle_quad_size: str | IField[primitives.Float2] | None = None, circle_tint: str | IField[primitives.ColorX] | None = None, cylinder_tint: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            height: Initial value for Height.
            color: Initial value for Color.
            cylinder_offset: Initial value for _cylinderOffset.
            cylinder_radius: Initial value for _cylinderRadius.
            cylinder_height: Initial value for _cylinderHeight.
            circle_quad_size: Initial value for _circleQuadSize.
            circle_tint: Initial value for _circleTint.
            cylinder_tint: Initial value for _cylinderTint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if height is not None:
            self.height = height
        if color is not None:
            self.color = color
        if cylinder_offset is not None:
            self.cylinder_offset = cylinder_offset
        if cylinder_radius is not None:
            self.cylinder_radius = cylinder_radius
        if cylinder_height is not None:
            self.cylinder_height = cylinder_height
        if circle_quad_size is not None:
            self.circle_quad_size = circle_quad_size
        if circle_tint is not None:
            self.circle_tint = circle_tint
        if cylinder_tint is not None:
            self.cylinder_tint = cylinder_tint

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
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def cylinder_offset(self) -> str | None:
        """Target ID of the _cylinderOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_cylinderOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cylinder_offset.setter
    def cylinder_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _cylinderOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cylinderOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cylinderOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def cylinder_radius(self) -> str | None:
        """Target ID of the _cylinderRadius reference (targets IField[np.float32])."""
        member = self.get_member("_cylinderRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cylinder_radius.setter
    def cylinder_radius(self, target: str | IField[np.float32] | None) -> None:
        """Set the _cylinderRadius reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cylinderRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cylinderRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def cylinder_height(self) -> str | None:
        """Target ID of the _cylinderHeight reference (targets IField[np.float32])."""
        member = self.get_member("_cylinderHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cylinder_height.setter
    def cylinder_height(self, target: str | IField[np.float32] | None) -> None:
        """Set the _cylinderHeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cylinderHeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cylinderHeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def circle_quad_size(self) -> str | None:
        """Target ID of the _circleQuadSize reference (targets IField[primitives.Float2])."""
        member = self.get_member("_circleQuadSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @circle_quad_size.setter
    def circle_quad_size(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _circleQuadSize reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_circleQuadSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_circleQuadSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def circle_tint(self) -> str | None:
        """Target ID of the _circleTint reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_circleTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @circle_tint.setter
    def circle_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _circleTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_circleTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_circleTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def cylinder_tint(self) -> str | None:
        """Target ID of the _cylinderTint reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_cylinderTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cylinder_tint.setter
    def cylinder_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _cylinderTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cylinderTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cylinderTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

