"""Generated component: VirtualHapticPointSampler."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualHapticPointSampler(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Virtual Haptic Point sampler is a component that is used as a way of picking up haptic sensations from the virtual environment inside Resonite, without needing a haptic device. This can be used as a way of making a device that beeps as it detects vibrations, temperature, pain, and force. It can also be used as a way of relaying vibration sensations via API to vibration devices not supported by Resonite, like speakers with base.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualHapticPointSampler"

    def __init__(self, radius: primitives.Float | None = None, show_debug_visual: primitives.Bool | None = None, debug_visual: str | OverlayFresnelMaterial | None = None, force: primitives.Float | None = None, pain: primitives.Float | None = None, temperature: primitives.Float | None = None, vibration: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            show_debug_visual: Initial value for ShowDebugVisual.
            debug_visual: Initial value for _debugVisual.
            force: Initial value for Force.
            pain: Initial value for Pain.
            temperature: Initial value for Temperature.
            vibration: Initial value for Vibration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if show_debug_visual is not None:
            self.show_debug_visual = show_debug_visual
        if debug_visual is not None:
            self.debug_visual = debug_visual
        if force is not None:
            self.force = force
        if pain is not None:
            self.pain = pain
        if temperature is not None:
            self.temperature = temperature
        if vibration is not None:
            self.vibration = vibration

    @property
    def radius(self) -> primitives.Float | None:
        """The radius of the sphere for this."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def show_debug_visual(self) -> primitives.Bool | None:
        """Whether to show the debug visual for this sampler."""
        member = self.get_member("ShowDebugVisual")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visual.setter
    def show_debug_visual(self, value: primitives.Bool) -> None:
        """Set the ShowDebugVisual field value."""
        member = self.get_member("ShowDebugVisual")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowDebugVisual", fields.FieldBool(value=value)
            )

    @property
    def debug_visual(self) -> str | None:
        """the material on the sphere of the current generated debug visual. Is null when ``ShowDebugVisual`` is false."""
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_visual.setter
    def debug_visual(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _debugVisual reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_debugVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def force(self) -> primitives.Float | None:
        """The force sensations picked up by this haptic point sampler."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: primitives.Float) -> None:
        """Set the Force field value."""
        member = self.get_member("Force")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Force", fields.FieldFloat(value=value)
            )

    @property
    def pain(self) -> primitives.Float | None:
        """The pain sensations picked up by this haptic point sampler."""
        member = self.get_member("Pain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pain.setter
    def pain(self, value: primitives.Float) -> None:
        """Set the Pain field value."""
        member = self.get_member("Pain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pain", fields.FieldFloat(value=value)
            )

    @property
    def temperature(self) -> primitives.Float | None:
        """The temperature sensations picked up by this haptic point sampler."""
        member = self.get_member("Temperature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @temperature.setter
    def temperature(self, value: primitives.Float) -> None:
        """Set the Temperature field value."""
        member = self.get_member("Temperature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Temperature", fields.FieldFloat(value=value)
            )

    @property
    def vibration(self) -> primitives.Float | None:
        """the vibration sensations picked up by this haptic point sampler."""
        member = self.get_member("Vibration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration.setter
    def vibration(self, value: primitives.Float) -> None:
        """Set the Vibration field value."""
        member = self.get_member("Vibration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vibration", fields.FieldFloat(value=value)
            )

