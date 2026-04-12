"""Generated component: HapticManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HapticManager(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Can be found under each user's User root slot, the HapticManager controls the locally injected haptics for everyone in the session besides yourself if this component is found underneath your own user root slot.

The HapticManager also allows you to locally see the debug visuals of each user in the form of green transparent shapes. However you need to check ShowDebugVisuals then hit Rebuild Injected Sources to see this change reflected, do the inverse to remove the debug visuals.

    Note this component functions locally and does not affect injected
    haptics on your own avatar, to do that you need to use the
    AvatarHapticSourceManager to override the injected behavior for your own
    avatar. If found on other user root slots other than yourself, this
    component does nothing and won't do any changes. HapticManger can be
    used to debug weird haptic collisions from other users in the session,
    or possibly help with the issues where there is "stuck" haptics from
    touching injected haptic zones by rebuilding the haptic zones. With the
    help of the ShowDebugVisuals you can see the haptic culling behavior if
    you step away from another user far enough.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HapticManager"

    def __init__(self, injected_body_part_intensity: primitives.Float | None = None, injected_hand_intensity: primitives.Float | None = None, injected_head_intensity: primitives.Float | None = None, injected_radius_start_ratio: primitives.Float | None = None, injected_radius_end_ratio: primitives.Float | None = None, injected_radius_power: primitives.Float | None = None, show_debug_visuals: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            injected_body_part_intensity: Initial value for InjectedBodyPartIntensity.
            injected_hand_intensity: Initial value for InjectedHandIntensity.
            injected_head_intensity: Initial value for InjectedHeadIntensity.
            injected_radius_start_ratio: Initial value for InjectedRadiusStartRatio.
            injected_radius_end_ratio: Initial value for InjectedRadiusEndRatio.
            injected_radius_power: Initial value for InjectedRadiusPower.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if injected_body_part_intensity is not None:
            self.injected_body_part_intensity = injected_body_part_intensity
        if injected_hand_intensity is not None:
            self.injected_hand_intensity = injected_hand_intensity
        if injected_head_intensity is not None:
            self.injected_head_intensity = injected_head_intensity
        if injected_radius_start_ratio is not None:
            self.injected_radius_start_ratio = injected_radius_start_ratio
        if injected_radius_end_ratio is not None:
            self.injected_radius_end_ratio = injected_radius_end_ratio
        if injected_radius_power is not None:
            self.injected_radius_power = injected_radius_power
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals

    @property
    def injected_body_part_intensity(self) -> primitives.Float | None:
        """Adjusts the haptic intensity of bodyparts that aren't the head and hands."""
        member = self.get_member("InjectedBodyPartIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @injected_body_part_intensity.setter
    def injected_body_part_intensity(self, value: primitives.Float) -> None:
        """Set the InjectedBodyPartIntensity field value."""
        member = self.get_member("InjectedBodyPartIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InjectedBodyPartIntensity", fields.FieldFloat(value=value)
            )

    @property
    def injected_hand_intensity(self) -> primitives.Float | None:
        """Adjusts the haptic intensity of the hands."""
        member = self.get_member("InjectedHandIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @injected_hand_intensity.setter
    def injected_hand_intensity(self, value: primitives.Float) -> None:
        """Set the InjectedHandIntensity field value."""
        member = self.get_member("InjectedHandIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InjectedHandIntensity", fields.FieldFloat(value=value)
            )

    @property
    def injected_head_intensity(self) -> primitives.Float | None:
        """Adjusts the haptic intensity of the head."""
        member = self.get_member("InjectedHeadIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @injected_head_intensity.setter
    def injected_head_intensity(self, value: primitives.Float) -> None:
        """Set the InjectedHeadIntensity field value."""
        member = self.get_member("InjectedHeadIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InjectedHeadIntensity", fields.FieldFloat(value=value)
            )

    @property
    def injected_radius_start_ratio(self) -> primitives.Float | None:
        """Adjusts the start radius of all injected haptics."""
        member = self.get_member("InjectedRadiusStartRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @injected_radius_start_ratio.setter
    def injected_radius_start_ratio(self, value: primitives.Float) -> None:
        """Set the InjectedRadiusStartRatio field value."""
        member = self.get_member("InjectedRadiusStartRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InjectedRadiusStartRatio", fields.FieldFloat(value=value)
            )

    @property
    def injected_radius_end_ratio(self) -> primitives.Float | None:
        """The InjectedRadiusEndRatio field value."""
        member = self.get_member("InjectedRadiusEndRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @injected_radius_end_ratio.setter
    def injected_radius_end_ratio(self, value: primitives.Float) -> None:
        """Set the InjectedRadiusEndRatio field value."""
        member = self.get_member("InjectedRadiusEndRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InjectedRadiusEndRatio", fields.FieldFloat(value=value)
            )

    @property
    def injected_radius_power(self) -> primitives.Float | None:
        """Adjusts the overall radius of all injected haptics."""
        member = self.get_member("InjectedRadiusPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @injected_radius_power.setter
    def injected_radius_power(self, value: primitives.Float) -> None:
        """Set the InjectedRadiusPower field value."""
        member = self.get_member("InjectedRadiusPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InjectedRadiusPower", fields.FieldFloat(value=value)
            )

    @property
    def show_debug_visuals(self) -> primitives.Bool | None:
        """Locally shows injected haptics for each user, Rebuild Injected Sources needs to be checked for this to work."""
        member = self.get_member("ShowDebugVisuals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visuals.setter
    def show_debug_visuals(self, value: primitives.Bool) -> None:
        """Set the ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowDebugVisuals", fields.FieldBool(value=value)
            )

