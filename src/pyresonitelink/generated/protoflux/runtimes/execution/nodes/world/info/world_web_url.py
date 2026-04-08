"""Generated component: WorldWebURL."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldWebURL(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The World Web URL node returns this world's Web URL. This node is interesting as it provides a Web Address for the world and there is no application this can be used for yet. When trying to use the contents of this node by putting the result into a web browser and going to that location, the web browser may warn you of potential security risks, and going past that there is only an error 403 page (access to the requested resource is recognized but is forbidden).

    Category: ProtoFlux/Runtimes/Execution/Nodes/World/Info

    **Images**: File:PotentialSecurityRiskAheadForGoResoniteCom.jpg|Security warning page from the Firefox Browser.
File:Error403OnGoResoniteCom.jpg|Error 403 Page on Go.Resonite.Com.


ProtoFlux:World:Info
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.WorldWebURL"

    pass

