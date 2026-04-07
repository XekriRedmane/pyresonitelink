"""Generated component: ComposeColorX."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.color_profile import ColorProfile
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ComposeColorX(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ComposeColorX.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ComposeColorX"

    def __init__(self, base_color: str | INodeValueOutput[primitives.Color] | None = None, profile: str | INodeValueOutput[ColorProfile] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            base_color: Initial value for BaseColor.
            profile: Initial value for Profile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if base_color is not None:
            self.base_color = base_color
        if profile is not None:
            self.profile = profile

    @property
    def base_color(self) -> str | None:
        """Target ID of the BaseColor reference (targets INodeValueOutput[primitives.Color])."""
        member = self.get_member("BaseColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base_color.setter
    def base_color(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the BaseColor reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("BaseColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BaseColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def profile(self) -> str | None:
        """Target ID of the Profile reference (targets INodeValueOutput[ColorProfile])."""
        member = self.get_member("Profile")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @profile.setter
    def profile(self, target: str | INodeValueOutput[ColorProfile] | None) -> None:
        """Set the Profile reference by target ID or INodeValueOutput[ColorProfile] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Profile")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Profile",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ColorProfile>'),
            )

