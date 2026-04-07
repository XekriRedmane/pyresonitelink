"""Generated component: GrabbableReceiverSurface."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrabbable_receiver import IGrabbableReceiver
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableReceiverSurface(GeneratedComponent, IGrabbableReceiver, IGrabbableReparentBlock, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbableReceiverSurface.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableReceiverSurface"

    def __init__(self, parent_placed: bool | None = None, override_parent: str | Slot | None = None, tween_time: np.float32 | None = None, max_distance: np.float32 | None = None, offset: np.float32 | None = None, check_offset: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_placed: Initial value for ParentPlaced.
            override_parent: Initial value for OverrideParent.
            tween_time: Initial value for TweenTime.
            max_distance: Initial value for MaxDistance.
            offset: Initial value for Offset.
            check_offset: Initial value for CheckOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parent_placed is not None:
            self.parent_placed = parent_placed
        if override_parent is not None:
            self.override_parent = override_parent
        if tween_time is not None:
            self.tween_time = tween_time
        if max_distance is not None:
            self.max_distance = max_distance
        if offset is not None:
            self.offset = offset
        if check_offset is not None:
            self.check_offset = check_offset

    @property
    def parent_placed(self) -> bool | None:
        """The ParentPlaced field value."""
        member = self.get_member("ParentPlaced")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_placed.setter
    def parent_placed(self, value: bool) -> None:
        """Set the ParentPlaced field value."""
        member = self.get_member("ParentPlaced")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentPlaced", fields.FieldBool(value=value)
            )

    @property
    def override_parent(self) -> str | None:
        """Target ID of the OverrideParent reference (targets Slot)."""
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_parent.setter
    def override_parent(self, target: str | Slot | None) -> None:
        """Set the OverrideParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def tween_time(self) -> np.float32 | None:
        """The TweenTime field value."""
        member = self.get_member("TweenTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tween_time.setter
    def tween_time(self, value: np.float32) -> None:
        """Set the TweenTime field value."""
        member = self.get_member("TweenTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TweenTime", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> np.float32 | None:
        """The MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: np.float32) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> np.float32 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: np.float32) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def check_offset(self) -> np.float32 | None:
        """The CheckOffset field value."""
        member = self.get_member("CheckOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @check_offset.setter
    def check_offset(self, value: np.float32) -> None:
        """Set the CheckOffset field value."""
        member = self.get_member("CheckOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheckOffset", fields.FieldFloat(value=value)
            )

    @property
    def directions(self) -> members.SyncList | None:
        """The Directions member."""
        member = self.get_member("Directions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @directions.setter
    def directions(self, value: members.SyncList) -> None:
        """Set the Directions member."""
        self.set_member("Directions", value)

    @property
    def tag_filter(self) -> members.SyncObject | None:
        """The TagFilter member."""
        member = self.get_member("TagFilter")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @tag_filter.setter
    def tag_filter(self, value: members.SyncObject) -> None:
        """Set the TagFilter member."""
        self.set_member("TagFilter", value)

