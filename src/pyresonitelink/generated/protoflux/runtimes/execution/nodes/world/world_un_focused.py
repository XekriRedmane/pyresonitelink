"""Generated component: WorldUnFocused."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldUnFocused(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Added: 2026.5.11.1342

Fires impulse as the user when a user has unfocused on the world to another world, but is still in the world.

    Category: ProtoFlux/Runtimes/Execution/Nodes/World

    **Video**: 6QA9JuulYmI
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.WorldUnFocused"

    def __init__(self, on_un_focused: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_un_focused: Initial value for OnUnFocused.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_un_focused is not None:
            self.on_un_focused = on_un_focused

    @property
    def on_un_focused(self) -> str | None:
        """Target ID of the OnUnFocused reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnUnFocused")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_un_focused.setter
    def on_un_focused(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnUnFocused reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnUnFocused")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnUnFocused",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

