"""Generated component: OnContactEnd."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.icollider import ICollider
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnContactEnd(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.OnContactEnd.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics/Events
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.OnContactEnd"

    def __init__(self, collider: str | IGlobalValueProxy[ICollider] | None = None, on_event: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            collider: Initial value for Collider.
            on_event: Initial value for OnEvent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if collider is not None:
            self.collider = collider
        if on_event is not None:
            self.on_event = on_event

    @property
    def collider(self) -> str | None:
        """Target ID of the Collider reference (targets IGlobalValueProxy[ICollider])."""
        member = self.get_member("Collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | IGlobalValueProxy[ICollider] | None) -> None:
        """Set the Collider reference by target ID or IGlobalValueProxy[ICollider] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.ICollider>'),
            )

    @property
    def on_event(self) -> str | None:
        """Target ID of the OnEvent reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnEvent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_event.setter
    def on_event(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnEvent reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnEvent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnEvent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def other(self) -> members.EmptyElement | None:
        """The Other member."""
        member = self.get_member("Other")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @other.setter
    def other(self, value: members.EmptyElement) -> None:
        """Set the Other member."""
        self.set_member("Other", value)

