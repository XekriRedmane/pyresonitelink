"""Generated component: DynamicImpulseReceiverWithObject+Proxy."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iproto_flux_node import IProtoFluxNode
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicImpulseReceiverWithObject+Proxy(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithObject<>+Proxy.

    Parameterize with a value type::

        DynamicImpulseReceiverWithObject+Proxy[np.float32]
        DynamicImpulseReceiverWithObject+Proxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithObject<>+Proxy"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithObject<>+Proxy"

    def __init__(self, node: str | IProtoFluxNode | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node

    @property
    def node(self) -> str | None:
        """Target ID of the Node reference (targets IProtoFluxNode)."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | IProtoFluxNode | None) -> None:
        """Set the Node reference by target ID or IProtoFluxNode instance."""
        target_id: str | None = target.id if isinstance(target, IProtoFluxNode) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IProtoFluxNode'),
            )

    @property
    def path(self) -> members.SyncList | None:
        """The Path member."""
        member = self.get_member("Path")
        if isinstance(member, members.SyncList):
            return member
        return None

    @path.setter
    def path(self, value: members.SyncList) -> None:
        """Set the Path member."""
        self.set_member("Path", value)

