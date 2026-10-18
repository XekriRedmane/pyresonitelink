"""Generated component: RawMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RawMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RawMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, uv0_dimensions: primitives.Int | None = None, uv1_dimensions: primitives.Int | None = None, uv2_dimensions: primitives.Int | None = None, uv3_dimensions: primitives.Int | None = None, uv4_dimensions: primitives.Int | None = None, uv5_dimensions: primitives.Int | None = None, uv6_dimensions: primitives.Int | None = None, uv7_dimensions: primitives.Int | None = None, uv8_dimensions: primitives.Int | None = None, colors_profile: ColorProfile | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            uv0_dimensions: Initial value for UV0_Dimensions.
            uv1_dimensions: Initial value for UV1_Dimensions.
            uv2_dimensions: Initial value for UV2_Dimensions.
            uv3_dimensions: Initial value for UV3_Dimensions.
            uv4_dimensions: Initial value for UV4_Dimensions.
            uv5_dimensions: Initial value for UV5_Dimensions.
            uv6_dimensions: Initial value for UV6_Dimensions.
            uv7_dimensions: Initial value for UV7_Dimensions.
            uv8_dimensions: Initial value for UV8_Dimensions.
            colors_profile: Initial value for ColorsProfile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if profile is not None:
            self.profile = profile
        if uv0_dimensions is not None:
            self.uv0_dimensions = uv0_dimensions
        if uv1_dimensions is not None:
            self.uv1_dimensions = uv1_dimensions
        if uv2_dimensions is not None:
            self.uv2_dimensions = uv2_dimensions
        if uv3_dimensions is not None:
            self.uv3_dimensions = uv3_dimensions
        if uv4_dimensions is not None:
            self.uv4_dimensions = uv4_dimensions
        if uv5_dimensions is not None:
            self.uv5_dimensions = uv5_dimensions
        if uv6_dimensions is not None:
            self.uv6_dimensions = uv6_dimensions
        if uv7_dimensions is not None:
            self.uv7_dimensions = uv7_dimensions
        if uv8_dimensions is not None:
            self.uv8_dimensions = uv8_dimensions
        if colors_profile is not None:
            self.colors_profile = colors_profile

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
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def points(self) -> list[primitives.Float3] | None:
        """The Points array values."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @points.setter
    def points(self, value: list[primitives.Float3]) -> None:
        """Set the Points array values."""
        member = self.get_member("Points")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.ArrayFloat3(values=value)
            )

    @property
    def normals(self) -> list[primitives.Float3] | None:
        """The Normals array values."""
        member = self.get_member("Normals")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @normals.setter
    def normals(self, value: list[primitives.Float3]) -> None:
        """Set the Normals array values."""
        member = self.get_member("Normals")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Normals", fields.ArrayFloat3(values=value)
            )

    @property
    def tangents(self) -> list[primitives.Float4] | None:
        """The Tangents array values."""
        member = self.get_member("Tangents")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @tangents.setter
    def tangents(self, value: list[primitives.Float4]) -> None:
        """Set the Tangents array values."""
        member = self.get_member("Tangents")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tangents", fields.ArrayFloat4(values=value)
            )

    @property
    def uv0s(self) -> list[primitives.Float4] | None:
        """The UV0s array values."""
        member = self.get_member("UV0s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv0s.setter
    def uv0s(self, value: list[primitives.Float4]) -> None:
        """Set the UV0s array values."""
        member = self.get_member("UV0s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV0s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv1s(self) -> list[primitives.Float4] | None:
        """The UV1s array values."""
        member = self.get_member("UV1s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv1s.setter
    def uv1s(self, value: list[primitives.Float4]) -> None:
        """Set the UV1s array values."""
        member = self.get_member("UV1s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV1s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv2s(self) -> list[primitives.Float4] | None:
        """The UV2s array values."""
        member = self.get_member("UV2s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv2s.setter
    def uv2s(self, value: list[primitives.Float4]) -> None:
        """Set the UV2s array values."""
        member = self.get_member("UV2s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV2s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv3s(self) -> list[primitives.Float4] | None:
        """The UV3s array values."""
        member = self.get_member("UV3s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv3s.setter
    def uv3s(self, value: list[primitives.Float4]) -> None:
        """Set the UV3s array values."""
        member = self.get_member("UV3s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV3s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv4s(self) -> list[primitives.Float4] | None:
        """The UV4s array values."""
        member = self.get_member("UV4s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv4s.setter
    def uv4s(self, value: list[primitives.Float4]) -> None:
        """Set the UV4s array values."""
        member = self.get_member("UV4s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV4s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv5s(self) -> list[primitives.Float4] | None:
        """The UV5s array values."""
        member = self.get_member("UV5s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv5s.setter
    def uv5s(self, value: list[primitives.Float4]) -> None:
        """Set the UV5s array values."""
        member = self.get_member("UV5s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV5s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv6s(self) -> list[primitives.Float4] | None:
        """The UV6s array values."""
        member = self.get_member("UV6s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv6s.setter
    def uv6s(self, value: list[primitives.Float4]) -> None:
        """Set the UV6s array values."""
        member = self.get_member("UV6s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV6s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv7s(self) -> list[primitives.Float4] | None:
        """The UV7s array values."""
        member = self.get_member("UV7s")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uv7s.setter
    def uv7s(self, value: list[primitives.Float4]) -> None:
        """Set the UV7s array values."""
        member = self.get_member("UV7s")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV7s", fields.ArrayFloat4(values=value)
            )

    @property
    def uv0_dimensions(self) -> primitives.Int | None:
        """The UV0_Dimensions field value."""
        member = self.get_member("UV0_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv0_dimensions.setter
    def uv0_dimensions(self, value: primitives.Int) -> None:
        """Set the UV0_Dimensions field value."""
        member = self.get_member("UV0_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV0_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv1_dimensions(self) -> primitives.Int | None:
        """The UV1_Dimensions field value."""
        member = self.get_member("UV1_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv1_dimensions.setter
    def uv1_dimensions(self, value: primitives.Int) -> None:
        """Set the UV1_Dimensions field value."""
        member = self.get_member("UV1_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV1_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv2_dimensions(self) -> primitives.Int | None:
        """The UV2_Dimensions field value."""
        member = self.get_member("UV2_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv2_dimensions.setter
    def uv2_dimensions(self, value: primitives.Int) -> None:
        """Set the UV2_Dimensions field value."""
        member = self.get_member("UV2_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV2_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv3_dimensions(self) -> primitives.Int | None:
        """The UV3_Dimensions field value."""
        member = self.get_member("UV3_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv3_dimensions.setter
    def uv3_dimensions(self, value: primitives.Int) -> None:
        """Set the UV3_Dimensions field value."""
        member = self.get_member("UV3_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV3_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv4_dimensions(self) -> primitives.Int | None:
        """The UV4_Dimensions field value."""
        member = self.get_member("UV4_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv4_dimensions.setter
    def uv4_dimensions(self, value: primitives.Int) -> None:
        """Set the UV4_Dimensions field value."""
        member = self.get_member("UV4_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV4_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv5_dimensions(self) -> primitives.Int | None:
        """The UV5_Dimensions field value."""
        member = self.get_member("UV5_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv5_dimensions.setter
    def uv5_dimensions(self, value: primitives.Int) -> None:
        """Set the UV5_Dimensions field value."""
        member = self.get_member("UV5_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV5_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv6_dimensions(self) -> primitives.Int | None:
        """The UV6_Dimensions field value."""
        member = self.get_member("UV6_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv6_dimensions.setter
    def uv6_dimensions(self, value: primitives.Int) -> None:
        """Set the UV6_Dimensions field value."""
        member = self.get_member("UV6_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV6_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv7_dimensions(self) -> primitives.Int | None:
        """The UV7_Dimensions field value."""
        member = self.get_member("UV7_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv7_dimensions.setter
    def uv7_dimensions(self, value: primitives.Int) -> None:
        """Set the UV7_Dimensions field value."""
        member = self.get_member("UV7_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV7_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def uv8_dimensions(self) -> primitives.Int | None:
        """The UV8_Dimensions field value."""
        member = self.get_member("UV8_Dimensions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv8_dimensions.setter
    def uv8_dimensions(self, value: primitives.Int) -> None:
        """Set the UV8_Dimensions field value."""
        member = self.get_member("UV8_Dimensions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UV8_Dimensions", fields.FieldInt(value=value)
            )

    @property
    def colors(self) -> list[primitives.Color] | None:
        """The Colors array values."""
        member = self.get_member("Colors")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @colors.setter
    def colors(self, value: list[primitives.Color]) -> None:
        """Set the Colors array values."""
        member = self.get_member("Colors")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Colors", fields.ArrayColor(values=value)
            )

    @property
    def colors_profile(self) -> ColorProfile | None:
        """The ColorsProfile enum value."""
        member = self.get_member("ColorsProfile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @colors_profile.setter
    def colors_profile(self, value: ColorProfile | str) -> None:
        """Set the ColorsProfile enum value."""
        member = self.get_member("ColorsProfile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ColorsProfile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def submeshes(self) -> members.SyncList | None:
        """The Submeshes member."""
        member = self.get_member("Submeshes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @submeshes.setter
    def submeshes(self, value: members.SyncList) -> None:
        """Set the Submeshes member."""
        self.set_member("Submeshes", value)

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

