"""Generated component: AvatarDebugHand."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.hierarchy_material_target import HierarchyMaterialTarget
from pyresonitelink.generated._types.pbs_metallic import PBS_Metallic
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarDebugHand(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Debug hand is a component that is used to show a debug visual when the Biped Rig Component has its "Debug Hand" sync delegate pressed.

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
        """The slots of the mesh renderers that are being used to debug the hand."""
        member = self.get_member("_objects")
        if isinstance(member, members.SyncList):
            return member
        return None

    @objects.setter
    def objects(self, value: members.SyncList) -> None:
        """Set _objects. The slots of the mesh renderers that are being used to debug the hand."""
        self.set_member("_objects", value)

    @property
    def material_target(self) -> str | None:
        """The component used as a reference to apply ``_material`` to the debug when ``_material`` changes."""
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
        """The material this component is using to render the visual"""
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

