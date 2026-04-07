"""Generated component: BentTubeMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BentTubeMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BentTubeMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BentTubeMesh"

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

