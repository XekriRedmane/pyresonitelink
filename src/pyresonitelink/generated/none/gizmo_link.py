"""Generated component: GizmoLink."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GizmoLink(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GizmoLink.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GizmoLink"

    def __init__(self, worker: str | Worker | None = None, gizmo: str | IComponentGizmo | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            worker: Initial value for _worker.
            gizmo: Initial value for _gizmo.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if worker is not None:
            self.worker = worker
        if gizmo is not None:
            self.gizmo = gizmo

    @property
    def worker(self) -> str | None:
        """Target ID of the _worker reference (targets Worker)."""
        member = self.get_member("_worker")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @worker.setter
    def worker(self, target: str | Worker | None) -> None:
        """Set the _worker reference by target ID or Worker instance."""
        target_id: str | None = target.id if isinstance(target, Worker) else target  # type: ignore[assignment]
        member = self.get_member("_worker")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worker",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Worker'),
            )

    @property
    def gizmo(self) -> str | None:
        """Target ID of the _gizmo reference (targets IComponentGizmo)."""
        member = self.get_member("_gizmo")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gizmo.setter
    def gizmo(self, target: str | IComponentGizmo | None) -> None:
        """Set the _gizmo reference by target ID or IComponentGizmo instance."""
        target_id: str | None = target.id if isinstance(target, IComponentGizmo) else target  # type: ignore[assignment]
        member = self.get_member("_gizmo")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_gizmo",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IComponentGizmo'),
            )

    @property
    def type_(self) -> members.FieldEnum | None:
        """The _type member."""
        member = self.get_member("_type")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @type_.setter
    def type_(self, value: members.FieldEnum) -> None:
        """Set the _type member."""
        self.set_member("_type", value)

