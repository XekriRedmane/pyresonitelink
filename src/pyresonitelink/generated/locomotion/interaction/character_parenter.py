"""Generated component: CharacterParenter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterParenter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Character Parenters are a component that allow for parenting or aligning the gravity of a user when they hit a collider.

    Category: Locomotion/Interaction

    **Behavior**: Disabling the collider the CharacterParenter is connected to might be preferred compared to disabling the slot or the CharacterParenter's enabled state itself, as disabling the collider will throw a ContactEnd event to the CharacterPareneter and correctly de-parent the user's inside. 

Disabling the CharacterParenter itself while users are inside the ParentSpace will mean the component can't de-parent users correctly and might not be wanted behavior.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterParenter"

    def __init__(self, triggers_only: primitives.Bool | None = None, nest_into_space: primitives.Bool | None = None, must_be_on_ground: primitives.Bool | None = None, ignore_parent_user: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def triggers_only(self) -> primitives.Bool | None:
        """Whether to only allow trigger colliders that are part of this component's slot hierarchy to activate parenting."""
        member = self.get_member("TriggersOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triggers_only.setter
    def triggers_only(self, value: primitives.Bool) -> None:
        """Set the TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriggersOnly", fields.FieldBool(value=value)
            )

    @property
    def nest_into_space(self) -> primitives.Bool | None:
        """Parent the user into the slot ``ParentSpace`` or not."""
        member = self.get_member("NestIntoSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @nest_into_space.setter
    def nest_into_space(self, value: primitives.Bool) -> None:
        """Set the NestIntoSpace field value."""
        member = self.get_member("NestIntoSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NestIntoSpace", fields.FieldBool(value=value)
            )

    @property
    def must_be_on_ground(self) -> primitives.Bool | None:
        """The user must be on the ground according to the character controller before they will be aligned/parented."""
        member = self.get_member("MustBeOnGround")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @must_be_on_ground.setter
    def must_be_on_ground(self, value: primitives.Bool) -> None:
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
        """What directions a user must be aligned to relative to the slot this component is on for them to get parented."""
        member = self.get_member("Filters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @filters.setter
    def filters(self, value: members.SyncList) -> None:
        """Set Filters. What directions a user must be aligned to relative to the slot this component is on for them to get parented."""
        self.set_member("Filters", value)

    @property
    def ignore_parent_user(self) -> primitives.Bool | None:
        """Ignore the active user of this component when attempting to parent a user."""
        member = self.get_member("IgnoreParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_parent_user.setter
    def ignore_parent_user(self, value: primitives.Bool) -> None:
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
        """The coordinate space that calculations should be done in."""
        member = self.get_member("ParentSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @parent_space.setter
    def parent_space(self, value: members.SyncObject) -> None:
        """Set ParentSpace. The coordinate space that calculations should be done in."""
        self.set_member("ParentSpace", value)

