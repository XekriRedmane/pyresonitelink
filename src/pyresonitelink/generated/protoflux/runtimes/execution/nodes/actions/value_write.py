"""Generated component: ValueWrite."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput


class ValueWrite(GenericComponent[T]):
    """Writes take Variable (Variable) as an input, and the type that Variable wraps will determine what Value (Generic) will take as a value. The node will then write Value (Generic) to the field Variable (Variable) wraps.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Actions

    **Optimizations**: The Write node can also be used to write to a Protoflux Source node instead of writing to a variable that is connected to a Drive node, enabling programs be be written with one less supporting node per Write node

    Parameterize with a value type::

        ValueWrite[primitives.Float]
        ValueWrite[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<>"

    def __init__(self, on_written: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, variable: str | IVariable | None = None, value: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
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
        """sends an impulse after * (Call) has been impulsed and the value has been written."""
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
        """sends an impulse after * (Call) has been impulsed and the value wasn't able to be written due to a missing target or a missing Variable (Variable) value"""
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
        """Target ID of the Variable reference (targets IVariable)."""
        member = self.get_member("Variable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @variable.setter
    def variable(self, target: str | IVariable | None) -> None:
        """Set the Variable reference by target ID or IVariable instance."""
        target_id: str | None = target.id if isinstance(target, IVariable) else target  # type: ignore[assignment]
        member = self.get_member("Variable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Variable",
                members.Reference(targetId=target_id, targetType='[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<,>'),
            )

    @property
    def value(self) -> str | None:
        """Value to write to the value pointed to by Variable (Variable)"""
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

