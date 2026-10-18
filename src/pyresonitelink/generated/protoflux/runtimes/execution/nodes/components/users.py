"""Generated component: Users."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Users(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Users node gives a Collection of users in the current world session.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Components
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Users"

    pass

