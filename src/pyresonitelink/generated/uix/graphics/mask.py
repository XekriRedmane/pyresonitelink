"""Generated component: Mask."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Mask(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The Mask component restricts the rendering of anything beneath it. It requires an Image component, text, arc, rectmesh, or anything that displays a graphic on the same slot. Only opaque areas of the graphic on the same slot will render the UIX below. This is also utilized in ScrollRect since it can mask anything outside of the scrolling viewport when using the component.

There is a UIX Tutorial that use masking and ScrollRects to help you understand how masks work.

|warning}}

}}

    Category: UIX/Graphics

    This can be used for fancy cutout effects.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Mask"

    def __init__(self, show_mask_graphic: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_mask_graphic: Initial value for ShowMaskGraphic.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show_mask_graphic is not None:
            self.show_mask_graphic = show_mask_graphic

    @property
    def show_mask_graphic(self) -> primitives.Bool | None:
        """Shows the graphic being used to do the masking for debug purposes."""
        member = self.get_member("ShowMaskGraphic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_mask_graphic.setter
    def show_mask_graphic(self, value: primitives.Bool) -> None:
        """Set the ShowMaskGraphic field value."""
        member = self.get_member("ShowMaskGraphic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowMaskGraphic", fields.FieldBool(value=value)
            )

