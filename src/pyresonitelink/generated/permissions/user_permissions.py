"""Generated component: UserPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserPermissions"

    def __init__(self, allow_enable_edit_mode: primitives.Bool | None = None, allow_respawn: primitives.Bool | None = None, allow_silence: primitives.Bool | None = None, allow_kick: primitives.Bool | None = None, allow_ban: primitives.Bool | None = None, allow_assign_roles: primitives.Bool | None = None, allow_see_other_roles: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_enable_edit_mode: Initial value for AllowEnableEditMode.
            allow_respawn: Initial value for AllowRespawn.
            allow_silence: Initial value for AllowSilence.
            allow_kick: Initial value for AllowKick.
            allow_ban: Initial value for AllowBan.
            allow_assign_roles: Initial value for AllowAssignRoles.
            allow_see_other_roles: Initial value for AllowSeeOtherRoles.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_enable_edit_mode is not None:
            self.allow_enable_edit_mode = allow_enable_edit_mode
        if allow_respawn is not None:
            self.allow_respawn = allow_respawn
        if allow_silence is not None:
            self.allow_silence = allow_silence
        if allow_kick is not None:
            self.allow_kick = allow_kick
        if allow_ban is not None:
            self.allow_ban = allow_ban
        if allow_assign_roles is not None:
            self.allow_assign_roles = allow_assign_roles
        if allow_see_other_roles is not None:
            self.allow_see_other_roles = allow_see_other_roles

    @property
    def allow_enable_edit_mode(self) -> primitives.Bool | None:
        """The AllowEnableEditMode field value."""
        member = self.get_member("AllowEnableEditMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_enable_edit_mode.setter
    def allow_enable_edit_mode(self, value: primitives.Bool) -> None:
        """Set the AllowEnableEditMode field value."""
        member = self.get_member("AllowEnableEditMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowEnableEditMode", fields.FieldBool(value=value)
            )

    @property
    def allow_respawn(self) -> primitives.Bool | None:
        """The AllowRespawn field value."""
        member = self.get_member("AllowRespawn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_respawn.setter
    def allow_respawn(self, value: primitives.Bool) -> None:
        """Set the AllowRespawn field value."""
        member = self.get_member("AllowRespawn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowRespawn", fields.FieldBool(value=value)
            )

    @property
    def allow_silence(self) -> primitives.Bool | None:
        """The AllowSilence field value."""
        member = self.get_member("AllowSilence")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_silence.setter
    def allow_silence(self, value: primitives.Bool) -> None:
        """Set the AllowSilence field value."""
        member = self.get_member("AllowSilence")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSilence", fields.FieldBool(value=value)
            )

    @property
    def allow_kick(self) -> primitives.Bool | None:
        """The AllowKick field value."""
        member = self.get_member("AllowKick")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_kick.setter
    def allow_kick(self, value: primitives.Bool) -> None:
        """Set the AllowKick field value."""
        member = self.get_member("AllowKick")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowKick", fields.FieldBool(value=value)
            )

    @property
    def allow_ban(self) -> primitives.Bool | None:
        """The AllowBan field value."""
        member = self.get_member("AllowBan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_ban.setter
    def allow_ban(self, value: primitives.Bool) -> None:
        """Set the AllowBan field value."""
        member = self.get_member("AllowBan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowBan", fields.FieldBool(value=value)
            )

    @property
    def allow_assign_roles(self) -> primitives.Bool | None:
        """The AllowAssignRoles field value."""
        member = self.get_member("AllowAssignRoles")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_assign_roles.setter
    def allow_assign_roles(self, value: primitives.Bool) -> None:
        """Set the AllowAssignRoles field value."""
        member = self.get_member("AllowAssignRoles")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowAssignRoles", fields.FieldBool(value=value)
            )

    @property
    def allow_see_other_roles(self) -> primitives.Bool | None:
        """The AllowSeeOtherRoles field value."""
        member = self.get_member("AllowSeeOtherRoles")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_see_other_roles.setter
    def allow_see_other_roles(self, value: primitives.Bool) -> None:
        """Set the AllowSeeOtherRoles field value."""
        member = self.get_member("AllowSeeOtherRoles")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSeeOtherRoles", fields.FieldBool(value=value)
            )

