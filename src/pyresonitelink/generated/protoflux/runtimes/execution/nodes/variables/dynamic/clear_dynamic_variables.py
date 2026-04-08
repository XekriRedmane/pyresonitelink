"""Generated component: ClearDynamicVariables."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ClearDynamicVariables(GeneratedComponent, IMappableNode, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Clear Dynamic Variables node takes in a slot hierarchy and a string literal path of the dynamic space name. For more information, see Dynamic Variables.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables/Dynamic
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ClearDynamicVariables"

    def __init__(self, target: str | INodeObjectOutput[Slot] | None = None, space_name: str | INodeObjectOutput[primitives.String] | None = None, on_not_found: str | INodeOperation | None = None, on_cleared: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            space_name: Initial value for SpaceName.
            on_not_found: Initial value for OnNotFound.
            on_cleared: Initial value for OnCleared.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if space_name is not None:
            self.space_name = space_name
        if on_not_found is not None:
            self.on_not_found = on_not_found
        if on_cleared is not None:
            self.on_cleared = on_cleared

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def space_name(self) -> str | None:
        """Target ID of the SpaceName reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("SpaceName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @space_name.setter
    def space_name(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the SpaceName reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("SpaceName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpaceName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def on_not_found(self) -> str | None:
        """Target ID of the OnNotFound reference (targets INodeOperation)."""
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_not_found.setter
    def on_not_found(self, target: str | INodeOperation | None) -> None:
        """Set the OnNotFound reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnNotFound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_cleared(self) -> str | None:
        """Target ID of the OnCleared reference (targets INodeOperation)."""
        member = self.get_member("OnCleared")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_cleared.setter
    def on_cleared(self, target: str | INodeOperation | None) -> None:
        """Set the OnCleared reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnCleared")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnCleared",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def cleared_count(self) -> members.EmptyElement | None:
        """The ClearedCount member."""
        member = self.get_member("ClearedCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @cleared_count.setter
    def cleared_count(self, value: members.EmptyElement) -> None:
        """Set the ClearedCount member."""
        self.set_member("ClearedCount", value)

