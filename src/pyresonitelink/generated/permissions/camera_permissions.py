"""Generated component: CameraPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CameraPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CameraPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CameraPermissions"

    def __init__(self, allow_framing_other_users: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_framing_other_users: Initial value for AllowFramingOtherUsers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_framing_other_users is not None:
            self.allow_framing_other_users = allow_framing_other_users

    @property
    def camera_mode_filter_mode(self) -> members.FieldEnum | None:
        """The CameraModeFilterMode member."""
        member = self.get_member("CameraModeFilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @camera_mode_filter_mode.setter
    def camera_mode_filter_mode(self, value: members.FieldEnum) -> None:
        """Set the CameraModeFilterMode member."""
        self.set_member("CameraModeFilterMode", value)

    @property
    def camera_modes(self) -> members.SyncList | None:
        """The CameraModes member."""
        member = self.get_member("CameraModes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @camera_modes.setter
    def camera_modes(self, value: members.SyncList) -> None:
        """Set the CameraModes member."""
        self.set_member("CameraModes", value)

    @property
    def allow_framing_other_users(self) -> bool | None:
        """The AllowFramingOtherUsers field value."""
        member = self.get_member("AllowFramingOtherUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_framing_other_users.setter
    def allow_framing_other_users(self, value: bool) -> None:
        """Set the AllowFramingOtherUsers field value."""
        member = self.get_member("AllowFramingOtherUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowFramingOtherUsers", fields.FieldBool(value=value)
            )

