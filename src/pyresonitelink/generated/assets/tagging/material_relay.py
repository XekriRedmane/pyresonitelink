"""Generated component: MaterialRelay."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imaterial_target import IMaterialTarget
from pyresonitelink.generated._types.imaterial_source import IMaterialSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialRelay(GeneratedComponent, IMaterialTarget, IMaterialSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MaterialRelay.

    Category: Assets/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialRelay"

    @property
    def material_refs(self) -> members.SyncList | None:
        """The MaterialRefs member."""
        member = self.get_member("MaterialRefs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @material_refs.setter
    def material_refs(self, value: members.SyncList) -> None:
        """Set the MaterialRefs member."""
        self.set_member("MaterialRefs", value)

