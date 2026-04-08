"""Generated component: LODGroup."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LODGroup(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LODGroup.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LODGroup"

    def __init__(self, cross_fade: bool | None = None, animate_cross_fading: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            cross_fade: Initial value for CrossFade.
            animate_cross_fading: Initial value for AnimateCrossFading.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if cross_fade is not None:
            self.cross_fade = cross_fade
        if animate_cross_fading is not None:
            self.animate_cross_fading = animate_cross_fading

    @property
    def lods(self) -> members.SyncList | None:
        """The LODs member."""
        member = self.get_member("LODs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @lods.setter
    def lods(self, value: members.SyncList) -> None:
        """Set the LODs member."""
        self.set_member("LODs", value)

    @property
    def cross_fade(self) -> bool | None:
        """The CrossFade field value."""
        member = self.get_member("CrossFade")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cross_fade.setter
    def cross_fade(self, value: bool) -> None:
        """Set the CrossFade field value."""
        member = self.get_member("CrossFade")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrossFade", fields.FieldBool(value=value)
            )

    @property
    def animate_cross_fading(self) -> bool | None:
        """The AnimateCrossFading field value."""
        member = self.get_member("AnimateCrossFading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animate_cross_fading.setter
    def animate_cross_fading(self, value: bool) -> None:
        """Set the AnimateCrossFading field value."""
        member = self.get_member("AnimateCrossFading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimateCrossFading", fields.FieldBool(value=value)
            )

