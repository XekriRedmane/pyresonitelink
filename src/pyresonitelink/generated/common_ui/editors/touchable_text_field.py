"""Generated component: TouchableTextField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchableTextField(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The TouchableTextField component, similar to a TextField for UIX, this component when combined with a TextEditor on the same slot, will allow any text in the world to be clicked on to make it become editable.

This allows the text to be edited in both directions: In the component and in the world directly.

    Category: Common UI/Editors

    Great for when you don't want to be bound by UIX to make editable texts.
    If the text is not responding or is not editing properly, try adding the
    BoxCollider component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchableTextField"

    def __init__(self, text_editor: str | TextEditor | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, edit_mode_only: primitives.Bool | None = None, active_user_root_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text_editor: Initial value for TextEditor.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            edit_mode_only: Initial value for EditModeOnly.
            active_user_root_only: Initial value for ActiveUserRootOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text_editor is not None:
            self.text_editor = text_editor
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if active_user_root_only is not None:
            self.active_user_root_only = active_user_root_only

    @property
    def text_editor(self) -> str | None:
        """The TextField to allow for bi-directional editing."""
        member = self.get_member("TextEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_editor.setter
    def text_editor(self, target: str | TextEditor | None) -> None:
        """Set the TextEditor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("TextEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def accept_out_of_sight_touch(self) -> primitives.Bool | None:
        """The AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
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
    def edit_mode_only(self) -> primitives.Bool | None:
        """Allows for the user to only edit this text in Edit Mode."""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: primitives.Bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def active_user_root_only(self) -> primitives.Bool | None:
        """Allows to only be editable when under the active user."""
        member = self.get_member("ActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_user_root_only.setter
    def active_user_root_only(self, value: primitives.Bool) -> None:
        """Set the ActiveUserRootOnly field value."""
        member = self.get_member("ActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUserRootOnly", fields.FieldBool(value=value)
            )

