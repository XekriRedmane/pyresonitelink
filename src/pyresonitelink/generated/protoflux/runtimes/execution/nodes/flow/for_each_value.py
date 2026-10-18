"""Generated component: ForEachValue."""

from typing import Any

TCollection = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ForEachValue(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """#REDIRECT ForEach

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ForEachValue<,>"

    def __init__(self, collection: str | INodeObjectOutput[TCollection] | None = None, reverse: str | INodeValueOutput[primitives.Bool] | None = None, loop_start: str | ISyncNodeOperation | None = None, loop_iteration: str | ISyncNodeOperation | None = None, loop_failed: str | INodeOperation | None = None, loop_end: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            collection: Initial value for Collection.
            reverse: Initial value for Reverse.
            loop_start: Initial value for LoopStart.
            loop_iteration: Initial value for LoopIteration.
            loop_failed: Initial value for LoopFailed.
            loop_end: Initial value for LoopEnd.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if collection is not None:
            self.collection = collection
        if reverse is not None:
            self.reverse = reverse
        if loop_start is not None:
            self.loop_start = loop_start
        if loop_iteration is not None:
            self.loop_iteration = loop_iteration
        if loop_failed is not None:
            self.loop_failed = loop_failed
        if loop_end is not None:
            self.loop_end = loop_end

    @property
    def collection(self) -> str | None:
        """Target ID of the Collection reference (targets INodeObjectOutput[TCollection])."""
        member = self.get_member("Collection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collection.setter
    def collection(self, target: str | INodeObjectOutput[TCollection] | None) -> None:
        """Set the Collection reference by target ID or INodeObjectOutput[TCollection] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Collection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Collection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<TCollection>'),
            )

    @property
    def reverse(self) -> str | None:
        """Target ID of the Reverse reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Reverse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reverse.setter
    def reverse(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Reverse reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Reverse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reverse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def loop_start(self) -> str | None:
        """Target ID of the LoopStart reference (targets ISyncNodeOperation)."""
        member = self.get_member("LoopStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_start.setter
    def loop_start(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the LoopStart reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("LoopStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def loop_iteration(self) -> str | None:
        """Target ID of the LoopIteration reference (targets ISyncNodeOperation)."""
        member = self.get_member("LoopIteration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_iteration.setter
    def loop_iteration(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the LoopIteration reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("LoopIteration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopIteration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def loop_failed(self) -> str | None:
        """Target ID of the LoopFailed reference (targets INodeOperation)."""
        member = self.get_member("LoopFailed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_failed.setter
    def loop_failed(self, target: str | INodeOperation | None) -> None:
        """Set the LoopFailed reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("LoopFailed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopFailed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def loop_end(self) -> str | None:
        """Target ID of the LoopEnd reference (targets INodeOperation)."""
        member = self.get_member("LoopEnd")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_end.setter
    def loop_end(self, target: str | INodeOperation | None) -> None:
        """Set the LoopEnd reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("LoopEnd")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopEnd",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def element(self) -> members.EmptyElement | None:
        """The Element member."""
        member = self.get_member("Element")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @element.setter
    def element(self, value: members.EmptyElement) -> None:
        """Set the Element member."""
        self.set_member("Element", value)

