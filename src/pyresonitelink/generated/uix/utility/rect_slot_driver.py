"""Generated component: RectSlotDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectSlotDriver(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The RectSlotDriver component, when attached to a UIX element slot, will automatically drive that slot's position and will provide a field ``_position`` for the user to use as a reference.

}}

    Category: UIX/Utility

    Mostly will be used for reference of a position of a UIX element.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectSlotDriver"

    def __init__(self, position: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position: Initial value for _position.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position is not None:
            self.position = position

    @property
    def position(self) -> str | None:
        """Internal - Sets the position of the slot for driving the value."""
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

