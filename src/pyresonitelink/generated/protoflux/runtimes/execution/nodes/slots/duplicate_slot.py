"""Generated component: DuplicateSlot."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DuplicateSlot(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Duplicate Slot node makes a copy of a slot and exposes the duplicated slot with the output called Duplicate which can be used for any nodes that accept the slot type.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.DuplicateSlot"

    def __init__(self, next: str | INodeOperation | None = None, template: str | INodeObjectOutput[Slot] | None = None, override_parent: str | INodeObjectOutput[Slot] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            template: Initial value for Template.
            override_parent: Initial value for OverrideParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if template is not None:
            self.template = template
        if override_parent is not None:
            self.override_parent = override_parent

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
    def template(self) -> str | None:
        """Target ID of the Template reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template.setter
    def template(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Template reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Template",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def override_parent(self) -> str | None:
        """Target ID of the OverrideParent reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_parent.setter
    def override_parent(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the OverrideParent reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def duplicate(self) -> members.EmptyElement | None:
        """The Duplicate member."""
        member = self.get_member("Duplicate")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @duplicate.setter
    def duplicate(self, value: members.EmptyElement) -> None:
        """Set the Duplicate member."""
        self.set_member("Duplicate", value)

