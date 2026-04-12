"""Generated component: ColorSky."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorSky(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ColorSky component creates a skybox with a color. Currently when this component is added to a slot, it will be immediately replaced with a Skybox and a material component automatically. It exists as a stub to maintain compatibility with legacy content.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColorSky"

    def __init__(self, base_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            base_color: Initial value for BaseColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if base_color is not None:
            self.base_color = base_color

    @property
    def base_color(self) -> primitives.ColorX | None:
        """Internal"""
        member = self.get_member("BaseColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_color.setter
    def base_color(self, value: primitives.ColorX) -> None:
        """Set the BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseColor", fields.FieldColorX(value=value)
            )

    @property
    def gradients(self) -> members.SyncList | None:
        """Internal"""
        member = self.get_member("_gradients")
        if isinstance(member, members.SyncList):
            return member
        return None

    @gradients.setter
    def gradients(self, value: members.SyncList) -> None:
        """Set _gradients. Internal"""
        self.set_member("_gradients", value)

