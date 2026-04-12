"""Generated component: PlatformColorPalette."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlatformColorPalette(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The PlatformColorPalette component is a quick way of getting the colors of Resonite's Branding. This also provides you with both the color values in ColorX form and Hex form.

    Category: Utility

    Attach to a slot and take any value as a source for a drive to drive a
    UI with Resonite's branding.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlatformColorPalette"

    @property
    def neutrals(self) -> members.SyncObject | None:
        """A list of neutral color and hexes used for UI backgrounds in resonite."""
        member = self.get_member("Neutrals")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @neutrals.setter
    def neutrals(self, value: members.SyncObject) -> None:
        """Set Neutrals. A list of neutral color and hexes used for UI backgrounds in resonite."""
        self.set_member("Neutrals", value)

    @property
    def hero(self) -> members.SyncObject | None:
        """A list of color and hexes used for bright colored buttons and text like yellow for selected inspector slots or used in other cases."""
        member = self.get_member("Hero")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hero.setter
    def hero(self, value: members.SyncObject) -> None:
        """Set Hero. A list of color and hexes used for bright colored buttons and text like yellow for selected inspector slots or used in other cases."""
        self.set_member("Hero", value)

    @property
    def mid(self) -> members.SyncObject | None:
        """The Mid member."""
        member = self.get_member("Mid")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @mid.setter
    def mid(self, value: members.SyncObject) -> None:
        """Set the Mid member."""
        self.set_member("Mid", value)

    @property
    def sub(self) -> members.SyncObject | None:
        """A darker color and hexes set used for buttons or UI that are darker due to being selected or used in other cases."""
        member = self.get_member("Sub")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @sub.setter
    def sub(self, value: members.SyncObject) -> None:
        """Set Sub. A darker color and hexes set used for buttons or UI that are darker due to being selected or used in other cases."""
        self.set_member("Sub", value)

    @property
    def dark(self) -> members.SyncObject | None:
        """A dark color and hexes set used for buttons or UI that is disabled or used in other cases."""
        member = self.get_member("Dark")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @dark.setter
    def dark(self, value: members.SyncObject) -> None:
        """Set Dark. A dark color and hexes set used for buttons or UI that is disabled or used in other cases."""
        self.set_member("Dark", value)

