"""Generated component: GlobalReference."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlobalReference(GenericComponent[T], IGlobalValueProxy[T], IComponent, IWorldEventReceiver):
    """The GlobalReference&lt;T&gt; component is used by ProtoFlux to define a global of a reference type.

    Category: ProtoFlux

    When not using ProtoFlux, This component has no use over more idiomatic
    components such as a ReferenceField. This node can be used with a global
    to output and a node that accepts it's Type as a global (ex: raw data
    tool tip events) this allows to use a global variable to be used in Flux
    as a value at the same time without needing to drive the global value in
    the node using it for its data. When using ProtoFlux, the underlying
    reference can be changed and any node that accepts a global reference
    input that references the component will update during execution. This
    can allow one to dynamically change things like where source nodes point
    to. This component can also simply be used for static global references
    that need to be referenced in a lot of places for when the overhead of
    dynamic variables is undesirable. When combined with the Global To
    Output node, this component provides more UX than sourcing a
    ReferenceField by being able to see the underlying reference directly.

    Parameterize with a value type::

        GlobalReference[primitives.Float]
        GlobalReference[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalReference<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalReference<>"

    def __init__(self, reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference

    @property
    def reference(self) -> str | None:
        """The underlying reference of the global."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | T | None) -> None:
        """Set the Reference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='T'),
            )

