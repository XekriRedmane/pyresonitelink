"""Generated component: DataModelBooleanToggle."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.idata_model_store import IDataModelStore
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataModelBooleanToggle(GeneratedComponent, IVariable, IDataModelStore, IProtoFluxEngineProxyNode, IMappableNode, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Data Model Boolean Toggle or Boolean Latch is a node that can be pulsed to toggle a Data Model Boolean between true and false.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelBooleanToggle"

    def __init__(self, on_set: str | INodeOperation | None = None, on_reset: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_set: Initial value for OnSet.
            on_reset: Initial value for OnReset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_set is not None:
            self.on_set = on_set
        if on_reset is not None:
            self.on_reset = on_reset

    @property
    def set_(self) -> members.EmptyElement | None:
        """Set the state to True."""
        member = self.get_member("Set")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @set_.setter
    def set_(self, value: members.EmptyElement) -> None:
        """Set Set. Set the state to True."""
        self.set_member("Set", value)

    @property
    def reset(self) -> members.EmptyElement | None:
        """Set the state to False."""
        member = self.get_member("Reset")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reset.setter
    def reset(self, value: members.EmptyElement) -> None:
        """Set Reset. Set the state to False."""
        self.set_member("Reset", value)

    @property
    def toggle(self) -> members.EmptyElement | None:
        """Toggle the state to the opposite state."""
        member = self.get_member("Toggle")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @toggle.setter
    def toggle(self, value: members.EmptyElement) -> None:
        """Set Toggle. Toggle the state to the opposite state."""
        self.set_member("Toggle", value)

    @property
    def on_set(self) -> str | None:
        """Fires when Set is pulsed or Toggle has switched the state to True."""
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
        """Fires when Reset is pulsed or Toggle has switched the state to False."""
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

