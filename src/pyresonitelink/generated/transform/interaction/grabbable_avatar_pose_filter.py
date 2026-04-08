"""Generated component: GrabbableAvatarPoseFilter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_pose_filter import IAvatarPoseFilter
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableAvatarPoseFilter(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbableAvatarPoseFilter.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableAvatarPoseFilter"

    def __init__(self, filter: str | IAvatarPoseFilter | None = None, priority: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            filter: Initial value for Filter.
            priority: Initial value for Priority.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if filter is not None:
            self.filter = filter
        if priority is not None:
            self.priority = priority

    @property
    def filter(self) -> str | None:
        """Target ID of the Filter reference (targets IAvatarPoseFilter)."""
        member = self.get_member("Filter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @filter.setter
    def filter(self, target: str | IAvatarPoseFilter | None) -> None:
        """Set the Filter reference by target ID or IAvatarPoseFilter instance."""
        target_id: str | None = target.id if isinstance(target, IAvatarPoseFilter) else target  # type: ignore[assignment]
        member = self.get_member("Filter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Filter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.IAvatarPoseFilter'),
            )

    @property
    def priority(self) -> np.int32 | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: np.int32) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

