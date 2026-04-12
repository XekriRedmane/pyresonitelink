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
    """Animator is a component that's used to play Animation and drive a list of fields using the contained animation data. The order and type of said fields is determined by the Animation in the ``Clip`` field, and the value sampled from the Animation for any field (``Fields``) is determined by the Animation's sampled value at the position the ``_playback`` is currently at. Sampling is determined by the type of Animation ``Clip`` is. You should be able to drive field by assigning ValueField's ``Value`` onto ``Fields``.

    Category: Rendering

    **Behavior**: This component doesn't require every item of ``Fields`` to be filled out to still function. This behavior can be taken advantage of.

In the case of Ghostly's Mantis Blade, the arm which the blade is attached to comes with an animation to animate the blade. However, the animation being imported onto a full VRIK rig will prevent the VRIK from being generated. Though if the model is imported again without the animation, the rig will not be animated but it will have VRIK. If the Animator component is moved to the root of the VRIK avatar and the user hits set up slots, then the animator will animate the mantis blade on the arm once again, even though most of the fields are empty.

To drive a VRIK like a person however, you cannot currently drive one directly or switch out the drivers with a VRIK at runtime. The game will actively fight what you are doing. Instead you should use an Anchor and pin the user via anchor constraints to make them pose into the position you want. Some user dance creations use this. For fingers, use the Finger Posing System.
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
        """Is populated by the length and properties of ``Clip`` and is used to determine what point at which to sample the ``Clip``."""
        member = self.get_member("_playback")
        if isinstance(member, members.SyncPlayback):
            return member
        return None

    @playback.setter
    def playback(self, value: members.SyncPlayback) -> None:
        """Set _playback. Is populated by the length and properties of ``Clip`` and is used to determine what point at which to sample the ``Clip``."""
        self.set_member("_playback", value)

    @property
    def clip(self) -> str | None:
        """An Animation used to determine the list of ``Fields`` on this component and their value/ref types."""
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
        """the list of values stored in this animation. Each field and it's type/animation data is determined by track index order."""
        member = self.get_member("Fields")
        if isinstance(member, members.SyncList):
            return member
        return None

    @fields.setter
    def fields(self, value: members.SyncList) -> None:
        """Set Fields. the list of values stored in this animation. Each field and it's type/animation data is determined by track index order."""
        self.set_member("Fields", value)

