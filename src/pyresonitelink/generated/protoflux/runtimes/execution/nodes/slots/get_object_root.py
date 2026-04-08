"""Generated component: GetObjectRoot."""

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


class GetObjectRoot(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.GetObjectRoot.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.GetObjectRoot"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, only_explicit: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            only_explicit: Initial value for OnlyExplicit.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if only_explicit is not None:
            self.only_explicit = only_explicit

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
    def only_explicit(self) -> str | None:
        """Target ID of the OnlyExplicit reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("OnlyExplicit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @only_explicit.setter
    def only_explicit(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the OnlyExplicit reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnlyExplicit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnlyExplicit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

