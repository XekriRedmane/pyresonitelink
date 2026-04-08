"""Generated component: TryEnumToUshort."""

from typing import Any

E = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TryEnumToUshort(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUshort<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Enums

    Parameterize with a value type::

        TryEnumToUshort[primitives.Float]
        TryEnumToUshort[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUshort<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUshort<>"

    def __init__(self, value: str | INodeValueOutput[E] | None = None, fail_value: str | INodeValueOutput[primitives.UShort] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            fail_value: Initial value for FailValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if fail_value is not None:
            self.fail_value = fail_value

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[E])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[E] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[E] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<E>'),
            )

    @property
    def fail_value(self) -> str | None:
        """Target ID of the FailValue reference (targets INodeValueOutput[primitives.UShort])."""
        member = self.get_member("FailValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fail_value.setter
    def fail_value(self, target: str | INodeValueOutput[primitives.UShort] | None) -> None:
        """Set the FailValue reference by target ID or INodeValueOutput[primitives.UShort] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("FailValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FailValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<ushort>'),
            )

