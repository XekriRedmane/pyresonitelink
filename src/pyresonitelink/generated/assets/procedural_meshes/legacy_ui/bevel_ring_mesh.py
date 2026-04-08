"""Generated component: BevelRingMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BevelRingMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BevelRingMesh.

    Category: Assets/Procedural Meshes/Legacy UI
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BevelRingMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, arc: primitives.Float | None = None, arc_offset: primitives.Float | None = None, radius: primitives.Float | None = None, width: primitives.Float | None = None, thickness: primitives.Float | None = None, tilt: primitives.Float | None = None, segments: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            arc: Initial value for Arc.
            arc_offset: Initial value for ArcOffset.
            radius: Initial value for Radius.
            width: Initial value for Width.
            thickness: Initial value for Thickness.
            tilt: Initial value for Tilt.
            segments: Initial value for Segments.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if arc is not None:
            self.arc = arc
        if arc_offset is not None:
            self.arc_offset = arc_offset
        if radius is not None:
            self.radius = radius
        if width is not None:
            self.width = width
        if thickness is not None:
            self.thickness = thickness
        if tilt is not None:
            self.tilt = tilt
        if segments is not None:
            self.segments = segments

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> primitives.Bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: primitives.Bool) -> None:
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
    def arc(self) -> primitives.Float | None:
        """The Arc field value."""
        member = self.get_member("Arc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc.setter
    def arc(self, value: primitives.Float) -> None:
        """Set the Arc field value."""
        member = self.get_member("Arc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Arc", fields.FieldFloat(value=value)
            )

    @property
    def arc_offset(self) -> primitives.Float | None:
        """The ArcOffset field value."""
        member = self.get_member("ArcOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc_offset.setter
    def arc_offset(self, value: primitives.Float) -> None:
        """Set the ArcOffset field value."""
        member = self.get_member("ArcOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ArcOffset", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> primitives.Float | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def width(self) -> primitives.Float | None:
        """The Width field value."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Float) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> primitives.Float | None:
        """The Thickness field value."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: primitives.Float) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def tilt(self) -> primitives.Float | None:
        """The Tilt field value."""
        member = self.get_member("Tilt")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tilt.setter
    def tilt(self, value: primitives.Float) -> None:
        """Set the Tilt field value."""
        member = self.get_member("Tilt")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tilt", fields.FieldFloat(value=value)
            )

    @property
    def segments(self) -> primitives.Int | None:
        """The Segments field value."""
        member = self.get_member("Segments")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @segments.setter
    def segments(self, value: primitives.Int) -> None:
        """Set the Segments field value."""
        member = self.get_member("Segments")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Segments", fields.FieldInt(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

