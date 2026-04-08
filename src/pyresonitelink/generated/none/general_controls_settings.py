"""Generated component: GeneralControlsSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GeneralControlsSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GeneralControlsSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GeneralControlsSettings"

    def __init__(self, double_click_interval: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            double_click_interval: Initial value for DoubleClickInterval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if double_click_interval is not None:
            self.double_click_interval = double_click_interval

    @property
    def primary_hand(self) -> members.FieldEnum | None:
        """The PrimaryHand member."""
        member = self.get_member("PrimaryHand")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @primary_hand.setter
    def primary_hand(self, value: members.FieldEnum) -> None:
        """Set the PrimaryHand member."""
        self.set_member("PrimaryHand", value)

    @property
    def double_click_interval(self) -> primitives.Float | None:
        """The DoubleClickInterval field value."""
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

