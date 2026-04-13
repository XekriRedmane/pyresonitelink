"""Generated component: GrabbingSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.hand_grab_type import HandGrabType
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GrabbingSettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbingSettings"

    def __init__(self, default_hand_grab_type: HandGrabType | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default_hand_grab_type: Initial value for DefaultHandGrabType.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default_hand_grab_type is not None:
            self.default_hand_grab_type = default_hand_grab_type

    @property
    def default_hand_grab_type(self) -> HandGrabType | None:
        """The hand grabbing mode a use has by default for their hands."""
        member = self.get_member("DefaultHandGrabType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return HandGrabType(member.value)
        return None

    @default_hand_grab_type.setter
    def default_hand_grab_type(self, value: HandGrabType | str) -> None:
        """Set DefaultHandGrabType. The hand grabbing mode a use has by default for their hands."""
        member = self.get_member("DefaultHandGrabType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DefaultHandGrabType",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

