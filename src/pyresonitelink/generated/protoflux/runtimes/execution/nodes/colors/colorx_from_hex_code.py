"""Generated component: ColorXFromHexCode."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorXFromHexCode(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Color From Hex Code is a ProtoFlux node that parses a hex color code such as "FFAEBB" into a ColorX.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors

    **References**: ProtoFlux:Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXFromHexCode"

    def __init__(self, hex_code: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hex_code: Initial value for HexCode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hex_code is not None:
            self.hex_code = hex_code

    @property
    def hex_code(self) -> str | None:
        """Target ID of the HexCode reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("HexCode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hex_code.setter
    def hex_code(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the HexCode reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("HexCode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HexCode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def color(self) -> members.EmptyElement | None:
        """The Color member."""
        member = self.get_member("Color")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @color.setter
    def color(self, value: members.EmptyElement) -> None:
        """Set the Color member."""
        self.set_member("Color", value)

    @property
    def parsed(self) -> members.EmptyElement | None:
        """The Parsed member."""
        member = self.get_member("Parsed")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @parsed.setter
    def parsed(self, value: members.EmptyElement) -> None:
        """Set the Parsed member."""
        self.set_member("Parsed", value)

