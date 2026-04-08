"""Generated component: Glue."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Glue(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Glue.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Glue"

    def __init__(self, active: primitives.Bool | None = None, dry_time: primitives.Float | None = None, expire: primitives.Double | None = None, gluing_user: str | User | None = None, force_dry: primitives.Bool | None = None, is_drying: primitives.Bool | None = None, dry_start_time: primitives.Double | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            active: Initial value for Active.
            dry_time: Initial value for DryTime.
            expire: Initial value for Expire.
            gluing_user: Initial value for GluingUser.
            force_dry: Initial value for _forceDry.
            is_drying: Initial value for isDrying.
            dry_start_time: Initial value for dryStartTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if active is not None:
            self.active = active
        if dry_time is not None:
            self.dry_time = dry_time
        if expire is not None:
            self.expire = expire
        if gluing_user is not None:
            self.gluing_user = gluing_user
        if force_dry is not None:
            self.force_dry = force_dry
        if is_drying is not None:
            self.is_drying = is_drying
        if dry_start_time is not None:
            self.dry_start_time = dry_start_time

    @property
    def glue_mode(self) -> members.FieldEnum | None:
        """The GlueMode member."""
        member = self.get_member("GlueMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @glue_mode.setter
    def glue_mode(self, value: members.FieldEnum) -> None:
        """Set the GlueMode member."""
        self.set_member("GlueMode", value)

    @property
    def active(self) -> primitives.Bool | None:
        """The Active field value."""
        member = self.get_member("Active")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active.setter
    def active(self, value: primitives.Bool) -> None:
        """Set the Active field value."""
        member = self.get_member("Active")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Active", fields.FieldBool(value=value)
            )

    @property
    def dry_time(self) -> primitives.Float | None:
        """The DryTime field value."""
        member = self.get_member("DryTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dry_time.setter
    def dry_time(self, value: primitives.Float) -> None:
        """Set the DryTime field value."""
        member = self.get_member("DryTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DryTime", fields.FieldFloat(value=value)
            )

    @property
    def expire(self) -> primitives.Double | None:
        """The Expire field value."""
        member = self.get_member("Expire")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expire.setter
    def expire(self, value: primitives.Double) -> None:
        """Set the Expire field value."""
        member = self.get_member("Expire")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Expire", fields.FieldDouble(value=value)
            )

    @property
    def gluing_user(self) -> str | None:
        """Target ID of the GluingUser reference (targets User)."""
        member = self.get_member("GluingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gluing_user.setter
    def gluing_user(self, target: str | User | None) -> None:
        """Set the GluingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("GluingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GluingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def force_dry(self) -> primitives.Bool | None:
        """The _forceDry field value."""
        member = self.get_member("_forceDry")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_dry.setter
    def force_dry(self, value: primitives.Bool) -> None:
        """Set the _forceDry field value."""
        member = self.get_member("_forceDry")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_forceDry", fields.FieldBool(value=value)
            )

    @property
    def is_drying(self) -> primitives.Bool | None:
        """The isDrying field value."""
        member = self.get_member("isDrying")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_drying.setter
    def is_drying(self, value: primitives.Bool) -> None:
        """Set the isDrying field value."""
        member = self.get_member("isDrying")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "isDrying", fields.FieldBool(value=value)
            )

    @property
    def dry_start_time(self) -> primitives.Double | None:
        """The dryStartTime field value."""
        member = self.get_member("dryStartTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dry_start_time.setter
    def dry_start_time(self, value: primitives.Double) -> None:
        """Set the dryStartTime field value."""
        member = self.get_member("dryStartTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "dryStartTime", fields.FieldDouble(value=value)
            )

