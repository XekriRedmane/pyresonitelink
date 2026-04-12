"""Generated component: GlobalDelegate."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlobalDelegate(GenericComponent[T], IGlobalValueProxy[T], IComponent, IWorldEventReceiver):
    """The GlobalDelegate&lt;T&gt; component is used by ProtoFlux to define a global of a sync delegate type.

    Category: ProtoFlux

    When not using ProtoFlux, This component has no use over more idiomatic
    components such as a
    ReferenceField&lt;SyncField&lt;WorldDelegate&gt;&gt;. When using
    ProtoFlux, the underlying reference can be changed and any node that
    accepts a global reference input that references the component will
    update during execution. This can allow one to dynamically change things
    like where method proxy nodes point to. This component can also simply
    be used for static global delegates that need to be referenced in a lot
    of places for when the overhead of dynamic variables is undesirable.
    When combined with the Global To Output node, this component provides
    more UX than sourcing a
    ReferenceField&lt;SyncField&lt;WorldDelegate&gt;&gt; by being able to
    see the underlying delegate directly from the UI.

    Parameterize with a value type::

        GlobalDelegate[primitives.Float]
        GlobalDelegate[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalDelegate<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalDelegate<>"

    pass

