"""Generated component: UserRefSource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.isource import ISource
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserRefSource(GeneratedComponent, IVariable, ISource, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.UserRefSource.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.UserRefSource"

    def __init__(self, source: str | IGlobalValueProxy[UserRef] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IGlobalValueProxy[UserRef])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IGlobalValueProxy[UserRef] | None) -> None:
        """Set the Source reference by target ID or IGlobalValueProxy[UserRef] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.UserRef>'),
            )

