"""Generated component: IsChildOf."""

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


class IsChildOf(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Is Child Of node determines if the ``Instance`` slot is a descendant of the ``Other`` slot. This check is recursive.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.IsChildOf"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, other: str | INodeObjectOutput[Slot] | None = None, include_self: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            other: Initial value for Other.
            include_self: Initial value for IncludeSelf.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if other is not None:
            self.other = other
        if include_self is not None:
            self.include_self = include_self

    @property
    def instance(self) -> str | None:
        """The slot to test."""
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
    def other(self) -> str | None:
        """The potential parent slot of ``Instance``."""
        member = self.get_member("Other")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @other.setter
    def other(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Other reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Other")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Other",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def include_self(self) -> str | None:
        """Target ID of the IncludeSelf reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("IncludeSelf")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @include_self.setter
    def include_self(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IncludeSelf reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IncludeSelf")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IncludeSelf",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

