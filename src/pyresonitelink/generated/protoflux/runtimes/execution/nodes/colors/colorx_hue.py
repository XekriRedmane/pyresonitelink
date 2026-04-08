"""Generated component: ColorXHue."""

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


class ColorXHue(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXHue.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXHue"

    def __init__(self, hue: str | INodeValueOutput[primitives.Float] | None = None, target_profile: str | INodeValueOutput[ColorProfile] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hue: Initial value for Hue.
            target_profile: Initial value for TargetProfile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hue is not None:
            self.hue = hue
        if target_profile is not None:
            self.target_profile = target_profile

    @property
    def hue(self) -> str | None:
        """Target ID of the Hue reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Hue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hue.setter
    def hue(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Hue reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Hue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Hue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def target_profile(self) -> str | None:
        """Target ID of the TargetProfile reference (targets INodeValueOutput[ColorProfile])."""
        member = self.get_member("TargetProfile")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_profile.setter
    def target_profile(self, target: str | INodeValueOutput[ColorProfile] | None) -> None:
        """Set the TargetProfile reference by target ID or INodeValueOutput[ColorProfile] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("TargetProfile")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetProfile",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ColorProfile>'),
            )

