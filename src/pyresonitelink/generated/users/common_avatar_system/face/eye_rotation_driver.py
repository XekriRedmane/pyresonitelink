"""Generated component: EyeRotationDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.eye_manager import EyeManager
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeRotationDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.EyeRotationDriver.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.EyeRotationDriver"

    def __init__(self, eye_manager: str | EyeManager | None = None, eye_motion_scale: np.float32 | None = None, eye_motion_exp: np.float32 | None = None, max_swing: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            eye_manager: Initial value for EyeManager.
            eye_motion_scale: Initial value for EyeMotionScale.
            eye_motion_exp: Initial value for EyeMotionExp.
            max_swing: Initial value for MaxSwing.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if eye_manager is not None:
            self.eye_manager = eye_manager
        if eye_motion_scale is not None:
            self.eye_motion_scale = eye_motion_scale
        if eye_motion_exp is not None:
            self.eye_motion_exp = eye_motion_exp
        if max_swing is not None:
            self.max_swing = max_swing

    @property
    def eye_manager(self) -> str | None:
        """Target ID of the EyeManager reference (targets EyeManager)."""
        member = self.get_member("EyeManager")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eye_manager.setter
    def eye_manager(self, target: str | EyeManager | None) -> None:
        """Set the EyeManager reference by target ID or EyeManager instance."""
        target_id: str | None = target.id if isinstance(target, EyeManager) else target  # type: ignore[assignment]
        member = self.get_member("EyeManager")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EyeManager",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.EyeManager'),
            )

    @property
    def eye_motion_scale(self) -> np.float32 | None:
        """The EyeMotionScale field value."""
        member = self.get_member("EyeMotionScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eye_motion_scale.setter
    def eye_motion_scale(self, value: np.float32) -> None:
        """Set the EyeMotionScale field value."""
        member = self.get_member("EyeMotionScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EyeMotionScale", fields.FieldFloat(value=value)
            )

    @property
    def eye_motion_exp(self) -> np.float32 | None:
        """The EyeMotionExp field value."""
        member = self.get_member("EyeMotionExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eye_motion_exp.setter
    def eye_motion_exp(self, value: np.float32) -> None:
        """Set the EyeMotionExp field value."""
        member = self.get_member("EyeMotionExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EyeMotionExp", fields.FieldFloat(value=value)
            )

    @property
    def max_swing(self) -> np.float32 | None:
        """The MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_swing.setter
    def max_swing(self, value: np.float32) -> None:
        """Set the MaxSwing field value."""
        member = self.get_member("MaxSwing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSwing", fields.FieldFloat(value=value)
            )

    @property
    def eyes(self) -> members.SyncList | None:
        """The Eyes member."""
        member = self.get_member("Eyes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @eyes.setter
    def eyes(self, value: members.SyncList) -> None:
        """Set the Eyes member."""
        self.set_member("Eyes", value)

