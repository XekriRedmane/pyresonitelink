"""Generated component: Consumable."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Consumable(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Consumable.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Consumable"

    def __init__(self, must_be_holding: bool | None = None, can_feed_to_others: bool | None = None, override_reference_point: str | Slot | None = None, radius: np.float32 | None = None, start_hysteresis: np.float32 | None = None, current_stage_index: np.int32 | None = None, destroy_on_consumed: bool | None = None, waiting_for_reset: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            must_be_holding: Initial value for MustBeHolding.
            can_feed_to_others: Initial value for CanFeedToOthers.
            override_reference_point: Initial value for OverrideReferencePoint.
            radius: Initial value for Radius.
            start_hysteresis: Initial value for StartHysteresis.
            current_stage_index: Initial value for CurrentStageIndex.
            destroy_on_consumed: Initial value for DestroyOnConsumed.
            waiting_for_reset: Initial value for _waitingForReset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if must_be_holding is not None:
            self.must_be_holding = must_be_holding
        if can_feed_to_others is not None:
            self.can_feed_to_others = can_feed_to_others
        if override_reference_point is not None:
            self.override_reference_point = override_reference_point
        if radius is not None:
            self.radius = radius
        if start_hysteresis is not None:
            self.start_hysteresis = start_hysteresis
        if current_stage_index is not None:
            self.current_stage_index = current_stage_index
        if destroy_on_consumed is not None:
            self.destroy_on_consumed = destroy_on_consumed
        if waiting_for_reset is not None:
            self.waiting_for_reset = waiting_for_reset

    @property
    def must_be_holding(self) -> bool | None:
        """The MustBeHolding field value."""
        member = self.get_member("MustBeHolding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @must_be_holding.setter
    def must_be_holding(self, value: bool) -> None:
        """Set the MustBeHolding field value."""
        member = self.get_member("MustBeHolding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MustBeHolding", fields.FieldBool(value=value)
            )

    @property
    def can_feed_to_others(self) -> bool | None:
        """The CanFeedToOthers field value."""
        member = self.get_member("CanFeedToOthers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_feed_to_others.setter
    def can_feed_to_others(self, value: bool) -> None:
        """Set the CanFeedToOthers field value."""
        member = self.get_member("CanFeedToOthers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CanFeedToOthers", fields.FieldBool(value=value)
            )

    @property
    def override_reference_point(self) -> str | None:
        """Target ID of the OverrideReferencePoint reference (targets Slot)."""
        member = self.get_member("OverrideReferencePoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_reference_point.setter
    def override_reference_point(self, target: str | Slot | None) -> None:
        """Set the OverrideReferencePoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideReferencePoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideReferencePoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def start_hysteresis(self) -> np.float32 | None:
        """The StartHysteresis field value."""
        member = self.get_member("StartHysteresis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_hysteresis.setter
    def start_hysteresis(self, value: np.float32) -> None:
        """Set the StartHysteresis field value."""
        member = self.get_member("StartHysteresis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartHysteresis", fields.FieldFloat(value=value)
            )

    @property
    def current_stage_index(self) -> np.int32 | None:
        """The CurrentStageIndex field value."""
        member = self.get_member("CurrentStageIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_stage_index.setter
    def current_stage_index(self, value: np.int32) -> None:
        """Set the CurrentStageIndex field value."""
        member = self.get_member("CurrentStageIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentStageIndex", fields.FieldInt(value=value)
            )

    @property
    def is_being_consumed(self) -> members.EmptyElement | None:
        """The IsBeingConsumed member."""
        member = self.get_member("IsBeingConsumed")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_being_consumed.setter
    def is_being_consumed(self, value: members.EmptyElement) -> None:
        """Set the IsBeingConsumed member."""
        self.set_member("IsBeingConsumed", value)

    @property
    def has_been_fully_consumed(self) -> members.EmptyElement | None:
        """The HasBeenFullyConsumed member."""
        member = self.get_member("HasBeenFullyConsumed")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_been_fully_consumed.setter
    def has_been_fully_consumed(self, value: members.EmptyElement) -> None:
        """Set the HasBeenFullyConsumed member."""
        self.set_member("HasBeenFullyConsumed", value)

    @property
    def currently_consuming_user(self) -> members.SyncObject | None:
        """The CurrentlyConsumingUser member."""
        member = self.get_member("CurrentlyConsumingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @currently_consuming_user.setter
    def currently_consuming_user(self, value: members.SyncObject) -> None:
        """Set the CurrentlyConsumingUser member."""
        self.set_member("CurrentlyConsumingUser", value)

    @property
    def destroy_on_consumed(self) -> bool | None:
        """The DestroyOnConsumed field value."""
        member = self.get_member("DestroyOnConsumed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @destroy_on_consumed.setter
    def destroy_on_consumed(self, value: bool) -> None:
        """Set the DestroyOnConsumed field value."""
        member = self.get_member("DestroyOnConsumed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DestroyOnConsumed", fields.FieldBool(value=value)
            )

    @property
    def stages(self) -> members.SyncList | None:
        """The Stages member."""
        member = self.get_member("Stages")
        if isinstance(member, members.SyncList):
            return member
        return None

    @stages.setter
    def stages(self, value: members.SyncList) -> None:
        """Set the Stages member."""
        self.set_member("Stages", value)

    @property
    def waiting_for_reset(self) -> bool | None:
        """The _waitingForReset field value."""
        member = self.get_member("_waitingForReset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @waiting_for_reset.setter
    def waiting_for_reset(self, value: bool) -> None:
        """Set the _waitingForReset field value."""
        member = self.get_member("_waitingForReset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_waitingForReset", fields.FieldBool(value=value)
            )

    @property
    def on_any_stage_consumed(self) -> members.SyncList | None:
        """The OnAnyStageConsumed member."""
        member = self.get_member("OnAnyStageConsumed")
        if isinstance(member, members.SyncList):
            return member
        return None

    @on_any_stage_consumed.setter
    def on_any_stage_consumed(self, value: members.SyncList) -> None:
        """Set the OnAnyStageConsumed member."""
        self.set_member("OnAnyStageConsumed", value)

    @property
    def on_fully_consumed(self) -> members.SyncList | None:
        """The OnFullyConsumed member."""
        member = self.get_member("OnFullyConsumed")
        if isinstance(member, members.SyncList):
            return member
        return None

    @on_fully_consumed.setter
    def on_fully_consumed(self, value: members.SyncList) -> None:
        """Set the OnFullyConsumed member."""
        self.set_member("OnFullyConsumed", value)

