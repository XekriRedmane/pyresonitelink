"""Generated component: ParseQuantity."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParseQuantity(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Parse Quantity node takes in a string containing a written quantity value, along with the string of the default unit to assume if no explicit unit is present as part of the input string. It returns the parsed quantity value as a quantity type and a bool indicating wether it parsed successfully.

To create this node, you need to specify a valid quantity type for its generic parameter. Examples: ``Mass``, ``Time``, and ``Voltage``.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Quantity

    Parameterize with a value type::

        ParseQuantity[primitives.Float]
        ParseQuantity[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<>"

    def __init__(self, str_: str | INodeObjectOutput[primitives.String] | None = None, default_unit: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            default_unit: Initial value for DefaultUnit.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_
        if default_unit is not None:
            self.default_unit = default_unit

    @property
    def str_(self) -> str | None:
        """The string to parse."""
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @str_.setter
    def str_(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Str reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Str",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def default_unit(self) -> str | None:
        """The default unit to assume if no unit is present in the input string."""
        member = self.get_member("DefaultUnit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_unit.setter
    def default_unit(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the DefaultUnit reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("DefaultUnit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultUnit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def value(self) -> members.EmptyElement | None:
        """The parsed quantity value."""
        member = self.get_member("Value")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @value.setter
    def value(self, value: members.EmptyElement) -> None:
        """Set Value. The parsed quantity value."""
        self.set_member("Value", value)

    @property
    def is_parsed(self) -> members.EmptyElement | None:
        """Wether the input string was parsed successfully."""
        member = self.get_member("IsParsed")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_parsed.setter
    def is_parsed(self, value: members.EmptyElement) -> None:
        """Set IsParsed. Wether the input string was parsed successfully."""
        self.set_member("IsParsed", value)

