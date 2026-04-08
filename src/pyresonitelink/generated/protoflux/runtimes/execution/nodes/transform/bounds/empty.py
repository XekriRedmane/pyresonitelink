"""Generated component: Empty."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Empty(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Empty node outputs an empty bounding box.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Bounds

    **Issues**: * Currently the empty bounding box is returning really large numbers in opposite directions, and is currently being investigated by Frooxius in this GitHub issue: #2090

ProtoFlux:Transform:Bounds
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.Empty"

    pass

