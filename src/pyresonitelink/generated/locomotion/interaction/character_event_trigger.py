"""Generated component: CharacterEventTrigger."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterEventTrigger(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The CharacterEventTrigger component invokes Action triggers whenever a user enters or exits an attached collider.

    Category: Locomotion/Interaction

    **Behavior**: == Examples ==
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterEventTrigger"

    def __init__(self, triggers_only: primitives.Bool | None = None, ignore_parent_user: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            ignore_parent_user: Initial value for IgnoreParentUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only
        if ignore_parent_user is not None:
            self.ignore_parent_user = ignore_parent_user

    @property
    def triggers_only(self) -> primitives.Bool | None:
        """Whether to only use Trigger type colliders on this hierarchy when detecting character collisions."""
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
    def ignore_parent_user(self) -> primitives.Bool | None:
        """If this component is under a user in the hierarchy, events from that user are ignored."""
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

