"""Generated component: LegacyVideoPlayer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.stereo_layout import StereoLayout
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.video_texture import VideoTexture
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.unlit_material import UnlitMaterial
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.legacy_slider import LegacySlider
from pyresonitelink.generated._types.video_exportable import VideoExportable
from pyresonitelink.generated._types.asset_proxy import AssetProxy
from pyresonitelink.generated._types.reference_proxy import ReferenceProxy
from pyresonitelink.generated._types.imaterial_source import IMaterialSource
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iui_interface import IUIInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyVideoPlayer(GeneratedComponent, IMaterialSource, IMaterialApplyPolicy, IPlayable, IItemMetadataSource, IUIInterface, IWorldEventReceiver):
    """The Legacy Video Player component is used to construct and control legacy video players.

    Used in legacy content. do not use in new content.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyVideoPlayer"

    def __init__(self, stereo_layout: StereoLayout | str | None = None, size_compensation: primitives.Float2 | None = None, video_provider: str | IAssetProvider[VideoTexture] | None = None, style: str | LegacyUIStyle | None = None, indicator_texture_url: str | IField[str] | None = None, indicator_tint: str | IField[primitives.ColorX] | None = None, collider_size: str | IField[primitives.Float3] | None = None, frame_width: str | IField[primitives.Float] | None = None, frame_height: str | IField[primitives.Float] | None = None, frame_material: str | PBS_RimMetallic | None = None, display_material: str | UnlitMaterial | None = None, display_material_texture: str | AssetRef[ITexture2D] | None = None, display_size: str | IField[primitives.Float2] | None = None, main_audio_output: str | AudioOutput | None = None, timeline_slider: str | LegacySlider | None = None, timeline_position: str | IField[primitives.Float3] | None = None, timeline_width: str | IField[primitives.Float] | None = None, position_drive: str | IField[primitives.Float] | None = None, volume_slider: str | LegacySlider | None = None, volume_position: str | IField[primitives.Float3] | None = None, volume_width: str | IField[primitives.Float] | None = None, volume_drive: str | IField[primitives.Float] | None = None, buttons_width: str | IField[primitives.Float] | None = None, buttons_height: str | IField[primitives.Float] | None = None, buttons_position: str | IField[primitives.Float3] | None = None, play_button_color: str | IField[primitives.ColorX] | None = None, pause_button_color: str | IField[primitives.ColorX] | None = None, stop_button_color: str | IField[primitives.ColorX] | None = None, loop_button_color: str | IField[primitives.ColorX] | None = None, audio_3d_button_color: str | IField[primitives.ColorX] | None = None, exportable: str | VideoExportable | None = None, asset_proxy: str | AssetProxy[VideoTexture] | None = None, reference_proxy: str | ReferenceProxy | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stereo_layout: Initial value for StereoLayout.
            size_compensation: Initial value for SizeCompensation.
            video_provider: Initial value for videoProvider.
            style: Initial value for _style.
            indicator_texture_url: Initial value for _indicatorTextureUrl.
            indicator_tint: Initial value for _indicatorTint.
            collider_size: Initial value for _colliderSize.
            frame_width: Initial value for _frameWidth.
            frame_height: Initial value for _frameHeight.
            frame_material: Initial value for _frameMaterial.
            display_material: Initial value for _displayMaterial.
            display_material_texture: Initial value for _displayMaterialTexture.
            display_size: Initial value for _displaySize.
            main_audio_output: Initial value for _mainAudioOutput.
            timeline_slider: Initial value for _timelineSlider.
            timeline_position: Initial value for _timelinePosition.
            timeline_width: Initial value for _timelineWidth.
            position_drive: Initial value for _positionDrive.
            volume_slider: Initial value for _volumeSlider.
            volume_position: Initial value for _volumePosition.
            volume_width: Initial value for _volumeWidth.
            volume_drive: Initial value for _volumeDrive.
            buttons_width: Initial value for _buttonsWidth.
            buttons_height: Initial value for _buttonsHeight.
            buttons_position: Initial value for _buttonsPosition.
            play_button_color: Initial value for _playButtonColor.
            pause_button_color: Initial value for _pauseButtonColor.
            stop_button_color: Initial value for _stopButtonColor.
            loop_button_color: Initial value for _loopButtonColor.
            audio_3d_button_color: Initial value for _audio3DButtonColor.
            exportable: Initial value for _exportable.
            asset_proxy: Initial value for _assetProxy.
            reference_proxy: Initial value for _referenceProxy.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stereo_layout is not None:
            self.stereo_layout = stereo_layout
        if size_compensation is not None:
            self.size_compensation = size_compensation
        if video_provider is not None:
            self.video_provider = video_provider
        if style is not None:
            self.style = style
        if indicator_texture_url is not None:
            self.indicator_texture_url = indicator_texture_url
        if indicator_tint is not None:
            self.indicator_tint = indicator_tint
        if collider_size is not None:
            self.collider_size = collider_size
        if frame_width is not None:
            self.frame_width = frame_width
        if frame_height is not None:
            self.frame_height = frame_height
        if frame_material is not None:
            self.frame_material = frame_material
        if display_material is not None:
            self.display_material = display_material
        if display_material_texture is not None:
            self.display_material_texture = display_material_texture
        if display_size is not None:
            self.display_size = display_size
        if main_audio_output is not None:
            self.main_audio_output = main_audio_output
        if timeline_slider is not None:
            self.timeline_slider = timeline_slider
        if timeline_position is not None:
            self.timeline_position = timeline_position
        if timeline_width is not None:
            self.timeline_width = timeline_width
        if position_drive is not None:
            self.position_drive = position_drive
        if volume_slider is not None:
            self.volume_slider = volume_slider
        if volume_position is not None:
            self.volume_position = volume_position
        if volume_width is not None:
            self.volume_width = volume_width
        if volume_drive is not None:
            self.volume_drive = volume_drive
        if buttons_width is not None:
            self.buttons_width = buttons_width
        if buttons_height is not None:
            self.buttons_height = buttons_height
        if buttons_position is not None:
            self.buttons_position = buttons_position
        if play_button_color is not None:
            self.play_button_color = play_button_color
        if pause_button_color is not None:
            self.pause_button_color = pause_button_color
        if stop_button_color is not None:
            self.stop_button_color = stop_button_color
        if loop_button_color is not None:
            self.loop_button_color = loop_button_color
        if audio_3d_button_color is not None:
            self.audio_3d_button_color = audio_3d_button_color
        if exportable is not None:
            self.exportable = exportable
        if asset_proxy is not None:
            self.asset_proxy = asset_proxy
        if reference_proxy is not None:
            self.reference_proxy = reference_proxy

    @property
    def stereo_layout(self) -> StereoLayout | None:
        """The layout of the stereo audio for the video player."""
        member = self.get_member("StereoLayout")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StereoLayout(member.value)
        return None

    @stereo_layout.setter
    def stereo_layout(self, value: StereoLayout | str) -> None:
        """Set StereoLayout. The layout of the stereo audio for the video player."""
        member = self.get_member("StereoLayout")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "StereoLayout",
                members.FieldEnum(value=str(value)),
            )

    @property
    def size_compensation(self) -> primitives.Float2 | None:
        """How to compensate for video size."""
        member = self.get_member("SizeCompensation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size_compensation.setter
    def size_compensation(self, value: primitives.Float2) -> None:
        """Set the SizeCompensation field value."""
        member = self.get_member("SizeCompensation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SizeCompensation", fields.FieldFloat2(value=value)
            )

    @property
    def video_provider(self) -> str | None:
        """The video provider component giving the audio and visual data for the video."""
        member = self.get_member("videoProvider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @video_provider.setter
    def video_provider(self, target: str | IAssetProvider[VideoTexture] | None) -> None:
        """Set the videoProvider reference by target ID or IAssetProvider[VideoTexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("videoProvider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "videoProvider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.VideoTexture>'),
            )

    @property
    def style(self) -> str | None:
        """The legacy ui style component being used for this video player."""
        member = self.get_member("_style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the _style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("_style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def indicator_texture_url(self) -> str | None:
        """The field to drive to control the video player's texture url"""
        member = self.get_member("_indicatorTextureUrl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @indicator_texture_url.setter
    def indicator_texture_url(self, target: str | IField[str] | None) -> None:
        """Set the _indicatorTextureUrl reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_indicatorTextureUrl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_indicatorTextureUrl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def indicator_tint(self) -> str | None:
        """The field to drive to control the video player's indictor's tint"""
        member = self.get_member("_indicatorTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @indicator_tint.setter
    def indicator_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _indicatorTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_indicatorTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_indicatorTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def collider_size(self) -> str | None:
        """The field to drive to control the video player's collider size"""
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def frame_width(self) -> str | None:
        """The field to drive to control the video player's border frame width"""
        member = self.get_member("_frameWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frame_width.setter
    def frame_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _frameWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frameWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frameWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def frame_height(self) -> str | None:
        """The field to drive to control the video player's border frame height"""
        member = self.get_member("_frameHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frame_height.setter
    def frame_height(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _frameHeight reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frameHeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frameHeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def frame_material(self) -> str | None:
        """The field to drive to control the video player's frame material"""
        member = self.get_member("_frameMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frame_material.setter
    def frame_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _frameMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_frameMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frameMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def display_material(self) -> str | None:
        """This stores the video player's display material."""
        member = self.get_member("_displayMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_material.setter
    def display_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _displayMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_displayMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_displayMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def display_material_texture(self) -> str | None:
        """The field to drive to control the video player's display material texture."""
        member = self.get_member("_displayMaterialTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_material_texture.setter
    def display_material_texture(self, target: str | AssetRef[ITexture2D] | None) -> None:
        """Set the _displayMaterialTexture reference by target ID or AssetRef[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("_displayMaterialTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_displayMaterialTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def display_size(self) -> str | None:
        """The field to drive to control the video player's display section size."""
        member = self.get_member("_displaySize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_size.setter
    def display_size(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _displaySize reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_displaySize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_displaySize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def main_audio_output(self) -> str | None:
        """This stores the video player's main audio output."""
        member = self.get_member("_mainAudioOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @main_audio_output.setter
    def main_audio_output(self, target: str | AudioOutput | None) -> None:
        """Set the _mainAudioOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("_mainAudioOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mainAudioOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def timeline_slider(self) -> str | None:
        """This stores the video player's timeline slider."""
        member = self.get_member("_timelineSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timeline_slider.setter
    def timeline_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _timelineSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_timelineSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timelineSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def timeline_position(self) -> str | None:
        """The field to drive to control the video player's timeline playhead position."""
        member = self.get_member("_timelinePosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timeline_position.setter
    def timeline_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _timelinePosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_timelinePosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timelinePosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def timeline_width(self) -> str | None:
        """The field to drive to control the video player's timeline ui width."""
        member = self.get_member("_timelineWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timeline_width.setter
    def timeline_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _timelineWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_timelineWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timelineWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def position_drive(self) -> str | None:
        """The field to drive to control the video player's ui position."""
        member = self.get_member("_positionDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_drive.setter
    def position_drive(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _positionDrive reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_positionDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positionDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def volume_slider(self) -> str | None:
        """This stores the video player's volume slider."""
        member = self.get_member("_volumeSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_slider.setter
    def volume_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _volumeSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_volumeSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumeSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def volume_position(self) -> str | None:
        """The field to drive to control the video player's volume amount."""
        member = self.get_member("_volumePosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_position.setter
    def volume_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _volumePosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_volumePosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumePosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def volume_width(self) -> str | None:
        """The field to drive to control the video player's volume ui width."""
        member = self.get_member("_volumeWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_width.setter
    def volume_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _volumeWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_volumeWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumeWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def volume_drive(self) -> str | None:
        """The field to drive to control the video player's volume for the audio output component."""
        member = self.get_member("_volumeDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_drive.setter
    def volume_drive(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _volumeDrive reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_volumeDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumeDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def buttons_width(self) -> str | None:
        """The field to drive to control the video player's button container widths."""
        member = self.get_member("_buttonsWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_width.setter
    def buttons_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _buttonsWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def buttons_height(self) -> str | None:
        """The field to drive to control the video player's button container height."""
        member = self.get_member("_buttonsHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_height.setter
    def buttons_height(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _buttonsHeight reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsHeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsHeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def buttons_position(self) -> str | None:
        """The field to drive to control the video player's button container position."""
        member = self.get_member("_buttonsPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_position.setter
    def buttons_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _buttonsPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def play_button_color(self) -> str | None:
        """The field to drive to control the video player's play button color."""
        member = self.get_member("_playButtonColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @play_button_color.setter
    def play_button_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _playButtonColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_playButtonColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_playButtonColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def pause_button_color(self) -> str | None:
        """The field to drive to control the video player's pause button color."""
        member = self.get_member("_pauseButtonColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pause_button_color.setter
    def pause_button_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _pauseButtonColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pauseButtonColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pauseButtonColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def stop_button_color(self) -> str | None:
        """The field to drive to control the video player's stop button color."""
        member = self.get_member("_stopButtonColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stop_button_color.setter
    def stop_button_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _stopButtonColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_stopButtonColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_stopButtonColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def loop_button_color(self) -> str | None:
        """The field to drive to control the video player's loop button color."""
        member = self.get_member("_loopButtonColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_button_color.setter
    def loop_button_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _loopButtonColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_loopButtonColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loopButtonColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def audio_3d_button_color(self) -> str | None:
        """The field to drive to control the video player's 3d audio button."""
        member = self.get_member("_audio3DButtonColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_3d_button_color.setter
    def audio_3d_button_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _audio3DButtonColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_audio3DButtonColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_audio3DButtonColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def exportable(self) -> str | None:
        """The component that is used to make this video player exportable."""
        member = self.get_member("_exportable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exportable.setter
    def exportable(self, target: str | VideoExportable | None) -> None:
        """Set the _exportable reference by target ID or VideoExportable instance."""
        target_id: str | None = target.id if isinstance(target, VideoExportable) else target  # type: ignore[assignment]
        member = self.get_member("_exportable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_exportable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VideoExportable'),
            )

    @property
    def asset_proxy(self) -> str | None:
        """The component that is used to allow this video to be dropped into asset fields for videos."""
        member = self.get_member("_assetProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset_proxy.setter
    def asset_proxy(self, target: str | AssetProxy[VideoTexture] | None) -> None:
        """Set the _assetProxy reference by target ID or AssetProxy[VideoTexture] instance."""
        target_id: str | None = target.id if isinstance(target, AssetProxy) else target  # type: ignore[assignment]
        member = self.get_member("_assetProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_assetProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetProxy<[FrooxEngine]FrooxEngine.VideoTexture>'),
            )

    @property
    def reference_proxy(self) -> str | None:
        """The component that allows this video to be dropped into texture and audio fields or receivers."""
        member = self.get_member("_referenceProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_proxy.setter
    def reference_proxy(self, target: str | ReferenceProxy | None) -> None:
        """Set the _referenceProxy reference by target ID or ReferenceProxy instance."""
        target_id: str | None = target.id if isinstance(target, ReferenceProxy) else target  # type: ignore[assignment]
        member = self.get_member("_referenceProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_referenceProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ReferenceProxy'),
            )

