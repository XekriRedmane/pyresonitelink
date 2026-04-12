"""Generated component: DelegateProxy."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.idelegate_proxy import IDelegateProxy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelegateProxy(GenericComponent[T], IDelegateProxy, IWorldEventReceiver):
    """The DelegateProxy is the Sync delegate version of a proxy used to store information about a world element in a user's hand before dropping it into a field. It's similar to grabbing a field name or a value.

    Used in delegate grabbing, is not used by the user directly.

    Parameterize with a value type::

        DelegateProxy[primitives.Float]
        DelegateProxy[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DelegateProxy<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DelegateProxy<>"

    pass

