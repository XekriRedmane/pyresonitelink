"""Generated component: DataModelObjectAssetRefStore+Store."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iproto_flux_node import IProtoFluxNode
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataModelObjectAssetRefStore+Store(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<>+Store.

    Parameterize with a value type::

        DataModelObjectAssetRefStore+Store[np.float32]
        DataModelObjectAssetRefStore+Store[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<>+Store"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<>+Store"

    def __init__(self, node: str | IProtoFluxNode | None = None, target: str | IAssetProvider[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if target is not None:
            self.target = target

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
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IAssetProvider[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IAssetProvider[T] | None) -> None:
        """Set the Target reference by target ID or IAssetProvider[T] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<T>'),
            )

