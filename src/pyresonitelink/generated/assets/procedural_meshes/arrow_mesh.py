"""Generated component: ArrowMesh."""

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


class ArrowMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ArrowMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ArrowMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, vector: primitives.Float3 | None = None, sides: np.int32 | None = None, body_radius: np.float32 | None = None, head_radius: np.float32 | None = None, head_length: np.float32 | None = None, minimal_body_length: np.float32 | None = None, sphere_on_zero: bool | None = None, body_uv_scale: primitives.Float2 | None = None, body_uv_offset: primitives.Float2 | None = None, head_uv_scale: primitives.Float2 | None = None, head_uv_offset: primitives.Float2 | None = None, base_color: primitives.ColorX | None = None, top_color: primitives.ColorX | None = None, head_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            vector: Initial value for Vector.
            sides: Initial value for Sides.
            body_radius: Initial value for BodyRadius.
            head_radius: Initial value for HeadRadius.
            head_length: Initial value for HeadLength.
            minimal_body_length: Initial value for MinimalBodyLength.
            sphere_on_zero: Initial value for SphereOnZero.
            body_uv_scale: Initial value for BodyUVScale.
            body_uv_offset: Initial value for BodyUVOffset.
            head_uv_scale: Initial value for HeadUVScale.
            head_uv_offset: Initial value for HeadUVOffset.
            base_color: Initial value for BaseColor.
            top_color: Initial value for TopColor.
            head_color: Initial value for HeadColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if vector is not None:
            self.vector = vector
        if sides is not None:
            self.sides = sides
        if body_radius is not None:
            self.body_radius = body_radius
        if head_radius is not None:
            self.head_radius = head_radius
        if head_length is not None:
            self.head_length = head_length
        if minimal_body_length is not None:
            self.minimal_body_length = minimal_body_length
        if sphere_on_zero is not None:
            self.sphere_on_zero = sphere_on_zero
        if body_uv_scale is not None:
            self.body_uv_scale = body_uv_scale
        if body_uv_offset is not None:
            self.body_uv_offset = body_uv_offset
        if head_uv_scale is not None:
            self.head_uv_scale = head_uv_scale
        if head_uv_offset is not None:
            self.head_uv_offset = head_uv_offset
        if base_color is not None:
            self.base_color = base_color
        if top_color is not None:
            self.top_color = top_color
        if head_color is not None:
            self.head_color = head_color

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
    def vector(self) -> primitives.Float3 | None:
        """The Vector field value."""
        member = self.get_member("Vector")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vector.setter
    def vector(self, value: primitives.Float3) -> None:
        """Set the Vector field value."""
        member = self.get_member("Vector")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vector", fields.FieldFloat3(value=value)
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
    def body_radius(self) -> np.float32 | None:
        """The BodyRadius field value."""
        member = self.get_member("BodyRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @body_radius.setter
    def body_radius(self, value: np.float32) -> None:
        """Set the BodyRadius field value."""
        member = self.get_member("BodyRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BodyRadius", fields.FieldFloat(value=value)
            )

    @property
    def head_radius(self) -> np.float32 | None:
        """The HeadRadius field value."""
        member = self.get_member("HeadRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_radius.setter
    def head_radius(self, value: np.float32) -> None:
        """Set the HeadRadius field value."""
        member = self.get_member("HeadRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadRadius", fields.FieldFloat(value=value)
            )

    @property
    def head_length(self) -> np.float32 | None:
        """The HeadLength field value."""
        member = self.get_member("HeadLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_length.setter
    def head_length(self, value: np.float32) -> None:
        """Set the HeadLength field value."""
        member = self.get_member("HeadLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadLength", fields.FieldFloat(value=value)
            )

    @property
    def minimal_body_length(self) -> np.float32 | None:
        """The MinimalBodyLength field value."""
        member = self.get_member("MinimalBodyLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimal_body_length.setter
    def minimal_body_length(self, value: np.float32) -> None:
        """Set the MinimalBodyLength field value."""
        member = self.get_member("MinimalBodyLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimalBodyLength", fields.FieldFloat(value=value)
            )

    @property
    def sphere_on_zero(self) -> bool | None:
        """The SphereOnZero field value."""
        member = self.get_member("SphereOnZero")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sphere_on_zero.setter
    def sphere_on_zero(self, value: bool) -> None:
        """Set the SphereOnZero field value."""
        member = self.get_member("SphereOnZero")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SphereOnZero", fields.FieldBool(value=value)
            )

    @property
    def body_uv_scale(self) -> primitives.Float2 | None:
        """The BodyUVScale field value."""
        member = self.get_member("BodyUVScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @body_uv_scale.setter
    def body_uv_scale(self, value: primitives.Float2) -> None:
        """Set the BodyUVScale field value."""
        member = self.get_member("BodyUVScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BodyUVScale", fields.FieldFloat2(value=value)
            )

    @property
    def body_uv_offset(self) -> primitives.Float2 | None:
        """The BodyUVOffset field value."""
        member = self.get_member("BodyUVOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @body_uv_offset.setter
    def body_uv_offset(self, value: primitives.Float2) -> None:
        """Set the BodyUVOffset field value."""
        member = self.get_member("BodyUVOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BodyUVOffset", fields.FieldFloat2(value=value)
            )

    @property
    def head_uv_scale(self) -> primitives.Float2 | None:
        """The HeadUVScale field value."""
        member = self.get_member("HeadUVScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_uv_scale.setter
    def head_uv_scale(self, value: primitives.Float2) -> None:
        """Set the HeadUVScale field value."""
        member = self.get_member("HeadUVScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadUVScale", fields.FieldFloat2(value=value)
            )

    @property
    def head_uv_offset(self) -> primitives.Float2 | None:
        """The HeadUVOffset field value."""
        member = self.get_member("HeadUVOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_uv_offset.setter
    def head_uv_offset(self, value: primitives.Float2) -> None:
        """Set the HeadUVOffset field value."""
        member = self.get_member("HeadUVOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadUVOffset", fields.FieldFloat2(value=value)
            )

    @property
    def base_color(self) -> primitives.ColorX | None:
        """The BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_color.setter
    def base_color(self, value: primitives.ColorX) -> None:
        """Set the BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseColor", fields.FieldColorX(value=value)
            )

    @property
    def top_color(self) -> primitives.ColorX | None:
        """The TopColor field value."""
        member = self.get_member("TopColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @top_color.setter
    def top_color(self, value: primitives.ColorX) -> None:
        """Set the TopColor field value."""
        member = self.get_member("TopColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TopColor", fields.FieldColorX(value=value)
            )

    @property
    def head_color(self) -> primitives.ColorX | None:
        """The HeadColor field value."""
        member = self.get_member("HeadColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_color.setter
    def head_color(self, value: primitives.ColorX) -> None:
        """Set the HeadColor field value."""
        member = self.get_member("HeadColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadColor", fields.FieldColorX(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

