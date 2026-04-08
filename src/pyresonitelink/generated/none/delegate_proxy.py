"""Generated component: DelegateProxy."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.idelegate_proxy import IDelegateProxy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelegateProxy(GenericComponent[T], IDelegateProxy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DelegateProxy<>.

    Parameterize with a value type::

        DelegateProxy[primitives.Float]
        DelegateProxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DelegateProxy<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DelegateProxy<>"

    pass

