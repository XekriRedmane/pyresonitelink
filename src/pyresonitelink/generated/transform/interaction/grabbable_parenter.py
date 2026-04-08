"""Generated component: GrabbableParenter."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrabbable_receiver import IGrabbableReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableParenter(GeneratedComponent, IGrabbableReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbableParenter.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableParenter"

    def __init__(self, parent_under: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_under: Initial value for ParentUnder.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parent_under is not None:
            self.parent_under = parent_under

    @property
    def parent_under(self) -> str | None:
        """Target ID of the ParentUnder reference (targets Slot)."""
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_under.setter
    def parent_under(self, target: str | Slot | None) -> None:
        """Set the ParentUnder reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

