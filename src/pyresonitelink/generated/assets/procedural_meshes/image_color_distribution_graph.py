"""Generated component: ImageColorDistributionGraph."""

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


class ImageColorDistributionGraph(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ImageColorDistributionGraph.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ImageColorDistributionGraph"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, texture: str | IAssetProvider[Texture2D] | None = None, max_texture_size: np.int32 | None = None, base_size: np.float32 | None = None, accumulate_size: np.float32 | None = None, max_size: np.float32 | None = None, scale: primitives.Float3 | None = None, alpha_threshold: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            texture: Initial value for Texture.
            max_texture_size: Initial value for MaxTextureSize.
            base_size: Initial value for BaseSize.
            accumulate_size: Initial value for AccumulateSize.
            max_size: Initial value for MaxSize.
            scale: Initial value for Scale.
            alpha_threshold: Initial value for AlphaThreshold.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if texture is not None:
            self.texture = texture
        if max_texture_size is not None:
            self.max_texture_size = max_texture_size
        if base_size is not None:
            self.base_size = base_size
        if accumulate_size is not None:
            self.accumulate_size = accumulate_size
        if max_size is not None:
            self.max_size = max_size
        if scale is not None:
            self.scale = scale
        if alpha_threshold is not None:
            self.alpha_threshold = alpha_threshold

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
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def color_space(self) -> members.FieldEnum | None:
        """The ColorSpace member."""
        member = self.get_member("ColorSpace")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @color_space.setter
    def color_space(self, value: members.FieldEnum) -> None:
        """Set the ColorSpace member."""
        self.set_member("ColorSpace", value)

    @property
    def max_texture_size(self) -> np.int32 | None:
        """The MaxTextureSize field value."""
        member = self.get_member("MaxTextureSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_texture_size.setter
    def max_texture_size(self, value: np.int32) -> None:
        """Set the MaxTextureSize field value."""
        member = self.get_member("MaxTextureSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTextureSize", fields.FieldInt(value=value)
            )

    @property
    def base_size(self) -> np.float32 | None:
        """The BaseSize field value."""
        member = self.get_member("BaseSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_size.setter
    def base_size(self, value: np.float32) -> None:
        """Set the BaseSize field value."""
        member = self.get_member("BaseSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseSize", fields.FieldFloat(value=value)
            )

    @property
    def accumulate_size(self) -> np.float32 | None:
        """The AccumulateSize field value."""
        member = self.get_member("AccumulateSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulate_size.setter
    def accumulate_size(self, value: np.float32) -> None:
        """Set the AccumulateSize field value."""
        member = self.get_member("AccumulateSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulateSize", fields.FieldFloat(value=value)
            )

    @property
    def max_size(self) -> np.float32 | None:
        """The MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: np.float32) -> None:
        """Set the MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSize", fields.FieldFloat(value=value)
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

    @property
    def alpha_threshold(self) -> np.float32 | None:
        """The AlphaThreshold field value."""
        member = self.get_member("AlphaThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_threshold.setter
    def alpha_threshold(self, value: np.float32) -> None:
        """Set the AlphaThreshold field value."""
        member = self.get_member("AlphaThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaThreshold", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

