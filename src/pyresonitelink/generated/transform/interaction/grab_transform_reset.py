"""Generated component: GrabTransformReset."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabTransformReset(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """The GrabTransformReset component resets transforms of a grabbable on the same slot upon grab and/or release.

    Category: Transform/Interaction

    Attach to the same slot as a grabbable Component to utilize its
    features.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabTransformReset"

    def __init__(self, reset_position_on_grab: primitives.Bool | None = None, reset_rotation_on_grab: primitives.Bool | None = None, reset_scale_on_grab: primitives.Bool | None = None, reset_position_on_release: primitives.Bool | None = None, reset_rotation_on_release: primitives.Bool | None = None, reset_scale_on_release: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reset_position_on_grab: Initial value for ResetPositionOnGrab.
            reset_rotation_on_grab: Initial value for ResetRotationOnGrab.
            reset_scale_on_grab: Initial value for ResetScaleOnGrab.
            reset_position_on_release: Initial value for ResetPositionOnRelease.
            reset_rotation_on_release: Initial value for ResetRotationOnRelease.
            reset_scale_on_release: Initial value for ResetScaleOnRelease.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reset_position_on_grab is not None:
            self.reset_position_on_grab = reset_position_on_grab
        if reset_rotation_on_grab is not None:
            self.reset_rotation_on_grab = reset_rotation_on_grab
        if reset_scale_on_grab is not None:
            self.reset_scale_on_grab = reset_scale_on_grab
        if reset_position_on_release is not None:
            self.reset_position_on_release = reset_position_on_release
        if reset_rotation_on_release is not None:
            self.reset_rotation_on_release = reset_rotation_on_release
        if reset_scale_on_release is not None:
            self.reset_scale_on_release = reset_scale_on_release

    @property
    def reset_position_on_grab(self) -> primitives.Bool | None:
        """Whether to set the grabbable position to 0 on grab."""
        member = self.get_member("ResetPositionOnGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_position_on_grab.setter
    def reset_position_on_grab(self, value: primitives.Bool) -> None:
        """Set the ResetPositionOnGrab field value."""
        member = self.get_member("ResetPositionOnGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetPositionOnGrab", fields.FieldBool(value=value)
            )

    @property
    def reset_rotation_on_grab(self) -> primitives.Bool | None:
        """Whether to set the grabbable rotation to 0 on grab."""
        member = self.get_member("ResetRotationOnGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_rotation_on_grab.setter
    def reset_rotation_on_grab(self, value: primitives.Bool) -> None:
        """Set the ResetRotationOnGrab field value."""
        member = self.get_member("ResetRotationOnGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetRotationOnGrab", fields.FieldBool(value=value)
            )

    @property
    def reset_scale_on_grab(self) -> primitives.Bool | None:
        """Whether to set the grabbable scale to 1 on grab."""
        member = self.get_member("ResetScaleOnGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_scale_on_grab.setter
    def reset_scale_on_grab(self, value: primitives.Bool) -> None:
        """Set the ResetScaleOnGrab field value."""
        member = self.get_member("ResetScaleOnGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetScaleOnGrab", fields.FieldBool(value=value)
            )

    @property
    def reset_position_on_release(self) -> primitives.Bool | None:
        """Whether to set the grabbable position to 0 on release."""
        member = self.get_member("ResetPositionOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_position_on_release.setter
    def reset_position_on_release(self, value: primitives.Bool) -> None:
        """Set the ResetPositionOnRelease field value."""
        member = self.get_member("ResetPositionOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetPositionOnRelease", fields.FieldBool(value=value)
            )

    @property
    def reset_rotation_on_release(self) -> primitives.Bool | None:
        """Whether to set the grabbable rotation to 0 on release."""
        member = self.get_member("ResetRotationOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_rotation_on_release.setter
    def reset_rotation_on_release(self, value: primitives.Bool) -> None:
        """Set the ResetRotationOnRelease field value."""
        member = self.get_member("ResetRotationOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetRotationOnRelease", fields.FieldBool(value=value)
            )

    @property
    def reset_scale_on_release(self) -> primitives.Bool | None:
        """Whether to set the grabbable scale to 1 on release."""
        member = self.get_member("ResetScaleOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_scale_on_release.setter
    def reset_scale_on_release(self, value: primitives.Bool) -> None:
        """Set the ResetScaleOnRelease field value."""
        member = self.get_member("ResetScaleOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetScaleOnRelease", fields.FieldBool(value=value)
            )

