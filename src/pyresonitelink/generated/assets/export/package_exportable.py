"""Generated component: PackageExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PackageExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The PackageExportable component takes in any Slot hierarchy as a field, and when the slot that has this exportable component on it gets exported, it will actually save a file on your device of the target slot hierarchy provided (and not the item that your exporting from unless it is also under that hierarchy).

    Category: Assets/Export

    This can be a better alternative than using the BinaryExportable for
    storage of assets, items, or worlds.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PackageExportable"

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
        """The slot hierarchy to be exported."""
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

