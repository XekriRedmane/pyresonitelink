"""Generated component: TrailsRenderBufferRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.trails_render_buffer import TrailsRenderBuffer
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrailsRenderBufferRenderer(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TrailsRenderBufferRenderer.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrailsRenderBufferRenderer"

    def __init__(self, buffer: str | IAssetProvider[TrailsRenderBuffer] | None = None, material: str | IAssetProvider[Material] | None = None, generate_lighting_data: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            buffer: Initial value for Buffer.
            material: Initial value for Material.
            generate_lighting_data: Initial value for GenerateLightingData.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if buffer is not None:
            self.buffer = buffer
        if material is not None:
            self.material = material
        if generate_lighting_data is not None:
            self.generate_lighting_data = generate_lighting_data

    @property
    def buffer(self) -> str | None:
        """Target ID of the Buffer reference (targets IAssetProvider[TrailsRenderBuffer])."""
        member = self.get_member("Buffer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buffer.setter
    def buffer(self, target: str | IAssetProvider[TrailsRenderBuffer] | None) -> None:
        """Set the Buffer reference by target ID or IAssetProvider[TrailsRenderBuffer] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Buffer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Buffer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.TrailsRenderBuffer>'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the Material reference (targets IAssetProvider[Material])."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the Material reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def texture_mode(self) -> members.FieldEnum | None:
        """The TextureMode member."""
        member = self.get_member("TextureMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @texture_mode.setter
    def texture_mode(self, value: members.FieldEnum) -> None:
        """Set the TextureMode member."""
        self.set_member("TextureMode", value)

    @property
    def motion_vector_mode(self) -> members.FieldEnum | None:
        """The MotionVectorMode member."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: members.FieldEnum) -> None:
        """Set the MotionVectorMode member."""
        self.set_member("MotionVectorMode", value)

    @property
    def generate_lighting_data(self) -> bool | None:
        """The GenerateLightingData field value."""
        member = self.get_member("GenerateLightingData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @generate_lighting_data.setter
    def generate_lighting_data(self, value: bool) -> None:
        """Set the GenerateLightingData field value."""
        member = self.get_member("GenerateLightingData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GenerateLightingData", fields.FieldBool(value=value)
            )

