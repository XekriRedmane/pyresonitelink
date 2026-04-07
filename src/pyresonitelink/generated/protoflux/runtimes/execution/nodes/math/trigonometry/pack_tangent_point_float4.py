"""Generated component: PackTangentPointFloat4."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PackTangentPointFloat4(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PackTangentPointFloat4.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Trigonometry
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PackTangentPointFloat4"

    def __init__(self, value: str | INodeValueOutput[primitives.Float4] | None = None, tangent: str | INodeValueOutput[primitives.Float4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            tangent: Initial value for Tangent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if tangent is not None:
            self.tangent = tangent

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[primitives.Float4])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[primitives.Float4] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float4>'),
            )

    @property
    def tangent(self) -> str | None:
        """Target ID of the Tangent reference (targets INodeValueOutput[primitives.Float4])."""
        member = self.get_member("Tangent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tangent.setter
    def tangent(self, target: str | INodeValueOutput[primitives.Float4] | None) -> None:
        """Set the Tangent reference by target ID or INodeValueOutput[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Tangent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tangent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float4>'),
            )

