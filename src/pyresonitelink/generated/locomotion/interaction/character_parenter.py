"""Generated component: CharacterParenter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterParenter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CharacterParenter.

    Category: Locomotion/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterParenter"

    def __init__(self, triggers_only: bool | None = None, nest_into_space: bool | None = None, must_be_on_ground: bool | None = None, ignore_parent_user: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            nest_into_space: Initial value for NestIntoSpace.
            must_be_on_ground: Initial value for MustBeOnGround.
            ignore_parent_user: Initial value for IgnoreParentUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only
        if nest_into_space is not None:
            self.nest_into_space = nest_into_space
        if must_be_on_ground is not None:
            self.must_be_on_ground = must_be_on_ground
        if ignore_parent_user is not None:
            self.ignore_parent_user = ignore_parent_user

    @property
    def triggers_only(self) -> bool | None:
        """The TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triggers_only.setter
    def triggers_only(self, value: bool) -> None:
        """Set the TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriggersOnly", fields.FieldBool(value=value)
            )

    @property
    def nest_into_space(self) -> bool | None:
        """The NestIntoSpace field value."""
        member = self.get_member("NestIntoSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @nest_into_space.setter
    def nest_into_space(self, value: bool) -> None:
        """Set the NestIntoSpace field value."""
        member = self.get_member("NestIntoSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NestIntoSpace", fields.FieldBool(value=value)
            )

    @property
    def must_be_on_ground(self) -> bool | None:
        """The MustBeOnGround field value."""
        member = self.get_member("MustBeOnGround")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @must_be_on_ground.setter
    def must_be_on_ground(self, value: bool) -> None:
        """Set the MustBeOnGround field value."""
        member = self.get_member("MustBeOnGround")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MustBeOnGround", fields.FieldBool(value=value)
            )

    @property
    def filters(self) -> members.SyncList | None:
        """The Filters member."""
        member = self.get_member("Filters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @filters.setter
    def filters(self, value: members.SyncList) -> None:
        """Set the Filters member."""
        self.set_member("Filters", value)

    @property
    def ignore_parent_user(self) -> bool | None:
        """The IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_parent_user.setter
    def ignore_parent_user(self, value: bool) -> None:
        """Set the IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreParentUser", fields.FieldBool(value=value)
            )

    @property
    def parent_space(self) -> members.SyncObject | None:
        """The ParentSpace member."""
        member = self.get_member("ParentSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @parent_space.setter
    def parent_space(self, value: members.SyncObject) -> None:
        """Set the ParentSpace member."""
        self.set_member("ParentSpace", value)

