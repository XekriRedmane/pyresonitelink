"""Generated component: VideoPlayerInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.video_texture import VideoTexture
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.stereo_layout import StereoLayout
from pyresonitelink.generated._types.panoramic_projection import PanoramicProjection
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoPlayerInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """The VideoPlayerInterface component is a favoritable item that is used to specify the UI elements of a custom Video Player.

    Category: Utility/Entity Interfaces

    Use either the existing Resonite video player under Resonite Essentials
    or make a UI by attaching the component and making one from scratch.
    Then save the item with this component to the inventory and favorite it
    so it becomes the default player upon restarting.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoPlayerInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, url: str | IField[str] | None = None, stream: str | IField[primitives.Bool] | None = None, video_clip: str | AssetRef[VideoTexture] | None = None, video_clip_texture: str | AssetRef[ITexture2D] | None = None, aspect_ratio: str | IField[primitives.Float] | None = None, default_video_clip: str | IAssetProvider[VideoTexture] | None = None, stereo_rendering_enabled: str | IField[primitives.Bool] | None = None, stereo_layout: str | IField[StereoLayout] | None = None, stereo_transform_left: str | IField[primitives.Float4] | None = None, stereo_transform_right: str | IField[primitives.Float4] | None = None, stereo_transform_scale_left: str | IField[primitives.Float2] | None = None, stereo_transform_offset_left: str | IField[primitives.Float2] | None = None, stereo_transform_scale_right: str | IField[primitives.Float2] | None = None, stereo_transform_offset_right: str | IField[primitives.Float2] | None = None, panoramic_rendering_enabled: str | IField[primitives.Bool] | None = None, panoramic_horizontal_fov: str | IField[primitives.Float] | None = None, panoramic_vertical_fov: str | IField[primitives.Float] | None = None, panoramic_projection: str | IField[PanoramicProjection] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            url: Initial value for URL.
            stream: Initial value for Stream.
            video_clip: Initial value for VideoClip.
            video_clip_texture: Initial value for VideoClipTexture.
            aspect_ratio: Initial value for AspectRatio.
            default_video_clip: Initial value for DefaultVideoClip.
            stereo_rendering_enabled: Initial value for StereoRenderingEnabled.
            stereo_layout: Initial value for StereoLayout.
            stereo_transform_left: Initial value for StereoTransformLeft.
            stereo_transform_right: Initial value for StereoTransformRight.
            stereo_transform_scale_left: Initial value for StereoTransformScaleLeft.
            stereo_transform_offset_left: Initial value for StereoTransformOffsetLeft.
            stereo_transform_scale_right: Initial value for StereoTransformScaleRight.
            stereo_transform_offset_right: Initial value for StereoTransformOffsetRight.
            panoramic_rendering_enabled: Initial value for PanoramicRenderingEnabled.
            panoramic_horizontal_fov: Initial value for PanoramicHorizontalFOV.
            panoramic_vertical_fov: Initial value for PanoramicVerticalFOV.
            panoramic_projection: Initial value for PanoramicProjection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if item_name is not None:
            self.item_name = item_name
        if spawning_user is not None:
            self.spawning_user = spawning_user
        if spawning_user_id is not None:
            self.spawning_user_id = spawning_user_id
        if is_instance is not None:
            self.is_instance = is_instance
        if url is not None:
            self.url = url
        if stream is not None:
            self.stream = stream
        if video_clip is not None:
            self.video_clip = video_clip
        if video_clip_texture is not None:
            self.video_clip_texture = video_clip_texture
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if default_video_clip is not None:
            self.default_video_clip = default_video_clip
        if stereo_rendering_enabled is not None:
            self.stereo_rendering_enabled = stereo_rendering_enabled
        if stereo_layout is not None:
            self.stereo_layout = stereo_layout
        if stereo_transform_left is not None:
            self.stereo_transform_left = stereo_transform_left
        if stereo_transform_right is not None:
            self.stereo_transform_right = stereo_transform_right
        if stereo_transform_scale_left is not None:
            self.stereo_transform_scale_left = stereo_transform_scale_left
        if stereo_transform_offset_left is not None:
            self.stereo_transform_offset_left = stereo_transform_offset_left
        if stereo_transform_scale_right is not None:
            self.stereo_transform_scale_right = stereo_transform_scale_right
        if stereo_transform_offset_right is not None:
            self.stereo_transform_offset_right = stereo_transform_offset_right
        if panoramic_rendering_enabled is not None:
            self.panoramic_rendering_enabled = panoramic_rendering_enabled
        if panoramic_horizontal_fov is not None:
            self.panoramic_horizontal_fov = panoramic_horizontal_fov
        if panoramic_vertical_fov is not None:
            self.panoramic_vertical_fov = panoramic_vertical_fov
        if panoramic_projection is not None:
            self.panoramic_projection = panoramic_projection

    @property
    def item_name(self) -> str | None:
        """The name of this favoritable item."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def spawning_user(self) -> str | None:
        """The user that spawned this favoritable item."""
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user.setter
    def spawning_user(self, target: str | UserRef | None) -> None:
        """Set the SpawningUser reference by target ID or UserRef instance."""
        target_id: str | None = target.id if isinstance(target, UserRef) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserRef'),
            )

    @property
    def spawning_user_id(self) -> str | None:
        """The field containing the ID of the user that spawned this favoritable item."""
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user_id.setter
    def spawning_user_id(self, target: str | IField[primitives.String] | None) -> None:
        """Set the SpawningUserID reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUserID",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def is_instance(self) -> primitives.Bool | None:
        """Whether this item is an instance."""
        member = self.get_member("IsInstance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_instance.setter
    def is_instance(self, value: primitives.Bool) -> None:
        """Set the IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsInstance", fields.FieldBool(value=value)
            )

    @property
    def url(self) -> str | None:
        """The field to fill with the URL of the imported video asset."""
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url.setter
    def url(self, target: str | IField[str] | None) -> None:
        """Set the URL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "URL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def stream(self) -> str | None:
        """The field to fill with whether this video player is showing stream."""
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream.setter
    def stream(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Stream reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def video_clip(self) -> str | None:
        """The field to fill with what the video being displayed is."""
        member = self.get_member("VideoClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @video_clip.setter
    def video_clip(self, target: str | AssetRef[VideoTexture] | None) -> None:
        """Set the VideoClip reference by target ID or AssetRef[VideoTexture] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("VideoClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VideoClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.VideoTexture>'),
            )

    @property
    def video_clip_texture(self) -> str | None:
        """The field to fill (Usually a material texture field) with the showing video texture."""
        member = self.get_member("VideoClipTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @video_clip_texture.setter
    def video_clip_texture(self, target: str | AssetRef[ITexture2D] | None) -> None:
        """Set the VideoClipTexture reference by target ID or AssetRef[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("VideoClipTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VideoClipTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def aspect_ratio(self) -> str | None:
        """The field to fill with what the video's aspect ratio is."""
        member = self.get_member("AspectRatio")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @aspect_ratio.setter
    def aspect_ratio(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the AspectRatio reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AspectRatio")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AspectRatio",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def default_video_clip(self) -> str | None:
        """The default video texture to use if one isn't filled in."""
        member = self.get_member("DefaultVideoClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_video_clip.setter
    def default_video_clip(self, target: str | IAssetProvider[VideoTexture] | None) -> None:
        """Set the DefaultVideoClip reference by target ID or IAssetProvider[VideoTexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("DefaultVideoClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultVideoClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.VideoTexture>'),
            )

    @property
    def stereo_rendering_enabled(self) -> str | None:
        """The field to fill with whether the video is a stero video (3D)"""
        member = self.get_member("StereoRenderingEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_rendering_enabled.setter
    def stereo_rendering_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the StereoRenderingEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoRenderingEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoRenderingEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def stereo_layout(self) -> str | None:
        """The field to fill with the kind of stero image layout the image has."""
        member = self.get_member("StereoLayout")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_layout.setter
    def stereo_layout(self, target: str | IField[StereoLayout] | None) -> None:
        """Set the StereoLayout reference by target ID or IField[StereoLayout] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoLayout")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoLayout",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[Elements.Core]Elements.Core.StereoLayout>'),
            )

    @property
    def stereo_transform_left(self) -> str | None:
        """The field to fill with what the rectangle area for the left eye should be."""
        member = self.get_member("StereoTransformLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_transform_left.setter
    def stereo_transform_left(self, target: str | IField[primitives.Float4] | None) -> None:
        """Set the StereoTransformLeft reference by target ID or IField[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoTransformLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoTransformLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float4>'),
            )

    @property
    def stereo_transform_right(self) -> str | None:
        """The field to fill with what the rectangle area for the right eye should be."""
        member = self.get_member("StereoTransformRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_transform_right.setter
    def stereo_transform_right(self, target: str | IField[primitives.Float4] | None) -> None:
        """Set the StereoTransformRight reference by target ID or IField[primitives.Float4] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoTransformRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoTransformRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float4>'),
            )

    @property
    def stereo_transform_scale_left(self) -> str | None:
        """The field to fill with what the UV scale for the left eye should be."""
        member = self.get_member("StereoTransformScaleLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_transform_scale_left.setter
    def stereo_transform_scale_left(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the StereoTransformScaleLeft reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoTransformScaleLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoTransformScaleLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def stereo_transform_offset_left(self) -> str | None:
        """The field to fill with what the UV offset for the left eye should be."""
        member = self.get_member("StereoTransformOffsetLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_transform_offset_left.setter
    def stereo_transform_offset_left(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the StereoTransformOffsetLeft reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoTransformOffsetLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoTransformOffsetLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def stereo_transform_scale_right(self) -> str | None:
        """The field to fill with what the UV scale for the right eye should be."""
        member = self.get_member("StereoTransformScaleRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_transform_scale_right.setter
    def stereo_transform_scale_right(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the StereoTransformScaleRight reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoTransformScaleRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoTransformScaleRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def stereo_transform_offset_right(self) -> str | None:
        """The field to fill with what the UV offset for the right eye should be."""
        member = self.get_member("StereoTransformOffsetRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stereo_transform_offset_right.setter
    def stereo_transform_offset_right(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the StereoTransformOffsetRight reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("StereoTransformOffsetRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StereoTransformOffsetRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def panoramic_rendering_enabled(self) -> str | None:
        """The field to fill with whether the video is a 360 video"""
        member = self.get_member("PanoramicRenderingEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panoramic_rendering_enabled.setter
    def panoramic_rendering_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the PanoramicRenderingEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PanoramicRenderingEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PanoramicRenderingEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def panoramic_horizontal_fov(self) -> str | None:
        """The field to fill with the video's horizontal 360 video FOV."""
        member = self.get_member("PanoramicHorizontalFOV")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panoramic_horizontal_fov.setter
    def panoramic_horizontal_fov(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the PanoramicHorizontalFOV reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PanoramicHorizontalFOV")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PanoramicHorizontalFOV",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def panoramic_vertical_fov(self) -> str | None:
        """The field to fill with the video's vertical 360 video FOV."""
        member = self.get_member("PanoramicVerticalFOV")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panoramic_vertical_fov.setter
    def panoramic_vertical_fov(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the PanoramicVerticalFOV reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PanoramicVerticalFOV")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PanoramicVerticalFOV",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def panoramic_projection(self) -> str | None:
        """The field to fill with what the video's panoramic texture arrangement is."""
        member = self.get_member("PanoramicProjection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panoramic_projection.setter
    def panoramic_projection(self, target: str | IField[PanoramicProjection] | None) -> None:
        """Set the PanoramicProjection reference by target ID or IField[PanoramicProjection] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PanoramicProjection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PanoramicProjection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[Elements.Core]Elements.Core.PanoramicProjection>'),
            )

