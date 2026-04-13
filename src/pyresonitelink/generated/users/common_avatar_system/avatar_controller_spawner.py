"""Generated component: AvatarControllerSpawner."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.avatar_controller_info import AvatarControllerInfo
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarControllerSpawner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarControllerSpawner component will spawn the corrosponding controller for the user when placed on an avatar under either the right or left hand.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarControllerSpawner"

    def __init__(self, spawn_root: str | Slot | None = None, material_override: str | IAssetProvider[Material] | None = None, source_controller_info: str | AvatarControllerInfo | None = None, last_spawned: Type | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            spawn_root: Initial value for SpawnRoot.
            material_override: Initial value for MaterialOverride.
            source_controller_info: Initial value for _sourceControllerInfo.
            last_spawned: Initial value for _lastSpawned.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if spawn_root is not None:
            self.spawn_root = spawn_root
        if material_override is not None:
            self.material_override = material_override
        if source_controller_info is not None:
            self.source_controller_info = source_controller_info
        if last_spawned is not None:
            self.last_spawned = last_spawned

    @property
    def spawn_root(self) -> str | None:
        """Where to spawn the model. (The Component attaches a slot called "root" under this when spawning the model, that becomes the model root)"""
        member = self.get_member("SpawnRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawn_root.setter
    def spawn_root(self, target: str | Slot | None) -> None:
        """Set the SpawnRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SpawnRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawnRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def material_override(self) -> str | None:
        """What material to replace the spawned model's materials with upon spawning."""
        member = self.get_member("MaterialOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material_override.setter
    def material_override(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the MaterialOverride reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MaterialOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaterialOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def source_controller_info(self) -> str | None:
        """The controller info this component grabbed in order to find and generate the right model."""
        member = self.get_member("_sourceControllerInfo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_controller_info.setter
    def source_controller_info(self, target: str | AvatarControllerInfo | None) -> None:
        """Set the _sourceControllerInfo reference by target ID or AvatarControllerInfo instance."""
        target_id: str | None = target.id if isinstance(target, AvatarControllerInfo) else target  # type: ignore[assignment]
        member = self.get_member("_sourceControllerInfo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sourceControllerInfo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarControllerInfo'),
            )

    @property
    def last_spawned(self) -> Type | None:
        """The froox engine type of the last controller type this component generated."""
        member = self.get_member("_lastSpawned")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @last_spawned.setter
    def last_spawned(self, value: Type | str) -> None:
        """Set _lastSpawned. The froox engine type of the last controller type this component generated."""
        member = self.get_member("_lastSpawned")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_lastSpawned",
                members.FieldEnum(value=str(value)),
            )

