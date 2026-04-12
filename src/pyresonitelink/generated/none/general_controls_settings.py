"""Generated component: GeneralControlsSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GeneralControlsSettings(GeneratedComponent, ICustomInspector):
    """See General Controls Settings.

    See General Controls Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GeneralControlsSettings"

    def __init__(self, primary_hand: Chirality | str | None = None, double_click_interval: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            primary_hand: Initial value for PrimaryHand.
            double_click_interval: Initial value for DoubleClickInterval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if primary_hand is not None:
            self.primary_hand = primary_hand
        if double_click_interval is not None:
            self.double_click_interval = double_click_interval

    @property
    def primary_hand(self) -> Chirality | None:
        """Adapts the game to your dominant hand. Some items and tools will adapt to this."""
        member = self.get_member("PrimaryHand")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @primary_hand.setter
    def primary_hand(self, value: Chirality | str) -> None:
        """Set PrimaryHand. Adapts the game to your dominant hand. Some items and tools will adapt to this."""
        member = self.get_member("PrimaryHand")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PrimaryHand",
                members.FieldEnum(value=str(value)),
            )

    @property
    def double_click_interval(self) -> primitives.Float | None:
        """Used to adjust the time window for any actions which require a double click."""
        member = self.get_member("DoubleClickInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @double_click_interval.setter
    def double_click_interval(self, value: primitives.Float) -> None:
        """Set the DoubleClickInterval field value."""
        member = self.get_member("DoubleClickInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoubleClickInterval", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

