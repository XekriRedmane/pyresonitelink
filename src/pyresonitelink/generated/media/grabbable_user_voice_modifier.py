"""Generated component: GrabbableUserVoiceModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableUserVoiceModifier(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbableUserVoiceModifier.

    Category: Media
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableUserVoiceModifier"

    def __init__(self, original_enabled: primitives.Bool | None = None, original_spatialize: primitives.Bool | None = None, original_spatial_blend: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            original_enabled: Initial value for _originalEnabled.
            original_spatialize: Initial value for _originalSpatialize.
            original_spatial_blend: Initial value for _originalSpatialBlend.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if original_enabled is not None:
            self.original_enabled = original_enabled
        if original_spatialize is not None:
            self.original_spatialize = original_spatialize
        if original_spatial_blend is not None:
            self.original_spatial_blend = original_spatial_blend

    @property
    def state_on_grabbed(self) -> members.FieldEnum | None:
        """The StateOnGrabbed member."""
        member = self.get_member("StateOnGrabbed")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @state_on_grabbed.setter
    def state_on_grabbed(self, value: members.FieldEnum) -> None:
        """Set the StateOnGrabbed member."""
        self.set_member("StateOnGrabbed", value)

    @property
    def state_on_released(self) -> members.FieldEnum | None:
        """The StateOnReleased member."""
        member = self.get_member("StateOnReleased")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @state_on_released.setter
    def state_on_released(self, value: members.FieldEnum) -> None:
        """Set the StateOnReleased member."""
        self.set_member("StateOnReleased", value)

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

