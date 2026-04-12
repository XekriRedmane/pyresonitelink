"""Generated component: GenericUserspaceDialogSpawner."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericUserspaceDialogSpawner(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """The GenericUserspaceDialogSpawner only works in dash space. The Generic type it takes has to be a component type. This component activates when on the slot as a button. When activated, this component attaches a new instance of T to the world, triggers ``Initializer`` with the new Component as an argument, and then positions it in front of the user in dash space. It needs a ModalOverlayManager above it in order to work.

    Category: Utility/Tools

    Parameterize with a value type::

        GenericUserspaceDialogSpawner[primitives.Float]
        GenericUserspaceDialogSpawner[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GenericUserspaceDialogSpawner<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.GenericUserspaceDialogSpawner<>"

    pass

