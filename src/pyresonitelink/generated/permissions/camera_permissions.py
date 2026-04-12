"""Generated component: CameraPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.list_filter_mode import ListFilterMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CameraPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The Camera Permissions component allows you to set up who can use certain camera modes on the streaming camera. Currently, the component allows setting permissions for camera modes per role.

    Category: Permissions

    First, add an item to the list of camera modes, and select a role at the
    bottom. Then, use ``CameraModeFilterMode`` to determine if users can use
    any of the items in the list of camera modes.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CameraPermissions"

    def __init__(self, camera_mode_filter_mode: ListFilterMode | str | None = None, allow_framing_other_users: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            camera_mode_filter_mode: Initial value for CameraModeFilterMode.
            allow_framing_other_users: Initial value for AllowFramingOtherUsers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if camera_mode_filter_mode is not None:
            self.camera_mode_filter_mode = camera_mode_filter_mode
        if allow_framing_other_users is not None:
            self.allow_framing_other_users = allow_framing_other_users

    @property
    def camera_mode_filter_mode(self) -> ListFilterMode | None:
        """Whether to allow or disallow the ``CameraModes``"""
        member = self.get_member("CameraModeFilterMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ListFilterMode(member.value)
        return None

    @camera_mode_filter_mode.setter
    def camera_mode_filter_mode(self, value: ListFilterMode | str) -> None:
        """Set CameraModeFilterMode. Whether to allow or disallow the ``CameraModes``"""
        member = self.get_member("CameraModeFilterMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CameraModeFilterMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def camera_modes(self) -> members.SyncList | None:
        """List of Camera modes which decide how a stream camera can look at users and/or the world."""
        member = self.get_member("CameraModes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @camera_modes.setter
    def camera_modes(self, value: members.SyncList) -> None:
        """Set CameraModes. List of Camera modes which decide how a stream camera can look at users and/or the world."""
        self.set_member("CameraModes", value)

    @property
    def allow_framing_other_users(self) -> primitives.Bool | None:
        """Determines whether focusing the camera on other user is allowed."""
        member = self.get_member("AllowFramingOtherUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_framing_other_users.setter
    def allow_framing_other_users(self, value: primitives.Bool) -> None:
        """Set the AllowFramingOtherUsers field value."""
        member = self.get_member("AllowFramingOtherUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowFramingOtherUsers", fields.FieldBool(value=value)
            )

