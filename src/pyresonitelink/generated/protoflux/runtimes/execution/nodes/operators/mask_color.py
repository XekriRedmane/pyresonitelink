"""Generated component: Mask_Color."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Mask_Color(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Mask_Color.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Mask_Color"

    def __init__(self, on_true: str | INodeValueOutput[primitives.Color] | None = None, on_false: str | INodeValueOutput[primitives.Color] | None = None, mask: str | INodeValueOutput[primitives.Bool4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_true: Initial value for OnTrue.
            on_false: Initial value for OnFalse.
            mask: Initial value for Mask.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_true is not None:
            self.on_true = on_true
        if on_false is not None:
            self.on_false = on_false
        if mask is not None:
            self.mask = mask

    @property
    def on_true(self) -> str | None:
        """Target ID of the OnTrue reference (targets INodeValueOutput[primitives.Color])."""
        member = self.get_member("OnTrue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_true.setter
    def on_true(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the OnTrue reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnTrue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnTrue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def on_false(self) -> str | None:
        """Target ID of the OnFalse reference (targets INodeValueOutput[primitives.Color])."""
        member = self.get_member("OnFalse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_false.setter
    def on_false(self, target: str | INodeValueOutput[primitives.Color] | None) -> None:
        """Set the OnFalse reference by target ID or INodeValueOutput[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnFalse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFalse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<color>'),
            )

    @property
    def mask(self) -> str | None:
        """Target ID of the Mask reference (targets INodeValueOutput[primitives.Bool4])."""
        member = self.get_member("Mask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mask.setter
    def mask(self, target: str | INodeValueOutput[primitives.Bool4] | None) -> None:
        """Set the Mask reference by target ID or INodeValueOutput[primitives.Bool4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Mask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool4>'),
            )

