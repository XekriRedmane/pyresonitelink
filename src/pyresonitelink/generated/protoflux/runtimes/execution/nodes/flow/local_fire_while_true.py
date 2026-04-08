"""Generated component: LocalFireWhileTrue."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_update_receiver import IExecutionUpdateReceiver
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalFireWhileTrue(GeneratedComponent, IExecutionUpdateReceiver, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Local Fire While True is a ProtoFlux node that will check Condition (bool) is true on the local machine rather on a specific user. Then the node will fire every game tick, sending impulses from OnUpdate (Call) on that specific user.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalFireWhileTrue"

    def __init__(self, on_update: str | ISyncNodeOperation | None = None, condition: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_update: Initial value for OnUpdate.
            condition: Initial value for Condition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_update is not None:
            self.on_update = on_update
        if condition is not None:
            self.condition = condition

    @property
    def on_update(self) -> str | None:
        """Target ID of the OnUpdate reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnUpdate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_update.setter
    def on_update(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnUpdate reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnUpdate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnUpdate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def condition(self) -> str | None:
        """Target ID of the Condition reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @condition.setter
    def condition(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Condition reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Condition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

