"""Generated component: GizmoLink."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GizmoLink(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The GizmoLink component handles the Interaction and connection of every Gizmo with their respective target. This is usually invisible to users and their inspectors, but upon opening a new inspector on a target of a Gizmo it appears. It is unknown if this is a bug. This component along with Gizmos do not save with items but Gizmos can save with a world.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GizmoLink"

    def __init__(self, worker: str | Worker | None = None, gizmo: str | IComponentGizmo | None = None, type_: Type | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            worker: Initial value for _worker.
            gizmo: Initial value for _gizmo.
            type_: Initial value for _type.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if worker is not None:
            self.worker = worker
        if gizmo is not None:
            self.gizmo = gizmo
        if type_ is not None:
            self.type_ = type_

    @property
    def worker(self) -> str | None:
        """The logic handling this component."""
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
        """The Gizmo this is making a Link for."""
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
    def type_(self) -> Type | None:
        """The C# Type of what this is targeting."""
        member = self.get_member("_type")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @type_.setter
    def type_(self, value: Type | str) -> None:
        """Set _type. The C# Type of what this is targeting."""
        member = self.get_member("_type")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_type",
                members.FieldEnum(value=str(value)),
            )

