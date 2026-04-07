"""Generated component: SampleTexture3D_UVW."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.texture3_d import Texture3D
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SampleTexture3D_UVW(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture3D_UVW.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture3D_UVW"

    def __init__(self, texture: str | INodeObjectOutput[Texture3D] | None = None, uvw: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            uvw: Initial value for UVW.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if uvw is not None:
            self.uvw = uvw

    @property
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets INodeObjectOutput[Texture3D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | INodeObjectOutput[Texture3D] | None) -> None:
        """Set the Texture reference by target ID or INodeObjectOutput[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

    @property
    def uvw(self) -> str | None:
        """Target ID of the UVW reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("UVW")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uvw.setter
    def uvw(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the UVW reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UVW")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UVW",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

