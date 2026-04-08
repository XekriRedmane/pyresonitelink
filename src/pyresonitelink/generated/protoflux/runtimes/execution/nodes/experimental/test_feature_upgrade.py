"""Generated component: TestFeatureUpgrade."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TestFeatureUpgrade(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Test Feature Upgrade node is a test node that may be removed in the future and is not meant for regular use, not many people know what this node does besides the Resonite Dev Team. As far as what is known about this node, it is used internally for testing purposes, and can be ignored. It makes sense that this node would be in the experimental category for this reason.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Experimental
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.TestFeatureUpgrade"

    pass

