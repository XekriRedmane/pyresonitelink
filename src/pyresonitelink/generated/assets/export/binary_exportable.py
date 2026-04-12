"""Generated component: BinaryExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.binary import Binary
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BinaryExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The BinaryExportable component takes in a Binary asset and allows the Slot to be exportable as a binary file on your device.

This is more of an uncommon way to export your files, but there are a couple of uses that are useful to know.

To export using this component, look at the file browser export section.

    Category: Assets/Export

    Using this component with the StaticBinary component, allows the user to
    export a binary file with a provided url. Keep in mind that exporting a
    binary file is one-way currently in Resonite (especially if you are
    thinking about local storage), this is due to the fact that Resonite
    uses the ``.bin`` as files that it does not recognize. So importing from
    a binary raw file is not doable.
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
        """The binary to be exported."""
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

