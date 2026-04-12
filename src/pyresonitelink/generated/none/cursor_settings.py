"""Generated component: CursorSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class CursorSettings(GeneratedComponent, ICustomInspector):
    """The CursorSettings component is used in the settings menu to allow the user to change the size of their cursor when it is under specific circumstances.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CursorSettings"

    def __init__(self, base_cursor_size: primitives.Float | None = None, grab_multiplier: primitives.Float | None = None, interaction_multiplier: primitives.Float | None = None, text_multiplier: primitives.Float | None = None, slider_multiplier: primitives.Float | None = None, direct_cursor_enabled: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            base_cursor_size: Initial value for BaseCursorSize.
            grab_multiplier: Initial value for GrabMultiplier.
            interaction_multiplier: Initial value for InteractionMultiplier.
            text_multiplier: Initial value for TextMultiplier.
            slider_multiplier: Initial value for SliderMultiplier.
            direct_cursor_enabled: Initial value for DirectCursorEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if base_cursor_size is not None:
            self.base_cursor_size = base_cursor_size
        if grab_multiplier is not None:
            self.grab_multiplier = grab_multiplier
        if interaction_multiplier is not None:
            self.interaction_multiplier = interaction_multiplier
        if text_multiplier is not None:
            self.text_multiplier = text_multiplier
        if slider_multiplier is not None:
            self.slider_multiplier = slider_multiplier
        if direct_cursor_enabled is not None:
            self.direct_cursor_enabled = direct_cursor_enabled

    @property
    def base_cursor_size(self) -> primitives.Float | None:
        """The cursor size by default."""
        member = self.get_member("BaseCursorSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_cursor_size.setter
    def base_cursor_size(self, value: primitives.Float) -> None:
        """Set the BaseCursorSize field value."""
        member = self.get_member("BaseCursorSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseCursorSize", fields.FieldFloat(value=value)
            )

    @property
    def grab_multiplier(self) -> primitives.Float | None:
        """The amount to multiply the cursor size by when grabbing something"""
        member = self.get_member("GrabMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_multiplier.setter
    def grab_multiplier(self, value: primitives.Float) -> None:
        """Set the GrabMultiplier field value."""
        member = self.get_member("GrabMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def interaction_multiplier(self) -> primitives.Float | None:
        """The amount to multiply the cursor size by when pressing a button or interacting with something."""
        member = self.get_member("InteractionMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interaction_multiplier.setter
    def interaction_multiplier(self, value: primitives.Float) -> None:
        """Set the InteractionMultiplier field value."""
        member = self.get_member("InteractionMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InteractionMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def text_multiplier(self) -> primitives.Float | None:
        """How much to multiply the cursor size when highlighting an editable text field."""
        member = self.get_member("TextMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @text_multiplier.setter
    def text_multiplier(self, value: primitives.Float) -> None:
        """Set the TextMultiplier field value."""
        member = self.get_member("TextMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def slider_multiplier(self) -> primitives.Float | None:
        """The amount to multiply the cursor size when sliding a slider."""
        member = self.get_member("SliderMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slider_multiplier.setter
    def slider_multiplier(self, value: primitives.Float) -> None:
        """Set the SliderMultiplier field value."""
        member = self.get_member("SliderMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SliderMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def direct_cursor_enabled(self) -> primitives.Bool | None:
        """The DirectCursorEnabled field value."""
        member = self.get_member("DirectCursorEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_cursor_enabled.setter
    def direct_cursor_enabled(self, value: primitives.Bool) -> None:
        """Set the DirectCursorEnabled field value."""
        member = self.get_member("DirectCursorEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectCursorEnabled", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

