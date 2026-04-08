"""Generated component: GrabbingSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GrabbingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbingSettings"

    @property
    def default_hand_grab_type(self) -> members.FieldEnum | None:
        """The DefaultHandGrabType member."""
        member = self.get_member("DefaultHandGrabType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @default_hand_grab_type.setter
    def default_hand_grab_type(self, value: members.FieldEnum) -> None:
        """Set the DefaultHandGrabType member."""
        self.set_member("DefaultHandGrabType", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

