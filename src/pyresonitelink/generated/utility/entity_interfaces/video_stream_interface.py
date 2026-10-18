"""Generated component: VideoStreamInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoStreamInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VideoStreamInterface.

    Category: Utility/Entity Interfaces
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoStreamInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, texture: str | AssetRef[ITexture2D] | None = None, audio: str | SyncRef[IWorldAudioDataSource] | None = None, aspect_ratio: str | IField[primitives.Float] | None = None, stream_sink_url: str | IField[primitives.String] | None = None, stream_enabled: str | SyncRef[IField[primitives.Bool]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            texture: Initial value for Texture.
            audio: Initial value for Audio.
            aspect_ratio: Initial value for AspectRatio.
            stream_sink_url: Initial value for StreamSinkURL.
            stream_enabled: Initial value for StreamEnabled.
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
        if texture is not None:
            self.texture = texture
        if audio is not None:
            self.audio = audio
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if stream_sink_url is not None:
            self.stream_sink_url = stream_sink_url
        if stream_enabled is not None:
            self.stream_enabled = stream_enabled

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
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets AssetRef[ITexture2D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | AssetRef[ITexture2D] | None) -> None:
        """Set the Texture reference by target ID or AssetRef[ITexture2D] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def audio(self) -> str | None:
        """Target ID of the Audio reference (targets SyncRef[IWorldAudioDataSource])."""
        member = self.get_member("Audio")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio.setter
    def audio(self, target: str | SyncRef[IWorldAudioDataSource] | None) -> None:
        """Set the Audio reference by target ID or SyncRef[IWorldAudioDataSource] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Audio")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Audio",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IWorldAudioDataSource>'),
            )

    @property
    def aspect_ratio(self) -> str | None:
        """Target ID of the AspectRatio reference (targets IField[primitives.Float])."""
        member = self.get_member("AspectRatio")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @aspect_ratio.setter
    def aspect_ratio(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the AspectRatio reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("AspectRatio")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AspectRatio",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def stream_sink_url(self) -> str | None:
        """Target ID of the StreamSinkURL reference (targets IField[primitives.String])."""
        member = self.get_member("StreamSinkURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream_sink_url.setter
    def stream_sink_url(self, target: str | IField[primitives.String] | None) -> None:
        """Set the StreamSinkURL reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("StreamSinkURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StreamSinkURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def stream_enabled(self) -> str | None:
        """Target ID of the StreamEnabled reference (targets SyncRef[IField[primitives.Bool]])."""
        member = self.get_member("StreamEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream_enabled.setter
    def stream_enabled(self, target: str | SyncRef[IField[primitives.Bool]] | None) -> None:
        """Set the StreamEnabled reference by target ID or SyncRef[IField[primitives.Bool]] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("StreamEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StreamEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IField<bool>>'),
            )

