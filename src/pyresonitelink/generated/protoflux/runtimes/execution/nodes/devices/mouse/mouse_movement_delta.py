"""Generated component: MouseMovementDelta."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MouseMovementDelta(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Mouse Movement Delta`` node returns the local user's mouse movement delta from their Resonite application. The faster you move your mouse within a frame, the larger the delta. If you are focused on the Resonite window, the mouse will always be centered in that window while you move the mouse around, and this node will listen for the changes in your mouse movement to calculate the dalta. When the resonite application is not focused, this node will not calculate the delta at all.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Mouse
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Mouse.MouseMovementDelta"

    pass

