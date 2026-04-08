"""Generated component: PlatformColorPalette."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlatformColorPalette(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PlatformColorPalette.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlatformColorPalette"

    @property
    def neutrals(self) -> members.SyncObject | None:
        """The Neutrals member."""
        member = self.get_member("Neutrals")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @neutrals.setter
    def neutrals(self, value: members.SyncObject) -> None:
        """Set the Neutrals member."""
        self.set_member("Neutrals", value)

    @property
    def hero(self) -> members.SyncObject | None:
        """The Hero member."""
        member = self.get_member("Hero")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @hero.setter
    def hero(self, value: members.SyncObject) -> None:
        """Set the Hero member."""
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
        """The Sub member."""
        member = self.get_member("Sub")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @sub.setter
    def sub(self, value: members.SyncObject) -> None:
        """Set the Sub member."""
        self.set_member("Sub", value)

    @property
    def dark(self) -> members.SyncObject | None:
        """The Dark member."""
        member = self.get_member("Dark")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @dark.setter
    def dark(self, value: members.SyncObject) -> None:
        """Set the Dark member."""
        self.set_member("Dark", value)

