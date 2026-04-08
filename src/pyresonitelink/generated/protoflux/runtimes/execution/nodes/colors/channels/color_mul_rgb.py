"""Generated component: ColorMulRGB."""

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


class ColorMulRGB(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorMulRGB.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors/Channels
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorMulRGB"

    def __init__(self, color: str | INodeValueOutput[primitives.Color] | None = None, value: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            color: Initial value for Color.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if color is not None:
            self.color = color
        if value is not None:
            self.value = value

    @property
    def color(self) -> str | None:
        """Target ID of the Color reference (targets INodeValueOutput[primitives.Color])."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the Color reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

