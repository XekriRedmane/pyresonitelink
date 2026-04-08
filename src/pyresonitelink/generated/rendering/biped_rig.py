"""Generated component: BipedRig."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BipedRig(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BipedRig.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BipedRig"

    def __init__(self, forward_axis: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            forward_axis: Initial value for ForwardAxis.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if forward_axis is not None:
            self.forward_axis = forward_axis

    @property
    def forward_axis(self) -> primitives.Float3 | None:
        """The ForwardAxis field value."""
        member = self.get_member("ForwardAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @forward_axis.setter
    def forward_axis(self, value: primitives.Float3) -> None:
        """Set the ForwardAxis field value."""
        member = self.get_member("ForwardAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForwardAxis", fields.FieldNullableFloat3(value=value)
            )

    @property
    def bones(self) -> members.SyncDictionary | None:
        """The Bones member."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncDictionary) -> None:
        """Set the Bones member."""
        self.set_member("Bones", value)

