"""Generated component: IcoSphereMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IcoSphereMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The IcoSphereMesh component procedurally generates a icosahedron mesh for use with a MeshRenderer, according to the parameters provided. 

As of Version 2020.10.25.1103, this value is clamped in the range [0,8] to prevent accidentally creating a mesh with an excessive number of vertices.

    Category: Assets/Procedural Meshes

    Attach to a slot and insert into a MeshRenderer to view the geometry.
    Don't forget to use a Material.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.IcoSphereMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, radius: primitives.Float | None = None, subdivisions: primitives.Int | None = None, flat_shading: primitives.Bool | None = None, flat_face_extrude: primitives.Float | None = None, flat_face_scale: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            radius: Initial value for Radius.
            subdivisions: Initial value for Subdivisions.
            flat_shading: Initial value for FlatShading.
            flat_face_extrude: Initial value for FlatFaceExtrude.
            flat_face_scale: Initial value for FlatFaceScale.
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
        if radius is not None:
            self.radius = radius
        if subdivisions is not None:
            self.subdivisions = subdivisions
        if flat_shading is not None:
            self.flat_shading = flat_shading
        if flat_face_extrude is not None:
            self.flat_face_extrude = flat_face_extrude
        if flat_face_scale is not None:
            self.flat_face_scale = flat_face_scale

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
    def radius(self) -> primitives.Float | None:
        """Radius of the IcoSphere"""
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
    def subdivisions(self) -> primitives.Int | None:
        """Number of IcoSphere subdivisions — Values are clamped in the range [0,8]"""
        member = self.get_member("Subdivisions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subdivisions.setter
    def subdivisions(self, value: primitives.Int) -> None:
        """Set the Subdivisions field value."""
        member = self.get_member("Subdivisions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Subdivisions", fields.FieldInt(value=value)
            )

    @property
    def flat_shading(self) -> primitives.Bool | None:
        """Use flat/faceted shading instead of smooth shading."""
        member = self.get_member("FlatShading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_shading.setter
    def flat_shading(self, value: primitives.Bool) -> None:
        """Set the FlatShading field value."""
        member = self.get_member("FlatShading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlatShading", fields.FieldBool(value=value)
            )

    @property
    def flat_face_extrude(self) -> primitives.Float | None:
        """Distance to extrude faces after being generated. Creates an "Exploded" appearance"""
        member = self.get_member("FlatFaceExtrude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_face_extrude.setter
    def flat_face_extrude(self, value: primitives.Float) -> None:
        """Set the FlatFaceExtrude field value."""
        member = self.get_member("FlatFaceExtrude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlatFaceExtrude", fields.FieldFloat(value=value)
            )

    @property
    def flat_face_scale(self) -> primitives.Float | None:
        """Scale of individual faces, relative to their base size."""
        member = self.get_member("FlatFaceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_face_scale.setter
    def flat_face_scale(self, value: primitives.Float) -> None:
        """Set the FlatFaceScale field value."""
        member = self.get_member("FlatFaceScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlatFaceScale", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

