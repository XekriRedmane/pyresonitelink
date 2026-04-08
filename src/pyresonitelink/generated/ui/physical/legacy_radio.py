"""Generated component: LegacyRadio."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ico_sphere_mesh import IcoSphereMesh
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.legacy_radio_group import LegacyRadioGroup
from pyresonitelink.generated._types.iradio import IRadio
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyRadio(GeneratedComponent, IRadio, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyRadio.

    Category: UI/Physical
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyRadio"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: bool | None = None, accept_remote_touch: bool | None = None, is_enabled: bool | None = None, radius: np.float32 | None = None, color: primitives.ColorX | None = None, selected: bool | None = None, collider_radius: str | IField[np.float32] | None = None, icosphere: str | IcoSphereMesh | None = None, material: str | PBS_RimMetallic | None = None, group: str | LegacyRadioGroup | None = None, order_number: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            is_enabled: Initial value for IsEnabled.
            radius: Initial value for Radius.
            color: Initial value for Color.
            selected: Initial value for Selected.
            collider_radius: Initial value for _colliderRadius.
            icosphere: Initial value for _icosphere.
            material: Initial value for _material.
            group: Initial value for _group.
            order_number: Initial value for _orderNumber.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if radius is not None:
            self.radius = radius
        if color is not None:
            self.color = color
        if selected is not None:
            self.selected = selected
        if collider_radius is not None:
            self.collider_radius = collider_radius
        if icosphere is not None:
            self.icosphere = icosphere
        if material is not None:
            self.material = material
        if group is not None:
            self.group = group
        if order_number is not None:
            self.order_number = order_number

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets LegacyUIStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the Style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def accept_physical_touch(self) -> bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def is_enabled(self) -> bool | None:
        """The IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        """Set the IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsEnabled", fields.FieldBool(value=value)
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
    def selected(self) -> bool | None:
        """The Selected field value."""
        member = self.get_member("Selected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected.setter
    def selected(self, value: bool) -> None:
        """Set the Selected field value."""
        member = self.get_member("Selected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Selected", fields.FieldBool(value=value)
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

    @property
    def icosphere(self) -> str | None:
        """Target ID of the _icosphere reference (targets IcoSphereMesh)."""
        member = self.get_member("_icosphere")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icosphere.setter
    def icosphere(self, target: str | IcoSphereMesh | None) -> None:
        """Set the _icosphere reference by target ID or IcoSphereMesh instance."""
        target_id: str | None = target.id if isinstance(target, IcoSphereMesh) else target  # type: ignore[assignment]
        member = self.get_member("_icosphere")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_icosphere",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IcoSphereMesh'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets PBS_RimMetallic)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _material reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def group(self) -> str | None:
        """Target ID of the _group reference (targets LegacyRadioGroup)."""
        member = self.get_member("_group")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group.setter
    def group(self, target: str | LegacyRadioGroup | None) -> None:
        """Set the _group reference by target ID or LegacyRadioGroup instance."""
        target_id: str | None = target.id if isinstance(target, LegacyRadioGroup) else target  # type: ignore[assignment]
        member = self.get_member("_group")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_group",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyRadioGroup'),
            )

    @property
    def order_number(self) -> np.int32 | None:
        """The _orderNumber field value."""
        member = self.get_member("_orderNumber")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order_number.setter
    def order_number(self, value: np.int32) -> None:
        """Set the _orderNumber field value."""
        member = self.get_member("_orderNumber")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_orderNumber", fields.FieldInt(value=value)
            )

