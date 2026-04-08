"""Generated component: ComposeBits_byte."""

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


class ComposeBits_byte(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_byte.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_byte"

    def __init__(self, bit0: str | INodeValueOutput[primitives.Bool] | None = None, bit1: str | INodeValueOutput[primitives.Bool] | None = None, bit2: str | INodeValueOutput[primitives.Bool] | None = None, bit3: str | INodeValueOutput[primitives.Bool] | None = None, bit4: str | INodeValueOutput[primitives.Bool] | None = None, bit5: str | INodeValueOutput[primitives.Bool] | None = None, bit6: str | INodeValueOutput[primitives.Bool] | None = None, bit7: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bit0: Initial value for Bit0.
            bit1: Initial value for Bit1.
            bit2: Initial value for Bit2.
            bit3: Initial value for Bit3.
            bit4: Initial value for Bit4.
            bit5: Initial value for Bit5.
            bit6: Initial value for Bit6.
            bit7: Initial value for Bit7.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bit0 is not None:
            self.bit0 = bit0
        if bit1 is not None:
            self.bit1 = bit1
        if bit2 is not None:
            self.bit2 = bit2
        if bit3 is not None:
            self.bit3 = bit3
        if bit4 is not None:
            self.bit4 = bit4
        if bit5 is not None:
            self.bit5 = bit5
        if bit6 is not None:
            self.bit6 = bit6
        if bit7 is not None:
            self.bit7 = bit7

    @property
    def bit0(self) -> str | None:
        """Target ID of the Bit0 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit0.setter
    def bit0(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit0 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit1(self) -> str | None:
        """Target ID of the Bit1 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit1.setter
    def bit1(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit1 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit2(self) -> str | None:
        """Target ID of the Bit2 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit2.setter
    def bit2(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit2 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit3(self) -> str | None:
        """Target ID of the Bit3 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit3.setter
    def bit3(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit3 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit3")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit3",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit4(self) -> str | None:
        """Target ID of the Bit4 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit4")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit4.setter
    def bit4(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit4 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit4")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit4",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit5(self) -> str | None:
        """Target ID of the Bit5 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit5")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit5.setter
    def bit5(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit5 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit5")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit5",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit6(self) -> str | None:
        """Target ID of the Bit6 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit6")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit6.setter
    def bit6(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit6 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit6")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit6",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit7(self) -> str | None:
        """Target ID of the Bit7 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit7")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit7.setter
    def bit7(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit7 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit7")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit7",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

