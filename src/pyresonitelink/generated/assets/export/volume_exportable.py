"""Generated component: VolumeExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VolumeExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The VolumeExportable component is used to export 3D textures (or 2D images that a layered on top of each other) as a ``.cube`` file format.

    Category: Assets/Export
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VolumeExportable"

    def __init__(self, volume: str | IAssetProvider[Texture3D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            volume: Initial value for Volume.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if volume is not None:
            self.volume = volume

    @property
    def volume(self) -> str | None:
        """The 3D Texture to be exported."""
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume.setter
    def volume(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the Volume reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Volume",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

