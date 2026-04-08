"""Generated component: DataModelObjectFieldStore."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
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


class DataModelObjectFieldStore(GenericComponent[T], IVariable, IDataModelStore, IProtoFluxEngineProxyNode, IMappableNode, INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectFieldStore<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Variables

    Parameterize with a value type::

        DataModelObjectFieldStore[primitives.Float]
        DataModelObjectFieldStore[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectFieldStore<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectFieldStore<>"

    pass

