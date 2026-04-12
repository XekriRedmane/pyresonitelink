"""Generated component: GaussianSplatExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.gaussian_splat import GaussianSplat
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The Gaussian Splat Exportable component allows for making a slot give an option to export as a Gaussian Splat.

    Category: Assets/Export
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatExportable"

    def __init__(self, splat: str | IAssetProvider[GaussianSplat] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            splat: Initial value for Splat.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if splat is not None:
            self.splat = splat

    @property
    def splat(self) -> str | None:
        """The splat to add as an option for export."""
        member = self.get_member("Splat")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @splat.setter
    def splat(self, target: str | IAssetProvider[GaussianSplat] | None) -> None:
        """Set the Splat reference by target ID or IAssetProvider[GaussianSplat] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Splat")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Splat",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.GaussianSplat>'),
            )

