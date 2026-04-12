"""Generated component: AvatarAnchorLocomotionRelease."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAnchorLocomotionRelease(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """The AvatarAnchorLocomotionRelease Component is used so a user can get out of an anchor with their controller when they get into an anchor.

    Category: Users/Common Avatar System/Anchors

    Has to be used on the same slot as an AvatarAnchor or it doesn't do
    anything.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchorLocomotionRelease"

    def __init__(self, release_on_binary_action: primitives.Bool | None = None, release_strength_threshold: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
    def release_on_binary_action(self) -> primitives.Bool | None:
        """Whether to allow the user to jump out of the anchor"""
        member = self.get_member("ReleaseOnBinaryAction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_on_binary_action.setter
    def release_on_binary_action(self, value: primitives.Bool) -> None:
        """Set the ReleaseOnBinaryAction field value."""
        member = self.get_member("ReleaseOnBinaryAction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleaseOnBinaryAction", fields.FieldBool(value=value)
            )

    @property
    def release_strength_threshold(self) -> primitives.Float | None:
        """The amount of pressing strength on the jump button needed to get out if not null."""
        member = self.get_member("ReleaseStrengthThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_strength_threshold.setter
    def release_strength_threshold(self, value: primitives.Float) -> None:
        """Set the ReleaseStrengthThreshold field value."""
        member = self.get_member("ReleaseStrengthThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleaseStrengthThreshold", fields.FieldNullableFloat(value=value)
            )

