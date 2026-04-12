"""Generated component: InvertedSmoothDeltaTime."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InvertedSmoothDeltaTime(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Inverted Smooth Delta Time`` node returns the frames per second, shown when pulling a display node from it and comparing it to the Dash's FPS counter. This will attempt to adjust to any lag or stutters by smoothing out the differences between the results.

This is done by taking the reciprocal of delta time: FPS = 1 / dT (+ some smoothing algorithm)

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.InvertedSmoothDeltaTime"

    pass

