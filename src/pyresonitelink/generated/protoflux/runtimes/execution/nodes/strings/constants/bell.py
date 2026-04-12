"""Generated component: Bell."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Bell(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Bell`` node is a character literal constant for the "Bell" character (Unicode: U+0007).

The Bell character was used to make a sound or flash the screen to get the attention of operators that were using older computer systems. This is no longer relevant in something like Resonite, but is provided for completeness.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Constants
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.Bell"

    pass

