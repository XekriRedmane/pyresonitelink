"""Generated component: ColorDepthGrid."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorDepthGrid(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColorDepthGrid.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColorDepthGrid"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, color_texture: str | IAssetProvider[Texture2D] | None = None, depth_texture: str | IAssetProvider[Texture2D] | None = None, horizontal_angle: np.float32 | None = None, vertical_angle: np.float32 | None = None, depth_offset: np.float32 | None = None, depth_scale: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            color_texture: Initial value for ColorTexture.
            depth_texture: Initial value for DepthTexture.
            horizontal_angle: Initial value for HorizontalAngle.
            vertical_angle: Initial value for VerticalAngle.
            depth_offset: Initial value for DepthOffset.
            depth_scale: Initial value for DepthScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if color_texture is not None:
            self.color_texture = color_texture
        if depth_texture is not None:
            self.depth_texture = depth_texture
        if horizontal_angle is not None:
            self.horizontal_angle = horizontal_angle
        if vertical_angle is not None:
            self.vertical_angle = vertical_angle
        if depth_offset is not None:
            self.depth_offset = depth_offset
        if depth_scale is not None:
            self.depth_scale = depth_scale

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
    def color_texture(self) -> str | None:
        """Target ID of the ColorTexture reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("ColorTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_texture.setter
    def color_texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the ColorTexture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ColorTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColorTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def depth_texture(self) -> str | None:
        """Target ID of the DepthTexture reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("DepthTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @depth_texture.setter
    def depth_texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the DepthTexture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("DepthTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DepthTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def projection(self) -> members.FieldEnum | None:
        """The Projection member."""
        member = self.get_member("Projection")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @projection.setter
    def projection(self, value: members.FieldEnum) -> None:
        """Set the Projection member."""
        self.set_member("Projection", value)

    @property
    def horizontal_angle(self) -> np.float32 | None:
        """The HorizontalAngle field value."""
        member = self.get_member("HorizontalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_angle.setter
    def horizontal_angle(self, value: np.float32) -> None:
        """Set the HorizontalAngle field value."""
        member = self.get_member("HorizontalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalAngle", fields.FieldFloat(value=value)
            )

    @property
    def vertical_angle(self) -> np.float32 | None:
        """The VerticalAngle field value."""
        member = self.get_member("VerticalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_angle.setter
    def vertical_angle(self, value: np.float32) -> None:
        """Set the VerticalAngle field value."""
        member = self.get_member("VerticalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalAngle", fields.FieldFloat(value=value)
            )

    @property
    def depth_offset(self) -> np.float32 | None:
        """The DepthOffset field value."""
        member = self.get_member("DepthOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_offset.setter
    def depth_offset(self, value: np.float32) -> None:
        """Set the DepthOffset field value."""
        member = self.get_member("DepthOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthOffset", fields.FieldFloat(value=value)
            )

    @property
    def depth_scale(self) -> np.float32 | None:
        """The DepthScale field value."""
        member = self.get_member("DepthScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_scale.setter
    def depth_scale(self, value: np.float32) -> None:
        """Set the DepthScale field value."""
        member = self.get_member("DepthScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthScale", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

