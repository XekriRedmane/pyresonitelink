"""Generated component: DesktopInteractionRelay."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.ifocusable import IFocusable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopInteractionRelay(GeneratedComponent, IUIInteractable, IFocusable, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DesktopInteractionRelay.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopInteractionRelay"

    def __init__(self, display_index: np.int32 | None = None, use_legacy_text_input: bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def display_index(self) -> np.int32 | None:
        """The DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_index.setter
    def display_index(self, value: np.int32) -> None:
        """Set the DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayIndex", fields.FieldInt(value=value)
            )

    @property
    def use_legacy_text_input(self) -> bool | None:
        """The UseLegacyTextInput field value."""
        member = self.get_member("UseLegacyTextInput")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_legacy_text_input.setter
    def use_legacy_text_input(self, value: bool) -> None:
        """Set the UseLegacyTextInput field value."""
        member = self.get_member("UseLegacyTextInput")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLegacyTextInput", fields.FieldBool(value=value)
            )

