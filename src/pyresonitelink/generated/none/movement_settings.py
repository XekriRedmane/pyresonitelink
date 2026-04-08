"""Generated component: MovementSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class MovementSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.MovementSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MovementSettings"

    def __init__(self, use_head_direction_for_movement: primitives.Bool | None = None, use_smooth_turn: primitives.Bool | None = None, smooth_turn_exclusive_mode: primitives.Bool | None = None, smooth_turn_speed: primitives.Float | None = None, snap_turn_angle: primitives.Float | None = None, no_clip_speed: primitives.Float | None = None, movement_deadzone: primitives.Float | None = None, turning_deadzone: primitives.Float | None = None, movement_exponent: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_head_direction_for_movement: Initial value for UseHeadDirectionForMovement.
            use_smooth_turn: Initial value for UseSmoothTurn.
            smooth_turn_exclusive_mode: Initial value for SmoothTurnExclusiveMode.
            smooth_turn_speed: Initial value for SmoothTurnSpeed.
            snap_turn_angle: Initial value for SnapTurnAngle.
            no_clip_speed: Initial value for NoClipSpeed.
            movement_deadzone: Initial value for MovementDeadzone.
            turning_deadzone: Initial value for TurningDeadzone.
            movement_exponent: Initial value for MovementExponent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_head_direction_for_movement is not None:
            self.use_head_direction_for_movement = use_head_direction_for_movement
        if use_smooth_turn is not None:
            self.use_smooth_turn = use_smooth_turn
        if smooth_turn_exclusive_mode is not None:
            self.smooth_turn_exclusive_mode = smooth_turn_exclusive_mode
        if smooth_turn_speed is not None:
            self.smooth_turn_speed = smooth_turn_speed
        if snap_turn_angle is not None:
            self.snap_turn_angle = snap_turn_angle
        if no_clip_speed is not None:
            self.no_clip_speed = no_clip_speed
        if movement_deadzone is not None:
            self.movement_deadzone = movement_deadzone
        if turning_deadzone is not None:
            self.turning_deadzone = turning_deadzone
        if movement_exponent is not None:
            self.movement_exponent = movement_exponent

    @property
    def left_sideways_mode(self) -> members.FieldEnum | None:
        """The LeftSidewaysMode member."""
        member = self.get_member("LeftSidewaysMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @left_sideways_mode.setter
    def left_sideways_mode(self, value: members.FieldEnum) -> None:
        """Set the LeftSidewaysMode member."""
        self.set_member("LeftSidewaysMode", value)

    @property
    def right_sideways_mode(self) -> members.FieldEnum | None:
        """The RightSidewaysMode member."""
        member = self.get_member("RightSidewaysMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @right_sideways_mode.setter
    def right_sideways_mode(self, value: members.FieldEnum) -> None:
        """Set the RightSidewaysMode member."""
        self.set_member("RightSidewaysMode", value)

    @property
    def use_head_direction_for_movement(self) -> primitives.Bool | None:
        """The UseHeadDirectionForMovement field value."""
        member = self.get_member("UseHeadDirectionForMovement")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_head_direction_for_movement.setter
    def use_head_direction_for_movement(self, value: primitives.Bool) -> None:
        """Set the UseHeadDirectionForMovement field value."""
        member = self.get_member("UseHeadDirectionForMovement")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseHeadDirectionForMovement", fields.FieldBool(value=value)
            )

    @property
    def use_smooth_turn(self) -> primitives.Bool | None:
        """The UseSmoothTurn field value."""
        member = self.get_member("UseSmoothTurn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_smooth_turn.setter
    def use_smooth_turn(self, value: primitives.Bool) -> None:
        """Set the UseSmoothTurn field value."""
        member = self.get_member("UseSmoothTurn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSmoothTurn", fields.FieldBool(value=value)
            )

    @property
    def smooth_turn_exclusive_mode(self) -> primitives.Bool | None:
        """The SmoothTurnExclusiveMode field value."""
        member = self.get_member("SmoothTurnExclusiveMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_turn_exclusive_mode.setter
    def smooth_turn_exclusive_mode(self, value: primitives.Bool) -> None:
        """Set the SmoothTurnExclusiveMode field value."""
        member = self.get_member("SmoothTurnExclusiveMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothTurnExclusiveMode", fields.FieldBool(value=value)
            )

    @property
    def smooth_turn_speed(self) -> primitives.Float | None:
        """The SmoothTurnSpeed field value."""
        member = self.get_member("SmoothTurnSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_turn_speed.setter
    def smooth_turn_speed(self, value: primitives.Float) -> None:
        """Set the SmoothTurnSpeed field value."""
        member = self.get_member("SmoothTurnSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothTurnSpeed", fields.FieldFloat(value=value)
            )

    @property
    def snap_turn_angle(self) -> primitives.Float | None:
        """The SnapTurnAngle field value."""
        member = self.get_member("SnapTurnAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_turn_angle.setter
    def snap_turn_angle(self, value: primitives.Float) -> None:
        """Set the SnapTurnAngle field value."""
        member = self.get_member("SnapTurnAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapTurnAngle", fields.FieldFloat(value=value)
            )

    @property
    def no_clip_speed(self) -> primitives.Float | None:
        """The NoClipSpeed field value."""
        member = self.get_member("NoClipSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @no_clip_speed.setter
    def no_clip_speed(self, value: primitives.Float) -> None:
        """Set the NoClipSpeed field value."""
        member = self.get_member("NoClipSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoClipSpeed", fields.FieldFloat(value=value)
            )

    @property
    def movement_deadzone(self) -> primitives.Float | None:
        """The MovementDeadzone field value."""
        member = self.get_member("MovementDeadzone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @movement_deadzone.setter
    def movement_deadzone(self, value: primitives.Float) -> None:
        """Set the MovementDeadzone field value."""
        member = self.get_member("MovementDeadzone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MovementDeadzone", fields.FieldFloat(value=value)
            )

    @property
    def turning_deadzone(self) -> primitives.Float | None:
        """The TurningDeadzone field value."""
        member = self.get_member("TurningDeadzone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @turning_deadzone.setter
    def turning_deadzone(self, value: primitives.Float) -> None:
        """Set the TurningDeadzone field value."""
        member = self.get_member("TurningDeadzone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TurningDeadzone", fields.FieldFloat(value=value)
            )

    @property
    def movement_exponent(self) -> primitives.Float | None:
        """The MovementExponent field value."""
        member = self.get_member("MovementExponent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @movement_exponent.setter
    def movement_exponent(self, value: primitives.Float) -> None:
        """Set the MovementExponent field value."""
        member = self.get_member("MovementExponent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MovementExponent", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

