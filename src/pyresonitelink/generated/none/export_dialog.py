"""Generated component: ExportDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ExportDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """See Exporting.

    See Exporting.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ExportDialog"

    def __init__(self, selected_export_option: primitives.Int | None = None, export_name: str | TextField | None = None, target_folder: primitives.String | None = None, edit_enabled: primitives.Bool | None = None, cancel: str | Button | None = None, export: str | Button | None = None, file_name: str | IField | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selected_export_option: Initial value for SelectedExportOption.
            export_name: Initial value for ExportName.
            target_folder: Initial value for _targetFolder.
            edit_enabled: Initial value for EditEnabled.
            cancel: Initial value for _cancel.
            export: Initial value for _export.
            file_name: Initial value for FileName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selected_export_option is not None:
            self.selected_export_option = selected_export_option
        if export_name is not None:
            self.export_name = export_name
        if target_folder is not None:
            self.target_folder = target_folder
        if edit_enabled is not None:
            self.edit_enabled = edit_enabled
        if cancel is not None:
            self.cancel = cancel
        if export is not None:
            self.export = export
        if file_name is not None:
            self.file_name = file_name

    @property
    def selected_export_option(self) -> primitives.Int | None:
        """What Export Option is selected."""
        member = self.get_member("SelectedExportOption")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_export_option.setter
    def selected_export_option(self, value: primitives.Int) -> None:
        """Set the SelectedExportOption field value."""
        member = self.get_member("SelectedExportOption")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedExportOption", fields.FieldInt(value=value)
            )

    @property
    def export_name(self) -> str | None:
        """The name of the Export file."""
        member = self.get_member("ExportName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @export_name.setter
    def export_name(self, target: str | TextField | None) -> None:
        """Set the ExportName reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("ExportName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ExportName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def target_folder(self) -> primitives.String | None:
        """The target folder location to Export to."""
        member = self.get_member("_targetFolder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_folder.setter
    def target_folder(self, value: primitives.String) -> None:
        """Set the _targetFolder field value."""
        member = self.get_member("_targetFolder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_targetFolder", fields.FieldString(value=value)
            )

    @property
    def edit_enabled(self) -> primitives.Bool | None:
        """Whether this component is edit enabled."""
        member = self.get_member("EditEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_enabled.setter
    def edit_enabled(self, value: primitives.Bool) -> None:
        """Set the EditEnabled field value."""
        member = self.get_member("EditEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditEnabled", fields.FieldBool(value=value)
            )

    @property
    def cancel(self) -> str | None:
        """The button for canceling the export."""
        member = self.get_member("_cancel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cancel.setter
    def cancel(self, target: str | Button | None) -> None:
        """Set the _cancel reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_cancel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cancel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def export(self) -> str | None:
        """The button to start the export."""
        member = self.get_member("_export")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @export.setter
    def export(self, target: str | Button | None) -> None:
        """Set the _export reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_export")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_export",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def export_options(self) -> members.SyncList | None:
        """The kinds of Export options available."""
        member = self.get_member("_exportOptions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @export_options.setter
    def export_options(self, value: members.SyncList) -> None:
        """Set _exportOptions. The kinds of Export options available."""
        self.set_member("_exportOptions", value)

    @property
    def file_name(self) -> str | None:
        """The name of the file when exporting."""
        member = self.get_member("FileName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @file_name.setter
    def file_name(self, target: str | IField | None) -> None:
        """Set the FileName reference by target ID or IField instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FileName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FileName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField'),
            )

