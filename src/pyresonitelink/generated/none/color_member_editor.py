"""Generated component: ColorMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.color_dialog_interface import ColorDialogInterface
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColorMemberEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColorMemberEditor"

    def __init__(self, continuous: primitives.Bool | None = None, path: primitives.String | None = None, target: str | IField | None = None, labels: primitives.Bool | None = None, vertical: primitives.Bool | None = None, color_drive: str | IField[primitives.ColorX] | None = None, color_drive_no_alpha: str | IField[primitives.ColorX] | None = None, color_dialog: str | ColorDialogInterface | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            labels: Initial value for Labels.
            vertical: Initial value for Vertical.
            color_drive: Initial value for _colorDrive.
            color_drive_no_alpha: Initial value for _colorDriveNoAlpha.
            color_dialog: Initial value for _colorDialog.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if continuous is not None:
            self.continuous = continuous
        if path is not None:
            self.path = path
        if target is not None:
            self.target = target
        if labels is not None:
            self.labels = labels
        if vertical is not None:
            self.vertical = vertical
        if color_drive is not None:
            self.color_drive = color_drive
        if color_drive_no_alpha is not None:
            self.color_drive_no_alpha = color_drive_no_alpha
        if color_dialog is not None:
            self.color_dialog = color_dialog

    @property
    def continuous(self) -> primitives.Bool | None:
        """The Continuous field value."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: primitives.Bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

    @property
    def path(self) -> primitives.String | None:
        """The _path field value."""
        member = self.get_member("_path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
        """Set the _path field value."""
        member = self.get_member("_path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_path", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets IField)."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField | None) -> None:
        """Set the _target reference by target ID or IField instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField'),
            )

    @property
    def labels(self) -> primitives.Bool | None:
        """The Labels field value."""
        member = self.get_member("Labels")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @labels.setter
    def labels(self, value: primitives.Bool) -> None:
        """Set the Labels field value."""
        member = self.get_member("Labels")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Labels", fields.FieldBool(value=value)
            )

    @property
    def vertical(self) -> primitives.Bool | None:
        """The Vertical field value."""
        member = self.get_member("Vertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical.setter
    def vertical(self, value: primitives.Bool) -> None:
        """Set the Vertical field value."""
        member = self.get_member("Vertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertical", fields.FieldBool(value=value)
            )

    @property
    def color_drive(self) -> str | None:
        """Target ID of the _colorDrive reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_colorDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_drive.setter
    def color_drive(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _colorDrive reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colorDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def color_drive_no_alpha(self) -> str | None:
        """Target ID of the _colorDriveNoAlpha reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_colorDriveNoAlpha")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_drive_no_alpha.setter
    def color_drive_no_alpha(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _colorDriveNoAlpha reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colorDriveNoAlpha")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorDriveNoAlpha",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def color_dialog(self) -> str | None:
        """Target ID of the _colorDialog reference (targets ColorDialogInterface)."""
        member = self.get_member("_colorDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_dialog.setter
    def color_dialog(self, target: str | ColorDialogInterface | None) -> None:
        """Set the _colorDialog reference by target ID or ColorDialogInterface instance."""
        target_id: str | None = target.id if isinstance(target, ColorDialogInterface) else target  # type: ignore[assignment]
        member = self.get_member("_colorDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ColorDialogInterface'),
            )

