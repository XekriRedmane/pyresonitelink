"""Generated component: WorkerInspector."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorkerInspector(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """A worker inspector (as opposed to Scene Inspector) is an inspector which only shows a single worker such as a component. When you grab a component reference and click Primary it will usually create one of these inspectors. You can grab sub-objects from some components which will create one of these inspectors when clicking Primary. Some workers are only obtainable via Ref Hacking which is one of the Things to Avoid.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorkerInspector"

    def __init__(self, target_container: str | Worker | None = None, target_worker: str | Worker | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_container: Initial value for _targetContainer.
            target_worker: Initial value for _targetWorker.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_container is not None:
            self.target_container = target_container
        if target_worker is not None:
            self.target_worker = target_worker

    @property
    def target_container(self) -> str | None:
        """The container which holds this component or proto component (FrooxEngine.ComponentBase)."""
        member = self.get_member("_targetContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_container.setter
    def target_container(self, target: str | Worker | None) -> None:
        """Set the _targetContainer reference by target ID or Worker instance."""
        target_id: str | None = target.id if isinstance(target, Worker) else target  # type: ignore[assignment]
        member = self.get_member("_targetContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Worker'),
            )

    @property
    def target_worker(self) -> str | None:
        """The component or proto component (FrooxEngine.ComponentBase) to view."""
        member = self.get_member("_targetWorker")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_worker.setter
    def target_worker(self, target: str | Worker | None) -> None:
        """Set the _targetWorker reference by target ID or Worker instance."""
        target_id: str | None = target.id if isinstance(target, Worker) else target  # type: ignore[assignment]
        member = self.get_member("_targetWorker")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetWorker",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Worker'),
            )

