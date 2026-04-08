"""Generated component: ColorToHSV."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorToHSV(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Color To HSL converts a Color to HSV. The result is represented as 3 separate Float values for Hue, Saturation, and Value.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorToHSV"

    def __init__(self, c: str | INodeValueOutput[primitives.Color] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            c: Initial value for C.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if c is not None:
            self.c = c

    @property
    def c(self) -> str | None:
        """Target ID of the C reference (targets INodeValueOutput[primitives.Color])."""
        member = self.get_member("C")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @c.setter
    def c(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the C reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("C")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "C",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def h(self) -> members.EmptyElement | None:
        """The H member."""
        member = self.get_member("H")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @h.setter
    def h(self, value: members.EmptyElement) -> None:
        """Set the H member."""
        self.set_member("H", value)

    @property
    def s(self) -> members.EmptyElement | None:
        """The S member."""
        member = self.get_member("S")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @s.setter
    def s(self, value: members.EmptyElement) -> None:
        """Set the S member."""
        self.set_member("S", value)

    @property
    def v(self) -> members.EmptyElement | None:
        """The V member."""
        member = self.get_member("V")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @v.setter
    def v(self, value: members.EmptyElement) -> None:
        """Set the V member."""
        self.set_member("V", value)

