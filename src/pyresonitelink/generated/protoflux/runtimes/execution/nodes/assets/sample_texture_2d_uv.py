"""Generated component: SampleTexture2D_UV."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.wrap_mode import WrapMode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleTexture2D_UV(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture2D_UV.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture2D_UV"

    def __init__(self, texture: str | INodeObjectOutput[Texture2D] | None = None, uv: str | INodeValueOutput[primitives.Float2] | None = None, wrap_mode: str | INodeValueOutput[WrapMode] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            uv: Initial value for UV.
            wrap_mode: Initial value for WrapMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if uv is not None:
            self.uv = uv
        if wrap_mode is not None:
            self.wrap_mode = wrap_mode

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
    def uv(self) -> str | None:
        """Target ID of the UV reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("UV")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv.setter
    def uv(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the UV reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UV")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UV",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def wrap_mode(self) -> str | None:
        """Target ID of the WrapMode reference (targets INodeValueOutput[WrapMode])."""
        member = self.get_member("WrapMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @wrap_mode.setter
    def wrap_mode(self, target: str | INodeValueOutput[WrapMode] | None) -> None:
        """Set the WrapMode reference by target ID or INodeValueOutput[WrapMode] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("WrapMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WrapMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Elements.Assets]Elements.Assets.WrapMode>'),
            )

