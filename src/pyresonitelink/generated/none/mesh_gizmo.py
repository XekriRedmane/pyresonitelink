"""Generated component: MeshGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.static_mesh import StaticMesh
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """The Mesh Gizmo component is used to set up and generate the visuals/behavior of mesh orbs which are physical item/references to mesh data.

    Used in mesh orbs used with the Mesh Tool and with scene inspectors for
    allowing physical hold able access to meshes for use in static and
    skinned mesh renderers.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshGizmo"

    def __init__(self, target: str | StaticMesh | None = None, inspector_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            inspector_root: Initial value for _inspectorRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if inspector_root is not None:
            self.inspector_root = inspector_root

    @property
    def target(self) -> str | None:
        """The static mesh that this is referencing and displaying."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | StaticMesh | None) -> None:
        """Set the _target reference by target ID or StaticMesh instance."""
        target_id: str | None = target.id if isinstance(target, StaticMesh) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticMesh'),
            )

    @property
    def inspector_root(self) -> str | None:
        """The inspector this component generated when it was made."""
        member = self.get_member("_inspectorRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inspector_root.setter
    def inspector_root(self, target: str | Slot | None) -> None:
        """Set the _inspectorRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_inspectorRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inspectorRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

