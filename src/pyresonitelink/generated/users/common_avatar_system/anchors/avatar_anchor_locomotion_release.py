"""Generated component: AvatarAnchorLocomotionRelease."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAnchorLocomotionRelease(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchorLocomotionRelease.

    Category: Users/Common Avatar System/Anchors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchorLocomotionRelease"

    def __init__(self, release_on_binary_action: bool | None = None, release_strength_threshold: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            release_on_binary_action: Initial value for ReleaseOnBinaryAction.
            release_strength_threshold: Initial value for ReleaseStrengthThreshold.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if release_on_binary_action is not None:
            self.release_on_binary_action = release_on_binary_action
        if release_strength_threshold is not None:
            self.release_strength_threshold = release_strength_threshold

    @property
    def release_on_binary_action(self) -> bool | None:
        """The ReleaseOnBinaryAction field value."""
        member = self.get_member("ReleaseOnBinaryAction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_on_binary_action.setter
    def release_on_binary_action(self, value: bool) -> None:
        """Set the ReleaseOnBinaryAction field value."""
        member = self.get_member("ReleaseOnBinaryAction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleaseOnBinaryAction", fields.FieldBool(value=value)
            )

    @property
    def release_strength_threshold(self) -> np.float32 | None:
        """The ReleaseStrengthThreshold field value."""
        member = self.get_member("ReleaseStrengthThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_strength_threshold.setter
    def release_strength_threshold(self, value: np.float32) -> None:
        """Set the ReleaseStrengthThreshold field value."""
        member = self.get_member("ReleaseStrengthThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleaseStrengthThreshold", fields.FieldNullableFloat(value=value)
            )

