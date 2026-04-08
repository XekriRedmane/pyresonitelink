"""Generated component: SmoothDeltaTime."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SmoothDeltaTime(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Smooth Delta Time node returns the change of time between two world updates, specifically the time between the current update and the one before. This node also does another step and tries to account for lag or stutters, smoothly changing the amount of time to match that change.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.SmoothDeltaTime"

    pass

