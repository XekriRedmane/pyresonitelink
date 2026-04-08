"""Generated component: GenericUserspaceDialogSpawner."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericUserspaceDialogSpawner(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GenericUserspaceDialogSpawner<>.

    Category: Utility/Tools

    Parameterize with a value type::

        GenericUserspaceDialogSpawner[np.float32]
        GenericUserspaceDialogSpawner[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GenericUserspaceDialogSpawner<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.GenericUserspaceDialogSpawner<>"

    pass

