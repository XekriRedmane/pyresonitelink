"""Generated component: ShiftEnum."""

from typing import Any

E = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ShiftEnum(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """See Enums for a more in depth explaination on what Enums are.

Shift Enum is a ProtoFlux node that when provided an Enum will give an enum with the provided Delta (Int) offset from said enum numerically according to the Enums page. "*" and "Value" will never be different enum types.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Enums

    Parameterize with a value type::

        ShiftEnum[primitives.Float]
        ShiftEnum[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<>"

    def __init__(self, value: str | INodeValueOutput[E] | None = None, delta: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            delta: Initial value for Delta.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if delta is not None:
            self.delta = delta

    @property
    def value(self) -> str | None:
        """The Enum to start at."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[E] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[E] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<E>'),
            )

    @property
    def delta(self) -> str | None:
        """The offset from Value (Enum Generic) to use for the returned * (Enum Generic)."""
        member = self.get_member("Delta")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delta.setter
    def delta(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Delta reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Delta")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Delta",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

