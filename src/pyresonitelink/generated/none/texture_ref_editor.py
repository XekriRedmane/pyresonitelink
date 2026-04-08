"""Generated component: TextureRefEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureRefEditor(GeneratedComponent, IUIGrabReceiver, IUIGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextureRefEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureRefEditor"

    def __init__(self, target_ref: str | AssetRef[ITexture2D] | None = None, drive: str | AssetRef[ITexture2D] | None = None, clear_reference_button: str | Button | None = None, open_inspector_button: str | Button | None = None, copy_texture_button: str | Button | None = None, paste_texture_button: str | Button | None = None, reference_text: str | IField[primitives.String] | None = None, info_text: str | IField[primitives.String] | None = None, is_normal_map: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_ref: Initial value for _targetRef.
            drive: Initial value for _drive.
            clear_reference_button: Initial value for _clearReferenceButton.
            open_inspector_button: Initial value for _openInspectorButton.
            copy_texture_button: Initial value for _copyTextureButton.
            paste_texture_button: Initial value for _pasteTextureButton.
            reference_text: Initial value for _referenceText.
            info_text: Initial value for _infoText.
            is_normal_map: Initial value for _isNormalMap.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_ref is not None:
            self.target_ref = target_ref
        if drive is not None:
            self.drive = drive
        if clear_reference_button is not None:
            self.clear_reference_button = clear_reference_button
        if open_inspector_button is not None:
            self.open_inspector_button = open_inspector_button
        if copy_texture_button is not None:
            self.copy_texture_button = copy_texture_button
        if paste_texture_button is not None:
            self.paste_texture_button = paste_texture_button
        if reference_text is not None:
            self.reference_text = reference_text
        if info_text is not None:
            self.info_text = info_text
        if is_normal_map is not None:
            self.is_normal_map = is_normal_map

    @property
    def target_ref(self) -> str | None:
        """Target ID of the _targetRef reference (targets AssetRef[ITexture2D])."""
        member = self.get_member("_targetRef")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_ref.setter
    def target_ref(self, target: str | AssetRef[ITexture2D] | None) -> None:
        """Set the _targetRef reference by target ID or AssetRef[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("_targetRef")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetRef",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def drive(self) -> str | None:
        """Target ID of the _drive reference (targets AssetRef[ITexture2D])."""
        member = self.get_member("_drive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive.setter
    def drive(self, target: str | AssetRef[ITexture2D] | None) -> None:
        """Set the _drive reference by target ID or AssetRef[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("_drive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_drive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def clear_reference_button(self) -> str | None:
        """Target ID of the _clearReferenceButton reference (targets Button)."""
        member = self.get_member("_clearReferenceButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clear_reference_button.setter
    def clear_reference_button(self, target: str | Button | None) -> None:
        """Set the _clearReferenceButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_clearReferenceButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_clearReferenceButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def open_inspector_button(self) -> str | None:
        """Target ID of the _openInspectorButton reference (targets Button)."""
        member = self.get_member("_openInspectorButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @open_inspector_button.setter
    def open_inspector_button(self, target: str | Button | None) -> None:
        """Set the _openInspectorButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_openInspectorButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_openInspectorButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def copy_texture_button(self) -> str | None:
        """Target ID of the _copyTextureButton reference (targets Button)."""
        member = self.get_member("_copyTextureButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @copy_texture_button.setter
    def copy_texture_button(self, target: str | Button | None) -> None:
        """Set the _copyTextureButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_copyTextureButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_copyTextureButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def paste_texture_button(self) -> str | None:
        """Target ID of the _pasteTextureButton reference (targets Button)."""
        member = self.get_member("_pasteTextureButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @paste_texture_button.setter
    def paste_texture_button(self, target: str | Button | None) -> None:
        """Set the _pasteTextureButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_pasteTextureButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pasteTextureButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def reference_text(self) -> str | None:
        """Target ID of the _referenceText reference (targets IField[primitives.String])."""
        member = self.get_member("_referenceText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_text.setter
    def reference_text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _referenceText reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_referenceText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_referenceText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def info_text(self) -> str | None:
        """Target ID of the _infoText reference (targets IField[primitives.String])."""
        member = self.get_member("_infoText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @info_text.setter
    def info_text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _infoText reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_infoText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_infoText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def is_normal_map(self) -> primitives.Bool | None:
        """The _isNormalMap field value."""
        member = self.get_member("_isNormalMap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_normal_map.setter
    def is_normal_map(self, value: primitives.Bool) -> None:
        """Set the _isNormalMap field value."""
        member = self.get_member("_isNormalMap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isNormalMap", fields.FieldBool(value=value)
            )

