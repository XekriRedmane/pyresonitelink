"""Generated component: LocomotionPermissions."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionPermissions"

    def __init__(self, min_scale: np.float32 | None = None, max_scale: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale

    @property
    def locomotion_list_mode(self) -> members.FieldEnum | None:
        """The LocomotionListMode member."""
        member = self.get_member("LocomotionListMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @locomotion_list_mode.setter
    def locomotion_list_mode(self, value: members.FieldEnum) -> None:
        """Set the LocomotionListMode member."""
        self.set_member("LocomotionListMode", value)

    @property
    def locomotions(self) -> members.SyncList | None:
        """The Locomotions member."""
        member = self.get_member("Locomotions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @locomotions.setter
    def locomotions(self, value: members.SyncList) -> None:
        """Set the Locomotions member."""
        self.set_member("Locomotions", value)

    @property
    def scaling(self) -> members.FieldEnum | None:
        """The Scaling member."""
        member = self.get_member("Scaling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @scaling.setter
    def scaling(self, value: members.FieldEnum) -> None:
        """Set the Scaling member."""
        self.set_member("Scaling", value)

    @property
    def min_scale(self) -> np.float32 | None:
        """The MinScale field value."""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: np.float32) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat(value=value)
            )

    @property
    def max_scale(self) -> np.float32 | None:
        """The MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: np.float32) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat(value=value)
            )

    @property
    def jump_to_user(self) -> members.FieldEnum | None:
        """The JumpToUser member."""
        member = self.get_member("JumpToUser")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @jump_to_user.setter
    def jump_to_user(self, value: members.FieldEnum) -> None:
        """Set the JumpToUser member."""
        self.set_member("JumpToUser", value)

