"""Generated component: AvatarNameTagAssigner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarNameTagAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarNameTagAssigner component is responsible for setting the nametag's text, color, and the ContactLink UserId. It basically defines what a nametag is.

    Category: Users/Common Avatar System/Nameplate

    **Behavior**: If an avatar contains this component when equipped, the user's default nametag will be hidden for those who have custom nameplates enabled.

When an avatar is dequipped the DequippedLabel contents will be written to the LabelTargets, by default the DequippedLabel is "---".
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarNameTagAssigner"

    def __init__(self, dequipped_label: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
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
        """A list of string fields that should be set to the user's display name when this component is under an avatar and the avatar is equipped."""
        member = self.get_member("LabelTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @label_targets.setter
    def label_targets(self, value: members.SyncList) -> None:
        """Set LabelTargets. A list of string fields that should be set to the user's display name when this component is under an avatar and the avatar is equipped."""
        self.set_member("LabelTargets", value)

    @property
    def user_id_targets(self) -> members.SyncList | None:
        """A list of string fields that should be set to the user's UUID (aka UserID) when this component is under an avatar and the avatar is equipped."""
        member = self.get_member("UserIdTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @user_id_targets.setter
    def user_id_targets(self, value: members.SyncList) -> None:
        """Set UserIdTargets. A list of string fields that should be set to the user's UUID (aka UserID) when this component is under an avatar and the avatar is equipped."""
        self.set_member("UserIdTargets", value)

    @property
    def color_targets(self) -> members.SyncList | None:
        """A list of colorX fields that should be set to the user's special color when this component is under an avatar and the avatar is equipped. Supporters, Staff, Mentors, and Moderators are some of the many users that get custom name plate colors through this component."""
        member = self.get_member("ColorTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @color_targets.setter
    def color_targets(self, value: members.SyncList) -> None:
        """Set ColorTargets. A list of colorX fields that should be set to the user's special color when this component is under an avatar and the avatar is equipped. Supporters, Staff, Mentors, and Moderators are some of the many users that get custom name plate colors through this component."""
        self.set_member("ColorTargets", value)

    @property
    def outline_targets(self) -> members.SyncList | None:
        """Similar to ``ColorTargets`` but for the outline."""
        member = self.get_member("OutlineTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @outline_targets.setter
    def outline_targets(self, value: members.SyncList) -> None:
        """Set OutlineTargets. Similar to ``ColorTargets`` but for the outline."""
        self.set_member("OutlineTargets", value)

    @property
    def background_targets(self) -> members.SyncList | None:
        """Similar to ``ColorTargets`` but for the background color."""
        member = self.get_member("BackgroundTargets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @background_targets.setter
    def background_targets(self, value: members.SyncList) -> None:
        """Set BackgroundTargets. Similar to ``ColorTargets`` but for the background color."""
        self.set_member("BackgroundTargets", value)

    @property
    def dequipped_label(self) -> primitives.String | None:
        """What text should display when the avatar this component belongs to is dequipped. You can be creative with this!"""
        member = self.get_member("DequippedLabel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dequipped_label.setter
    def dequipped_label(self, value: primitives.String) -> None:
        """Set the DequippedLabel field value."""
        member = self.get_member("DequippedLabel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DequippedLabel", fields.FieldString(value=value)
            )

