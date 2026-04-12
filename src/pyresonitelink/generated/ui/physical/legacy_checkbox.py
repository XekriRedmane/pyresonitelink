"""Generated component: LegacyCheckbox."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.bevel_box_mesh import BevelBoxMesh
from pyresonitelink.generated._types.legacy_horizontal_choice_bar import LegacyHorizontalChoiceBar
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.icheckbox import ICheckbox
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyCheckbox(GeneratedComponent, ICheckbox, ITouchable, IWorldEventReceiver):
    """The LegacyCheckbox component is used in old migrated content. This is a Legacy component and should not be used for new content. This should be replaced whenever possible.

    Category: UI/Physical

    Just dont.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyCheckbox"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, is_checked: primitives.Bool | None = None, is_enabled: primitives.Bool | None = None, drive_field: str | IField[primitives.Bool] | None = None, allow_write_back: primitives.Bool | None = None, size: primitives.Float | None = None, bevel_percent: primitives.Float | None = None, color: primitives.ColorX | None = None, shell_mesh: str | BevelBoxMesh | None = None, check_mesh: str | BevelBoxMesh | None = None, title_bar: str | LegacyHorizontalChoiceBar | None = None, shell_size: str | IField[primitives.Float3] | None = None, shell_bevel: str | IField[primitives.Float] | None = None, check_size: str | IField[primitives.Float3] | None = None, check_bevel: str | IField[primitives.Float] | None = None, collider_size: str | IField[primitives.Float3] | None = None, shell_material: str | PBS_RimMetallic | None = None, check_material: str | PBS_RimMetallic | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            is_checked: Initial value for IsChecked.
            is_enabled: Initial value for IsEnabled.
            drive_field: Initial value for DriveField.
            allow_write_back: Initial value for AllowWriteBack.
            size: Initial value for Size.
            bevel_percent: Initial value for BevelPercent.
            color: Initial value for Color.
            shell_mesh: Initial value for _shellMesh.
            check_mesh: Initial value for _checkMesh.
            title_bar: Initial value for _titleBar.
            shell_size: Initial value for _shellSize.
            shell_bevel: Initial value for _shellBevel.
            check_size: Initial value for _checkSize.
            check_bevel: Initial value for _checkBevel.
            collider_size: Initial value for _colliderSize.
            shell_material: Initial value for _shellMaterial.
            check_material: Initial value for _checkMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if is_checked is not None:
            self.is_checked = is_checked
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if drive_field is not None:
            self.drive_field = drive_field
        if allow_write_back is not None:
            self.allow_write_back = allow_write_back
        if size is not None:
            self.size = size
        if bevel_percent is not None:
            self.bevel_percent = bevel_percent
        if color is not None:
            self.color = color
        if shell_mesh is not None:
            self.shell_mesh = shell_mesh
        if check_mesh is not None:
            self.check_mesh = check_mesh
        if title_bar is not None:
            self.title_bar = title_bar
        if shell_size is not None:
            self.shell_size = shell_size
        if shell_bevel is not None:
            self.shell_bevel = shell_bevel
        if check_size is not None:
            self.check_size = check_size
        if check_bevel is not None:
            self.check_bevel = check_bevel
        if collider_size is not None:
            self.collider_size = collider_size
        if shell_material is not None:
            self.shell_material = shell_material
        if check_material is not None:
            self.check_material = check_material

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
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def is_checked(self) -> primitives.Bool | None:
        """Whether the checkbox is checked."""
        member = self.get_member("IsChecked")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_checked.setter
    def is_checked(self, value: primitives.Bool) -> None:
        """Set the IsChecked field value."""
        member = self.get_member("IsChecked")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsChecked", fields.FieldBool(value=value)
            )

    @property
    def is_enabled(self) -> primitives.Bool | None:
        """The IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_enabled.setter
    def is_enabled(self, value: primitives.Bool) -> None:
        """Set the IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsEnabled", fields.FieldBool(value=value)
            )

    @property
    def drive_field(self) -> str | None:
        """The field to drive with this checkbooks state."""
        member = self.get_member("DriveField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive_field.setter
    def drive_field(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the DriveField reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DriveField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DriveField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def allow_write_back(self) -> primitives.Bool | None:
        """Whether changes to the target value of ``DriveField`` are sent to this component's checked state instead."""
        member = self.get_member("AllowWriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_write_back.setter
    def allow_write_back(self, value: primitives.Bool) -> None:
        """Set the AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowWriteBack", fields.FieldBool(value=value)
            )

    @property
    def size(self) -> primitives.Float | None:
        """How big the check box is."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat(value=value)
            )

    @property
    def bevel_percent(self) -> primitives.Float | None:
        """How beveled the check box is."""
        member = self.get_member("BevelPercent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bevel_percent.setter
    def bevel_percent(self, value: primitives.Float) -> None:
        """Set the BevelPercent field value."""
        member = self.get_member("BevelPercent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BevelPercent", fields.FieldFloat(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The color of the check box."""
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
    def shell_mesh(self) -> str | None:
        """The outer shell of the check box."""
        member = self.get_member("_shellMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shell_mesh.setter
    def shell_mesh(self, target: str | BevelBoxMesh | None) -> None:
        """Set the _shellMesh reference by target ID or BevelBoxMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelBoxMesh) else target  # type: ignore[assignment]
        member = self.get_member("_shellMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shellMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelBoxMesh'),
            )

    @property
    def check_mesh(self) -> str | None:
        """The inner check box indicator of the check box."""
        member = self.get_member("_checkMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_mesh.setter
    def check_mesh(self, target: str | BevelBoxMesh | None) -> None:
        """Set the _checkMesh reference by target ID or BevelBoxMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelBoxMesh) else target  # type: ignore[assignment]
        member = self.get_member("_checkMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_checkMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelBoxMesh'),
            )

    @property
    def title_bar(self) -> str | None:
        """unused."""
        member = self.get_member("_titleBar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title_bar.setter
    def title_bar(self, target: str | LegacyHorizontalChoiceBar | None) -> None:
        """Set the _titleBar reference by target ID or LegacyHorizontalChoiceBar instance."""
        target_id: str | None = target.id if isinstance(target, LegacyHorizontalChoiceBar) else target  # type: ignore[assignment]
        member = self.get_member("_titleBar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_titleBar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyHorizontalChoiceBar'),
            )

    @property
    def shell_size(self) -> str | None:
        """The field to drive for the outer shell size mesh."""
        member = self.get_member("_shellSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shell_size.setter
    def shell_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _shellSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_shellSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shellSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def shell_bevel(self) -> str | None:
        """The field to drive for the outer shell bevel."""
        member = self.get_member("_shellBevel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shell_bevel.setter
    def shell_bevel(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _shellBevel reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_shellBevel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shellBevel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def check_size(self) -> str | None:
        """The field to drive for the check indicator size."""
        member = self.get_member("_checkSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_size.setter
    def check_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _checkSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_checkSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_checkSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def check_bevel(self) -> str | None:
        """The field to drive for the check indicator bevel."""
        member = self.get_member("_checkBevel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_bevel.setter
    def check_bevel(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _checkBevel reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_checkBevel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_checkBevel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def collider_size(self) -> str | None:
        """The field to drive for the collider size."""
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def shell_material(self) -> str | None:
        """The field to drive to set the shell material."""
        member = self.get_member("_shellMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shell_material.setter
    def shell_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _shellMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_shellMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shellMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def check_material(self) -> str | None:
        """The field to drive to set the check indicator material."""
        member = self.get_member("_checkMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_material.setter
    def check_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _checkMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_checkMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_checkMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

