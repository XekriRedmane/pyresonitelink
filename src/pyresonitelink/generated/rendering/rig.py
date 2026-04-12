"""Generated component: Rig."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Rig(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The Rig component is used to inform what bones are "Rig" bones for components like Dynamic Bone Chains.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Rig"

    @property
    def bones(self) -> members.SyncList | None:
        """The bones that are a part of the item this component is on."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncList) -> None:
        """Set Bones. The bones that are a part of the item this component is on."""
        self.set_member("Bones", value)

