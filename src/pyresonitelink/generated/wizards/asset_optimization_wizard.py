"""Generated component: AssetOptimizationWizard."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.int_text_editor_parser import IntTextEditorParser
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetOptimizationWizard(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AssetOptimizationWizard.

    Category: Wizards
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetOptimizationWizard"

    def __init__(self, root: str | Slot | None = None, ignore_nonpersistent_users: bool | None = None, max_resolution: str | IntTextEditorParser | None = None, message: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            ignore_nonpersistent_users: Initial value for IgnoreNonpersistentUsers.
            max_resolution: Initial value for _maxResolution.
            message: Initial value for _message.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if ignore_nonpersistent_users is not None:
            self.ignore_nonpersistent_users = ignore_nonpersistent_users
        if max_resolution is not None:
            self.max_resolution = max_resolution
        if message is not None:
            self.message = message

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets Slot)."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def ignore_nonpersistent_users(self) -> bool | None:
        """The IgnoreNonpersistentUsers field value."""
        member = self.get_member("IgnoreNonpersistentUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_nonpersistent_users.setter
    def ignore_nonpersistent_users(self, value: bool) -> None:
        """Set the IgnoreNonpersistentUsers field value."""
        member = self.get_member("IgnoreNonpersistentUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreNonpersistentUsers", fields.FieldBool(value=value)
            )

    @property
    def max_resolution(self) -> str | None:
        """Target ID of the _maxResolution reference (targets IntTextEditorParser)."""
        member = self.get_member("_maxResolution")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_resolution.setter
    def max_resolution(self, target: str | IntTextEditorParser | None) -> None:
        """Set the _maxResolution reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_maxResolution")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maxResolution",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def message(self) -> str | None:
        """Target ID of the _message reference (targets Text)."""
        member = self.get_member("_message")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @message.setter
    def message(self, target: str | Text | None) -> None:
        """Set the _message reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_message")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_message",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

