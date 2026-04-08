"""Generated component: PlayOneShot."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.nullable import Nullable
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.audio_rolloff_curve import AudioRolloffCurve
from pyresonitelink.generated._types.audio_distance_space import AudioDistanceSpace
from pyresonitelink.generated._types.audio_type_group import AudioTypeGroup
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlayOneShot(GeneratedComponent, IMappableNode, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Play One Shot is a ProtoFlux node that creates a new audio source under the provided Root (Slot) (except when ParentUnderRoot (bool) is enabled) with the provided parameters. Play One Shot is under Audio in the Protoflux Node creation menu

    Category: ProtoFlux/Runtimes/Execution/Nodes/Audio
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.PlayOneShot"

    def __init__(self, clip: str | INodeObjectOutput[IAssetProvider[AudioClip]] | None = None, volume: str | INodeValueOutput[primitives.Float] | None = None, speed: str | INodeValueOutput[primitives.Float] | None = None, spatialize: str | INodeValueOutput[primitives.Bool] | None = None, spatial_blend: str | INodeValueOutput[primitives.Float] | None = None, global_: str | INodeObjectOutput[Nullable[primitives.Bool]] | None = None, point: str | INodeValueOutput[primitives.Float3] | None = None, root: str | INodeObjectOutput[Slot] | None = None, parent_under_root: str | INodeValueOutput[primitives.Bool] | None = None, priority: str | INodeValueOutput[primitives.Int] | None = None, doppler: str | INodeValueOutput[primitives.Float] | None = None, min_distance: str | INodeValueOutput[primitives.Float] | None = None, max_distance: str | INodeValueOutput[primitives.Float] | None = None, rolloff: str | INodeValueOutput[AudioRolloffCurve] | None = None, distance_space: str | INodeValueOutput[AudioDistanceSpace] | None = None, min_scale: str | INodeValueOutput[primitives.Float] | None = None, max_scale: str | INodeValueOutput[primitives.Float] | None = None, group: str | INodeValueOutput[AudioTypeGroup] | None = None, ignore_audio_effects: str | INodeValueOutput[primitives.Bool] | None = None, local_only: str | INodeValueOutput[primitives.Bool] | None = None, on_started_playing: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            clip: Initial value for Clip.
            volume: Initial value for Volume.
            speed: Initial value for Speed.
            spatialize: Initial value for Spatialize.
            spatial_blend: Initial value for SpatialBlend.
            global_: Initial value for Global.
            point: Initial value for Point.
            root: Initial value for Root.
            parent_under_root: Initial value for ParentUnderRoot.
            priority: Initial value for Priority.
            doppler: Initial value for Doppler.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            rolloff: Initial value for Rolloff.
            distance_space: Initial value for DistanceSpace.
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            group: Initial value for Group.
            ignore_audio_effects: Initial value for IgnoreAudioEffects.
            local_only: Initial value for LocalOnly.
            on_started_playing: Initial value for OnStartedPlaying.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if clip is not None:
            self.clip = clip
        if volume is not None:
            self.volume = volume
        if speed is not None:
            self.speed = speed
        if spatialize is not None:
            self.spatialize = spatialize
        if spatial_blend is not None:
            self.spatial_blend = spatial_blend
        if global_ is not None:
            self.global_ = global_
        if point is not None:
            self.point = point
        if root is not None:
            self.root = root
        if parent_under_root is not None:
            self.parent_under_root = parent_under_root
        if priority is not None:
            self.priority = priority
        if doppler is not None:
            self.doppler = doppler
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if rolloff is not None:
            self.rolloff = rolloff
        if distance_space is not None:
            self.distance_space = distance_space
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if group is not None:
            self.group = group
        if ignore_audio_effects is not None:
            self.ignore_audio_effects = ignore_audio_effects
        if local_only is not None:
            self.local_only = local_only
        if on_started_playing is not None:
            self.on_started_playing = on_started_playing

    @property
    def clip(self) -> str | None:
        """Target ID of the Clip reference (targets INodeObjectOutput[IAssetProvider[AudioClip]])."""
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clip.setter
    def clip(self, target: str | INodeObjectOutput[IAssetProvider[AudioClip]] | None) -> None:
        """Set the Clip reference by target ID or INodeObjectOutput[IAssetProvider[AudioClip]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Clip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>>'),
            )

    @property
    def volume(self) -> str | None:
        """Target ID of the Volume reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume.setter
    def volume(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Volume reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Volume",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def speed(self) -> str | None:
        """Target ID of the Speed reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Speed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @speed.setter
    def speed(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Speed reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Speed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Speed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def spatialize(self) -> str | None:
        """Target ID of the Spatialize reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatialize.setter
    def spatialize(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Spatialize reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Spatialize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Spatialize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def spatial_blend(self) -> str | None:
        """Target ID of the SpatialBlend reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("SpatialBlend")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatial_blend.setter
    def spatial_blend(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the SpatialBlend reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SpatialBlend")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpatialBlend",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def global_(self) -> str | None:
        """Target ID of the Global reference (targets INodeObjectOutput[Nullable[primitives.Bool]])."""
        member = self.get_member("Global")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @global_.setter
    def global_(self, target: str | INodeObjectOutput[Nullable[primitives.Bool]] | None) -> None:
        """Set the Global reference by target ID or INodeObjectOutput[Nullable[primitives.Bool]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Global")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Global",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Nullable<bool>>'),
            )

    @property
    def point(self) -> str | None:
        """Target ID of the Point reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point.setter
    def point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Root reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def parent_under_root(self) -> str | None:
        """Target ID of the ParentUnderRoot reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ParentUnderRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_under_root.setter
    def parent_under_root(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ParentUnderRoot reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ParentUnderRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentUnderRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def priority(self) -> str | None:
        """Target ID of the Priority reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Priority")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @priority.setter
    def priority(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Priority reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Priority")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Priority",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def doppler(self) -> str | None:
        """Target ID of the Doppler reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Doppler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @doppler.setter
    def doppler(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Doppler reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Doppler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Doppler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def min_distance(self) -> str | None:
        """Target ID of the MinDistance reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("MinDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min_distance.setter
    def min_distance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MinDistance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MinDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MinDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def max_distance(self) -> str | None:
        """Target ID of the MaxDistance reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("MaxDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_distance.setter
    def max_distance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MaxDistance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MaxDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaxDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def rolloff(self) -> str | None:
        """Target ID of the Rolloff reference (targets INodeValueOutput[AudioRolloffCurve])."""
        member = self.get_member("Rolloff")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rolloff.setter
    def rolloff(self, target: str | INodeValueOutput[AudioRolloffCurve] | None) -> None:
        """Set the Rolloff reference by target ID or INodeValueOutput[AudioRolloffCurve] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Rolloff")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rolloff",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Awwdio]Awwdio.AudioRolloffCurve>'),
            )

    @property
    def distance_space(self) -> str | None:
        """Target ID of the DistanceSpace reference (targets INodeValueOutput[AudioDistanceSpace])."""
        member = self.get_member("DistanceSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance_space.setter
    def distance_space(self, target: str | INodeValueOutput[AudioDistanceSpace] | None) -> None:
        """Set the DistanceSpace reference by target ID or INodeValueOutput[AudioDistanceSpace] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DistanceSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DistanceSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.AudioDistanceSpace>'),
            )

    @property
    def min_scale(self) -> str | None:
        """Target ID of the MinScale reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("MinScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min_scale.setter
    def min_scale(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MinScale reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MinScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MinScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def max_scale(self) -> str | None:
        """Target ID of the MaxScale reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("MaxScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_scale.setter
    def max_scale(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MaxScale reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MaxScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaxScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def group(self) -> str | None:
        """Target ID of the Group reference (targets INodeValueOutput[AudioTypeGroup])."""
        member = self.get_member("Group")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group.setter
    def group(self, target: str | INodeValueOutput[AudioTypeGroup] | None) -> None:
        """Set the Group reference by target ID or INodeValueOutput[AudioTypeGroup] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Group")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Group",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.AudioTypeGroup>'),
            )

    @property
    def ignore_audio_effects(self) -> str | None:
        """Target ID of the IgnoreAudioEffects reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("IgnoreAudioEffects")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_audio_effects.setter
    def ignore_audio_effects(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IgnoreAudioEffects reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreAudioEffects")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreAudioEffects",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def local_only(self) -> str | None:
        """Target ID of the LocalOnly reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("LocalOnly")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_only.setter
    def local_only(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the LocalOnly reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LocalOnly")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalOnly",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def audio(self) -> members.EmptyElement | None:
        """The Audio member."""
        member = self.get_member("Audio")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @audio.setter
    def audio(self, value: members.EmptyElement) -> None:
        """Set the Audio member."""
        self.set_member("Audio", value)

    @property
    def on_started_playing(self) -> str | None:
        """Target ID of the OnStartedPlaying reference (targets INodeOperation)."""
        member = self.get_member("OnStartedPlaying")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_started_playing.setter
    def on_started_playing(self, target: str | INodeOperation | None) -> None:
        """Set the OnStartedPlaying reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStartedPlaying")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStartedPlaying",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

