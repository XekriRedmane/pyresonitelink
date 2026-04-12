"""Generated component: DesktopInteractionRelay."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.ifocusable import IFocusable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopInteractionRelay(GeneratedComponent, IUIInteractable, IFocusable, IUIComputeComponent, IWorldEventReceiver):
    """The DesktopInteractionRelay component only works in user space. When part of a UIX, it sends events from user inputs (the position is determined by the RectTransform) to the desktop display at ``DisplayIndex``

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopInteractionRelay"

    def __init__(self, display_index: primitives.Int | None = None, use_legacy_text_input: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_index: Initial value for DisplayIndex.
            use_legacy_text_input: Initial value for UseLegacyTextInput.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_index is not None:
            self.display_index = display_index
        if use_legacy_text_input is not None:
            self.use_legacy_text_input = use_legacy_text_input

    @property
    def display_index(self) -> primitives.Int | None:
        """The display to send Interactions to."""
        member = self.get_member("DisplayIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_index.setter
    def display_index(self, value: primitives.Int) -> None:
        """Set the DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayIndex", fields.FieldInt(value=value)
            )

    @property
    def use_legacy_text_input(self) -> primitives.Bool | None:
        """Whether to use the legacy text input system."""
        member = self.get_member("UseLegacyTextInput")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_legacy_text_input.setter
    def use_legacy_text_input(self, value: primitives.Bool) -> None:
        """Set the UseLegacyTextInput field value."""
        member = self.get_member("UseLegacyTextInput")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLegacyTextInput", fields.FieldBool(value=value)
            )

