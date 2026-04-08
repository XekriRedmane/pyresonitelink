"""Generated component: UserSpawn."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserSpawn(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The User Spawn node is an event that fires when a user spawns/respawns in the current world this node is in, as well as providing that user.

    Category: ProtoFlux/Runtimes/Execution/Nodes/World
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.UserSpawn"

    def __init__(self, only_host: str | INodeValueOutput[primitives.Bool] | None = None, on_spawn: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            only_host: Initial value for OnlyHost.
            on_spawn: Initial value for OnSpawn.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if only_host is not None:
            self.only_host = only_host
        if on_spawn is not None:
            self.on_spawn = on_spawn

    @property
    def only_host(self) -> str | None:
        """Target ID of the OnlyHost reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("OnlyHost")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @only_host.setter
    def only_host(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the OnlyHost reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnlyHost")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnlyHost",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_spawn(self) -> str | None:
        """Target ID of the OnSpawn reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnSpawn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_spawn.setter
    def on_spawn(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnSpawn reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSpawn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSpawn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def spawned_user(self) -> members.EmptyElement | None:
        """The SpawnedUser member."""
        member = self.get_member("SpawnedUser")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @spawned_user.setter
    def spawned_user(self, value: members.EmptyElement) -> None:
        """Set the SpawnedUser member."""
        self.set_member("SpawnedUser", value)

