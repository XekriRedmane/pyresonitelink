"""Generated component: OnDestroying."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnDestroying(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The On Destroying node sends an impulse out of Trigger whenever the node is marked for destruction. This will not preserve Async tasks, as since those create delays they will be destroyed before execution of the task finishes.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Events
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.OnDestroying"

    def __init__(self, trigger: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            trigger: Initial value for Trigger.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if trigger is not None:
            self.trigger = trigger

    @property
    def trigger(self) -> str | None:
        """Target ID of the Trigger reference (targets ISyncNodeOperation)."""
        member = self.get_member("Trigger")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trigger.setter
    def trigger(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Trigger reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Trigger")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Trigger",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

