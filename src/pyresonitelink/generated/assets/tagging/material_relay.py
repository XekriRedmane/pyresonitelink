"""Generated component: MaterialRelay."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imaterial_target import IMaterialTarget
from pyresonitelink.generated._types.imaterial_source import IMaterialSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialRelay(GeneratedComponent, IMaterialTarget, IMaterialSource, IWorldEventReceiver):
    """The MaterialRelay component is used to specify to a Material Tool when hitting a slot tagged with this component what materials to grab/apply to when using the tool.

    Category: Assets/Tagging

    Attach to the root of an object and provide a list of material storage
    fields from, for example, MeshRenderer or SkinnedMeshRenderer to make
    Relays for.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialRelay"

    @property
    def material_refs(self) -> members.SyncList | None:
        """A list of material storage fields that a material tool when applying should apply to. The first non null item in the list is the one a material tool will pick up when using the secondary action."""
        member = self.get_member("MaterialRefs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @material_refs.setter
    def material_refs(self, value: members.SyncList) -> None:
        """Set MaterialRefs. A list of material storage fields that a material tool when applying should apply to. The first non null item in the list is the one a material tool will pick up when using the secondary action."""
        self.set_member("MaterialRefs", value)

