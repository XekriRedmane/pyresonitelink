"""Generated component: VoicePermission."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VoicePermission(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VoicePermission.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VoicePermission"

    def __init__(self, allow_change_other_users: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_change_other_users: Initial value for AllowChangeOtherUsers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_change_other_users is not None:
            self.allow_change_other_users = allow_change_other_users

    @property
    def max_allowed_voice_mode(self) -> members.FieldEnum | None:
        """The MaxAllowedVoiceMode member."""
        member = self.get_member("MaxAllowedVoiceMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @max_allowed_voice_mode.setter
    def max_allowed_voice_mode(self, value: members.FieldEnum) -> None:
        """Set the MaxAllowedVoiceMode member."""
        self.set_member("MaxAllowedVoiceMode", value)

    @property
    def allow_change_other_users(self) -> primitives.Bool | None:
        """The AllowChangeOtherUsers field value."""
        member = self.get_member("AllowChangeOtherUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_change_other_users.setter
    def allow_change_other_users(self, value: primitives.Bool) -> None:
        """Set the AllowChangeOtherUsers field value."""
        member = self.get_member("AllowChangeOtherUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowChangeOtherUsers", fields.FieldBool(value=value)
            )

