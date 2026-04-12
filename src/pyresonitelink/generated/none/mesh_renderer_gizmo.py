"""Generated component: MeshRendererGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.mesh_collider import MeshCollider
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.idev_mode_receiver import IDevModeReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshRendererGizmo(GeneratedComponent, IComponentGizmo, IDevModeReceiver, IWorldEventReceiver):
    """The MeshRenderer Gizmo is used to change the Bounding properties to a mesh object using the dev tool.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshRendererGizmo"

    def __init__(self, target: str | MeshRenderer | None = None, mesh_collider: str | MeshCollider | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            mesh_collider: Initial value for _meshCollider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if mesh_collider is not None:
            self.mesh_collider = mesh_collider

    @property
    def target(self) -> str | None:
        """The mesh renderer to edit."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | MeshRenderer | None) -> None:
        """Set the _target reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def mesh_collider(self) -> str | None:
        """The mesh collider to edit along with ``_target``."""
        member = self.get_member("_meshCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh_collider.setter
    def mesh_collider(self, target: str | MeshCollider | None) -> None:
        """Set the _meshCollider reference by target ID or MeshCollider instance."""
        target_id: str | None = target.id if isinstance(target, MeshCollider) else target  # type: ignore[assignment]
        member = self.get_member("_meshCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_meshCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshCollider'),
            )

