"""Generated component: ComposeFinger."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.finger_type import FingerType
from pyresonitelink.generated._types.finger_segment_type import FingerSegmentType
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ComposeFinger(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Compose Finger is a ProtoFlux node that allows you to get a body node enum from a FingerType, FingerSegmentType and a Chirality also known as a side.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Body Nodes
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodes.ComposeFinger"

    def __init__(self, finger: str | INodeValueOutput[FingerType] | None = None, segment: str | INodeValueOutput[FingerSegmentType] | None = None, chirality: str | INodeValueOutput[Chirality] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            finger: Initial value for Finger.
            segment: Initial value for Segment.
            chirality: Initial value for Chirality.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if finger is not None:
            self.finger = finger
        if segment is not None:
            self.segment = segment
        if chirality is not None:
            self.chirality = chirality

    @property
    def finger(self) -> str | None:
        """Target ID of the Finger reference (targets INodeValueOutput[FingerType])."""
        member = self.get_member("Finger")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @finger.setter
    def finger(self, target: str | INodeValueOutput[FingerType] | None) -> None:
        """Set the Finger reference by target ID or INodeValueOutput[FingerType] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Finger")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Finger",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.FingerType>'),
            )

    @property
    def segment(self) -> str | None:
        """Target ID of the Segment reference (targets INodeValueOutput[FingerSegmentType])."""
        member = self.get_member("Segment")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @segment.setter
    def segment(self, target: str | INodeValueOutput[FingerSegmentType] | None) -> None:
        """Set the Segment reference by target ID or INodeValueOutput[FingerSegmentType] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Segment")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Segment",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.FingerSegmentType>'),
            )

    @property
    def chirality(self) -> str | None:
        """Target ID of the Chirality reference (targets INodeValueOutput[Chirality])."""
        member = self.get_member("Chirality")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chirality.setter
    def chirality(self, target: str | INodeValueOutput[Chirality] | None) -> None:
        """Set the Chirality reference by target ID or INodeValueOutput[Chirality] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Chirality")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Chirality",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>'),
            )

