"""Generated component: OperatingSystemSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class OperatingSystemSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.OperatingSystemSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OperatingSystemSettings"

    def __init__(self, keep_original_screenshot_format: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            keep_original_screenshot_format: Initial value for KeepOriginalScreenshotFormat.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if keep_original_screenshot_format is not None:
            self.keep_original_screenshot_format = keep_original_screenshot_format

    @property
    def keep_original_screenshot_format(self) -> bool | None:
        """The KeepOriginalScreenshotFormat field value."""
        member = self.get_member("KeepOriginalScreenshotFormat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @keep_original_screenshot_format.setter
    def keep_original_screenshot_format(self, value: bool) -> None:
        """Set the KeepOriginalScreenshotFormat field value."""
        member = self.get_member("KeepOriginalScreenshotFormat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KeepOriginalScreenshotFormat", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

