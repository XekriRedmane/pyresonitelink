"""Generated component: FontMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.culling import Culling
from pyresonitelink.generated._enums.ztest import ZTest
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_unlit_material import TextUnlitMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FontMaterial(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The FontMaterial component is a Legacy component that was used for rendering text.

    Don't use. Obsolete.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FontMaterial"

    def __init__(self, outline_thickness: primitives.Float | None = None, outline_color: primitives.ColorX | None = None, face_softness: primitives.Float | None = None, face_dilate: primitives.Float | None = None, culling: Culling | str | None = None, ztest: ZTest | str | None = None, render_queue: primitives.Int | None = None, converted_material: str | TextUnlitMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            outline_thickness: Initial value for OutlineThickness.
            outline_color: Initial value for OutlineColor.
            face_softness: Initial value for FaceSoftness.
            face_dilate: Initial value for FaceDilate.
            culling: Initial value for Culling.
            ztest: Initial value for ZTest.
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
        if culling is not None:
            self.culling = culling
        if ztest is not None:
            self.ztest = ztest
        if render_queue is not None:
            self.render_queue = render_queue
        if converted_material is not None:
            self.converted_material = converted_material

    @property
    def outline_thickness(self) -> primitives.Float | None:
        """The thickness of the outer border of the characters."""
        member = self.get_member("OutlineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_thickness.setter
    def outline_thickness(self, value: primitives.Float) -> None:
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
        """The color of the outer border on characters."""
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
    def face_softness(self) -> primitives.Float | None:
        """How much to soften the edges of the characters to make them not so sharp."""
        member = self.get_member("FaceSoftness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_softness.setter
    def face_softness(self, value: primitives.Float) -> None:
        """Set the FaceSoftness field value."""
        member = self.get_member("FaceSoftness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceSoftness", fields.FieldFloat(value=value)
            )

    @property
    def face_dilate(self) -> primitives.Float | None:
        """How much to puff up the characters and make them more bold."""
        member = self.get_member("FaceDilate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_dilate.setter
    def face_dilate(self, value: primitives.Float) -> None:
        """Set the FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceDilate", fields.FieldFloat(value=value)
            )

    @property
    def culling(self) -> Culling | None:
        """The Culling enum value."""
        member = self.get_member("Culling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Culling(member.value)
        return None

    @culling.setter
    def culling(self, value: Culling | str) -> None:
        """Set the Culling enum value."""
        member = self.get_member("Culling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Culling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def ztest(self) -> ZTest | None:
        """The ZTest enum value."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ZTest(member.value)
        return None

    @ztest.setter
    def ztest(self, value: ZTest | str) -> None:
        """Set the ZTest enum value."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ZTest",
                members.FieldEnum(value=str(value)),
            )

    @property
    def render_queue(self) -> primitives.Int | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: primitives.Int) -> None:
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
        """The converted material version of this material."""
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

