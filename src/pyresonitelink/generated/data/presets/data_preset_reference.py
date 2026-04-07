"""Generated component: DataPresetReference."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.idata_preset_entry import IDataPresetEntry
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataPresetReference(GenericComponent[T], IDataPresetEntry, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DataPresetReference<>.

    Category: Data/Presets

    Parameterize with a value type::

        DataPresetReference[np.float32]
        DataPresetReference[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataPresetReference<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DataPresetReference<>"

    def __init__(self, preset_reference: str | T | None = None, target_reference: str | SyncRef[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            preset_reference: Initial value for PresetReference.
            target_reference: Initial value for TargetReference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if preset_reference is not None:
            self.preset_reference = preset_reference
        if target_reference is not None:
            self.target_reference = target_reference

    @property
    def preset_reference(self) -> str | None:
        """Target ID of the PresetReference reference (targets T)."""
        member = self.get_member("PresetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preset_reference.setter
    def preset_reference(self, target: str | T | None) -> None:
        """Set the PresetReference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("PresetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PresetReference",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def target_reference(self) -> str | None:
        """Target ID of the TargetReference reference (targets SyncRef[T])."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[T] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

