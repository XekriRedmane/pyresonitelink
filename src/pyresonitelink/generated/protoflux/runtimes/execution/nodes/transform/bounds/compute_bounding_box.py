"""Generated component: ComputeBoundingBox."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ComputeBoundingBox(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.ComputeBoundingBox.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Bounds
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.ComputeBoundingBox"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, include_inactive: str | INodeValueOutput[primitives.Bool] | None = None, coordinate_space: str | INodeObjectOutput[Slot] | None = None, only_with_tag: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            include_inactive: Initial value for IncludeInactive.
            coordinate_space: Initial value for CoordinateSpace.
            only_with_tag: Initial value for OnlyWithTag.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if include_inactive is not None:
            self.include_inactive = include_inactive
        if coordinate_space is not None:
            self.coordinate_space = coordinate_space
        if only_with_tag is not None:
            self.only_with_tag = only_with_tag

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
    def include_inactive(self) -> str | None:
        """Target ID of the IncludeInactive reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("IncludeInactive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @include_inactive.setter
    def include_inactive(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IncludeInactive reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IncludeInactive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IncludeInactive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def coordinate_space(self) -> str | None:
        """Target ID of the CoordinateSpace reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("CoordinateSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @coordinate_space.setter
    def coordinate_space(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the CoordinateSpace reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("CoordinateSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CoordinateSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def only_with_tag(self) -> str | None:
        """Target ID of the OnlyWithTag reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("OnlyWithTag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @only_with_tag.setter
    def only_with_tag(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the OnlyWithTag reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnlyWithTag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnlyWithTag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

