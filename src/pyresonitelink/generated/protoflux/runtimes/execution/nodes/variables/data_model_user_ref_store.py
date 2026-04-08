"""Generated component: DataModelUserRefStore."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.idata_model_store import IDataModelStore
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataModelUserRefStore(GeneratedComponent, IVariable, IDataModelStore, IProtoFluxEngineProxyNode, IMappableNode, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The '''DataModelUserRefStore''' type allows storing persistent user references, meaning they are not lost when saving an object, the world, or a user leaving and rejoining the session. DataModelUserRefStore is not to be confused with a regular Data Model Store, which does not persist. When using the protoflux tool with a node that writes a User to create a Data Model Store, a DataModelUserRefStore is automatically created instead of the regular DataModelStore type. This node achieves persistence by storing a UserRef internally, but still outputs a regular User for use in flux. If the user who is stored is not in the session, the output will be null.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelUserRefStore"

    pass

