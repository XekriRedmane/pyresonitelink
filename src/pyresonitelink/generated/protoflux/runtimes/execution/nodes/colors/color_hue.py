"""Generated component: ColorHue."""

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


class ColorHue(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Color Hue returns a color with a given hue value. This is equivalent to using HSV To Color with a value and saturation equal to 1.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorHue"

    def __init__(self, hue: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hue: Initial value for Hue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hue is not None:
            self.hue = hue

    @property
    def hue(self) -> str | None:
        """The hue to get a color for. Values must be in the range [0, 1], values outside this range are wrapped to it. For example a value of 1.5 gives the same result as 0.5."""
        member = self.get_member("Hue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hue.setter
    def hue(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Hue reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Hue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Hue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

