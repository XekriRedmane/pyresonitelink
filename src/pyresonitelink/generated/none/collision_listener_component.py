"""Generated component: CollisionListenerComponent."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CollisionListenerComponent(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CollisionListenerComponent.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CollisionListenerComponent"

    def __init__(self, triggers_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only

    @property
    def triggers_only(self) -> primitives.Bool | None:
        """The TriggersOnly field value."""
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

