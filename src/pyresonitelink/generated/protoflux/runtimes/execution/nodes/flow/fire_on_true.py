"""Generated component: FireOnTrue."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FireOnTrue(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnTrue.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnTrue"

    def __init__(self, only_for_user: str | INodeObjectOutput[User] | None = None, on_changed: str | ISyncNodeOperation | None = None, condition: str | INodeValueOutput[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            only_for_user: Initial value for OnlyForUser.
            on_changed: Initial value for OnChanged.
            condition: Initial value for Condition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if only_for_user is not None:
            self.only_for_user = only_for_user
        if on_changed is not None:
            self.on_changed = on_changed
        if condition is not None:
            self.condition = condition

    @property
    def only_for_user(self) -> str | None:
        """Target ID of the OnlyForUser reference (targets INodeObjectOutput[User])."""
        member = self.get_member("OnlyForUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @only_for_user.setter
    def only_for_user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the OnlyForUser reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnlyForUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnlyForUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def on_changed(self) -> str | None:
        """Target ID of the OnChanged reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnChanged")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_changed.setter
    def on_changed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnChanged reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnChanged")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnChanged",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def condition(self) -> str | None:
        """Target ID of the Condition reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @condition.setter
    def condition(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Condition reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Condition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

