"""Generated component: GlobalDelegate."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlobalDelegate(GenericComponent[T], IGlobalValueProxy[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.GlobalDelegate<>.

    Category: ProtoFlux

    Parameterize with a value type::

        GlobalDelegate[primitives.Float]
        GlobalDelegate[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalDelegate<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalDelegate<>"

    pass

