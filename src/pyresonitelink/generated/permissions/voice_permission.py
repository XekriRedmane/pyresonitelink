"""Generated component: VoicePermission."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.voice_mode import VoiceMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VoicePermission(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The VoicePermission component changes the allowed voice modes for users with the selected roles in a world.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VoicePermission"

    def __init__(self, max_allowed_voice_mode: VoiceMode | str | None = None, allow_change_other_users: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_allowed_voice_mode: Initial value for MaxAllowedVoiceMode.
            allow_change_other_users: Initial value for AllowChangeOtherUsers.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_allowed_voice_mode is not None:
            self.max_allowed_voice_mode = max_allowed_voice_mode
        if allow_change_other_users is not None:
            self.allow_change_other_users = allow_change_other_users

    @property
    def max_allowed_voice_mode(self) -> VoiceMode | None:
        """The maximum allowed voice mode allowed for the selected roles."""
        member = self.get_member("MaxAllowedVoiceMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VoiceMode(member.value)
        return None

    @max_allowed_voice_mode.setter
    def max_allowed_voice_mode(self, value: VoiceMode | str) -> None:
        """Set MaxAllowedVoiceMode. The maximum allowed voice mode allowed for the selected roles."""
        member = self.get_member("MaxAllowedVoiceMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MaxAllowedVoiceMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def allow_change_other_users(self) -> primitives.Bool | None:
        """Whether the selected roles are allowed to change the voice mode of other users mainly through the User Inspector."""
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

