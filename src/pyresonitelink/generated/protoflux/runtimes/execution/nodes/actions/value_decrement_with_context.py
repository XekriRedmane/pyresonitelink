"""Generated component: ValueDecrementWithContext."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueDecrementWithContext(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Decrements take Variable (Variable Pseudo-generic) as a global, and will decrease the value that Variable (Variable Pseudo-generic) points to by 1.

If you need to subtract more than 1 from your value, use the Sub node instead.|suggestion}}

    Category: ProtoFlux/Runtimes/Execution/Nodes/Actions
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<,>"

    def __init__(self, on_written: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, variable: str | IVariable | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_written: Initial value for OnWritten.
            on_fail: Initial value for OnFail.
            variable: Initial value for Variable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_written is not None:
            self.on_written = on_written
        if on_fail is not None:
            self.on_fail = on_fail
        if variable is not None:
            self.variable = variable

    @property
    def on_written(self) -> str | None:
        """sends an impulse after * (Call) has been impulsed and the value pointed to by Variable (Variable Pseudo-generic) has been decremented."""
        member = self.get_member("OnWritten")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_written.setter
    def on_written(self, target: str | INodeOperation | None) -> None:
        """Set the OnWritten reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnWritten")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnWritten",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_fail(self) -> str | None:
        """sends an impulse after * (Call) has been impulsed and the value wasn't able to be decremented due to a missing target or Variable (Variable Pseudo-generic) not pointing to a valid IValue`1."""
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_fail.setter
    def on_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def variable(self) -> str | None:
        """Target ID of the Variable reference (targets IVariable)."""
        member = self.get_member("Variable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @variable.setter
    def variable(self, target: str | IVariable | None) -> None:
        """Set the Variable reference by target ID or IVariable instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Variable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Variable",
                members.Reference(targetId=target_id, targetType='[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<,>'),
            )

