"""Generated component: Tau."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Tau(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Tau node outputs the mathematical constant tau. Tau is a constant that represents 2PI. Tau is the circumference of a circle with a radius of one.

Applications this constant can be used in:
- Circumference, angular, and rotation measurements
- Wave Generation (combined with Sin)
- Shader Programming (usually simplifying/streamlining the code)

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Constants
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Constants.Tau"

    pass

