"""Generated component: MaterialSet."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_asset_list import SyncAssetList
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialSet(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MaterialSet.

    Category: Rendering/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialSet"

    def __init__(self, active_set_index: np.int32 | None = None, target: str | SyncAssetList[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            active_set_index: Initial value for ActiveSetIndex.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if active_set_index is not None:
            self.active_set_index = active_set_index
        if target is not None:
            self.target = target

    @property
    def active_set_index(self) -> np.int32 | None:
        """The ActiveSetIndex field value."""
        member = self.get_member("ActiveSetIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_set_index.setter
    def active_set_index(self, value: np.int32) -> None:
        """Set the ActiveSetIndex field value."""
        member = self.get_member("ActiveSetIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveSetIndex", fields.FieldInt(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncAssetList[Material])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncAssetList[Material] | None) -> None:
        """Set the Target reference by target ID or SyncAssetList[Material] instance."""
        target_id: str | None = target.id if isinstance(target, SyncAssetList) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncAssetList<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def sets(self) -> members.SyncList | None:
        """The Sets member."""
        member = self.get_member("Sets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sets.setter
    def sets(self, value: members.SyncList) -> None:
        """Set the Sets member."""
        self.set_member("Sets", value)

