"""Generated component: Comment."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Comment(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Comment is a component that allows you to store text for another person using an inspector, ex: another content creator. This is useful for explaining what a slot is for or does.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Comment"

    def __init__(self, text: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text: Initial value for Text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text is not None:
            self.text = text

    @property
    def text(self) -> primitives.String | None:
        """The text to store for others to see when in an inspector"""
        member = self.get_member("Text")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @text.setter
    def text(self, value: primitives.String) -> None:
        """Set the Text field value."""
        member = self.get_member("Text")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Text", fields.FieldString(value=value)
            )

