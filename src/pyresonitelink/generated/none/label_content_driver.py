"""Generated component: LabelContentDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LabelContentDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LabelContentDriver.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LabelContentDriver"

    def __init__(self, auto_update: bool | None = None, padding: primitives.Float2 | None = None, base_width: np.float32 | None = None, orient_at_local_user: bool | None = None, content_root: str | Slot | None = None, target_point: str | Slot | None = None, content_rotation: primitives.FloatQ | None = None, content_rotation_drive: str | IField[primitives.FloatQ] | None = None, label_position: str | IField[primitives.Float3] | None = None, label_width: str | IField[np.float32] | None = None, line_width: str | IField[np.float32] | None = None, label_rotation: str | IField[primitives.FloatQ] | None = None, point_position: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_update: Initial value for AutoUpdate.
            padding: Initial value for Padding.
            base_width: Initial value for BaseWidth.
            orient_at_local_user: Initial value for OrientAtLocalUser.
            content_root: Initial value for _contentRoot.
            target_point: Initial value for _targetPoint.
            content_rotation: Initial value for _contentRotation.
            content_rotation_drive: Initial value for _contentRotationDrive.
            label_position: Initial value for _labelPosition.
            label_width: Initial value for _labelWidth.
            line_width: Initial value for _lineWidth.
            label_rotation: Initial value for _labelRotation.
            point_position: Initial value for _pointPosition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_update is not None:
            self.auto_update = auto_update
        if padding is not None:
            self.padding = padding
        if base_width is not None:
            self.base_width = base_width
        if orient_at_local_user is not None:
            self.orient_at_local_user = orient_at_local_user
        if content_root is not None:
            self.content_root = content_root
        if target_point is not None:
            self.target_point = target_point
        if content_rotation is not None:
            self.content_rotation = content_rotation
        if content_rotation_drive is not None:
            self.content_rotation_drive = content_rotation_drive
        if label_position is not None:
            self.label_position = label_position
        if label_width is not None:
            self.label_width = label_width
        if line_width is not None:
            self.line_width = line_width
        if label_rotation is not None:
            self.label_rotation = label_rotation
        if point_position is not None:
            self.point_position = point_position

    @property
    def auto_update(self) -> bool | None:
        """The AutoUpdate field value."""
        member = self.get_member("AutoUpdate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_update.setter
    def auto_update(self, value: bool) -> None:
        """Set the AutoUpdate field value."""
        member = self.get_member("AutoUpdate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoUpdate", fields.FieldBool(value=value)
            )

    @property
    def padding(self) -> primitives.Float2 | None:
        """The Padding field value."""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: primitives.Float2) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldFloat2(value=value)
            )

    @property
    def base_width(self) -> np.float32 | None:
        """The BaseWidth field value."""
        member = self.get_member("BaseWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_width.setter
    def base_width(self, value: np.float32) -> None:
        """Set the BaseWidth field value."""
        member = self.get_member("BaseWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseWidth", fields.FieldFloat(value=value)
            )

    @property
    def content_orient_space(self) -> members.SyncObject | None:
        """The ContentOrientSpace member."""
        member = self.get_member("ContentOrientSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @content_orient_space.setter
    def content_orient_space(self, value: members.SyncObject) -> None:
        """Set the ContentOrientSpace member."""
        self.set_member("ContentOrientSpace", value)

    @property
    def orient_at_local_user(self) -> bool | None:
        """The OrientAtLocalUser field value."""
        member = self.get_member("OrientAtLocalUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orient_at_local_user.setter
    def orient_at_local_user(self, value: bool) -> None:
        """Set the OrientAtLocalUser field value."""
        member = self.get_member("OrientAtLocalUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrientAtLocalUser", fields.FieldBool(value=value)
            )

    @property
    def content_root(self) -> str | None:
        """Target ID of the _contentRoot reference (targets Slot)."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_point(self) -> str | None:
        """Target ID of the _targetPoint reference (targets Slot)."""
        member = self.get_member("_targetPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_point.setter
    def target_point(self, target: str | Slot | None) -> None:
        """Set the _targetPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_targetPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def content_rotation(self) -> primitives.FloatQ | None:
        """The _contentRotation field value."""
        member = self.get_member("_contentRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @content_rotation.setter
    def content_rotation(self, value: primitives.FloatQ) -> None:
        """Set the _contentRotation field value."""
        member = self.get_member("_contentRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_contentRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def content_rotation_drive(self) -> str | None:
        """Target ID of the _contentRotationDrive reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_contentRotationDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_rotation_drive.setter
    def content_rotation_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _contentRotationDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_contentRotationDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRotationDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def label_position(self) -> str | None:
        """Target ID of the _labelPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_labelPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label_position.setter
    def label_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _labelPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_labelPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_labelPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def label_width(self) -> str | None:
        """Target ID of the _labelWidth reference (targets IField[np.float32])."""
        member = self.get_member("_labelWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label_width.setter
    def label_width(self, target: str | IField[np.float32] | None) -> None:
        """Set the _labelWidth reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_labelWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_labelWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def line_width(self) -> str | None:
        """Target ID of the _lineWidth reference (targets IField[np.float32])."""
        member = self.get_member("_lineWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_width.setter
    def line_width(self, target: str | IField[np.float32] | None) -> None:
        """Set the _lineWidth reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_lineWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lineWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def label_rotation(self) -> str | None:
        """Target ID of the _labelRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_labelRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label_rotation.setter
    def label_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _labelRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_labelRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_labelRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def point_position(self) -> str | None:
        """Target ID of the _pointPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_pointPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point_position.setter
    def point_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _pointPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pointPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pointPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

