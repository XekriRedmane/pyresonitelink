"""Generated component: ObjectWriteLatch."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput


class ObjectWriteLatch(GenericComponent[T]):
    """Write latches take a Variable (Variable) as a global input, and the Variable will determine what SetValue (Generic) and ResetValue (Generic) will take as a value. The set and reset value inputs will never take different types from each other.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Actions

    Parameterize with a value type::

        ObjectWriteLatch[primitives.Float]
        ObjectWriteLatch[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ObjectWriteLatch<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ObjectWriteLatch<>"

    def __init__(self, on_set: str | INodeOperation | None = None, on_reset: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, variable: str | IVariable | None = None, set_value: str | INodeObjectOutput[T] | None = None, reset_value: str | INodeObjectOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_set: Initial value for OnSet.
            on_reset: Initial value for OnReset.
            on_fail: Initial value for OnFail.
            variable: Initial value for Variable.
            set_value: Initial value for SetValue.
            reset_value: Initial value for ResetValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_set is not None:
            self.on_set = on_set
        if on_reset is not None:
            self.on_reset = on_reset
        if on_fail is not None:
            self.on_fail = on_fail
        if variable is not None:
            self.variable = variable
        if set_value is not None:
            self.set_value = set_value
        if reset_value is not None:
            self.reset_value = reset_value

    @property
    def on_set(self) -> str | None:
        """Target ID of the OnSet reference (targets INodeOperation)."""
        member = self.get_member("OnSet")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_set.setter
    def on_set(self, target: str | INodeOperation | None) -> None:
        """Set the OnSet reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSet")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSet",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

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
    def set_(self) -> members.EmptyElement | None:
        """The Set member."""
        member = self.get_member("Set")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @set_.setter
    def set_(self, value: members.EmptyElement) -> None:
        """Set the Set member."""
        self.set_member("Set", value)

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
    def set_value(self) -> str | None:
        """Target ID of the SetValue reference (targets INodeObjectOutput[T])."""
        member = self.get_member("SetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @set_value.setter
    def set_value(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the SetValue reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("SetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

    @property
    def reset_value(self) -> str | None:
        """Target ID of the ResetValue reference (targets INodeObjectOutput[T])."""
        member = self.get_member("ResetValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reset_value.setter
    def reset_value(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the ResetValue reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("ResetValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ResetValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

