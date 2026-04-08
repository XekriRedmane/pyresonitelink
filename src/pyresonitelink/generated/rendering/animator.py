"""Generated component: Animator."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.animation import Animation
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Animator(GeneratedComponent, IPlayable, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Animator.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Animator"

    def __init__(self, clip: str | IAssetProvider[Animation] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            clip: Initial value for Clip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if clip is not None:
            self.clip = clip

    @property
    def playback(self) -> members.SyncPlayback | None:
        """The _playback member."""
        member = self.get_member("_playback")
        if isinstance(member, members.SyncPlayback):
            return member
        return None

    @playback.setter
    def playback(self, value: members.SyncPlayback) -> None:
        """Set the _playback member."""
        self.set_member("_playback", value)

    @property
    def clip(self) -> str | None:
        """Target ID of the Clip reference (targets IAssetProvider[Animation])."""
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clip.setter
    def clip(self, target: str | IAssetProvider[Animation] | None) -> None:
        """Set the Clip reference by target ID or IAssetProvider[Animation] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Clip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Animation>'),
            )

    @property
    def fields(self) -> members.SyncList | None:
        """The Fields member."""
        member = self.get_member("Fields")
        if isinstance(member, members.SyncList):
            return member
        return None

    @fields.setter
    def fields(self, value: members.SyncList) -> None:
        """Set the Fields member."""
        self.set_member("Fields", value)

