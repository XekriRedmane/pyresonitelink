"""Generated component: GetTexture3D_Pixel."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetTexture3D_Pixel(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetTexture3D_Pixel.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetTexture3D_Pixel"

    def __init__(self, texture: str | INodeObjectOutput[Texture3D] | None = None, position: str | INodeValueOutput[primitives.Int3] | None = None, mip_level: str | INodeValueOutput[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            position: Initial value for Position.
            mip_level: Initial value for MipLevel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if position is not None:
            self.position = position
        if mip_level is not None:
            self.mip_level = mip_level

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
    def position(self) -> str | None:
        """Target ID of the Position reference (targets INodeValueOutput[primitives.Int3])."""
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | INodeValueOutput[primitives.Int3] | None) -> None:
        """Set the Position reference by target ID or INodeValueOutput[primitives.Int3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int3>'),
            )

    @property
    def mip_level(self) -> str | None:
        """Target ID of the MipLevel reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("MipLevel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mip_level.setter
    def mip_level(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the MipLevel reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MipLevel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MipLevel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

