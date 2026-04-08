"""Generated component: OnGrabbableReleased."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OnGrabbableReleased(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """On Grabbable Released is a ProtoFlux node that monitors an IGrabbable for when something or someone lets go of it and sends an Impulse.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/Grabbable
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableReleased"

    def __init__(self, grabbable: str | IGlobalValueProxy[IGrabbable] | None = None, on_released: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            grabbable: Initial value for Grabbable.
            on_released: Initial value for OnReleased.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if grabbable is not None:
            self.grabbable = grabbable
        if on_released is not None:
            self.on_released = on_released

    @property
    def grabbable(self) -> str | None:
        """Target ID of the Grabbable reference (targets IGlobalValueProxy[IGrabbable])."""
        member = self.get_member("Grabbable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbable.setter
    def grabbable(self, target: str | IGlobalValueProxy[IGrabbable] | None) -> None:
        """Set the Grabbable reference by target ID or IGlobalValueProxy[IGrabbable] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Grabbable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Grabbable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.IGrabbable>'),
            )

    @property
    def on_released(self) -> str | None:
        """Target ID of the OnReleased reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnReleased")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_released.setter
    def on_released(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnReleased reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReleased")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReleased",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

