"""Generated component: Pi."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Pi(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Pi node outputs the mathematical constant π.

Applications this can be used in:
- Geometry and Circle Calculations
- Rotations and Angle Calculations
- Wave Generation (combined with Sin)
- Physics Simulations (especially when dealing with circular motion, pendulum movements, or orbital mechanics)
- Procedural Generation (especially curves)
- Lighting and Shading (used in lighting models to calculate angles and intensities of light, reflections, and refractions)
- Animation Curves

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Constants
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Constants.Pi"

    pass

