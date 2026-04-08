"""Generated component: MissingComponent."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MissingComponent(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MissingComponent.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MissingComponent"

    def __init__(self, type_: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            type_: Initial value for Type.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if type_ is not None:
            self.type_ = type_

    @property
    def type_(self) -> primitives.String | None:
        """The Type field value."""
        member = self.get_member("Type")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @type_.setter
    def type_(self, value: primitives.String) -> None:
        """Set the Type field value."""
        member = self.get_member("Type")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Type", fields.FieldString(value=value)
            )

