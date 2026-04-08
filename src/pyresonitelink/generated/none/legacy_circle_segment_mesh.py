"""Generated component: LegacyCircleSegmentMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyCircleSegmentMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyCircleSegmentMesh.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyCircleSegmentMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, expand_lerp: np.float32 | None = None, inner_circle: bool | None = None, radius_start: np.float32 | None = None, thickness: np.float32 | None = None, main_segment_arc: np.float32 | None = None, separation_angle: np.float32 | None = None, menu_main_segment_arc: np.float32 | None = None, circle_item_count: np.int32 | None = None, menu_radius_start: np.float32 | None = None, menu_thickness: np.float32 | None = None, fill_color: primitives.ColorX | None = None, outline_color: primitives.ColorX | None = None, outline_width: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            expand_lerp: Initial value for ExpandLerp.
            inner_circle: Initial value for InnerCircle.
            radius_start: Initial value for RadiusStart.
            thickness: Initial value for Thickness.
            main_segment_arc: Initial value for MainSegmentArc.
            separation_angle: Initial value for SeparationAngle.
            menu_main_segment_arc: Initial value for MenuMainSegmentArc.
            circle_item_count: Initial value for CircleItemCount.
            menu_radius_start: Initial value for MenuRadiusStart.
            menu_thickness: Initial value for MenuThickness.
            fill_color: Initial value for FillColor.
            outline_color: Initial value for OutlineColor.
            outline_width: Initial value for OutlineWidth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if expand_lerp is not None:
            self.expand_lerp = expand_lerp
        if inner_circle is not None:
            self.inner_circle = inner_circle
        if radius_start is not None:
            self.radius_start = radius_start
        if thickness is not None:
            self.thickness = thickness
        if main_segment_arc is not None:
            self.main_segment_arc = main_segment_arc
        if separation_angle is not None:
            self.separation_angle = separation_angle
        if menu_main_segment_arc is not None:
            self.menu_main_segment_arc = menu_main_segment_arc
        if circle_item_count is not None:
            self.circle_item_count = circle_item_count
        if menu_radius_start is not None:
            self.menu_radius_start = menu_radius_start
        if menu_thickness is not None:
            self.menu_thickness = menu_thickness
        if fill_color is not None:
            self.fill_color = fill_color
        if outline_color is not None:
            self.outline_color = outline_color
        if outline_width is not None:
            self.outline_width = outline_width

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: bool) -> None:
        """Set the OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideBoundingBox", fields.FieldBool(value=value)
            )

    @property
    def overriden_bounding_box(self) -> primitives.BoundingBox | None:
        """The OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overriden_bounding_box.setter
    def overriden_bounding_box(self, value: primitives.BoundingBox) -> None:
        """Set the OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverridenBoundingBox", fields.FieldBoundingBox(value=value)
            )

    @property
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def expand_lerp(self) -> np.float32 | None:
        """The ExpandLerp field value."""
        member = self.get_member("ExpandLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expand_lerp.setter
    def expand_lerp(self, value: np.float32) -> None:
        """Set the ExpandLerp field value."""
        member = self.get_member("ExpandLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExpandLerp", fields.FieldFloat(value=value)
            )

    @property
    def inner_circle(self) -> bool | None:
        """The InnerCircle field value."""
        member = self.get_member("InnerCircle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_circle.setter
    def inner_circle(self, value: bool) -> None:
        """Set the InnerCircle field value."""
        member = self.get_member("InnerCircle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerCircle", fields.FieldBool(value=value)
            )

    @property
    def radius_start(self) -> np.float32 | None:
        """The RadiusStart field value."""
        member = self.get_member("RadiusStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_start.setter
    def radius_start(self, value: np.float32) -> None:
        """Set the RadiusStart field value."""
        member = self.get_member("RadiusStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusStart", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> np.float32 | None:
        """The Thickness field value."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: np.float32) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def main_segment_arc(self) -> np.float32 | None:
        """The MainSegmentArc field value."""
        member = self.get_member("MainSegmentArc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @main_segment_arc.setter
    def main_segment_arc(self, value: np.float32) -> None:
        """Set the MainSegmentArc field value."""
        member = self.get_member("MainSegmentArc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MainSegmentArc", fields.FieldFloat(value=value)
            )

    @property
    def separation_angle(self) -> np.float32 | None:
        """The SeparationAngle field value."""
        member = self.get_member("SeparationAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separation_angle.setter
    def separation_angle(self, value: np.float32) -> None:
        """Set the SeparationAngle field value."""
        member = self.get_member("SeparationAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SeparationAngle", fields.FieldFloat(value=value)
            )

    @property
    def menu_main_segment_arc(self) -> np.float32 | None:
        """The MenuMainSegmentArc field value."""
        member = self.get_member("MenuMainSegmentArc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @menu_main_segment_arc.setter
    def menu_main_segment_arc(self, value: np.float32) -> None:
        """Set the MenuMainSegmentArc field value."""
        member = self.get_member("MenuMainSegmentArc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MenuMainSegmentArc", fields.FieldFloat(value=value)
            )

    @property
    def circle_item_count(self) -> np.int32 | None:
        """The CircleItemCount field value."""
        member = self.get_member("CircleItemCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_item_count.setter
    def circle_item_count(self, value: np.int32) -> None:
        """Set the CircleItemCount field value."""
        member = self.get_member("CircleItemCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CircleItemCount", fields.FieldInt(value=value)
            )

    @property
    def menu_radius_start(self) -> np.float32 | None:
        """The MenuRadiusStart field value."""
        member = self.get_member("MenuRadiusStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @menu_radius_start.setter
    def menu_radius_start(self, value: np.float32) -> None:
        """Set the MenuRadiusStart field value."""
        member = self.get_member("MenuRadiusStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MenuRadiusStart", fields.FieldFloat(value=value)
            )

    @property
    def menu_thickness(self) -> np.float32 | None:
        """The MenuThickness field value."""
        member = self.get_member("MenuThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @menu_thickness.setter
    def menu_thickness(self, value: np.float32) -> None:
        """Set the MenuThickness field value."""
        member = self.get_member("MenuThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MenuThickness", fields.FieldFloat(value=value)
            )

    @property
    def fill_color(self) -> primitives.ColorX | None:
        """The FillColor field value."""
        member = self.get_member("FillColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_color.setter
    def fill_color(self, value: primitives.ColorX) -> None:
        """Set the FillColor field value."""
        member = self.get_member("FillColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillColor", fields.FieldColorX(value=value)
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
    def circle_item_overrides(self) -> members.SyncList | None:
        """The CircleItemOverrides member."""
        member = self.get_member("CircleItemOverrides")
        if isinstance(member, members.SyncList):
            return member
        return None

    @circle_item_overrides.setter
    def circle_item_overrides(self, value: members.SyncList) -> None:
        """Set the CircleItemOverrides member."""
        self.set_member("CircleItemOverrides", value)

    @property
    def independent_segments(self) -> members.SyncList | None:
        """The IndependentSegments member."""
        member = self.get_member("IndependentSegments")
        if isinstance(member, members.SyncList):
            return member
        return None

    @independent_segments.setter
    def independent_segments(self, value: members.SyncList) -> None:
        """Set the IndependentSegments member."""
        self.set_member("IndependentSegments", value)

    @property
    def outline_width(self) -> np.float32 | None:
        """The OutlineWidth field value."""
        member = self.get_member("OutlineWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_width.setter
    def outline_width(self, value: np.float32) -> None:
        """Set the OutlineWidth field value."""
        member = self.get_member("OutlineWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineWidth", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

