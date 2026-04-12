"""Generated component: ImageColorDistributionGraph."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.space import Space
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ImageColorDistributionGraph(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The ImageColorDistributionGraph component is used to make mesh data for a set of points with colors and sizes based on a provided image's pixels. The mesh needs to be used with Billboard geometry to be viewed properly.

    Category: Assets/Procedural Meshes

    Attach this component to a slot, and place it into a Mesh Renderer
    Component with an Unlit Material set to use billboard geometry to view
    the mesh and its graph points.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ImageColorDistributionGraph"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, texture: str | IAssetProvider[Texture2D] | None = None, color_space: Space | str | None = None, max_texture_size: primitives.Int | None = None, base_size: primitives.Float | None = None, accumulate_size: primitives.Float | None = None, max_size: primitives.Float | None = None, scale: primitives.Float3 | None = None, alpha_threshold: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            texture: Initial value for Texture.
            color_space: Initial value for ColorSpace.
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
        if profile is not None:
            self.profile = profile
        if texture is not None:
            self.texture = texture
        if color_space is not None:
            self.color_space = color_space
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
    def texture(self) -> str | None:
        """The texture to analyze and use to generate the vertex graph for this mesh."""
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
    def color_space(self) -> Space | None:
        """The color space to use for X, Y, and Z coordinates on the graph for."""
        member = self.get_member("ColorSpace")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Space(member.value)
        return None

    @color_space.setter
    def color_space(self, value: Space | str) -> None:
        """Set ColorSpace. The color space to use for X, Y, and Z coordinates on the graph for."""
        member = self.get_member("ColorSpace")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ColorSpace",
                members.FieldEnum(value=str(value)),
            )

    @property
    def max_texture_size(self) -> primitives.Int | None:
        """The max size of the image on one axis that this image will use when making the graph. The image gets resized internally to fit this size."""
        member = self.get_member("MaxTextureSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_texture_size.setter
    def max_texture_size(self, value: primitives.Int) -> None:
        """Set the MaxTextureSize field value."""
        member = self.get_member("MaxTextureSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTextureSize", fields.FieldInt(value=value)
            )

    @property
    def base_size(self) -> primitives.Float | None:
        """The size of any color point on the graph at minimum."""
        member = self.get_member("BaseSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_size.setter
    def base_size(self, value: primitives.Float) -> None:
        """Set the BaseSize field value."""
        member = self.get_member("BaseSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseSize", fields.FieldFloat(value=value)
            )

    @property
    def accumulate_size(self) -> primitives.Float | None:
        """How much to add to the size of a graph point if a color is repeated with the same RGB values."""
        member = self.get_member("AccumulateSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulate_size.setter
    def accumulate_size(self, value: primitives.Float) -> None:
        """Set the AccumulateSize field value."""
        member = self.get_member("AccumulateSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulateSize", fields.FieldFloat(value=value)
            )

    @property
    def max_size(self) -> primitives.Float | None:
        """The maximum size a color point on the graph can be."""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: primitives.Float) -> None:
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
        """How much to scale the graph up or down."""
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
    def alpha_threshold(self) -> primitives.Float | None:
        """if alpha is below this threshold, then don't add the color to the graph."""
        member = self.get_member("AlphaThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_threshold.setter
    def alpha_threshold(self, value: primitives.Float) -> None:
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

