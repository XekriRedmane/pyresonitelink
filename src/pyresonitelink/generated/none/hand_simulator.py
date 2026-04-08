"""Generated component: HandSimulator."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HandSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The HandSimulator component is used to control the logic for the transforms of a hand when overridden or interacting with something.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HandSimulator"

    def __init__(self, side: Chirality | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            side: Initial value for Side.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if side is not None:
            self.side = side

    @property
    def side(self) -> Chirality | None:
        """The hand side to simulate for."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @side.setter
    def side(self, value: Chirality | str) -> None:
        """Set Side. The hand side to simulate for."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Side",
                members.FieldEnum(value=str(value)),
            )

