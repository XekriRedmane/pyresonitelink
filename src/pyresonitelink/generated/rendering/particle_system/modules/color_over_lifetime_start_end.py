"""Generated component: ColorOverLifetimeStartEnd."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorOverLifetimeStartEnd(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorOverLifetimeStartEnd.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorOverLifetimeStartEnd"

    def __init__(self, start_color: primitives.ColorX | None = None, end_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start_color: Initial value for StartColor.
            end_color: Initial value for EndColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start_color is not None:
            self.start_color = start_color
        if end_color is not None:
            self.end_color = end_color

    @property
    def start_color(self) -> primitives.ColorX | None:
        """The StartColor field value."""
        member = self.get_member("StartColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_color.setter
    def start_color(self, value: primitives.ColorX) -> None:
        """Set the StartColor field value."""
        member = self.get_member("StartColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartColor", fields.FieldColorX(value=value)
            )

    @property
    def end_color(self) -> primitives.ColorX | None:
        """The EndColor field value."""
        member = self.get_member("EndColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_color.setter
    def end_color(self, value: primitives.ColorX) -> None:
        """Set the EndColor field value."""
        member = self.get_member("EndColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndColor", fields.FieldColorX(value=value)
            )

