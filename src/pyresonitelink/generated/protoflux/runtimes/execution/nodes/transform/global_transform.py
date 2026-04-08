"""Generated component: GlobalTransform."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlobalTransform(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Global Transform node outputs the position, rotation and scale of the input slot in global coordinate space, i.e. the slot's transform relative to the world root slot.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.GlobalTransform"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance

    @property
    def instance(self) -> str | None:
        """Target ID of the Instance reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @instance.setter
    def instance(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Instance reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Instance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def global_position(self) -> members.EmptyElement | None:
        """The GlobalPosition member."""
        member = self.get_member("GlobalPosition")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @global_position.setter
    def global_position(self, value: members.EmptyElement) -> None:
        """Set the GlobalPosition member."""
        self.set_member("GlobalPosition", value)

    @property
    def global_rotation(self) -> members.EmptyElement | None:
        """The GlobalRotation member."""
        member = self.get_member("GlobalRotation")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @global_rotation.setter
    def global_rotation(self, value: members.EmptyElement) -> None:
        """Set the GlobalRotation member."""
        self.set_member("GlobalRotation", value)

    @property
    def global_scale(self) -> members.EmptyElement | None:
        """The GlobalScale member."""
        member = self.get_member("GlobalScale")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @global_scale.setter
    def global_scale(self, value: members.EmptyElement) -> None:
        """Set the GlobalScale member."""
        self.set_member("GlobalScale", value)

