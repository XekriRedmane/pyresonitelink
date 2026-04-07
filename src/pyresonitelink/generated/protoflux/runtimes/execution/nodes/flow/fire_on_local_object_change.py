"""Generated component: FireOnLocalObjectChange."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation


class FireOnLocalObjectChange(GenericComponent[T]):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalObjectChange<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow

    Parameterize with a value type::

        FireOnLocalObjectChange[np.float32]
        FireOnLocalObjectChange[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalObjectChange<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalObjectChange<>"

    def __init__(self, value: str | INodeObjectOutput[T] | None = None, on_change: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            on_change: Initial value for OnChange.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if on_change is not None:
            self.on_change = on_change

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeObjectOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

    @property
    def on_change(self) -> str | None:
        """Target ID of the OnChange reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnChange")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_change.setter
    def on_change(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnChange reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnChange")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnChange",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

