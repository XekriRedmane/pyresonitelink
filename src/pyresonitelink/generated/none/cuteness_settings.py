"""Generated component: CutenessSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class CutenessSettings(GeneratedComponent, ICustomInspector):
    """This component is solely a joke, and is supposed to make a setting that marks U-GlitchFur as cute and cannot be changed. It only appears for that user.

    **Behavior**: If ``AmCute`` is ever disabled, it is re-enabled automatically within the next 1-10 seconds.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CutenessSettings"

    def __init__(self, am_cute: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            am_cute: Initial value for AmCute.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if am_cute is not None:
            self.am_cute = am_cute

    @property
    def am_cute(self) -> primitives.Bool | None:
        """An unchangeable bool that stays true for U-GlitchFur. The description reads: "This setting indicates if the current user is very cute. When this setting is on, the current user makes a legally binding admission of their own cuteness."."""
        member = self.get_member("AmCute")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @am_cute.setter
    def am_cute(self, value: primitives.Bool) -> None:
        """Set the AmCute field value."""
        member = self.get_member("AmCute")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AmCute", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

