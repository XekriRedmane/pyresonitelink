"""Generated component: ColorToHexCode."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorToHexCode(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Color To Hex Code converts a Color to a string hex color code such as "#FFAABC".

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors

    **Gallery**: File:Protoflux_Color_To_Hex.webp|A simple example of Color To Hex with an input and an output display.
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorToHexCode"

    def __init__(self, color: str | INodeValueOutput[primitives.Color] | None = None, short_form: str | INodeValueOutput[primitives.Bool] | None = None, include_alpha: str | INodeValueOutput[primitives.Bool] | None = None, prefix: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            color: Initial value for Color.
            short_form: Initial value for ShortForm.
            include_alpha: Initial value for IncludeAlpha.
            prefix: Initial value for Prefix.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if color is not None:
            self.color = color
        if short_form is not None:
            self.short_form = short_form
        if include_alpha is not None:
            self.include_alpha = include_alpha
        if prefix is not None:
            self.prefix = prefix

    @property
    def color(self) -> str | None:
        """The color to convert. Color components are clamped to the range 0-1."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the Color reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def short_form(self) -> str | None:
        """If true, convert to a short form such as "#FAC" instead of "#FFAACC"."""
        member = self.get_member("ShortForm")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @short_form.setter
    def short_form(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ShortForm reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ShortForm")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ShortForm",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def include_alpha(self) -> str | None:
        """If true, include the alpha channel as the last component."""
        member = self.get_member("IncludeAlpha")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @include_alpha.setter
    def include_alpha(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IncludeAlpha reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IncludeAlpha")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IncludeAlpha",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def prefix(self) -> str | None:
        """The string to prefix the color code with. Defaults to "#"."""
        member = self.get_member("Prefix")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @prefix.setter
    def prefix(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Prefix reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Prefix")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Prefix",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

