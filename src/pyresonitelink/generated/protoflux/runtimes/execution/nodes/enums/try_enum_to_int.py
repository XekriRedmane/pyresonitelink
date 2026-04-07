"""Generated component: TryEnumToInt."""

from typing import Any
import numpy as np

E = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TryEnumToInt(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToInt<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Enums

    Parameterize with a value type::

        TryEnumToInt[np.float32]
        TryEnumToInt[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToInt<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToInt<>"

    def __init__(self, value: str | INodeValueOutput[E] | None = None, fail_value: str | INodeValueOutput[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the FailValue reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("FailValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fail_value.setter
    def fail_value(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the FailValue reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("FailValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FailValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

