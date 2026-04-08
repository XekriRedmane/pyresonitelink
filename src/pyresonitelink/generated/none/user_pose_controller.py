"""Generated component: UserPoseController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.screen_controller import ScreenController
from pyresonitelink.generated._types.locomotion_animation_configuration import LocomotionAnimationConfiguration
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserPoseController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserPoseController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserPoseController"

    def __init__(self, screen_controller: str | ScreenController | None = None, body_horizontal_angle: primitives.Float | None = None, render_debug_visuals: primitives.Bool | None = None, pause_locomotion_animation: primitives.Bool | None = None, override_locomotion_velocity: primitives.Float3 | None = None, override_locomotion_angular_velocity: primitives.Float | None = None, simulation_speed_ratio: primitives.Float | None = None, default_config: str | LocomotionAnimationConfiguration | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            screen_controller: Initial value for ScreenController.
            body_horizontal_angle: Initial value for BodyHorizontalAngle.
            render_debug_visuals: Initial value for RenderDebugVisuals.
            pause_locomotion_animation: Initial value for PauseLocomotionAnimation.
            override_locomotion_velocity: Initial value for OverrideLocomotionVelocity.
            override_locomotion_angular_velocity: Initial value for OverrideLocomotionAngularVelocity.
            simulation_speed_ratio: Initial value for SimulationSpeedRatio.
            default_config: Initial value for _defaultConfig.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if screen_controller is not None:
            self.screen_controller = screen_controller
        if body_horizontal_angle is not None:
            self.body_horizontal_angle = body_horizontal_angle
        if render_debug_visuals is not None:
            self.render_debug_visuals = render_debug_visuals
        if pause_locomotion_animation is not None:
            self.pause_locomotion_animation = pause_locomotion_animation
        if override_locomotion_velocity is not None:
            self.override_locomotion_velocity = override_locomotion_velocity
        if override_locomotion_angular_velocity is not None:
            self.override_locomotion_angular_velocity = override_locomotion_angular_velocity
        if simulation_speed_ratio is not None:
            self.simulation_speed_ratio = simulation_speed_ratio
        if default_config is not None:
            self.default_config = default_config

    @property
    def screen_controller(self) -> str | None:
        """Target ID of the ScreenController reference (targets ScreenController)."""
        member = self.get_member("ScreenController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_controller.setter
    def screen_controller(self, target: str | ScreenController | None) -> None:
        """Set the ScreenController reference by target ID or ScreenController instance."""
        target_id: str | None = target.id if isinstance(target, ScreenController) else target  # type: ignore[assignment]
        member = self.get_member("ScreenController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ScreenController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScreenController'),
            )

    @property
    def body_horizontal_angle(self) -> primitives.Float | None:
        """The BodyHorizontalAngle field value."""
        member = self.get_member("BodyHorizontalAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @body_horizontal_angle.setter
    def body_horizontal_angle(self, value: primitives.Float) -> None:
        """Set the BodyHorizontalAngle field value."""
        member = self.get_member("BodyHorizontalAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BodyHorizontalAngle", fields.FieldFloat(value=value)
            )

    @property
    def render_debug_visuals(self) -> primitives.Bool | None:
        """The RenderDebugVisuals field value."""
        member = self.get_member("RenderDebugVisuals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_debug_visuals.setter
    def render_debug_visuals(self, value: primitives.Bool) -> None:
        """Set the RenderDebugVisuals field value."""
        member = self.get_member("RenderDebugVisuals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderDebugVisuals", fields.FieldBool(value=value)
            )

    @property
    def pause_locomotion_animation(self) -> primitives.Bool | None:
        """The PauseLocomotionAnimation field value."""
        member = self.get_member("PauseLocomotionAnimation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pause_locomotion_animation.setter
    def pause_locomotion_animation(self, value: primitives.Bool) -> None:
        """Set the PauseLocomotionAnimation field value."""
        member = self.get_member("PauseLocomotionAnimation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PauseLocomotionAnimation", fields.FieldBool(value=value)
            )

    @property
    def override_locomotion_velocity(self) -> primitives.Float3 | None:
        """The OverrideLocomotionVelocity field value."""
        member = self.get_member("OverrideLocomotionVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_locomotion_velocity.setter
    def override_locomotion_velocity(self, value: primitives.Float3) -> None:
        """Set the OverrideLocomotionVelocity field value."""
        member = self.get_member("OverrideLocomotionVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideLocomotionVelocity", fields.FieldNullableFloat3(value=value)
            )

    @property
    def override_locomotion_angular_velocity(self) -> primitives.Float | None:
        """The OverrideLocomotionAngularVelocity field value."""
        member = self.get_member("OverrideLocomotionAngularVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_locomotion_angular_velocity.setter
    def override_locomotion_angular_velocity(self, value: primitives.Float) -> None:
        """Set the OverrideLocomotionAngularVelocity field value."""
        member = self.get_member("OverrideLocomotionAngularVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideLocomotionAngularVelocity", fields.FieldNullableFloat(value=value)
            )

    @property
    def simulation_speed_ratio(self) -> primitives.Float | None:
        """The SimulationSpeedRatio field value."""
        member = self.get_member("SimulationSpeedRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simulation_speed_ratio.setter
    def simulation_speed_ratio(self, value: primitives.Float) -> None:
        """Set the SimulationSpeedRatio field value."""
        member = self.get_member("SimulationSpeedRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimulationSpeedRatio", fields.FieldFloat(value=value)
            )

    @property
    def default_config(self) -> str | None:
        """Target ID of the _defaultConfig reference (targets LocomotionAnimationConfiguration)."""
        member = self.get_member("_defaultConfig")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_config.setter
    def default_config(self, target: str | LocomotionAnimationConfiguration | None) -> None:
        """Set the _defaultConfig reference by target ID or LocomotionAnimationConfiguration instance."""
        target_id: str | None = target.id if isinstance(target, LocomotionAnimationConfiguration) else target  # type: ignore[assignment]
        member = self.get_member("_defaultConfig")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_defaultConfig",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LocomotionAnimationConfiguration'),
            )

