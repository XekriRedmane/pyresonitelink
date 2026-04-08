"""Generated component: CameraFrustumMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CameraFrustumMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CameraFrustumMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CameraFrustumMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, orientation: primitives.FloatQ | None = None, near: primitives.Float | None = None, far: primitives.Float | None = None, horizontal_angle: primitives.Float | None = None, vertical_angle: primitives.Float | None = None, dual_sided: primitives.Bool | None = None, near_cap: primitives.Bool | None = None, far_cap: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            orientation: Initial value for Orientation.
            near: Initial value for Near.
            far: Initial value for Far.
            horizontal_angle: Initial value for HorizontalAngle.
            vertical_angle: Initial value for VerticalAngle.
            dual_sided: Initial value for DualSided.
            near_cap: Initial value for NearCap.
            far_cap: Initial value for FarCap.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if orientation is not None:
            self.orientation = orientation
        if near is not None:
            self.near = near
        if far is not None:
            self.far = far
        if horizontal_angle is not None:
            self.horizontal_angle = horizontal_angle
        if vertical_angle is not None:
            self.vertical_angle = vertical_angle
        if dual_sided is not None:
            self.dual_sided = dual_sided
        if near_cap is not None:
            self.near_cap = near_cap
        if far_cap is not None:
            self.far_cap = far_cap

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
    def orientation(self) -> primitives.FloatQ | None:
        """The Orientation field value."""
        member = self.get_member("Orientation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orientation.setter
    def orientation(self, value: primitives.FloatQ) -> None:
        """Set the Orientation field value."""
        member = self.get_member("Orientation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Orientation", fields.FieldFloatQ(value=value)
            )

    @property
    def near(self) -> primitives.Float | None:
        """The Near field value."""
        member = self.get_member("Near")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near.setter
    def near(self, value: primitives.Float) -> None:
        """Set the Near field value."""
        member = self.get_member("Near")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Near", fields.FieldFloat(value=value)
            )

    @property
    def far(self) -> primitives.Float | None:
        """The Far field value."""
        member = self.get_member("Far")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far.setter
    def far(self, value: primitives.Float) -> None:
        """Set the Far field value."""
        member = self.get_member("Far")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Far", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_angle(self) -> primitives.Float | None:
        """The HorizontalAngle field value."""
        member = self.get_member("HorizontalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_angle.setter
    def horizontal_angle(self, value: primitives.Float) -> None:
        """Set the HorizontalAngle field value."""
        member = self.get_member("HorizontalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalAngle", fields.FieldFloat(value=value)
            )

    @property
    def vertical_angle(self) -> primitives.Float | None:
        """The VerticalAngle field value."""
        member = self.get_member("VerticalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_angle.setter
    def vertical_angle(self, value: primitives.Float) -> None:
        """Set the VerticalAngle field value."""
        member = self.get_member("VerticalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalAngle", fields.FieldFloat(value=value)
            )

    @property
    def dual_sided(self) -> primitives.Bool | None:
        """The DualSided field value."""
        member = self.get_member("DualSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dual_sided.setter
    def dual_sided(self, value: primitives.Bool) -> None:
        """Set the DualSided field value."""
        member = self.get_member("DualSided")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DualSided", fields.FieldBool(value=value)
            )

    @property
    def near_cap(self) -> primitives.Bool | None:
        """The NearCap field value."""
        member = self.get_member("NearCap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_cap.setter
    def near_cap(self, value: primitives.Bool) -> None:
        """Set the NearCap field value."""
        member = self.get_member("NearCap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearCap", fields.FieldBool(value=value)
            )

    @property
    def far_cap(self) -> primitives.Bool | None:
        """The FarCap field value."""
        member = self.get_member("FarCap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_cap.setter
    def far_cap(self, value: primitives.Bool) -> None:
        """Set the FarCap field value."""
        member = self.get_member("FarCap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarCap", fields.FieldBool(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

