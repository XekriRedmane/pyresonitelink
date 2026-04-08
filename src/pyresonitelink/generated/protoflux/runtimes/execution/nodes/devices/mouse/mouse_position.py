"""Generated component: MousePosition."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MousePosition(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Mouse Position node returns the local user's mouse position from their Resonite application in pixels. The mouse position calculation starts at the top-left of the Resonite window. If you are focused on the Resonite window, the mouse will usually be centered in that window while you move the mouse around (unless interacting with a UI or in freecam mode), giving an almost constant output from this node (in this case, x axis divided by 2 and y axis divided by 2). When the Resonite application is not focused, the cursor won't be tracked at all and will snap to the bottom left (returning "[0; max Y]" of your Resonite window size). Having multiple monitors will not affect this node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Mouse
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Mouse.MousePosition"

    pass

