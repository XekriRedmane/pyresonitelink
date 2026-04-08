"""Generated component: AvatarDebugHand."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.hierarchy_material_target import HierarchyMaterialTarget
from pyresonitelink.generated._types.pbs_metallic import PBS_Metallic
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarDebugHand(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarDebugHand.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarDebugHand"

    def __init__(self, material_target: str | HierarchyMaterialTarget | None = None, material: str | PBS_Metallic | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material_target: Initial value for _materialTarget.
            material: Initial value for _material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material_target is not None:
            self.material_target = material_target
        if material is not None:
            self.material = material

    @property
    def objects(self) -> members.SyncList | None:
        """The _objects member."""
        member = self.get_member("_objects")
        if isinstance(member, members.SyncList):
            return member
        return None

    @objects.setter
    def objects(self, value: members.SyncList) -> None:
        """Set the _objects member."""
        self.set_member("_objects", value)

    @property
    def material_target(self) -> str | None:
        """Target ID of the _materialTarget reference (targets HierarchyMaterialTarget)."""
        member = self.get_member("_materialTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material_target.setter
    def material_target(self, target: str | HierarchyMaterialTarget | None) -> None:
        """Set the _materialTarget reference by target ID or HierarchyMaterialTarget instance."""
        target_id: str | None = target.id if isinstance(target, HierarchyMaterialTarget) else target  # type: ignore[assignment]
        member = self.get_member("_materialTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_materialTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.HierarchyMaterialTarget'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets PBS_Metallic)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | PBS_Metallic | None) -> None:
        """Set the _material reference by target ID or PBS_Metallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_Metallic) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_Metallic'),
            )

