"""Generated component: IcoSphereMesh."""

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


class IcoSphereMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.IcoSphereMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.IcoSphereMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, radius: np.float32 | None = None, subdivisions: np.int32 | None = None, flat_shading: bool | None = None, flat_face_extrude: np.float32 | None = None, flat_face_scale: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
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
    def subdivisions(self) -> np.int32 | None:
        """The Subdivisions field value."""
        member = self.get_member("Subdivisions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subdivisions.setter
    def subdivisions(self, value: np.int32) -> None:
        """Set the Subdivisions field value."""
        member = self.get_member("Subdivisions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Subdivisions", fields.FieldInt(value=value)
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
    def flat_face_extrude(self) -> np.float32 | None:
        """The FlatFaceExtrude field value."""
        member = self.get_member("FlatFaceExtrude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_face_extrude.setter
    def flat_face_extrude(self, value: np.float32) -> None:
        """Set the FlatFaceExtrude field value."""
        member = self.get_member("FlatFaceExtrude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlatFaceExtrude", fields.FieldFloat(value=value)
            )

    @property
    def flat_face_scale(self) -> np.float32 | None:
        """The FlatFaceScale field value."""
        member = self.get_member("FlatFaceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flat_face_scale.setter
    def flat_face_scale(self, value: np.float32) -> None:
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

