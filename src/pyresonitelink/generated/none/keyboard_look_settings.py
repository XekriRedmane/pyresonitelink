"""Generated component: KeyboardLookSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class KeyboardLookSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.KeyboardLookSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.KeyboardLookSettings"

    def __init__(self, look_enabled: bool | None = None, horizontal_speed: np.float32 | None = None, vertical_speed: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            look_enabled: Initial value for LookEnabled.
            horizontal_speed: Initial value for HorizontalSpeed.
            vertical_speed: Initial value for VerticalSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if look_enabled is not None:
            self.look_enabled = look_enabled
        if horizontal_speed is not None:
            self.horizontal_speed = horizontal_speed
        if vertical_speed is not None:
            self.vertical_speed = vertical_speed

    @property
    def look_enabled(self) -> bool | None:
        """The LookEnabled field value."""
        member = self.get_member("LookEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @look_enabled.setter
    def look_enabled(self, value: bool) -> None:
        """Set the LookEnabled field value."""
        member = self.get_member("LookEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LookEnabled", fields.FieldBool(value=value)
            )

    @property
    def horizontal_speed(self) -> np.float32 | None:
        """The HorizontalSpeed field value."""
        member = self.get_member("HorizontalSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_speed.setter
    def horizontal_speed(self, value: np.float32) -> None:
        """Set the HorizontalSpeed field value."""
        member = self.get_member("HorizontalSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalSpeed", fields.FieldFloat(value=value)
            )

    @property
    def vertical_speed(self) -> np.float32 | None:
        """The VerticalSpeed field value."""
        member = self.get_member("VerticalSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_speed.setter
    def vertical_speed(self, value: np.float32) -> None:
        """Set the VerticalSpeed field value."""
        member = self.get_member("VerticalSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalSpeed", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

