"""Generated component: UI_TargettingController."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_interface import IUIInterface


class UI_TargettingController(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.UI_TargettingController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UI_TargettingController"

    def __init__(self, target: str | IUIInterface | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IUIInterface)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IUIInterface | None) -> None:
        """Set the Target reference by target ID or IUIInterface instance."""
        target_id: str | None = target.id if isinstance(target, IUIInterface) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IUIInterface'),
            )

