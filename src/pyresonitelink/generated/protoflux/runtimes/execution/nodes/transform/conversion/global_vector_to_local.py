"""Generated component: GlobalVectorToLocal."""

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


class GlobalVectorToLocal(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """ContinuouslyChanging nodes

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Conversion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.GlobalVectorToLocal"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, global_vector: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            global_vector: Initial value for GlobalVector.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if global_vector is not None:
            self.global_vector = global_vector

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
    def global_vector(self) -> str | None:
        """Target ID of the GlobalVector reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("GlobalVector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @global_vector.setter
    def global_vector(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the GlobalVector reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("GlobalVector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GlobalVector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

