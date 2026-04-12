"""Generated component: LODGroup."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LODGroup(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """A LOD (Level Of Detail) Group allows you to define behaviors to load alternate meshes for objects based on their relative size on a user's screen. This is commonly used to replace complex and finely detailed meshes with simplified versions based on a user's distance from the object.

    Category: Rendering

    **Behavior**: This also influences the images seen of renderers viewed in mirrors. meaning that a renderer specified by this component can look different in the mirror vs if it's right beside you, at the exact same moment.

This component relies heavily on the behavior of Unity when it's forced to the unity side via Connectors in FrooxEngine.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LODGroup"

    def __init__(self, cross_fade: primitives.Bool | None = None, animate_cross_fading: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """A list of different LOD stages with renderers that should appear for each stage."""
        member = self.get_member("LODs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @lods.setter
    def lods(self, value: members.SyncList) -> None:
        """Set LODs. A list of different LOD stages with renderers that should appear for each stage."""
        self.set_member("LODs", value)

    @property
    def cross_fade(self) -> primitives.Bool | None:
        """Cross fade on the Unity LOD component."""
        member = self.get_member("CrossFade")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cross_fade.setter
    def cross_fade(self, value: primitives.Bool) -> None:
        """Set the CrossFade field value."""
        member = self.get_member("CrossFade")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrossFade", fields.FieldBool(value=value)
            )

    @property
    def animate_cross_fading(self) -> primitives.Bool | None:
        """Animate Cross fade on the Unity LOD component."""
        member = self.get_member("AnimateCrossFading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animate_cross_fading.setter
    def animate_cross_fading(self, value: primitives.Bool) -> None:
        """Set the AnimateCrossFading field value."""
        member = self.get_member("AnimateCrossFading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimateCrossFading", fields.FieldBool(value=value)
            )

