"""Generated component: DashSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DashSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.DashSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DashSettings"

    def __init__(self, dash_curvature: np.float32 | None = None, open_close_speed: np.float32 | None = None, allow_replacing_settings: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dash_curvature: Initial value for DashCurvature.
            open_close_speed: Initial value for OpenCloseSpeed.
            allow_replacing_settings: Initial value for AllowReplacingSettings.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dash_curvature is not None:
            self.dash_curvature = dash_curvature
        if open_close_speed is not None:
            self.open_close_speed = open_close_speed
        if allow_replacing_settings is not None:
            self.allow_replacing_settings = allow_replacing_settings

    @property
    def dash_curvature(self) -> np.float32 | None:
        """The DashCurvature field value."""
        member = self.get_member("DashCurvature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dash_curvature.setter
    def dash_curvature(self, value: np.float32) -> None:
        """Set the DashCurvature field value."""
        member = self.get_member("DashCurvature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DashCurvature", fields.FieldFloat(value=value)
            )

    @property
    def open_close_speed(self) -> np.float32 | None:
        """The OpenCloseSpeed field value."""
        member = self.get_member("OpenCloseSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open_close_speed.setter
    def open_close_speed(self, value: np.float32) -> None:
        """Set the OpenCloseSpeed field value."""
        member = self.get_member("OpenCloseSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpenCloseSpeed", fields.FieldFloat(value=value)
            )

    @property
    def allow_replacing_settings(self) -> bool | None:
        """The AllowReplacingSettings field value."""
        member = self.get_member("AllowReplacingSettings")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_replacing_settings.setter
    def allow_replacing_settings(self, value: bool) -> None:
        """Set the AllowReplacingSettings field value."""
        member = self.get_member("AllowReplacingSettings")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowReplacingSettings", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

