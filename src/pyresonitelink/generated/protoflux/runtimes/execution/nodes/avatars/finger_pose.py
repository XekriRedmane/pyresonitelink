"""Generated component: FingerPose."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.body_node import BodyNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPose(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.FingerPose.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.FingerPose"

    def __init__(self, pose_source: str | INodeObjectOutput[IFingerPoseSourceComponent] | None = None, finger_node: str | INodeValueOutput[BodyNode] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pose_source: Initial value for PoseSource.
            finger_node: Initial value for FingerNode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pose_source is not None:
            self.pose_source = pose_source
        if finger_node is not None:
            self.finger_node = finger_node

    @property
    def pose_source(self) -> str | None:
        """Target ID of the PoseSource reference (targets INodeObjectOutput[IFingerPoseSourceComponent])."""
        member = self.get_member("PoseSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pose_source.setter
    def pose_source(self, target: str | INodeObjectOutput[IFingerPoseSourceComponent] | None) -> None:
        """Set the PoseSource reference by target ID or INodeObjectOutput[IFingerPoseSourceComponent] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("PoseSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PoseSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent>'),
            )

    @property
    def finger_node(self) -> str | None:
        """Target ID of the FingerNode reference (targets INodeValueOutput[BodyNode])."""
        member = self.get_member("FingerNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @finger_node.setter
    def finger_node(self, target: str | INodeValueOutput[BodyNode] | None) -> None:
        """Set the FingerNode reference by target ID or INodeValueOutput[BodyNode] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("FingerNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FingerNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>'),
            )

    @property
    def position(self) -> members.EmptyElement | None:
        """The Position member."""
        member = self.get_member("Position")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @position.setter
    def position(self, value: members.EmptyElement) -> None:
        """Set the Position member."""
        self.set_member("Position", value)

    @property
    def rotation(self) -> members.EmptyElement | None:
        """The Rotation member."""
        member = self.get_member("Rotation")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @rotation.setter
    def rotation(self, value: members.EmptyElement) -> None:
        """Set the Rotation member."""
        self.set_member("Rotation", value)

