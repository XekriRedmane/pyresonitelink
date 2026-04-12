"""Generated component: ViewOverriden."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ViewOverriden(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The View Overriden node returns if the local user's view output is being overridden by something.

When in Desktop Mode or, starting Resonite in VR mode and then hot-swapping to Desktop Mode, this node will return as true.

When changing your view by using a different head proxy, templated head proxy, or something else that moves your view point (such as the AvatarUserRootOverrideAssigner or AvatarObjectSlot components), this node will return as true.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Users/Local Output
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.LocalOutput.ViewOverriden"

    pass

