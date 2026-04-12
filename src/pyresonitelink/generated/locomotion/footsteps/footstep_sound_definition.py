"""Generated component: FootstepSoundDefinition."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifootstep_sound_material import IFootstepSoundMaterial
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepSoundDefinition(GeneratedComponent, IFootstepSoundMaterial, IWorldEventReceiver):
    """The FootstepSoundDefinition component can be referenced by other components which can trigger this to play noise during footstep events.

    Category: Locomotion/Footsteps

    Used to play sound when footsteps happen on surfaces or it receives a
    footstep event.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FootstepSoundDefinition"

    def __init__(self, parent_under: str | Slot | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_under: Initial value for ParentUnder.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parent_under is not None:
            self.parent_under = parent_under
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance

    @property
    def parent_under(self) -> str | None:
        """The slot to parent played sounds under."""
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_under.setter
    def parent_under(self, target: str | Slot | None) -> None:
        """Set the ParentUnder reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def min_distance(self) -> primitives.Float | None:
        """The minimum distance the audio can be heard from before playing at maximum amount."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: primitives.Float) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldNullableFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """The max distance before the audio cannot be heard anymore."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldNullableFloat(value=value)
            )

    @property
    def rolloff_mode(self) -> members.FieldEnum | None:
        """How played audio should fall off based on distance."""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rolloff_mode.setter
    def rolloff_mode(self, value: members.FieldEnum) -> None:
        """Set RolloffMode. How played audio should fall off based on distance."""
        self.set_member("RolloffMode", value)

    @property
    def clips(self) -> members.SyncList | None:
        """Different footsteps that can play when this component is triggered"""
        member = self.get_member("Clips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @clips.setter
    def clips(self, value: members.SyncList) -> None:
        """Set Clips. Different footsteps that can play when this component is triggered"""
        self.set_member("Clips", value)

