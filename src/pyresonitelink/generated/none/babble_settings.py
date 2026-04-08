"""Generated component: BabbleSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class BabbleSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.BabbleSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BabbleSettings"

    def __init__(self, osc_data_port: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            osc_data_port: Initial value for OSC_DataPort.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if osc_data_port is not None:
            self.osc_data_port = osc_data_port

    @property
    def osc_data_port(self) -> np.int32 | None:
        """The OSC_DataPort field value."""
        member = self.get_member("OSC_DataPort")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @osc_data_port.setter
    def osc_data_port(self, value: np.int32) -> None:
        """Set the OSC_DataPort field value."""
        member = self.get_member("OSC_DataPort")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OSC_DataPort", fields.FieldInt(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

