"""Generated component: ElapsedTimeTimeSpan."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ElapsedTimeTimeSpan(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.ElapsedTimeTimeSpan.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.ElapsedTimeTimeSpan"

    def __init__(self, on_reset: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_reset: Initial value for OnReset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_reset is not None:
            self.on_reset = on_reset

    @property
    def reset(self) -> members.EmptyElement | None:
        """The Reset member."""
        member = self.get_member("Reset")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reset.setter
    def reset(self, value: members.EmptyElement) -> None:
        """Set the Reset member."""
        self.set_member("Reset", value)

    @property
    def on_reset(self) -> str | None:
        """Target ID of the OnReset reference (targets INodeOperation)."""
        member = self.get_member("OnReset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_reset.setter
    def on_reset(self, target: str | INodeOperation | None) -> None:
        """Set the OnReset reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

