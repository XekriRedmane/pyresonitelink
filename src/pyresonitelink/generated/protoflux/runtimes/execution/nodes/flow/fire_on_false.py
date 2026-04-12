"""Generated component: FireOnFalse."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class FireOnFalse(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The FireOnFalse node will listen for changes on its input bool and fire an impulse for the specified user whenever the input turns from ``True`` to ``False`` across updates.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow

    **See also**: * FireOnLocalFalse will fire an impulse for every user that detects ``False`` rather than a specific user.
* FireOnTrue
* FireOnChange
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnFalse"

    def __init__(self, only_for_user: str | INodeObjectOutput[User] | None = None, on_changed: str | ISyncNodeOperation | None = None, condition: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The user that will listen to the boolean and fire the impulse."""
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
        """Fires a single impulse from the specified user whenever the provided input turns from ``True`` to ``False`` across updates."""
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
        """The bool that should be listened to for changes."""
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @condition.setter
    def condition(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Condition reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Condition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

