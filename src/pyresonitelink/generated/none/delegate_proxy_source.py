"""Generated component: DelegateProxySource."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelegateProxySource(GenericComponent[T], IUIGrabbable, IWorldEventReceiver):
    """The DelegateProxySource component is used to make a Button UIX element give a sync delegate proxy when grabbed. To use almost any sync delegate with this component, provide "Delegate" as the type.

    Attach to a slot with a valid UIX Button and provide a delegate to
    proxy. When the area is grabbed, the user will have the delegate in
    their hand.

    Parameterize with a value type::

        DelegateProxySource[primitives.Float]
        DelegateProxySource[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DelegateProxySource<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DelegateProxySource<>"

    pass

