"""Generated component: AvatarNameTagAssigner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarNameTagAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarNameTagAssigner.

    Category: Users/Common Avatar System/Nameplate
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarNameTagAssigner"

    def __init__(self, dequipped_label: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dequipped_label: Initial value for DequippedLabel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dequipped_label is not None:
            self.dequipped_label = dequipped_label

    @property
    def label_targets(self) -> members.SyncList | None:
        """The LabelTargets member."""
        member = self.get_member("LabelTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @label_targets.setter
    def label_targets(self, value: members.SyncList) -> None:
        """Set the LabelTargets member."""
        self.set_member("LabelTargets", value)

    @property
    def user_id_targets(self) -> members.SyncList | None:
        """The UserIdTargets member."""
        member = self.get_member("UserIdTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @user_id_targets.setter
    def user_id_targets(self, value: members.SyncList) -> None:
        """Set the UserIdTargets member."""
        self.set_member("UserIdTargets", value)

    @property
    def color_targets(self) -> members.SyncList | None:
        """The ColorTargets member."""
        member = self.get_member("ColorTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @color_targets.setter
    def color_targets(self, value: members.SyncList) -> None:
        """Set the ColorTargets member."""
        self.set_member("ColorTargets", value)

    @property
    def outline_targets(self) -> members.SyncList | None:
        """The OutlineTargets member."""
        member = self.get_member("OutlineTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @outline_targets.setter
    def outline_targets(self, value: members.SyncList) -> None:
        """Set the OutlineTargets member."""
        self.set_member("OutlineTargets", value)

    @property
    def background_targets(self) -> members.SyncList | None:
        """The BackgroundTargets member."""
        member = self.get_member("BackgroundTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @background_targets.setter
    def background_targets(self, value: members.SyncList) -> None:
        """Set the BackgroundTargets member."""
        self.set_member("BackgroundTargets", value)

    @property
    def dequipped_label(self) -> str | None:
        """The DequippedLabel field value."""
        member = self.get_member("DequippedLabel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dequipped_label.setter
    def dequipped_label(self, value: str) -> None:
        """Set the DequippedLabel field value."""
        member = self.get_member("DequippedLabel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DequippedLabel", fields.FieldString(value=value)
            )

