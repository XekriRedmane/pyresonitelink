"""Generated component: GrabbableUserVoiceModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.voice_state import VoiceState
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableUserVoiceModifier(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """Frooxius commented on May 27, 2020
Hmm, this component is technically deprecated with the voice switching system and it will have to be redesigned. It works by modifying the voice AudioOutput on the user, but with the introduction of the voice controls those now control the user's voice.

This component isn't usable now. and try AudioOutput instead.

    Category: Media
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableUserVoiceModifier"

    def __init__(self, state_on_grabbed: VoiceState | str | None = None, state_on_released: VoiceState | str | None = None, original_enabled: primitives.Bool | None = None, original_spatialize: primitives.Bool | None = None, original_spatial_blend: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            state_on_grabbed: Initial value for StateOnGrabbed.
            state_on_released: Initial value for StateOnReleased.
            original_enabled: Initial value for _originalEnabled.
            original_spatialize: Initial value for _originalSpatialize.
            original_spatial_blend: Initial value for _originalSpatialBlend.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if state_on_grabbed is not None:
            self.state_on_grabbed = state_on_grabbed
        if state_on_released is not None:
            self.state_on_released = state_on_released
        if original_enabled is not None:
            self.original_enabled = original_enabled
        if original_spatialize is not None:
            self.original_spatialize = original_spatialize
        if original_spatial_blend is not None:
            self.original_spatial_blend = original_spatial_blend

    @property
    def state_on_grabbed(self) -> VoiceState | None:
        """The StateOnGrabbed enum value."""
        member = self.get_member("StateOnGrabbed")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VoiceState(member.value)
        return None

    @state_on_grabbed.setter
    def state_on_grabbed(self, value: VoiceState | str) -> None:
        """Set the StateOnGrabbed enum value."""
        member = self.get_member("StateOnGrabbed")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "StateOnGrabbed",
                members.FieldEnum(value=str(value)),
            )

    @property
    def state_on_released(self) -> VoiceState | None:
        """The StateOnReleased enum value."""
        member = self.get_member("StateOnReleased")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VoiceState(member.value)
        return None

    @state_on_released.setter
    def state_on_released(self, value: VoiceState | str) -> None:
        """Set the StateOnReleased enum value."""
        member = self.get_member("StateOnReleased")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "StateOnReleased",
                members.FieldEnum(value=str(value)),
            )

    @property
    def original_enabled(self) -> primitives.Bool | None:
        """The _originalEnabled field value."""
        member = self.get_member("_originalEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_enabled.setter
    def original_enabled(self, value: primitives.Bool) -> None:
        """Set the _originalEnabled field value."""
        member = self.get_member("_originalEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalEnabled", fields.FieldBool(value=value)
            )

    @property
    def original_spatialize(self) -> primitives.Bool | None:
        """The _originalSpatialize field value."""
        member = self.get_member("_originalSpatialize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_spatialize.setter
    def original_spatialize(self, value: primitives.Bool) -> None:
        """Set the _originalSpatialize field value."""
        member = self.get_member("_originalSpatialize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalSpatialize", fields.FieldBool(value=value)
            )

    @property
    def original_spatial_blend(self) -> primitives.Float | None:
        """The _originalSpatialBlend field value."""
        member = self.get_member("_originalSpatialBlend")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_spatial_blend.setter
    def original_spatial_blend(self, value: primitives.Float) -> None:
        """Set the _originalSpatialBlend field value."""
        member = self.get_member("_originalSpatialBlend")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalSpatialBlend", fields.FieldFloat(value=value)
            )

