"""Generated component: ComposeBits_short."""

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


class ComposeBits_short(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_short.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_short"

    def __init__(self, bit0: str | INodeValueOutput[primitives.Bool] | None = None, bit1: str | INodeValueOutput[primitives.Bool] | None = None, bit2: str | INodeValueOutput[primitives.Bool] | None = None, bit3: str | INodeValueOutput[primitives.Bool] | None = None, bit4: str | INodeValueOutput[primitives.Bool] | None = None, bit5: str | INodeValueOutput[primitives.Bool] | None = None, bit6: str | INodeValueOutput[primitives.Bool] | None = None, bit7: str | INodeValueOutput[primitives.Bool] | None = None, bit8: str | INodeValueOutput[primitives.Bool] | None = None, bit9: str | INodeValueOutput[primitives.Bool] | None = None, bit10: str | INodeValueOutput[primitives.Bool] | None = None, bit11: str | INodeValueOutput[primitives.Bool] | None = None, bit12: str | INodeValueOutput[primitives.Bool] | None = None, bit13: str | INodeValueOutput[primitives.Bool] | None = None, bit14: str | INodeValueOutput[primitives.Bool] | None = None, bit15: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
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
            bit8: Initial value for Bit8.
            bit9: Initial value for Bit9.
            bit10: Initial value for Bit10.
            bit11: Initial value for Bit11.
            bit12: Initial value for Bit12.
            bit13: Initial value for Bit13.
            bit14: Initial value for Bit14.
            bit15: Initial value for Bit15.
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
        if bit8 is not None:
            self.bit8 = bit8
        if bit9 is not None:
            self.bit9 = bit9
        if bit10 is not None:
            self.bit10 = bit10
        if bit11 is not None:
            self.bit11 = bit11
        if bit12 is not None:
            self.bit12 = bit12
        if bit13 is not None:
            self.bit13 = bit13
        if bit14 is not None:
            self.bit14 = bit14
        if bit15 is not None:
            self.bit15 = bit15

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

    @property
    def bit8(self) -> str | None:
        """Target ID of the Bit8 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit8")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit8.setter
    def bit8(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit8 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit8")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit8",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit9(self) -> str | None:
        """Target ID of the Bit9 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit9")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit9.setter
    def bit9(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit9 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit9")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit9",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit10(self) -> str | None:
        """Target ID of the Bit10 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit10")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit10.setter
    def bit10(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit10 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit10")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit10",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit11(self) -> str | None:
        """Target ID of the Bit11 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit11")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit11.setter
    def bit11(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit11 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit11")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit11",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit12(self) -> str | None:
        """Target ID of the Bit12 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit12")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit12.setter
    def bit12(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit12 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit12")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit12",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit13(self) -> str | None:
        """Target ID of the Bit13 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit13")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit13.setter
    def bit13(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit13 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit13")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit13",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit14(self) -> str | None:
        """Target ID of the Bit14 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit14")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit14.setter
    def bit14(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit14 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit14")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit14",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit15(self) -> str | None:
        """Target ID of the Bit15 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit15")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit15.setter
    def bit15(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit15 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit15")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit15",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

