"""Generated component: TypeProxy."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iproto_flux_node import IProtoFluxNode
from pyresonitelink.generated._types.ilast_value_proxy import ILastValueProxy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeProxy(GeneratedComponent, ILastValueProxy, IWorldEventReceiver):
    """Wrapper for [ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.TypeProxy.
    """

    COMPONENT_TYPE = "[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.TypeProxy"

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

    @property
    def last(self) -> members.FieldEnum | None:
        """The Last member."""
        member = self.get_member("Last")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @last.setter
    def last(self, value: members.FieldEnum) -> None:
        """Set the Last member."""
        self.set_member("Last", value)

