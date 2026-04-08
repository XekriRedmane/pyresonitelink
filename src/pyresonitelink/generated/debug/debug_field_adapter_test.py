"""Generated component: DebugFieldAdapterTest."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugFieldAdapterTest(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugFieldAdapterTest.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugFieldAdapterTest"

    def __init__(self, inverted_color: primitives.ColorX | None = None, source_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            inverted_color: Initial value for InvertedColor.
            source_color: Initial value for SourceColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if inverted_color is not None:
            self.inverted_color = inverted_color
        if source_color is not None:
            self.source_color = source_color

    @property
    def inverted_color(self) -> primitives.ColorX | None:
        """The InvertedColor field value."""
        member = self.get_member("InvertedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inverted_color.setter
    def inverted_color(self, value: primitives.ColorX) -> None:
        """Set the InvertedColor field value."""
        member = self.get_member("InvertedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InvertedColor", fields.FieldColorX(value=value)
            )

    @property
    def source_color(self) -> primitives.ColorX | None:
        """The SourceColor field value."""
        member = self.get_member("SourceColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source_color.setter
    def source_color(self, value: primitives.ColorX) -> None:
        """Set the SourceColor field value."""
        member = self.get_member("SourceColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SourceColor", fields.FieldColorX(value=value)
            )

