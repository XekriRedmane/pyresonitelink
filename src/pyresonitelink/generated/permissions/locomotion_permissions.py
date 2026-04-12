"""Generated component: LocomotionPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.list_filter_mode import ListFilterMode
from pyresonitelink.generated._enums.permission_state import PermissionState
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The LocomotionPermissions component allows you to control what locomotions users can use in your world.

    Category: Permissions

    **Introduction**: The LocomotionPermissions component allows you to control what locomotions users can use in your world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionPermissions"

    def __init__(self, locomotion_list_mode: ListFilterMode | str | None = None, scaling: PermissionState | str | None = None, min_scale: primitives.Float | None = None, max_scale: primitives.Float | None = None, jump_to_user: PermissionState | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            locomotion_list_mode: Initial value for LocomotionListMode.
            scaling: Initial value for Scaling.
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            jump_to_user: Initial value for JumpToUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if locomotion_list_mode is not None:
            self.locomotion_list_mode = locomotion_list_mode
        if scaling is not None:
            self.scaling = scaling
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if jump_to_user is not None:
            self.jump_to_user = jump_to_user

    @property
    def locomotion_list_mode(self) -> ListFilterMode | None:
        """Whether to blacklist or whitelist the ``Locomotions``."""
        member = self.get_member("LocomotionListMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ListFilterMode(member.value)
        return None

    @locomotion_list_mode.setter
    def locomotion_list_mode(self, value: ListFilterMode | str) -> None:
        """Set LocomotionListMode. Whether to blacklist or whitelist the ``Locomotions``."""
        member = self.get_member("LocomotionListMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "LocomotionListMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def locomotions(self) -> members.SyncList | None:
        """List of ``Locomotions`` to blacklist/whitelist."""
        member = self.get_member("Locomotions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @locomotions.setter
    def locomotions(self, value: members.SyncList) -> None:
        """Set Locomotions. List of ``Locomotions`` to blacklist/whitelist."""
        self.set_member("Locomotions", value)

    @property
    def scaling(self) -> PermissionState | None:
        """Whether self scale is Disallowed, Allowed, or Edit Mode Only."""
        member = self.get_member("Scaling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PermissionState(member.value)
        return None

    @scaling.setter
    def scaling(self, value: PermissionState | str) -> None:
        """Set Scaling. Whether self scale is Disallowed, Allowed, or Edit Mode Only."""
        member = self.get_member("Scaling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Scaling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_scale(self) -> primitives.Float | None:
        """Minimum scale"""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: primitives.Float) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat(value=value)
            )

    @property
    def max_scale(self) -> primitives.Float | None:
        """Maximum scale"""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: primitives.Float) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat(value=value)
            )

    @property
    def jump_to_user(self) -> PermissionState | None:
        """Whether jumping to users is Disallowed, Allowed, or Edit Mode Only."""
        member = self.get_member("JumpToUser")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PermissionState(member.value)
        return None

    @jump_to_user.setter
    def jump_to_user(self, value: PermissionState | str) -> None:
        """Set JumpToUser. Whether jumping to users is Disallowed, Allowed, or Edit Mode Only."""
        member = self.get_member("JumpToUser")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "JumpToUser",
                members.FieldEnum(value=str(value)),
            )

