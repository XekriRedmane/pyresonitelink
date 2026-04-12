"""Generated component: BlackBodyColor."""

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


class BlackBodyColor(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Black Body Color returns a color value of the light emitted by an ideal black body radiator. This can be used to calculate appropriate values for various color temperatures.

This node can convert color values in the range 1000 - 40000 Kelvin. Values outside this range are clamped.

The implementation in Resonite appears to use this table as a source of values. For values more granular than 100 Kelvin, the node interpolates linearly between the closest two values.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.BlackBodyColor"

    def __init__(self, temperature: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            temperature: Initial value for Temperature.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if temperature is not None:
            self.temperature = temperature

    @property
    def temperature(self) -> str | None:
        """The temperature, in Kelvin, to calculate the resulting color for."""
        member = self.get_member("Temperature")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @temperature.setter
    def temperature(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Temperature reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Temperature")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Temperature",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

