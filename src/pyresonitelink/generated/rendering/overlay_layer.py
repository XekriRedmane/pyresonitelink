"""Generated component: OverlayLayer."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OverlayLayer(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The OverlayLayer component instructs the renderer to render the hierarchy it is attached to on top of everything else. In desktop mode the component also causes the hierarchy to render directly in front of the camera, mimicking a 2D user interface.

    Category: Rendering

    **Behavior**: When enabled, OverlayLayer will tell the renderer to render the hierarchy under the slot (including the slot) on top of everything else. Internally, this is done by setting the layer of each GameObject in the hierarchy to ``Overlay``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OverlayLayer"

    pass

