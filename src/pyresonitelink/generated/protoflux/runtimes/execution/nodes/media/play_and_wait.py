"""Generated component: PlayAndWait."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlayAndWait(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.PlayAndWait.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Media
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.PlayAndWait"

    def __init__(self, target: str | INodeObjectOutput[IPlayable] | None = None, on_started: str | INodeOperation | None = None, on_playback_finished: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            on_started: Initial value for OnStarted.
            on_playback_finished: Initial value for OnPlaybackFinished.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if on_started is not None:
            self.on_started = on_started
        if on_playback_finished is not None:
            self.on_playback_finished = on_playback_finished

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets INodeObjectOutput[IPlayable])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[IPlayable] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[IPlayable] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IPlayable>'),
            )

    @property
    def on_started(self) -> str | None:
        """Target ID of the OnStarted reference (targets INodeOperation)."""
        member = self.get_member("OnStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_started.setter
    def on_started(self, target: str | INodeOperation | None) -> None:
        """Set the OnStarted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_playback_finished(self) -> str | None:
        """Target ID of the OnPlaybackFinished reference (targets INodeOperation)."""
        member = self.get_member("OnPlaybackFinished")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_playback_finished.setter
    def on_playback_finished(self, target: str | INodeOperation | None) -> None:
        """Set the OnPlaybackFinished reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnPlaybackFinished")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnPlaybackFinished",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

