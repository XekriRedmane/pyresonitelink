"""Generated component: WorldLoadingProgressInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.progress_stage import ProgressStage
from pyresonitelink.generated._types.progress_bar_interface import ProgressBarInterface
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldLoadingProgressInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """The WorldLoadingProgressInterface component is the key component in the creation of a user-definable world loading progress bar. See Favorites for favoritable items like this one.

    Category: Utility/Entity Interfaces

    Use either the existing Resonite world loading bar under Resonite
    Essentials or make a UI by attaching the component and making one from
    scratch. Then save the item with this component to the inventory and
    favorite it so it becomes the default world load indicator upon
    restarting.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldLoadingProgressInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, progress: str | IField[primitives.Float] | None = None, world_name: str | IField[primitives.String] | None = None, stage: str | IField[ProgressStage] | None = None, phase_name: str | IField[primitives.String] | None = None, sub_phase_name: str | IField[primitives.String] | None = None, has_completed: str | IField[primitives.Bool] | None = None, has_failed: str | IField[primitives.Bool] | None = None, completion_message: str | IField[primitives.String] | None = None, failure_reason: str | IField[primitives.String] | None = None, loading_assets: str | IField[primitives.Bool] | None = None, loaded_assets: str | IField[primitives.Int] | None = None, total_assets: str | IField[primitives.Int] | None = None, loaded_textures_2d: str | IField[primitives.Int] | None = None, total_textures_2d: str | IField[primitives.Int] | None = None, loaded_textures_3d: str | IField[primitives.Int] | None = None, total_textures_3d: str | IField[primitives.Int] | None = None, loaded_cubemaps: str | IField[primitives.Int] | None = None, total_cubemaps: str | IField[primitives.Int] | None = None, loaded_videos: str | IField[primitives.Int] | None = None, total_videos: str | IField[primitives.Int] | None = None, loaded_meshes: str | IField[primitives.Int] | None = None, total_meshes: str | IField[primitives.Int] | None = None, loaded_audio_clips: str | IField[primitives.Int] | None = None, total_audio_clips: str | IField[primitives.Int] | None = None, loaded_shaders: str | IField[primitives.Int] | None = None, total_shaders: str | IField[primitives.Int] | None = None, loaded_fonts: str | IField[primitives.Int] | None = None, total_fonts: str | IField[primitives.Int] | None = None, bytes_downloaded: str | IField[primitives.Long] | None = None, total_bytes: str | IField[primitives.Long] | None = None, bytes_per_second: str | IField[primitives.Long] | None = None, progress_bar: str | ProgressBarInterface | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            progress: Initial value for Progress.
            world_name: Initial value for WorldName.
            stage: Initial value for Stage.
            phase_name: Initial value for PhaseName.
            sub_phase_name: Initial value for SubPhaseName.
            has_completed: Initial value for HasCompleted.
            has_failed: Initial value for HasFailed.
            completion_message: Initial value for CompletionMessage.
            failure_reason: Initial value for FailureReason.
            loading_assets: Initial value for LoadingAssets.
            loaded_assets: Initial value for LoadedAssets.
            total_assets: Initial value for TotalAssets.
            loaded_textures_2d: Initial value for LoadedTextures2D.
            total_textures_2d: Initial value for TotalTextures2D.
            loaded_textures_3d: Initial value for LoadedTextures3D.
            total_textures_3d: Initial value for TotalTextures3D.
            loaded_cubemaps: Initial value for LoadedCubemaps.
            total_cubemaps: Initial value for TotalCubemaps.
            loaded_videos: Initial value for LoadedVideos.
            total_videos: Initial value for TotalVideos.
            loaded_meshes: Initial value for LoadedMeshes.
            total_meshes: Initial value for TotalMeshes.
            loaded_audio_clips: Initial value for LoadedAudioClips.
            total_audio_clips: Initial value for TotalAudioClips.
            loaded_shaders: Initial value for LoadedShaders.
            total_shaders: Initial value for TotalShaders.
            loaded_fonts: Initial value for LoadedFonts.
            total_fonts: Initial value for TotalFonts.
            bytes_downloaded: Initial value for BytesDownloaded.
            total_bytes: Initial value for TotalBytes.
            bytes_per_second: Initial value for BytesPerSecond.
            progress_bar: Initial value for ProgressBar.
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
        if progress is not None:
            self.progress = progress
        if world_name is not None:
            self.world_name = world_name
        if stage is not None:
            self.stage = stage
        if phase_name is not None:
            self.phase_name = phase_name
        if sub_phase_name is not None:
            self.sub_phase_name = sub_phase_name
        if has_completed is not None:
            self.has_completed = has_completed
        if has_failed is not None:
            self.has_failed = has_failed
        if completion_message is not None:
            self.completion_message = completion_message
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if loading_assets is not None:
            self.loading_assets = loading_assets
        if loaded_assets is not None:
            self.loaded_assets = loaded_assets
        if total_assets is not None:
            self.total_assets = total_assets
        if loaded_textures_2d is not None:
            self.loaded_textures_2d = loaded_textures_2d
        if total_textures_2d is not None:
            self.total_textures_2d = total_textures_2d
        if loaded_textures_3d is not None:
            self.loaded_textures_3d = loaded_textures_3d
        if total_textures_3d is not None:
            self.total_textures_3d = total_textures_3d
        if loaded_cubemaps is not None:
            self.loaded_cubemaps = loaded_cubemaps
        if total_cubemaps is not None:
            self.total_cubemaps = total_cubemaps
        if loaded_videos is not None:
            self.loaded_videos = loaded_videos
        if total_videos is not None:
            self.total_videos = total_videos
        if loaded_meshes is not None:
            self.loaded_meshes = loaded_meshes
        if total_meshes is not None:
            self.total_meshes = total_meshes
        if loaded_audio_clips is not None:
            self.loaded_audio_clips = loaded_audio_clips
        if total_audio_clips is not None:
            self.total_audio_clips = total_audio_clips
        if loaded_shaders is not None:
            self.loaded_shaders = loaded_shaders
        if total_shaders is not None:
            self.total_shaders = total_shaders
        if loaded_fonts is not None:
            self.loaded_fonts = loaded_fonts
        if total_fonts is not None:
            self.total_fonts = total_fonts
        if bytes_downloaded is not None:
            self.bytes_downloaded = bytes_downloaded
        if total_bytes is not None:
            self.total_bytes = total_bytes
        if bytes_per_second is not None:
            self.bytes_per_second = bytes_per_second
        if progress_bar is not None:
            self.progress_bar = progress_bar

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
    def progress(self) -> str | None:
        """Float field where 0.0 - 1.0 progress will be written."""
        member = self.get_member("Progress")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress.setter
    def progress(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Progress reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Progress")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Progress",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def world_name(self) -> str | None:
        """String field where the loading world's name will be written."""
        member = self.get_member("WorldName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_name.setter
    def world_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the WorldName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("WorldName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def stage(self) -> str | None:
        """The field to write with the current progress stage of the currently loading world. This is written by the world loading main process."""
        member = self.get_member("Stage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stage.setter
    def stage(self, target: str | IField[ProgressStage] | None) -> None:
        """Set the Stage reference by target ID or IField[ProgressStage] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Stage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ProgressStage>'),
            )

    @property
    def phase_name(self) -> str | None:
        """String field where the current loading phase name will be written."""
        member = self.get_member("PhaseName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @phase_name.setter
    def phase_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the PhaseName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PhaseName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PhaseName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def sub_phase_name(self) -> str | None:
        """String field where the current loading sub-phase name will be written."""
        member = self.get_member("SubPhaseName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sub_phase_name.setter
    def sub_phase_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the SubPhaseName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SubPhaseName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SubPhaseName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def has_completed(self) -> str | None:
        """Boolean field that will be set to true on loading completion."""
        member = self.get_member("HasCompleted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_completed.setter
    def has_completed(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasCompleted reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasCompleted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasCompleted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def has_failed(self) -> str | None:
        """Boolean field that will be set to true on loading failure."""
        member = self.get_member("HasFailed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_failed.setter
    def has_failed(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasFailed reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasFailed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasFailed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def completion_message(self) -> str | None:
        """String field where message indicating completion will be written."""
        member = self.get_member("CompletionMessage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @completion_message.setter
    def completion_message(self, target: str | IField[primitives.String] | None) -> None:
        """Set the CompletionMessage reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CompletionMessage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CompletionMessage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def failure_reason(self) -> str | None:
        """String field where message indicating reason for loading failure will be written."""
        member = self.get_member("FailureReason")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @failure_reason.setter
    def failure_reason(self, target: str | IField[primitives.String] | None) -> None:
        """Set the FailureReason reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FailureReason")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FailureReason",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def loading_assets(self) -> str | None:
        """Boolean field that is set true while loading assets."""
        member = self.get_member("LoadingAssets")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loading_assets.setter
    def loading_assets(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the LoadingAssets reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadingAssets")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadingAssets",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def loaded_assets(self) -> str | None:
        """Integer field counting loaded assets."""
        member = self.get_member("LoadedAssets")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_assets.setter
    def loaded_assets(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedAssets reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedAssets")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedAssets",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_assets(self) -> str | None:
        """Integer field counting total assets to be loaded."""
        member = self.get_member("TotalAssets")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_assets.setter
    def total_assets(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalAssets reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalAssets")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalAssets",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_textures_2d(self) -> str | None:
        """Integer field counting loaded ITexture2D assets."""
        member = self.get_member("LoadedTextures2D")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_textures_2d.setter
    def loaded_textures_2d(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedTextures2D reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedTextures2D")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedTextures2D",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_textures_2d(self) -> str | None:
        """Integer field counting total ITexture2D assets to be loaded."""
        member = self.get_member("TotalTextures2D")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_textures_2d.setter
    def total_textures_2d(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalTextures2D reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalTextures2D")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalTextures2D",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_textures_3d(self) -> str | None:
        """Integer field counting loaded ITexture3D assets."""
        member = self.get_member("LoadedTextures3D")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_textures_3d.setter
    def loaded_textures_3d(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedTextures3D reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedTextures3D")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedTextures3D",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_textures_3d(self) -> str | None:
        """Integer field counting total ITexture3D assets to be loaded."""
        member = self.get_member("TotalTextures3D")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_textures_3d.setter
    def total_textures_3d(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalTextures3D reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalTextures3D")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalTextures3D",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_cubemaps(self) -> str | None:
        """Integer field counting loaded Cubemap assets."""
        member = self.get_member("LoadedCubemaps")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_cubemaps.setter
    def loaded_cubemaps(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedCubemaps reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedCubemaps")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedCubemaps",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_cubemaps(self) -> str | None:
        """Integer field counting total Cubemap assets to be loaded."""
        member = self.get_member("TotalCubemaps")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_cubemaps.setter
    def total_cubemaps(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalCubemaps reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalCubemaps")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalCubemaps",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_videos(self) -> str | None:
        """Integer field counting loaded Video assets."""
        member = self.get_member("LoadedVideos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_videos.setter
    def loaded_videos(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedVideos reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedVideos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedVideos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_videos(self) -> str | None:
        """Integer field counting total Video assets to be loaded."""
        member = self.get_member("TotalVideos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_videos.setter
    def total_videos(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalVideos reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalVideos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalVideos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_meshes(self) -> str | None:
        """Integer field counting loaded Mesh assets."""
        member = self.get_member("LoadedMeshes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_meshes.setter
    def loaded_meshes(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedMeshes reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedMeshes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedMeshes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_meshes(self) -> str | None:
        """Integer field counting total Mesh assets to be loaded."""
        member = self.get_member("TotalMeshes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_meshes.setter
    def total_meshes(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalMeshes reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalMeshes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalMeshes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_audio_clips(self) -> str | None:
        """Integer field counting loaded Audio assets."""
        member = self.get_member("LoadedAudioClips")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_audio_clips.setter
    def loaded_audio_clips(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedAudioClips reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedAudioClips")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedAudioClips",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_audio_clips(self) -> str | None:
        """Integer field counting total Audio assets to be loaded."""
        member = self.get_member("TotalAudioClips")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_audio_clips.setter
    def total_audio_clips(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalAudioClips reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalAudioClips")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalAudioClips",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_shaders(self) -> str | None:
        """Integer field counting loaded Shader assets."""
        member = self.get_member("LoadedShaders")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_shaders.setter
    def loaded_shaders(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedShaders reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedShaders")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedShaders",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_shaders(self) -> str | None:
        """Integer field counting total Shader assets to be loaded."""
        member = self.get_member("TotalShaders")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_shaders.setter
    def total_shaders(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalShaders reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalShaders")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalShaders",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def loaded_fonts(self) -> str | None:
        """Integer field counting loaded Font assets."""
        member = self.get_member("LoadedFonts")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loaded_fonts.setter
    def loaded_fonts(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the LoadedFonts reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LoadedFonts")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadedFonts",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_fonts(self) -> str | None:
        """Integer field counting total Font assets to be loaded."""
        member = self.get_member("TotalFonts")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_fonts.setter
    def total_fonts(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalFonts reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalFonts")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalFonts",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def bytes_downloaded(self) -> str | None:
        """Long field counting total bytes downloaded so far."""
        member = self.get_member("BytesDownloaded")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bytes_downloaded.setter
    def bytes_downloaded(self, target: str | IField[primitives.Long] | None) -> None:
        """Set the BytesDownloaded reference by target ID or IField[primitives.Long] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BytesDownloaded")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BytesDownloaded",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<long>'),
            )

    @property
    def total_bytes(self) -> str | None:
        """Long field count of total bytes expected to be downloaded."""
        member = self.get_member("TotalBytes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_bytes.setter
    def total_bytes(self, target: str | IField[primitives.Long] | None) -> None:
        """Set the TotalBytes reference by target ID or IField[primitives.Long] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalBytes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalBytes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<long>'),
            )

    @property
    def bytes_per_second(self) -> str | None:
        """Long field indicating current Bytes-per-Second download rate."""
        member = self.get_member("BytesPerSecond")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bytes_per_second.setter
    def bytes_per_second(self, target: str | IField[primitives.Long] | None) -> None:
        """Set the BytesPerSecond reference by target ID or IField[primitives.Long] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BytesPerSecond")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BytesPerSecond",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<long>'),
            )

    @property
    def progress_bar(self) -> str | None:
        """Reference to a Component:ProgressBarInterface component to use as the progress Bae visual."""
        member = self.get_member("ProgressBar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress_bar.setter
    def progress_bar(self, target: str | ProgressBarInterface | None) -> None:
        """Set the ProgressBar reference by target ID or ProgressBarInterface instance."""
        target_id: str | None = target.id if isinstance(target, ProgressBarInterface) else target  # type: ignore[assignment]
        member = self.get_member("ProgressBar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProgressBar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProgressBarInterface'),
            )

