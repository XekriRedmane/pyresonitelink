"""Generated component: FontMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_unlit_material import TextUnlitMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FontMaterial(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FontMaterial.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FontMaterial"

    def __init__(self, outline_thickness: np.float32 | None = None, outline_color: primitives.ColorX | None = None, face_softness: np.float32 | None = None, face_dilate: np.float32 | None = None, render_queue: np.int32 | None = None, converted_material: str | TextUnlitMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            outline_thickness: Initial value for OutlineThickness.
            outline_color: Initial value for OutlineColor.
            face_softness: Initial value for FaceSoftness.
            face_dilate: Initial value for FaceDilate.
            render_queue: Initial value for RenderQueue.
            converted_material: Initial value for _convertedMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if outline_thickness is not None:
            self.outline_thickness = outline_thickness
        if outline_color is not None:
            self.outline_color = outline_color
        if face_softness is not None:
            self.face_softness = face_softness
        if face_dilate is not None:
            self.face_dilate = face_dilate
        if render_queue is not None:
            self.render_queue = render_queue
        if converted_material is not None:
            self.converted_material = converted_material

    @property
    def outline_thickness(self) -> np.float32 | None:
        """The OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_thickness.setter
    def outline_thickness(self, value: np.float32) -> None:
        """Set the OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineThickness", fields.FieldFloat(value=value)
            )

    @property
    def outline_color(self) -> primitives.ColorX | None:
        """The OutlineColor field value."""
        member = self.get_member("OutlineColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_color.setter
    def outline_color(self, value: primitives.ColorX) -> None:
        """Set the OutlineColor field value."""
        member = self.get_member("OutlineColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineColor", fields.FieldColorX(value=value)
            )

    @property
    def face_softness(self) -> np.float32 | None:
        """The FaceSoftness field value."""
        member = self.get_member("FaceSoftness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_softness.setter
    def face_softness(self, value: np.float32) -> None:
        """Set the FaceSoftness field value."""
        member = self.get_member("FaceSoftness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceSoftness", fields.FieldFloat(value=value)
            )

    @property
    def face_dilate(self) -> np.float32 | None:
        """The FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_dilate.setter
    def face_dilate(self, value: np.float32) -> None:
        """Set the FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceDilate", fields.FieldFloat(value=value)
            )

    @property
    def culling(self) -> members.FieldEnum | None:
        """The Culling member."""
        member = self.get_member("Culling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @culling.setter
    def culling(self, value: members.FieldEnum) -> None:
        """Set the Culling member."""
        self.set_member("Culling", value)

    @property
    def ztest(self) -> members.FieldEnum | None:
        """The ZTest member."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ztest.setter
    def ztest(self, value: members.FieldEnum) -> None:
        """Set the ZTest member."""
        self.set_member("ZTest", value)

    @property
    def render_queue(self) -> np.int32 | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: np.int32) -> None:
        """Set the RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderQueue", fields.FieldInt(value=value)
            )

    @property
    def converted_material(self) -> str | None:
        """Target ID of the _convertedMaterial reference (targets TextUnlitMaterial)."""
        member = self.get_member("_convertedMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @converted_material.setter
    def converted_material(self, target: str | TextUnlitMaterial | None) -> None:
        """Set the _convertedMaterial reference by target ID or TextUnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, TextUnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_convertedMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_convertedMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextUnlitMaterial'),
            )

