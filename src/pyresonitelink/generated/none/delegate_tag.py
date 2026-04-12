"""Generated component: DelegateTag."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelegateTag(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The Delegate Tag component is used to store a delegate of type T

    Parameterize with a value type::

        DelegateTag[primitives.Float]
        DelegateTag[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DelegateTag<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DelegateTag<>"

    pass

