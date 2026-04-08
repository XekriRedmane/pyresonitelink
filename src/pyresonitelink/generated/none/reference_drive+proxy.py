"""Generated component: ReferenceDrive+Proxy."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iproto_flux_node import IProtoFluxNode
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceDrive+Proxy(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.CoreNodes.ReferenceDrive<>+Proxy.

    Parameterize with a value type::

        ReferenceDrive+Proxy[np.float32]
        ReferenceDrive+Proxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.CoreNodes.ReferenceDrive<>+Proxy"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ProtoFlux.CoreNodes.ReferenceDrive<>+Proxy"

    def __init__(self, node: str | IProtoFluxNode | None = None, drive: str | SyncRef[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            drive: Initial value for Drive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if drive is not None:
            self.drive = drive

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
    def drive(self) -> str | None:
        """Target ID of the Drive reference (targets SyncRef[T])."""
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @drive.setter
    def drive(self, target: str | SyncRef[T] | None) -> None:
        """Set the Drive reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Drive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Drive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

