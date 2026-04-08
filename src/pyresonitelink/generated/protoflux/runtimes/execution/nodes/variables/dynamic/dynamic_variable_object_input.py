"""Generated component: DynamicVariableObjectInput."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicVariableObjectInput(GenericComponent[T], IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableObjectInput<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic

    Parameterize with a value type::

        DynamicVariableObjectInput[primitives.Float]
        DynamicVariableObjectInput[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableObjectInput<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableObjectInput<>"

    def __init__(self, variable_name: str | IGlobalValueProxy[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def variable_name(self) -> str | None:
        """Target ID of the VariableName reference (targets IGlobalValueProxy[primitives.String])."""
        member = self.get_member("VariableName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @variable_name.setter
    def variable_name(self, target: str | IGlobalValueProxy[primitives.String] | None) -> None:
        """Set the VariableName reference by target ID or IGlobalValueProxy[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("VariableName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VariableName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<string>'),
            )

    @property
    def value(self) -> members.EmptyElement | None:
        """The Value member."""
        member = self.get_member("Value")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @value.setter
    def value(self, value: members.EmptyElement) -> None:
        """Set the Value member."""
        self.set_member("Value", value)

    @property
    def has_value(self) -> members.EmptyElement | None:
        """The HasValue member."""
        member = self.get_member("HasValue")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_value.setter
    def has_value(self, value: members.EmptyElement) -> None:
        """Set the HasValue member."""
        self.set_member("HasValue", value)

