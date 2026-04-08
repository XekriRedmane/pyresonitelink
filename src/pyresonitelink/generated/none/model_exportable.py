"""Generated component: ModelExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ModelExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ModelExportable.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ModelExportable"

    def __init__(self, root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets Slot)."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def only_components(self) -> members.SyncList | None:
        """The OnlyComponents member."""
        member = self.get_member("OnlyComponents")
        if isinstance(member, members.SyncList):
            return member
        return None

    @only_components.setter
    def only_components(self, value: members.SyncList) -> None:
        """Set the OnlyComponents member."""
        self.set_member("OnlyComponents", value)

