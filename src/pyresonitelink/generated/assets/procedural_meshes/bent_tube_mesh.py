"""Generated component: BentTubeMesh."""

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


class BentTubeMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BentTubeMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BentTubeMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, radius: np.float32 | None = None, sides: np.int32 | None = None, segments: np.int32 | None = None, start_point: primitives.Float3 | None = None, direct_target_point: primitives.Float3 | None = None, actual_target_point: primitives.Float3 | None = None, start_point_color: primitives.ColorX | None = None, end_point_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            radius: Initial value for Radius.
            sides: Initial value for Sides.
            segments: Initial value for Segments.
            start_point: Initial value for StartPoint.
            direct_target_point: Initial value for DirectTargetPoint.
            actual_target_point: Initial value for ActualTargetPoint.
            start_point_color: Initial value for StartPointColor.
            end_point_color: Initial value for EndPointColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if radius is not None:
            self.radius = radius
        if sides is not None:
            self.sides = sides
        if segments is not None:
            self.segments = segments
        if start_point is not None:
            self.start_point = start_point
        if direct_target_point is not None:
            self.direct_target_point = direct_target_point
        if actual_target_point is not None:
            self.actual_target_point = actual_target_point
        if start_point_color is not None:
            self.start_point_color = start_point_color
        if end_point_color is not None:
            self.end_point_color = end_point_color

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
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def sides(self) -> np.int32 | None:
        """The Sides field value."""
        member = self.get_member("Sides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sides.setter
    def sides(self, value: np.int32) -> None:
        """Set the Sides field value."""
        member = self.get_member("Sides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Sides", fields.FieldInt(value=value)
            )

    @property
    def segments(self) -> np.int32 | None:
        """The Segments field value."""
        member = self.get_member("Segments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @segments.setter
    def segments(self, value: np.int32) -> None:
        """Set the Segments field value."""
        member = self.get_member("Segments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Segments", fields.FieldInt(value=value)
            )

    @property
    def start_point(self) -> primitives.Float3 | None:
        """The StartPoint field value."""
        member = self.get_member("StartPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_point.setter
    def start_point(self, value: primitives.Float3) -> None:
        """Set the StartPoint field value."""
        member = self.get_member("StartPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartPoint", fields.FieldFloat3(value=value)
            )

    @property
    def direct_target_point(self) -> primitives.Float3 | None:
        """The DirectTargetPoint field value."""
        member = self.get_member("DirectTargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_target_point.setter
    def direct_target_point(self, value: primitives.Float3) -> None:
        """Set the DirectTargetPoint field value."""
        member = self.get_member("DirectTargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectTargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def actual_target_point(self) -> primitives.Float3 | None:
        """The ActualTargetPoint field value."""
        member = self.get_member("ActualTargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_target_point.setter
    def actual_target_point(self, value: primitives.Float3) -> None:
        """Set the ActualTargetPoint field value."""
        member = self.get_member("ActualTargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActualTargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def start_point_color(self) -> primitives.ColorX | None:
        """The StartPointColor field value."""
        member = self.get_member("StartPointColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_point_color.setter
    def start_point_color(self, value: primitives.ColorX) -> None:
        """Set the StartPointColor field value."""
        member = self.get_member("StartPointColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartPointColor", fields.FieldColorX(value=value)
            )

    @property
    def end_point_color(self) -> primitives.ColorX | None:
        """The EndPointColor field value."""
        member = self.get_member("EndPointColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_point_color.setter
    def end_point_color(self, value: primitives.ColorX) -> None:
        """Set the EndPointColor field value."""
        member = self.get_member("EndPointColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndPointColor", fields.FieldColorX(value=value)
            )

    @property
    def ends(self) -> members.FieldEnum | None:
        """The Ends member."""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ends.setter
    def ends(self, value: members.FieldEnum) -> None:
        """Set the Ends member."""
        self.set_member("Ends", value)

    @property
    def shading(self) -> members.FieldEnum | None:
        """The Shading member."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shading.setter
    def shading(self, value: members.FieldEnum) -> None:
        """Set the Shading member."""
        self.set_member("Shading", value)

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

