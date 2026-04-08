"""Generated component: ColorXToProfile."""

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


class ColorXToProfile(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ColorX To Profile node takes in a ColorX and the target ColorProfile, then returns the new profiled Color.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXToProfile"

    def __init__(self, color: str | INodeValueOutput[primitives.ColorX] | None = None, profile: str | INodeValueOutput[ColorProfile] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            color: Initial value for Color.
            profile: Initial value for Profile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if color is not None:
            self.color = color
        if profile is not None:
            self.profile = profile

    @property
    def color(self) -> str | None:
        """Target ID of the Color reference (targets INodeValueOutput[primitives.ColorX])."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the Color reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
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

