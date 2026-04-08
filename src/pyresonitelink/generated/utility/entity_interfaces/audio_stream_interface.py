"""Generated component: AudioStreamInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iaudio_stream import IAudioStream
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioStreamInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioStreamInterface.

    Category: Utility/Entity Interfaces
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioStreamInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, source: str | SyncRef[IAudioStream] | None = None, bitrate: str | IField[primitives.Int] | None = None, volume: str | IField[primitives.Float] | None = None, spatialize: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            source: Initial value for Source.
            bitrate: Initial value for Bitrate.
            volume: Initial value for Volume.
            spatialize: Initial value for Spatialize.
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
        if source is not None:
            self.source = source
        if bitrate is not None:
            self.bitrate = bitrate
        if volume is not None:
            self.volume = volume
        if spatialize is not None:
            self.spatialize = spatialize

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
    def source(self) -> str | None:
        """Target ID of the Source reference (targets SyncRef[IAudioStream])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | SyncRef[IAudioStream] | None) -> None:
        """Set the Source reference by target ID or SyncRef[IAudioStream] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IAudioStream>'),
            )

    @property
    def bitrate(self) -> str | None:
        """Target ID of the Bitrate reference (targets IField[primitives.Int])."""
        member = self.get_member("Bitrate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bitrate.setter
    def bitrate(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the Bitrate reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Bitrate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bitrate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def volume(self) -> str | None:
        """Target ID of the Volume reference (targets IField[primitives.Float])."""
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
        """Target ID of the Spatialize reference (targets IField[primitives.Bool])."""
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

