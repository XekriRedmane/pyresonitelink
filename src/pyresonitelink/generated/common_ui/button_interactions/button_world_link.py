"""Generated component: ButtonWorldLink."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.world_link import WorldLink
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonWorldLink(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonWorldLink component takes in a WorldLink Component. When an IButton is pressed while this component is in the same slot as it, this component will attempt to open a world that is provided from that world link component.

}}

    Category: Common UI/Button Interactions

    This allows a user to make customizable world loading buttons, either as
    a way to go to another world or to pre-load a world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonWorldLink"

    def __init__(self, world_link: str | WorldLink | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_link: Initial value for WorldLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_link is not None:
            self.world_link = world_link

    @property
    def world_link(self) -> str | None:
        """The WorldLink component that contains the world information."""
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_link.setter
    def world_link(self, target: str | WorldLink | None) -> None:
        """Set the WorldLink reference by target ID or WorldLink instance."""
        target_id: str | None = target.id if isinstance(target, WorldLink) else target  # type: ignore[assignment]
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldLink'),
            )

