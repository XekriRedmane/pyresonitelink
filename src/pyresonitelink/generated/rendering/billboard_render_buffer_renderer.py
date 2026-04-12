"""Generated component: BillboardRenderBufferRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.billboard_alignment import BillboardAlignment
from pyresonitelink.generated._enums.motion_vector_mode import MotionVectorMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.point_render_buffer import PointRenderBuffer
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BillboardRenderBufferRenderer(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The BillboardRenderBufferRenderer component is used as a debug component to determine the states of Photon Dust buffers during the simulation process.

    Category: Rendering

    Used in debugging Photon Dust
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BillboardRenderBufferRenderer"

    def __init__(self, buffer: str | IAssetProvider[PointRenderBuffer] | None = None, material: str | IAssetProvider[Material] | None = None, alignment: BillboardAlignment | str | None = None, motion_vector_mode: MotionVectorMode | str | None = None, min_billboard_screen_size: primitives.Float | None = None, max_billboard_screen_size: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            buffer: Initial value for Buffer.
            material: Initial value for Material.
            alignment: Initial value for Alignment.
            motion_vector_mode: Initial value for MotionVectorMode.
            min_billboard_screen_size: Initial value for MinBillboardScreenSize.
            max_billboard_screen_size: Initial value for MaxBillboardScreenSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if buffer is not None:
            self.buffer = buffer
        if material is not None:
            self.material = material
        if alignment is not None:
            self.alignment = alignment
        if motion_vector_mode is not None:
            self.motion_vector_mode = motion_vector_mode
        if min_billboard_screen_size is not None:
            self.min_billboard_screen_size = min_billboard_screen_size
        if max_billboard_screen_size is not None:
            self.max_billboard_screen_size = max_billboard_screen_size

    @property
    def buffer(self) -> str | None:
        """The renderer to render point buffers."""
        member = self.get_member("Buffer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buffer.setter
    def buffer(self, target: str | IAssetProvider[PointRenderBuffer] | None) -> None:
        """Set the Buffer reference by target ID or IAssetProvider[PointRenderBuffer] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Buffer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Buffer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.PointRenderBuffer>'),
            )

    @property
    def material(self) -> str | None:
        """The material to render this with."""
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
    def alignment(self) -> BillboardAlignment | None:
        """How to align the particles."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BillboardAlignment(member.value)
        return None

    @alignment.setter
    def alignment(self, value: BillboardAlignment | str) -> None:
        """Set Alignment. How to align the particles."""
        member = self.get_member("Alignment")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Alignment",
                members.FieldEnum(value=str(value)),
            )

    @property
    def motion_vector_mode(self) -> MotionVectorMode | None:
        """How to render the object motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MotionVectorMode(member.value)
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: MotionVectorMode | str) -> None:
        """Set MotionVectorMode. How to render the object motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MotionVectorMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_billboard_screen_size(self) -> primitives.Float | None:
        """The minimum size of particles rendered."""
        member = self.get_member("MinBillboardScreenSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_billboard_screen_size.setter
    def min_billboard_screen_size(self, value: primitives.Float) -> None:
        """Set the MinBillboardScreenSize field value."""
        member = self.get_member("MinBillboardScreenSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinBillboardScreenSize", fields.FieldFloat(value=value)
            )

    @property
    def max_billboard_screen_size(self) -> primitives.Float | None:
        """The maximum size of particles rendered."""
        member = self.get_member("MaxBillboardScreenSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_billboard_screen_size.setter
    def max_billboard_screen_size(self, value: primitives.Float) -> None:
        """Set the MaxBillboardScreenSize field value."""
        member = self.get_member("MaxBillboardScreenSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxBillboardScreenSize", fields.FieldFloat(value=value)
            )

