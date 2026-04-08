"""Generated component: Rig."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Rig(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Rig.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Rig"

    @property
    def bones(self) -> members.SyncList | None:
        """The Bones member."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncList) -> None:
        """Set the Bones member."""
        self.set_member("Bones", value)

