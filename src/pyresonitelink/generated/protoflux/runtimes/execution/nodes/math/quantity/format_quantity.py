"""Generated component: FormatQuantity."""

from typing import Any

U = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FormatQuantity(GenericComponent[T], INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Format Quantity node takes in value as a quantity type, the unit in which the quantity should be displayed as a string, as well as wether to use the unit's long name instead of the short form. It returns a formatted string containing the quantity value in the specified unit.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Quantity

    Parameterize with a value type::

        FormatQuantity[primitives.Float]
        FormatQuantity[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<>"

    def __init__(self, value: str | INodeValueOutput[U] | None = None, format_unit: str | INodeObjectOutput[primitives.String] | None = None, format_number: str | INodeObjectOutput[primitives.String] | None = None, use_long_names: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            format_unit: Initial value for FormatUnit.
            format_number: Initial value for FormatNumber.
            use_long_names: Initial value for UseLongNames.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if format_unit is not None:
            self.format_unit = format_unit
        if format_number is not None:
            self.format_number = format_number
        if use_long_names is not None:
            self.use_long_names = use_long_names

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[U])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[U] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[U] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<U>'),
            )

    @property
    def format_unit(self) -> str | None:
        """Target ID of the FormatUnit reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("FormatUnit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_unit.setter
    def format_unit(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the FormatUnit reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FormatUnit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FormatUnit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def format_number(self) -> str | None:
        """Target ID of the FormatNumber reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("FormatNumber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_number.setter
    def format_number(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the FormatNumber reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FormatNumber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FormatNumber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def use_long_names(self) -> str | None:
        """Target ID of the UseLongNames reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("UseLongNames")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @use_long_names.setter
    def use_long_names(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the UseLongNames reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UseLongNames")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UseLongNames",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

