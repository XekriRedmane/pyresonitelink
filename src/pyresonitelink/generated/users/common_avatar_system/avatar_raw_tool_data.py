"""Generated component: AvatarRawToolData."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarRawToolData(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarRawToolData.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarRawToolData"

    def __init__(self, pressing_primary: bool | None = None, pressing_secondary: bool | None = None, pressing_grab: bool | None = None, primary_strength: np.float32 | None = None, secondary_axis: primitives.Float2 | None = None, active_user: str | User | None = None, strength_stream: str | ValueStream[np.float32] | None = None, axis_stream: str | ValueStream[primitives.Float2] | None = None, primary_stream: str | ValueStream[bool] | None = None, secondary_stream: str | ValueStream[bool] | None = None, grab_stream: str | ValueStream[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pressing_primary: Initial value for PressingPrimary.
            pressing_secondary: Initial value for PressingSecondary.
            pressing_grab: Initial value for PressingGrab.
            primary_strength: Initial value for PrimaryStrength.
            secondary_axis: Initial value for SecondaryAxis.
            active_user: Initial value for _activeUser.
            strength_stream: Initial value for _strengthStream.
            axis_stream: Initial value for _axisStream.
            primary_stream: Initial value for _primaryStream.
            secondary_stream: Initial value for _secondaryStream.
            grab_stream: Initial value for _grabStream.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pressing_primary is not None:
            self.pressing_primary = pressing_primary
        if pressing_secondary is not None:
            self.pressing_secondary = pressing_secondary
        if pressing_grab is not None:
            self.pressing_grab = pressing_grab
        if primary_strength is not None:
            self.primary_strength = primary_strength
        if secondary_axis is not None:
            self.secondary_axis = secondary_axis
        if active_user is not None:
            self.active_user = active_user
        if strength_stream is not None:
            self.strength_stream = strength_stream
        if axis_stream is not None:
            self.axis_stream = axis_stream
        if primary_stream is not None:
            self.primary_stream = primary_stream
        if secondary_stream is not None:
            self.secondary_stream = secondary_stream
        if grab_stream is not None:
            self.grab_stream = grab_stream

    @property
    def controller_side(self) -> members.FieldEnum | None:
        """The ControllerSide member."""
        member = self.get_member("ControllerSide")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @controller_side.setter
    def controller_side(self, value: members.FieldEnum) -> None:
        """Set the ControllerSide member."""
        self.set_member("ControllerSide", value)

    @property
    def pressing_primary(self) -> bool | None:
        """The PressingPrimary field value."""
        member = self.get_member("PressingPrimary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressing_primary.setter
    def pressing_primary(self, value: bool) -> None:
        """Set the PressingPrimary field value."""
        member = self.get_member("PressingPrimary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressingPrimary", fields.FieldBool(value=value)
            )

    @property
    def pressing_secondary(self) -> bool | None:
        """The PressingSecondary field value."""
        member = self.get_member("PressingSecondary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressing_secondary.setter
    def pressing_secondary(self, value: bool) -> None:
        """Set the PressingSecondary field value."""
        member = self.get_member("PressingSecondary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressingSecondary", fields.FieldBool(value=value)
            )

    @property
    def pressing_grab(self) -> bool | None:
        """The PressingGrab field value."""
        member = self.get_member("PressingGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pressing_grab.setter
    def pressing_grab(self, value: bool) -> None:
        """Set the PressingGrab field value."""
        member = self.get_member("PressingGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PressingGrab", fields.FieldBool(value=value)
            )

    @property
    def primary_strength(self) -> np.float32 | None:
        """The PrimaryStrength field value."""
        member = self.get_member("PrimaryStrength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @primary_strength.setter
    def primary_strength(self, value: np.float32) -> None:
        """Set the PrimaryStrength field value."""
        member = self.get_member("PrimaryStrength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PrimaryStrength", fields.FieldFloat(value=value)
            )

    @property
    def secondary_axis(self) -> primitives.Float2 | None:
        """The SecondaryAxis field value."""
        member = self.get_member("SecondaryAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_axis.setter
    def secondary_axis(self, value: primitives.Float2) -> None:
        """Set the SecondaryAxis field value."""
        member = self.get_member("SecondaryAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryAxis", fields.FieldFloat2(value=value)
            )

    @property
    def active_user(self) -> str | None:
        """Target ID of the _activeUser reference (targets User)."""
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_user.setter
    def active_user(self, target: str | User | None) -> None:
        """Set the _activeUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def strength_stream(self) -> str | None:
        """Target ID of the _strengthStream reference (targets ValueStream[np.float32])."""
        member = self.get_member("_strengthStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @strength_stream.setter
    def strength_stream(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the _strengthStream reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_strengthStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_strengthStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def axis_stream(self) -> str | None:
        """Target ID of the _axisStream reference (targets ValueStream[primitives.Float2])."""
        member = self.get_member("_axisStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @axis_stream.setter
    def axis_stream(self, target: str | ValueStream[primitives.Float2] | None) -> None:
        """Set the _axisStream reference by target ID or ValueStream[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_axisStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_axisStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float2>'),
            )

    @property
    def primary_stream(self) -> str | None:
        """Target ID of the _primaryStream reference (targets ValueStream[bool])."""
        member = self.get_member("_primaryStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_stream.setter
    def primary_stream(self, target: str | ValueStream[bool] | None) -> None:
        """Set the _primaryStream reference by target ID or ValueStream[bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_primaryStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_primaryStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def secondary_stream(self) -> str | None:
        """Target ID of the _secondaryStream reference (targets ValueStream[bool])."""
        member = self.get_member("_secondaryStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_stream.setter
    def secondary_stream(self, target: str | ValueStream[bool] | None) -> None:
        """Set the _secondaryStream reference by target ID or ValueStream[bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_secondaryStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_secondaryStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def grab_stream(self) -> str | None:
        """Target ID of the _grabStream reference (targets ValueStream[bool])."""
        member = self.get_member("_grabStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grab_stream.setter
    def grab_stream(self, target: str | ValueStream[bool] | None) -> None:
        """Set the _grabStream reference by target ID or ValueStream[bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_grabStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

