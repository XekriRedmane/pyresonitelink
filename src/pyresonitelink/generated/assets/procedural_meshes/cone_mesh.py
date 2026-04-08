"""Generated component: ConeMesh."""

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


class ConeMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ConeMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConeMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, height: np.float32 | None = None, radius_base: np.float32 | None = None, radius_top: np.float32 | None = None, sides: np.int32 | None = None, caps: bool | None = None, flat_shading: bool | None = None, uv_scale: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            height: Initial value for Height.
            radius_base: Initial value for RadiusBase.
            radius_top: Initial value for RadiusTop.
            sides: Initial value for Sides.
            caps: Initial value for Caps.
            flat_shading: Initial value for FlatShading.
            uv_scale: Initial value for UVScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if height is not None:
            self.height = height
        if radius_base is not None:
            self.radius_base = radius_base
        if radius_top is not None:
            self.radius_top = radius_top
        if sides is not None:
            self.sides = sides
        if caps is not None:
            self.caps = caps
        if flat_shading is not None:
            self.flat_shading = flat_shading
        if uv_scale is not None:
            self.uv_scale = uv_scale

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
    def height(self) -> np.float32 | None:
        """The Height field value."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: np.float32) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def radius_base(self) -> np.float32 | None:
        """The RadiusBase field value."""
        member = self.get_member("RadiusBase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_base.setter
    def radius_base(self, value: np.float32) -> None:
        """Set the RadiusBase field value."""
        member = self.get_member("RadiusBase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusBase", fields.FieldFloat(value=value)
            )

    @property
    def radius_top(self) -> np.float32 | None:
        """The RadiusTop field value."""
        member = self.get_member("RadiusTop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_top.setter
    def radius_top(self, value: np.float32) -> None:
        """Set the RadiusTop field value."""
        member = self.get_member("RadiusTop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusTop", fields.FieldFloat(value=value)
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
    def caps(self) -> bool | None:
        """The Caps field value."""
        member = self.get_member("Caps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @caps.setter
    def caps(self, value: bool) -> None:
        """Set the Caps field value."""
        member = self.get_member("Caps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Caps", fields.FieldBool(value=value)
            )

    @property
    def flat_shading(self) -> bool | None:
        """The FlatShading field value."""
        member = self.get_member("FlatShading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_shading.setter
    def flat_shading(self, value: bool) -> None:
        """Set the FlatShading field value."""
        member = self.get_member("FlatShading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlatShading", fields.FieldBool(value=value)
            )

    @property
    def uv_scale(self) -> primitives.Float2 | None:
        """The UVScale field value."""
        member = self.get_member("UVScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_scale.setter
    def uv_scale(self, value: primitives.Float2) -> None:
        """Set the UVScale field value."""
        member = self.get_member("UVScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVScale", fields.FieldFloat2(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

