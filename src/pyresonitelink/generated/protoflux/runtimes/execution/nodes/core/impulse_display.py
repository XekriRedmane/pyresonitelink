"""Generated component: ImpulseDisplay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ImpulseDisplay(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Impulse Display node displays incoming impulses to the node. The node will display:

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseDisplay"

    def __init__(self, debug_text: str | Text | None = None, timeline_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            debug_text: Initial value for _debugText.
            timeline_root: Initial value for _timelineRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if debug_text is not None:
            self.debug_text = debug_text
        if timeline_root is not None:
            self.timeline_root = timeline_root

    @property
    def debug_text(self) -> str | None:
        """Target ID of the _debugText reference (targets Text)."""
        member = self.get_member("_debugText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_text.setter
    def debug_text(self, target: str | Text | None) -> None:
        """Set the _debugText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_debugText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_debugText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def timeline_root(self) -> str | None:
        """Target ID of the _timelineRoot reference (targets Slot)."""
        member = self.get_member("_timelineRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timeline_root.setter
    def timeline_root(self, target: str | Slot | None) -> None:
        """Set the _timelineRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_timelineRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timelineRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

