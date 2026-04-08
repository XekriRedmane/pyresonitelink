"""Generated component: TriggerHapticsOnController."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TriggerHapticsOnController(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Haptics.TriggerHapticsOnController.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Haptics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Haptics.TriggerHapticsOnController"

    def __init__(self, next: str | INodeOperation | None = None, side: str | INodeValueOutput[Chirality] | None = None, relative_intensity: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            side: Initial value for Side.
            relative_intensity: Initial value for RelativeIntensity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if side is not None:
            self.side = side
        if relative_intensity is not None:
            self.relative_intensity = relative_intensity

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def side(self) -> str | None:
        """Target ID of the Side reference (targets INodeValueOutput[Chirality])."""
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side.setter
    def side(self, target: str | INodeValueOutput[Chirality] | None) -> None:
        """Set the Side reference by target ID or INodeValueOutput[Chirality] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Side",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>'),
            )

    @property
    def relative_intensity(self) -> str | None:
        """Target ID of the RelativeIntensity reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("RelativeIntensity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @relative_intensity.setter
    def relative_intensity(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the RelativeIntensity reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RelativeIntensity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RelativeIntensity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

