"""Generated component: HandSimulator."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HandSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HandSimulator.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HandSimulator"

    @property
    def side(self) -> members.FieldEnum | None:
        """The Side member."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @side.setter
    def side(self, value: members.FieldEnum) -> None:
        """Set the Side member."""
        self.set_member("Side", value)

