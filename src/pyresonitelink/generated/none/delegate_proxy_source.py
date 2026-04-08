"""Generated component: DelegateProxySource."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelegateProxySource(GenericComponent[T], IUIGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DelegateProxySource<>.

    Parameterize with a value type::

        DelegateProxySource[np.float32]
        DelegateProxySource[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DelegateProxySource<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DelegateProxySource<>"

    pass

