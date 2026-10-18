"""Generated component: NewLine."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NewLine(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``New Line`` node is a character literal constant that represents a new line in text. Note that this node comes in two versions: A char version and a String version.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Constants
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.NewLine"

    pass

