"""Generated component: ColorSky."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorSky(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColorSky.
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
        """The BaseColor field value."""
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
        """The _gradients member."""
        member = self.get_member("_gradients")
        if isinstance(member, members.SyncList):
            return member
        return None

    @gradients.setter
    def gradients(self, value: members.SyncList) -> None:
        """Set the _gradients member."""
        self.set_member("_gradients", value)

