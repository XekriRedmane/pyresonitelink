"""Generated component: BoxMeshGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.box_mesh import BoxMesh
from pyresonitelink.generated._types.box_gizmo import BoxGizmo
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxMeshGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BoxMeshGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxMeshGizmo"

    def __init__(self, target: str | BoxMesh | None = None, cube_gizmo: str | BoxGizmo | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            cube_gizmo: Initial value for _cubeGizmo.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if cube_gizmo is not None:
            self.cube_gizmo = cube_gizmo

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets BoxMesh)."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | BoxMesh | None) -> None:
        """Set the _target reference by target ID or BoxMesh instance."""
        target_id: str | None = target.id if isinstance(target, BoxMesh) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxMesh'),
            )

    @property
    def cube_gizmo(self) -> str | None:
        """Target ID of the _cubeGizmo reference (targets BoxGizmo)."""
        member = self.get_member("_cubeGizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cube_gizmo.setter
    def cube_gizmo(self, target: str | BoxGizmo | None) -> None:
        """Set the _cubeGizmo reference by target ID or BoxGizmo instance."""
        target_id: str | None = target.id if isinstance(target, BoxGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_cubeGizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cubeGizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxGizmo'),
            )

