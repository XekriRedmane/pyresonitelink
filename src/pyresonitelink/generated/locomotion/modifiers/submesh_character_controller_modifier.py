"""Generated component: SubmeshCharacterControllerModifier."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SubmeshCharacterControllerModifier(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SubmeshCharacterControllerModifier.

    Category: Locomotion/Modifiers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SubmeshCharacterControllerModifier"

    @property
    def parameter(self) -> members.FieldEnum | None:
        """The Parameter member."""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @parameter.setter
    def parameter(self, value: members.FieldEnum) -> None:
        """Set the Parameter member."""
        self.set_member("Parameter", value)

    @property
    def modification_mode(self) -> members.FieldEnum | None:
        """The ModificationMode member."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @modification_mode.setter
    def modification_mode(self, value: members.FieldEnum) -> None:
        """Set the ModificationMode member."""
        self.set_member("ModificationMode", value)

    @property
    def values(self) -> members.SyncList | None:
        """The Values member."""
        member = self.get_member("Values")
        if isinstance(member, members.SyncList):
            return member
        return None

    @values.setter
    def values(self, value: members.SyncList) -> None:
        """Set the Values member."""
        self.set_member("Values", value)

