"""Generated component: AsyncDynamicImpulseReceiverWithObject."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AsyncDynamicImpulseReceiverWithObject(GenericComponent[T], IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithObject<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async

    Parameterize with a value type::

        AsyncDynamicImpulseReceiverWithObject[np.float32]
        AsyncDynamicImpulseReceiverWithObject[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithObject<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithObject<>"

    def __init__(self, tag: str | IGlobalValueProxy[str] | None = None, on_triggered: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tag: Initial value for Tag.
            on_triggered: Initial value for OnTriggered.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tag is not None:
            self.tag = tag
        if on_triggered is not None:
            self.on_triggered = on_triggered

    @property
    def tag(self) -> str | None:
        """Target ID of the Tag reference (targets IGlobalValueProxy[str])."""
        member = self.get_member("Tag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tag.setter
    def tag(self, target: str | IGlobalValueProxy[str] | None) -> None:
        """Set the Tag reference by target ID or IGlobalValueProxy[str] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Tag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<string>'),
            )

    @property
    def on_triggered(self) -> str | None:
        """Target ID of the OnTriggered reference (targets INodeOperation)."""
        member = self.get_member("OnTriggered")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_triggered.setter
    def on_triggered(self, target: str | INodeOperation | None) -> None:
        """Set the OnTriggered reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnTriggered")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnTriggered",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
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

