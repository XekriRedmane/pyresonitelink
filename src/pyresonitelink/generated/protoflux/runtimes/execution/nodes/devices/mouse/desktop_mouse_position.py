"""Generated component: DesktopMousePosition."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopMousePosition(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Desktop Mouse Position node returns the local user's mouse position from their device. The mouse position calculation starts at the top-left of the main monitor. If you are focused on the Resonite application, the mouse will always be centered in that window while you move the mouse around, giving a consistent result from this node. If you have multiple monitors, it will track the mouse outside of Resonite and calculate accordingly, sometimes returning really large values depending how your system is set up.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Mouse
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Mouse.DesktopMousePosition"

    pass

