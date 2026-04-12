"""Generated component: IgnoreLayout."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IgnoreLayout(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The IgnoreLayout component makes a UIX element ignore the parent slot's layout component, and then draws over other elements (within that same hierarchy level of slots) inside of the parent's RectTransform.

}}

    Category: UIX/Layout

    Attach to a slot which the elements within should ignore the layout of
    the parent slot.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.IgnoreLayout"

    pass

