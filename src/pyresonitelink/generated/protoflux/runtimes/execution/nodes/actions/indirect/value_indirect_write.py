"""Generated component: ValueIndirectWrite."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput


class ValueIndirectWrite(GenericComponent[T]):
    """Indirect writes can be commonly found in legacy content that has been migrated from other platforms. Indirect writes take Variable (Variable) as an input, and the type that Variable wraps will determine what Value (Generic) will take as a value. The node will then write Value (Generic) to the field Variable (Variable) wraps.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Actions/Indirect

    **Indirect Write or Write?**: The difference between a Write node and an Indirect Write is in how they reference the variable they affect.  In a Write node, what is called a Global is used to hold the variable, and this reference is only evaluated when the Protoflux starts executing.  Therefore, code that changes the variable for a normal Write during its execution will have no effect.

In contrast, an Indirect Write node uses a normal input for its variable, which is evaluated whenever the node is called.  This allows for the variable to be programmatically changed during the flow of execution, such as via a multiplexer with an indeterminate number of possible inputs.

In short, if you're writing to a static variable stick with normal Write, while if your code might change the variable you're writing to during execution use Indirect Write instead.

    Parameterize with a value type::

        ValueIndirectWrite[primitives.Float]
        ValueIndirectWrite[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<>"

    def __init__(self, on_written: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, variable: str | INodeObjectOutput[IVariable] | None = None, value: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_written: Initial value for OnWritten.
            on_fail: Initial value for OnFail.
            variable: Initial value for Variable.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_written is not None:
            self.on_written = on_written
        if on_fail is not None:
            self.on_fail = on_fail
        if variable is not None:
            self.variable = variable
        if value is not None:
            self.value = value

    @property
    def on_written(self) -> str | None:
        """Target ID of the OnWritten reference (targets INodeOperation)."""
        member = self.get_member("OnWritten")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_written.setter
    def on_written(self, target: str | INodeOperation | None) -> None:
        """Set the OnWritten reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
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
        """Target ID of the OnFail reference (targets INodeOperation)."""
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_fail.setter
    def on_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
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
        """Target ID of the Variable reference (targets INodeObjectOutput[IVariable])."""
        member = self.get_member("Variable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @variable.setter
    def variable(self, target: str | INodeObjectOutput[IVariable] | None) -> None:
        """Set the Variable reference by target ID or INodeObjectOutput[IVariable] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Variable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Variable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<,>>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

