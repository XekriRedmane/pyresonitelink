"""Generated component: MouseScrollDelta2D."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MouseScrollDelta2D(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Mouse Scroll Delta 2D node returns the local user's mouse scroll wheel delta from their Resonite application. If you are focused on the Resonite window, this node will listen for changes on your scroll wheel. The faster you scroll within a frame, the larger the delta.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Mouse
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Mouse.MouseScrollDelta2D"

    pass

