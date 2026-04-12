"""Generated component: RawDeltaTime."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawDeltaTime(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The RawDeltaTime node returns the time it took to perform the last update in seconds.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time

    **See also**: * DeltaTime returns the same value as this node, but clamped to a maximum of 0.1 seconds.
* SmoothDeltaTime tries to smooth out the delta time to minimize interference from stutters.
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.RawDeltaTime"

    pass

