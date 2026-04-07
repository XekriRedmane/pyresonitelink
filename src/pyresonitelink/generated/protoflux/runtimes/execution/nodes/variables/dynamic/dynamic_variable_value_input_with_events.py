"""Generated component: DynamicVariableValueInputWithEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicVariableValueInputWithEvents(GenericComponent[T], IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic

    Parameterize with a value type::

        DynamicVariableValueInputWithEvents[np.float32]
        DynamicVariableValueInputWithEvents[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<>"

    def __init__(self, variable_name: str | IGlobalValueProxy[str] | None = None, detecting_user: str | INodeObjectOutput[User] | None = None, on_space_linked: str | ISyncNodeOperation | None = None, on_space_unlinked: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            detecting_user: Initial value for DetectingUser.
            on_space_linked: Initial value for OnSpaceLinked.
            on_space_unlinked: Initial value for OnSpaceUnlinked.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if detecting_user is not None:
            self.detecting_user = detecting_user
        if on_space_linked is not None:
            self.on_space_linked = on_space_linked
        if on_space_unlinked is not None:
            self.on_space_unlinked = on_space_unlinked

    @property
    def variable_name(self) -> str | None:
        """Target ID of the VariableName reference (targets IGlobalValueProxy[str])."""
        member = self.get_member("VariableName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @variable_name.setter
    def variable_name(self, target: str | IGlobalValueProxy[str] | None) -> None:
        """Set the VariableName reference by target ID or IGlobalValueProxy[str] instance."""
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
    def detecting_user(self) -> str | None:
        """Target ID of the DetectingUser reference (targets INodeObjectOutput[User])."""
        member = self.get_member("DetectingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detecting_user.setter
    def detecting_user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the DetectingUser reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("DetectingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DetectingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def on_space_linked(self) -> str | None:
        """Target ID of the OnSpaceLinked reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnSpaceLinked")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_space_linked.setter
    def on_space_linked(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnSpaceLinked reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSpaceLinked")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSpaceLinked",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def on_space_unlinked(self) -> str | None:
        """Target ID of the OnSpaceUnlinked reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnSpaceUnlinked")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_space_unlinked.setter
    def on_space_unlinked(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnSpaceUnlinked reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSpaceUnlinked")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSpaceUnlinked",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
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

