"""Generated component: HoverArea."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_hoverable import IUIHoverable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HoverArea(GeneratedComponent, IUIHoverable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.HoverArea.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.HoverArea"

    def __init__(self, is_hovering: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_hovering: Initial value for IsHovering.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_hovering is not None:
            self.is_hovering = is_hovering

    @property
    def is_hovering(self) -> bool | None:
        """The IsHovering field value."""
        member = self.get_member("IsHovering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_hovering.setter
    def is_hovering(self, value: bool) -> None:
        """Set the IsHovering field value."""
        member = self.get_member("IsHovering")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsHovering", fields.FieldBool(value=value)
            )

