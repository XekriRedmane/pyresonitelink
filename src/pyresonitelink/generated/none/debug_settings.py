"""Generated component: DebugSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DebugSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugSettings"

    def __init__(self, debug_input_bindings: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            debug_input_bindings: Initial value for DebugInputBindings.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if debug_input_bindings is not None:
            self.debug_input_bindings = debug_input_bindings

    @property
    def debug_input_bindings(self) -> primitives.Bool | None:
        """The DebugInputBindings field value."""
        member = self.get_member("DebugInputBindings")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_input_bindings.setter
    def debug_input_bindings(self, value: primitives.Bool) -> None:
        """Set the DebugInputBindings field value."""
        member = self.get_member("DebugInputBindings")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DebugInputBindings", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

