"""Generated component: HiddenLayer."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HiddenLayer(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The HiddenLayer component prevents rendering of the hierarchy it is applied to unless disabled or viewed through a camera that is explicitly set to render it. The Hidden Layer component is used for the Dash Menu's curved ui.

    Category: Rendering

    Attach to a slot which components on and below the slot should not
    render their visuals. The visuals will still render if viewed by a
    camera instructed to specifically render the hierarchy of the hidden
    layer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HiddenLayer"

    pass

