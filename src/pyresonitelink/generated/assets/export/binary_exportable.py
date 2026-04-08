"""Generated component: BinaryExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.binary import Binary
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BinaryExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BinaryExportable.

    Category: Assets/Export
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BinaryExportable"

    def __init__(self, binary: str | IAssetProvider[Binary] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            binary: Initial value for Binary.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if binary is not None:
            self.binary = binary

    @property
    def binary(self) -> str | None:
        """Target ID of the Binary reference (targets IAssetProvider[Binary])."""
        member = self.get_member("Binary")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @binary.setter
    def binary(self, target: str | IAssetProvider[Binary] | None) -> None:
        """Set the Binary reference by target ID or IAssetProvider[Binary] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Binary")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Binary",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Binary>'),
            )

