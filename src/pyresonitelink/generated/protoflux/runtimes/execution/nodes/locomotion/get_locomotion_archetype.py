"""Generated component: GetLocomotionArchetype."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ilocomotion_module import ILocomotionModule
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetLocomotionArchetype(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.GetLocomotionArchetype.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Locomotion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.GetLocomotionArchetype"

    def __init__(self, module: str | INodeObjectOutput[ILocomotionModule] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            module: Initial value for Module.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if module is not None:
            self.module = module

    @property
    def module(self) -> str | None:
        """Target ID of the Module reference (targets INodeObjectOutput[ILocomotionModule])."""
        member = self.get_member("Module")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @module.setter
    def module(self, target: str | INodeObjectOutput[ILocomotionModule] | None) -> None:
        """Set the Module reference by target ID or INodeObjectOutput[ILocomotionModule] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Module")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Module",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.ILocomotionModule>'),
            )

