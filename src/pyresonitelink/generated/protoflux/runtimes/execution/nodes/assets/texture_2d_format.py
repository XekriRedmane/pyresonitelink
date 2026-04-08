"""Generated component: Texture2D_Format."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Texture2D_Format(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.Texture2D_Format.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.Texture2D_Format"

    def __init__(self, texture: str | INodeObjectOutput[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture

    @property
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets INodeObjectOutput[Texture2D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | INodeObjectOutput[Texture2D] | None) -> None:
        """Set the Texture reference by target ID or INodeObjectOutput[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def size(self) -> members.EmptyElement | None:
        """The Size member."""
        member = self.get_member("Size")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @size.setter
    def size(self, value: members.EmptyElement) -> None:
        """Set the Size member."""
        self.set_member("Size", value)

    @property
    def format_(self) -> members.EmptyElement | None:
        """The Format member."""
        member = self.get_member("Format")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @format_.setter
    def format_(self, value: members.EmptyElement) -> None:
        """Set the Format member."""
        self.set_member("Format", value)

    @property
    def mip_map_count(self) -> members.EmptyElement | None:
        """The MipMapCount member."""
        member = self.get_member("MipMapCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @mip_map_count.setter
    def mip_map_count(self, value: members.EmptyElement) -> None:
        """Set the MipMapCount member."""
        self.set_member("MipMapCount", value)

