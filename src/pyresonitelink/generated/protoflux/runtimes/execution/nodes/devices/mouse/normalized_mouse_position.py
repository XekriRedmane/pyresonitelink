"""Generated component: NormalizedMousePosition."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NormalizedMousePosition(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Normalized Mouse Position node returns the local user's normalized mouse position from their Resonite application (0 to 1 on both the x and y axis). The normalized mouse position calculation starts at the top-left of the Resonite window. If you are focused on the Resonite window, the mouse will always be centered in that window while you move the mouse around (unless interacting with a UI or in freecam mode), giving a consistent result from this node (in this case, it is usually around 0.5 for both the X and Y axis). When the Resonite application is not focused, the cursor won't be tracked at all and will snap to the bottom left (returning "[0; 1]"). Having multiple monitors will not affect this node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Mouse
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Mouse.NormalizedMousePosition"

    pass

