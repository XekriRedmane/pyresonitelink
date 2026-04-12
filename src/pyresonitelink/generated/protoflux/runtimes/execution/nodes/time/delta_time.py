"""Generated component: DeltaTime."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DeltaTime(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The DeltaTime node returns the time it took to perform the last update in seconds, clamped to a maximum value of 0.1 seconds.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time

    **See also**: * SmoothDeltaTime tries to smooth out the delta time to minimize interference from stutters.
* RawDeltaTime returns the raw, unclamped update time.
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Time.DeltaTime"

    pass

