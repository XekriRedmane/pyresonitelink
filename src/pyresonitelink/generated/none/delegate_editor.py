"""Generated component: DelegateEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_delegate import ISyncDelegate
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelegateEditor(GeneratedComponent, IUIGrabReceiver, IUIGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DelegateEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DelegateEditor"

    def __init__(self, target_delegate: str | ISyncDelegate | None = None, text_drive: str | IField[primitives.String] | None = None, button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_delegate: Initial value for _targetDelegate.
            text_drive: Initial value for _textDrive.
            button: Initial value for _button.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_delegate is not None:
            self.target_delegate = target_delegate
        if text_drive is not None:
            self.text_drive = text_drive
        if button is not None:
            self.button = button

    @property
    def target_delegate(self) -> str | None:
        """Target ID of the _targetDelegate reference (targets ISyncDelegate)."""
        member = self.get_member("_targetDelegate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_delegate.setter
    def target_delegate(self, target: str | ISyncDelegate | None) -> None:
        """Set the _targetDelegate reference by target ID or ISyncDelegate instance."""
        target_id: str | None = target.id if isinstance(target, ISyncDelegate) else target  # type: ignore[assignment]
        member = self.get_member("_targetDelegate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetDelegate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncDelegate'),
            )

    @property
    def text_drive(self) -> str | None:
        """Target ID of the _textDrive reference (targets IField[primitives.String])."""
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_drive.setter
    def text_drive(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _textDrive reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def button(self) -> str | None:
        """Target ID of the _button reference (targets Button)."""
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button.setter
    def button(self, target: str | Button | None) -> None:
        """Set the _button reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

