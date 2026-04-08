"""Generated component: NamePlateInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NamePlateInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.NamePlateInterface.

    Category: Utility/Entity Interfaces
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NamePlateInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, username: str | IField[primitives.String] | None = None, user_id: str | IField[primitives.String] | None = None, icon_url: str | IField[str] | None = None, target_user: str | SyncRef[User] | None = None, target_user_ref: str | UserRef | None = None, voice_stream: str | SyncRef[IWorldAudioDataSource] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            username: Initial value for Username.
            user_id: Initial value for UserID.
            icon_url: Initial value for IconURL.
            target_user: Initial value for TargetUser.
            target_user_ref: Initial value for TargetUserRef.
            voice_stream: Initial value for VoiceStream.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if item_name is not None:
            self.item_name = item_name
        if spawning_user is not None:
            self.spawning_user = spawning_user
        if spawning_user_id is not None:
            self.spawning_user_id = spawning_user_id
        if is_instance is not None:
            self.is_instance = is_instance
        if username is not None:
            self.username = username
        if user_id is not None:
            self.user_id = user_id
        if icon_url is not None:
            self.icon_url = icon_url
        if target_user is not None:
            self.target_user = target_user
        if target_user_ref is not None:
            self.target_user_ref = target_user_ref
        if voice_stream is not None:
            self.voice_stream = voice_stream

    @property
    def item_name(self) -> str | None:
        """Target ID of the ItemName reference (targets IField[primitives.String])."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def spawning_user(self) -> str | None:
        """Target ID of the SpawningUser reference (targets UserRef)."""
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user.setter
    def spawning_user(self, target: str | UserRef | None) -> None:
        """Set the SpawningUser reference by target ID or UserRef instance."""
        target_id: str | None = target.id if isinstance(target, UserRef) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserRef'),
            )

    @property
    def spawning_user_id(self) -> str | None:
        """Target ID of the SpawningUserID reference (targets IField[primitives.String])."""
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user_id.setter
    def spawning_user_id(self, target: str | IField[primitives.String] | None) -> None:
        """Set the SpawningUserID reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUserID",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def is_instance(self) -> primitives.Bool | None:
        """The IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_instance.setter
    def is_instance(self, value: primitives.Bool) -> None:
        """Set the IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsInstance", fields.FieldBool(value=value)
            )

    @property
    def username(self) -> str | None:
        """Target ID of the Username reference (targets IField[primitives.String])."""
        member = self.get_member("Username")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username.setter
    def username(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Username reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Username")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Username",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def user_id(self) -> str | None:
        """Target ID of the UserID reference (targets IField[primitives.String])."""
        member = self.get_member("UserID")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_id.setter
    def user_id(self, target: str | IField[primitives.String] | None) -> None:
        """Set the UserID reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UserID")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UserID",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def icon_url(self) -> str | None:
        """Target ID of the IconURL reference (targets IField[str])."""
        member = self.get_member("IconURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_url.setter
    def icon_url(self, target: str | IField[str] | None) -> None:
        """Set the IconURL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IconURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IconURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def target_user(self) -> str | None:
        """Target ID of the TargetUser reference (targets SyncRef[User])."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_user.setter
    def target_user(self, target: str | SyncRef[User] | None) -> None:
        """Set the TargetUser reference by target ID or SyncRef[User] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def target_user_ref(self) -> str | None:
        """Target ID of the TargetUserRef reference (targets UserRef)."""
        member = self.get_member("TargetUserRef")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_user_ref.setter
    def target_user_ref(self, target: str | UserRef | None) -> None:
        """Set the TargetUserRef reference by target ID or UserRef instance."""
        target_id: str | None = target.id if isinstance(target, UserRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetUserRef")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetUserRef",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserRef'),
            )

    @property
    def voice_stream(self) -> str | None:
        """Target ID of the VoiceStream reference (targets SyncRef[IWorldAudioDataSource])."""
        member = self.get_member("VoiceStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @voice_stream.setter
    def voice_stream(self, target: str | SyncRef[IWorldAudioDataSource] | None) -> None:
        """Set the VoiceStream reference by target ID or SyncRef[IWorldAudioDataSource] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("VoiceStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VoiceStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IWorldAudioDataSource>'),
            )

