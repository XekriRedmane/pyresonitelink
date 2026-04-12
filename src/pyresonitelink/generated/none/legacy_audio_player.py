"""Generated component: LegacyAudioPlayer."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.audio_clip_player import AudioClipPlayer
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.unlit_material import UnlitMaterial
from pyresonitelink.generated._types.ring_mesh import RingMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.item import Item
from pyresonitelink.generated._types.audio_exportable import AudioExportable
from pyresonitelink.generated._types.asset_proxy import AssetProxy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAudioPlayer(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The LegacyAudioPlayer component is a leftover Component from content migrated from other platforms. It should not be used, and should be replaced whenever possible.

For a replacement see Audio Player.

    Not to be used.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyAudioPlayer"

    def __init__(self, audio_clip: str | IAssetProvider[AudioClip] | None = None, clip_player: str | AudioClipPlayer | None = None, audio_output: str | AudioOutput | None = None, waveform_material: str | UnlitMaterial | None = None, playback_material: str | UnlitMaterial | None = None, waveform_ring_mesh: str | RingMesh | None = None, playback_ring_mesh: str | RingMesh | None = None, playback_ring_arc: str | IField[primitives.Float] | None = None, volume_ring_arc: str | IField[primitives.Float] | None = None, playback_time_text: str | IField[primitives.String] | None = None, clip_length_time_text: str | IField[primitives.String] | None = None, icon_texture_url: str | IField[str] | None = None, stop_item: str | Item | None = None, loop_item: str | Item | None = None, spatial_item: str | Item | None = None, loop_icon_url: str | IField[str] | None = None, spatial_icon_url: str | IField[str] | None = None, exportable: str | AudioExportable | None = None, asset_proxy: str | AssetProxy[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_clip: Initial value for AudioClip.
            clip_player: Initial value for _clipPlayer.
            audio_output: Initial value for _audioOutput.
            waveform_material: Initial value for _waveformMaterial.
            playback_material: Initial value for _playbackMaterial.
            waveform_ring_mesh: Initial value for _waveformRingMesh.
            playback_ring_mesh: Initial value for _playbackRingMesh.
            playback_ring_arc: Initial value for _playbackRingArc.
            volume_ring_arc: Initial value for _volumeRingArc.
            playback_time_text: Initial value for _playbackTimeText.
            clip_length_time_text: Initial value for _clipLengthTimeText.
            icon_texture_url: Initial value for _iconTextureURL.
            stop_item: Initial value for _stopItem.
            loop_item: Initial value for _loopItem.
            spatial_item: Initial value for _spatialItem.
            loop_icon_url: Initial value for _loopIconURL.
            spatial_icon_url: Initial value for _spatialIconURL.
            exportable: Initial value for _exportable.
            asset_proxy: Initial value for _assetProxy.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_clip is not None:
            self.audio_clip = audio_clip
        if clip_player is not None:
            self.clip_player = clip_player
        if audio_output is not None:
            self.audio_output = audio_output
        if waveform_material is not None:
            self.waveform_material = waveform_material
        if playback_material is not None:
            self.playback_material = playback_material
        if waveform_ring_mesh is not None:
            self.waveform_ring_mesh = waveform_ring_mesh
        if playback_ring_mesh is not None:
            self.playback_ring_mesh = playback_ring_mesh
        if playback_ring_arc is not None:
            self.playback_ring_arc = playback_ring_arc
        if volume_ring_arc is not None:
            self.volume_ring_arc = volume_ring_arc
        if playback_time_text is not None:
            self.playback_time_text = playback_time_text
        if clip_length_time_text is not None:
            self.clip_length_time_text = clip_length_time_text
        if icon_texture_url is not None:
            self.icon_texture_url = icon_texture_url
        if stop_item is not None:
            self.stop_item = stop_item
        if loop_item is not None:
            self.loop_item = loop_item
        if spatial_item is not None:
            self.spatial_item = spatial_item
        if loop_icon_url is not None:
            self.loop_icon_url = loop_icon_url
        if spatial_icon_url is not None:
            self.spatial_icon_url = spatial_icon_url
        if exportable is not None:
            self.exportable = exportable
        if asset_proxy is not None:
            self.asset_proxy = asset_proxy

    @property
    def audio_clip(self) -> str | None:
        """The audio clip for this audio player."""
        member = self.get_member("AudioClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_clip.setter
    def audio_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the AudioClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AudioClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AudioClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def clip_player(self) -> str | None:
        """The audio clip player that will play the audio clip."""
        member = self.get_member("_clipPlayer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clip_player.setter
    def clip_player(self, target: str | AudioClipPlayer | None) -> None:
        """Set the _clipPlayer reference by target ID or AudioClipPlayer instance."""
        target_id: str | None = target.id if isinstance(target, AudioClipPlayer) else target  # type: ignore[assignment]
        member = self.get_member("_clipPlayer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_clipPlayer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioClipPlayer'),
            )

    @property
    def audio_output(self) -> str | None:
        """The audio output for the audio clip."""
        member = self.get_member("_audioOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_output.setter
    def audio_output(self, target: str | AudioOutput | None) -> None:
        """Set the _audioOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("_audioOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_audioOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def waveform_material(self) -> str | None:
        """The material that is used on the ring visual."""
        member = self.get_member("_waveformMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @waveform_material.setter
    def waveform_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _waveformMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_waveformMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_waveformMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def playback_material(self) -> str | None:
        """The material that is used for the playback visual."""
        member = self.get_member("_playbackMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback_material.setter
    def playback_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _playbackMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_playbackMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_playbackMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def waveform_ring_mesh(self) -> str | None:
        """The mesh used for the waveform ring visual."""
        member = self.get_member("_waveformRingMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @waveform_ring_mesh.setter
    def waveform_ring_mesh(self, target: str | RingMesh | None) -> None:
        """Set the _waveformRingMesh reference by target ID or RingMesh instance."""
        target_id: str | None = target.id if isinstance(target, RingMesh) else target  # type: ignore[assignment]
        member = self.get_member("_waveformRingMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_waveformRingMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RingMesh'),
            )

    @property
    def playback_ring_mesh(self) -> str | None:
        """The mesh used for the playback ring visual."""
        member = self.get_member("_playbackRingMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback_ring_mesh.setter
    def playback_ring_mesh(self, target: str | RingMesh | None) -> None:
        """Set the _playbackRingMesh reference by target ID or RingMesh instance."""
        target_id: str | None = target.id if isinstance(target, RingMesh) else target  # type: ignore[assignment]
        member = self.get_member("_playbackRingMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_playbackRingMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RingMesh'),
            )

    @property
    def playback_ring_arc(self) -> str | None:
        """The field to drive to make the visual for the playback ring."""
        member = self.get_member("_playbackRingArc")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback_ring_arc.setter
    def playback_ring_arc(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _playbackRingArc reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_playbackRingArc")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_playbackRingArc",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def volume_ring_arc(self) -> str | None:
        """The field to drive to make the visual for the audio arc."""
        member = self.get_member("_volumeRingArc")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_ring_arc.setter
    def volume_ring_arc(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _volumeRingArc reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_volumeRingArc")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumeRingArc",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def playback_time_text(self) -> str | None:
        """The field to drive for the playback time text."""
        member = self.get_member("_playbackTimeText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback_time_text.setter
    def playback_time_text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _playbackTimeText reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_playbackTimeText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_playbackTimeText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def clip_length_time_text(self) -> str | None:
        """The field to drive for the audio clip length text."""
        member = self.get_member("_clipLengthTimeText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clip_length_time_text.setter
    def clip_length_time_text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _clipLengthTimeText reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_clipLengthTimeText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_clipLengthTimeText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def icon_texture_url(self) -> str | None:
        """The field to drive with the icon texture URI."""
        member = self.get_member("_iconTextureURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_texture_url.setter
    def icon_texture_url(self, target: str | IField[str] | None) -> None:
        """Set the _iconTextureURL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_iconTextureURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconTextureURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def stop_item(self) -> str | None:
        """The item that can be clicked to stop playback."""
        member = self.get_member("_stopItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stop_item.setter
    def stop_item(self, target: str | Item | None) -> None:
        """Set the _stopItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_stopItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_stopItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def loop_item(self) -> str | None:
        """The item that can be clicked to loop playback."""
        member = self.get_member("_loopItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_item.setter
    def loop_item(self, target: str | Item | None) -> None:
        """Set the _loopItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_loopItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loopItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def spatial_item(self) -> str | None:
        """The item that can be clicked to spatialize or unspatialize the audio."""
        member = self.get_member("_spatialItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatial_item.setter
    def spatial_item(self, target: str | Item | None) -> None:
        """Set the _spatialItem reference by target ID or Item instance."""
        target_id: str | None = target.id if isinstance(target, Item) else target  # type: ignore[assignment]
        member = self.get_member("_spatialItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spatialItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySegmentCircleMenuController+Item'),
            )

    @property
    def loop_icon_url(self) -> str | None:
        """The field to drive with the loop icon texture URI."""
        member = self.get_member("_loopIconURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_icon_url.setter
    def loop_icon_url(self, target: str | IField[str] | None) -> None:
        """Set the _loopIconURL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_loopIconURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loopIconURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def spatial_icon_url(self) -> str | None:
        """The field to drive with the spatialize icon URI."""
        member = self.get_member("_spatialIconURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatial_icon_url.setter
    def spatial_icon_url(self, target: str | IField[str] | None) -> None:
        """Set the _spatialIconURL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_spatialIconURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spatialIconURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def exportable(self) -> str | None:
        """The audio exportable component used to handle the export behavior of this audio player."""
        member = self.get_member("_exportable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exportable.setter
    def exportable(self, target: str | AudioExportable | None) -> None:
        """Set the _exportable reference by target ID or AudioExportable instance."""
        target_id: str | None = target.id if isinstance(target, AudioExportable) else target  # type: ignore[assignment]
        member = self.get_member("_exportable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_exportable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioExportable'),
            )

    @property
    def asset_proxy(self) -> str | None:
        """The asset proxy used to handle dropping this audio player into fields that accept audio clips."""
        member = self.get_member("_assetProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset_proxy.setter
    def asset_proxy(self, target: str | AssetProxy[AudioClip] | None) -> None:
        """Set the _assetProxy reference by target ID or AssetProxy[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, AssetProxy) else target  # type: ignore[assignment]
        member = self.get_member("_assetProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_assetProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetProxy<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

