"""Generated component: Mask."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Mask(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Mask.

    Category: UIX/Graphics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Mask"

    def __init__(self, show_mask_graphic: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_mask_graphic: Initial value for ShowMaskGraphic.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show_mask_graphic is not None:
            self.show_mask_graphic = show_mask_graphic

    @property
    def show_mask_graphic(self) -> bool | None:
        """The ShowMaskGraphic field value."""
        member = self.get_member("ShowMaskGraphic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_mask_graphic.setter
    def show_mask_graphic(self, value: bool) -> None:
        """Set the ShowMaskGraphic field value."""
        member = self.get_member("ShowMaskGraphic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowMaskGraphic", fields.FieldBool(value=value)
            )

