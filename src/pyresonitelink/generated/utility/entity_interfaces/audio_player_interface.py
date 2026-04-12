"""Generated component: AudioPlayerInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.audio_type_group import AudioTypeGroup
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioPlayerInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """The AudioPlayerInterface component is used on AudioClip objects that are spawned in by the user to allow the engine to interface with the stored audio clip.

This is a favorite-able item. See Favorites.

    Category: Utility/Entity Interfaces

    This can be attached to a slot in order for the user to make own audio
    clip interface for when they import an audio clip. Although, it may be
    easier to edit the default existing audio clip player interface.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioPlayerInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, url: str | IField[str] | None = None, clip: str | AssetRef[AudioClip] | None = None, group: str | IField[AudioTypeGroup] | None = None, volume: str | IField[primitives.Float] | None = None, spatialize: str | IField[primitives.Bool] | None = None, doppler: str | IField[primitives.Float] | None = None, default_audio_clip: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            url: Initial value for URL.
            clip: Initial value for Clip.
            group: Initial value for Group.
            volume: Initial value for Volume.
            spatialize: Initial value for Spatialize.
            doppler: Initial value for Doppler.
            default_audio_clip: Initial value for DefaultAudioClip.
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
        if url is not None:
            self.url = url
        if clip is not None:
            self.clip = clip
        if group is not None:
            self.group = group
        if volume is not None:
            self.volume = volume
        if spatialize is not None:
            self.spatialize = spatialize
        if doppler is not None:
            self.doppler = doppler
        if default_audio_clip is not None:
            self.default_audio_clip = default_audio_clip

    @property
    def item_name(self) -> str | None:
        """The name of the audio clip."""
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
        """The user that spawned this audio clip."""
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
        """The field of the UserRef that stores the spawning user's id."""
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
        """Whether this audio clip interface is a spawned interface or one being edited currently by the user. Usually set to true by the game when loaded as a user's favorite audio clip player"""
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
    def url(self) -> str | None:
        """The field of the URI on the Type:AudioClip this component interfaces with."""
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url.setter
    def url(self, target: str | IField[str] | None) -> None:
        """Set the URL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "URL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def clip(self) -> str | None:
        """The Type:AudioClip interfaced by this component."""
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clip.setter
    def clip(self, target: str | AssetRef[AudioClip] | None) -> None:
        """Set the Clip reference by target ID or AssetRef[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Clip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def group(self) -> str | None:
        """The audio group setting for this audio clip."""
        member = self.get_member("Group")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group.setter
    def group(self, target: str | IField[AudioTypeGroup] | None) -> None:
        """Set the Group reference by target ID or IField[AudioTypeGroup] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Group")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Group",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.AudioTypeGroup>'),
            )

    @property
    def volume(self) -> str | None:
        """The volume setting of this audio clip."""
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume.setter
    def volume(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Volume reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Volume",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def spatialize(self) -> str | None:
        """The Spatialize setting of the audio clip."""
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatialize.setter
    def spatialize(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Spatialize reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Spatialize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def doppler(self) -> str | None:
        """The Doppler setting of the audio clip."""
        member = self.get_member("Doppler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @doppler.setter
    def doppler(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Doppler reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Doppler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Doppler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def default_audio_clip(self) -> str | None:
        """The audio clip"""
        member = self.get_member("DefaultAudioClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_audio_clip.setter
    def default_audio_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the DefaultAudioClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("DefaultAudioClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultAudioClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

