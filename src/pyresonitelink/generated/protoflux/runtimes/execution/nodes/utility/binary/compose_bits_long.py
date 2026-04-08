"""Generated component: ComposeBits_long."""

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


class ComposeBits_long(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_long.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_long"

    def __init__(self, bit0: str | INodeValueOutput[primitives.Bool] | None = None, bit1: str | INodeValueOutput[primitives.Bool] | None = None, bit2: str | INodeValueOutput[primitives.Bool] | None = None, bit3: str | INodeValueOutput[primitives.Bool] | None = None, bit4: str | INodeValueOutput[primitives.Bool] | None = None, bit5: str | INodeValueOutput[primitives.Bool] | None = None, bit6: str | INodeValueOutput[primitives.Bool] | None = None, bit7: str | INodeValueOutput[primitives.Bool] | None = None, bit8: str | INodeValueOutput[primitives.Bool] | None = None, bit9: str | INodeValueOutput[primitives.Bool] | None = None, bit10: str | INodeValueOutput[primitives.Bool] | None = None, bit11: str | INodeValueOutput[primitives.Bool] | None = None, bit12: str | INodeValueOutput[primitives.Bool] | None = None, bit13: str | INodeValueOutput[primitives.Bool] | None = None, bit14: str | INodeValueOutput[primitives.Bool] | None = None, bit15: str | INodeValueOutput[primitives.Bool] | None = None, bit16: str | INodeValueOutput[primitives.Bool] | None = None, bit17: str | INodeValueOutput[primitives.Bool] | None = None, bit18: str | INodeValueOutput[primitives.Bool] | None = None, bit19: str | INodeValueOutput[primitives.Bool] | None = None, bit20: str | INodeValueOutput[primitives.Bool] | None = None, bit21: str | INodeValueOutput[primitives.Bool] | None = None, bit22: str | INodeValueOutput[primitives.Bool] | None = None, bit23: str | INodeValueOutput[primitives.Bool] | None = None, bit24: str | INodeValueOutput[primitives.Bool] | None = None, bit25: str | INodeValueOutput[primitives.Bool] | None = None, bit26: str | INodeValueOutput[primitives.Bool] | None = None, bit27: str | INodeValueOutput[primitives.Bool] | None = None, bit28: str | INodeValueOutput[primitives.Bool] | None = None, bit29: str | INodeValueOutput[primitives.Bool] | None = None, bit30: str | INodeValueOutput[primitives.Bool] | None = None, bit31: str | INodeValueOutput[primitives.Bool] | None = None, bit32: str | INodeValueOutput[primitives.Bool] | None = None, bit33: str | INodeValueOutput[primitives.Bool] | None = None, bit34: str | INodeValueOutput[primitives.Bool] | None = None, bit35: str | INodeValueOutput[primitives.Bool] | None = None, bit36: str | INodeValueOutput[primitives.Bool] | None = None, bit37: str | INodeValueOutput[primitives.Bool] | None = None, bit38: str | INodeValueOutput[primitives.Bool] | None = None, bit39: str | INodeValueOutput[primitives.Bool] | None = None, bit40: str | INodeValueOutput[primitives.Bool] | None = None, bit41: str | INodeValueOutput[primitives.Bool] | None = None, bit42: str | INodeValueOutput[primitives.Bool] | None = None, bit43: str | INodeValueOutput[primitives.Bool] | None = None, bit44: str | INodeValueOutput[primitives.Bool] | None = None, bit45: str | INodeValueOutput[primitives.Bool] | None = None, bit46: str | INodeValueOutput[primitives.Bool] | None = None, bit47: str | INodeValueOutput[primitives.Bool] | None = None, bit48: str | INodeValueOutput[primitives.Bool] | None = None, bit49: str | INodeValueOutput[primitives.Bool] | None = None, bit50: str | INodeValueOutput[primitives.Bool] | None = None, bit51: str | INodeValueOutput[primitives.Bool] | None = None, bit52: str | INodeValueOutput[primitives.Bool] | None = None, bit53: str | INodeValueOutput[primitives.Bool] | None = None, bit54: str | INodeValueOutput[primitives.Bool] | None = None, bit55: str | INodeValueOutput[primitives.Bool] | None = None, bit56: str | INodeValueOutput[primitives.Bool] | None = None, bit57: str | INodeValueOutput[primitives.Bool] | None = None, bit58: str | INodeValueOutput[primitives.Bool] | None = None, bit59: str | INodeValueOutput[primitives.Bool] | None = None, bit60: str | INodeValueOutput[primitives.Bool] | None = None, bit61: str | INodeValueOutput[primitives.Bool] | None = None, bit62: str | INodeValueOutput[primitives.Bool] | None = None, bit63: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
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
            bit16: Initial value for Bit16.
            bit17: Initial value for Bit17.
            bit18: Initial value for Bit18.
            bit19: Initial value for Bit19.
            bit20: Initial value for Bit20.
            bit21: Initial value for Bit21.
            bit22: Initial value for Bit22.
            bit23: Initial value for Bit23.
            bit24: Initial value for Bit24.
            bit25: Initial value for Bit25.
            bit26: Initial value for Bit26.
            bit27: Initial value for Bit27.
            bit28: Initial value for Bit28.
            bit29: Initial value for Bit29.
            bit30: Initial value for Bit30.
            bit31: Initial value for Bit31.
            bit32: Initial value for Bit32.
            bit33: Initial value for Bit33.
            bit34: Initial value for Bit34.
            bit35: Initial value for Bit35.
            bit36: Initial value for Bit36.
            bit37: Initial value for Bit37.
            bit38: Initial value for Bit38.
            bit39: Initial value for Bit39.
            bit40: Initial value for Bit40.
            bit41: Initial value for Bit41.
            bit42: Initial value for Bit42.
            bit43: Initial value for Bit43.
            bit44: Initial value for Bit44.
            bit45: Initial value for Bit45.
            bit46: Initial value for Bit46.
            bit47: Initial value for Bit47.
            bit48: Initial value for Bit48.
            bit49: Initial value for Bit49.
            bit50: Initial value for Bit50.
            bit51: Initial value for Bit51.
            bit52: Initial value for Bit52.
            bit53: Initial value for Bit53.
            bit54: Initial value for Bit54.
            bit55: Initial value for Bit55.
            bit56: Initial value for Bit56.
            bit57: Initial value for Bit57.
            bit58: Initial value for Bit58.
            bit59: Initial value for Bit59.
            bit60: Initial value for Bit60.
            bit61: Initial value for Bit61.
            bit62: Initial value for Bit62.
            bit63: Initial value for Bit63.
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
        if bit16 is not None:
            self.bit16 = bit16
        if bit17 is not None:
            self.bit17 = bit17
        if bit18 is not None:
            self.bit18 = bit18
        if bit19 is not None:
            self.bit19 = bit19
        if bit20 is not None:
            self.bit20 = bit20
        if bit21 is not None:
            self.bit21 = bit21
        if bit22 is not None:
            self.bit22 = bit22
        if bit23 is not None:
            self.bit23 = bit23
        if bit24 is not None:
            self.bit24 = bit24
        if bit25 is not None:
            self.bit25 = bit25
        if bit26 is not None:
            self.bit26 = bit26
        if bit27 is not None:
            self.bit27 = bit27
        if bit28 is not None:
            self.bit28 = bit28
        if bit29 is not None:
            self.bit29 = bit29
        if bit30 is not None:
            self.bit30 = bit30
        if bit31 is not None:
            self.bit31 = bit31
        if bit32 is not None:
            self.bit32 = bit32
        if bit33 is not None:
            self.bit33 = bit33
        if bit34 is not None:
            self.bit34 = bit34
        if bit35 is not None:
            self.bit35 = bit35
        if bit36 is not None:
            self.bit36 = bit36
        if bit37 is not None:
            self.bit37 = bit37
        if bit38 is not None:
            self.bit38 = bit38
        if bit39 is not None:
            self.bit39 = bit39
        if bit40 is not None:
            self.bit40 = bit40
        if bit41 is not None:
            self.bit41 = bit41
        if bit42 is not None:
            self.bit42 = bit42
        if bit43 is not None:
            self.bit43 = bit43
        if bit44 is not None:
            self.bit44 = bit44
        if bit45 is not None:
            self.bit45 = bit45
        if bit46 is not None:
            self.bit46 = bit46
        if bit47 is not None:
            self.bit47 = bit47
        if bit48 is not None:
            self.bit48 = bit48
        if bit49 is not None:
            self.bit49 = bit49
        if bit50 is not None:
            self.bit50 = bit50
        if bit51 is not None:
            self.bit51 = bit51
        if bit52 is not None:
            self.bit52 = bit52
        if bit53 is not None:
            self.bit53 = bit53
        if bit54 is not None:
            self.bit54 = bit54
        if bit55 is not None:
            self.bit55 = bit55
        if bit56 is not None:
            self.bit56 = bit56
        if bit57 is not None:
            self.bit57 = bit57
        if bit58 is not None:
            self.bit58 = bit58
        if bit59 is not None:
            self.bit59 = bit59
        if bit60 is not None:
            self.bit60 = bit60
        if bit61 is not None:
            self.bit61 = bit61
        if bit62 is not None:
            self.bit62 = bit62
        if bit63 is not None:
            self.bit63 = bit63

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

    @property
    def bit16(self) -> str | None:
        """Target ID of the Bit16 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit16")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit16.setter
    def bit16(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit16 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit16")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit16",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit17(self) -> str | None:
        """Target ID of the Bit17 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit17")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit17.setter
    def bit17(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit17 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit17")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit17",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit18(self) -> str | None:
        """Target ID of the Bit18 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit18")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit18.setter
    def bit18(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit18 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit18")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit18",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit19(self) -> str | None:
        """Target ID of the Bit19 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit19")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit19.setter
    def bit19(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit19 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit19")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit19",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit20(self) -> str | None:
        """Target ID of the Bit20 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit20")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit20.setter
    def bit20(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit20 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit20")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit20",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit21(self) -> str | None:
        """Target ID of the Bit21 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit21")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit21.setter
    def bit21(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit21 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit21")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit21",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit22(self) -> str | None:
        """Target ID of the Bit22 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit22")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit22.setter
    def bit22(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit22 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit22")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit22",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit23(self) -> str | None:
        """Target ID of the Bit23 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit23")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit23.setter
    def bit23(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit23 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit23")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit23",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit24(self) -> str | None:
        """Target ID of the Bit24 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit24")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit24.setter
    def bit24(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit24 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit24")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit24",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit25(self) -> str | None:
        """Target ID of the Bit25 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit25")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit25.setter
    def bit25(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit25 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit25")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit25",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit26(self) -> str | None:
        """Target ID of the Bit26 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit26")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit26.setter
    def bit26(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit26 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit26")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit26",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit27(self) -> str | None:
        """Target ID of the Bit27 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit27")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit27.setter
    def bit27(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit27 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit27")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit27",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit28(self) -> str | None:
        """Target ID of the Bit28 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit28")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit28.setter
    def bit28(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit28 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit28")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit28",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit29(self) -> str | None:
        """Target ID of the Bit29 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit29")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit29.setter
    def bit29(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit29 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit29")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit29",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit30(self) -> str | None:
        """Target ID of the Bit30 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit30")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit30.setter
    def bit30(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit30 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit30")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit30",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit31(self) -> str | None:
        """Target ID of the Bit31 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit31")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit31.setter
    def bit31(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit31 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit31")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit31",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit32(self) -> str | None:
        """Target ID of the Bit32 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit32")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit32.setter
    def bit32(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit32 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit32")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit32",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit33(self) -> str | None:
        """Target ID of the Bit33 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit33")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit33.setter
    def bit33(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit33 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit33")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit33",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit34(self) -> str | None:
        """Target ID of the Bit34 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit34")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit34.setter
    def bit34(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit34 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit34")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit34",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit35(self) -> str | None:
        """Target ID of the Bit35 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit35")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit35.setter
    def bit35(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit35 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit35")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit35",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit36(self) -> str | None:
        """Target ID of the Bit36 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit36")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit36.setter
    def bit36(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit36 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit36")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit36",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit37(self) -> str | None:
        """Target ID of the Bit37 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit37")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit37.setter
    def bit37(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit37 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit37")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit37",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit38(self) -> str | None:
        """Target ID of the Bit38 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit38")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit38.setter
    def bit38(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit38 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit38")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit38",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit39(self) -> str | None:
        """Target ID of the Bit39 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit39")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit39.setter
    def bit39(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit39 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit39")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit39",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit40(self) -> str | None:
        """Target ID of the Bit40 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit40")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit40.setter
    def bit40(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit40 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit40")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit40",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit41(self) -> str | None:
        """Target ID of the Bit41 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit41")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit41.setter
    def bit41(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit41 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit41")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit41",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit42(self) -> str | None:
        """Target ID of the Bit42 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit42")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit42.setter
    def bit42(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit42 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit42")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit42",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit43(self) -> str | None:
        """Target ID of the Bit43 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit43")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit43.setter
    def bit43(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit43 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit43")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit43",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit44(self) -> str | None:
        """Target ID of the Bit44 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit44")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit44.setter
    def bit44(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit44 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit44")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit44",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit45(self) -> str | None:
        """Target ID of the Bit45 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit45")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit45.setter
    def bit45(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit45 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit45")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit45",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit46(self) -> str | None:
        """Target ID of the Bit46 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit46")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit46.setter
    def bit46(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit46 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit46")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit46",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit47(self) -> str | None:
        """Target ID of the Bit47 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit47")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit47.setter
    def bit47(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit47 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit47")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit47",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit48(self) -> str | None:
        """Target ID of the Bit48 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit48")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit48.setter
    def bit48(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit48 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit48")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit48",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit49(self) -> str | None:
        """Target ID of the Bit49 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit49")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit49.setter
    def bit49(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit49 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit49")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit49",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit50(self) -> str | None:
        """Target ID of the Bit50 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit50")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit50.setter
    def bit50(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit50 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit50")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit50",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit51(self) -> str | None:
        """Target ID of the Bit51 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit51")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit51.setter
    def bit51(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit51 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit51")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit51",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit52(self) -> str | None:
        """Target ID of the Bit52 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit52")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit52.setter
    def bit52(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit52 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit52")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit52",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit53(self) -> str | None:
        """Target ID of the Bit53 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit53")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit53.setter
    def bit53(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit53 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit53")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit53",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit54(self) -> str | None:
        """Target ID of the Bit54 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit54")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit54.setter
    def bit54(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit54 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit54")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit54",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit55(self) -> str | None:
        """Target ID of the Bit55 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit55")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit55.setter
    def bit55(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit55 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit55")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit55",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit56(self) -> str | None:
        """Target ID of the Bit56 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit56")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit56.setter
    def bit56(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit56 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit56")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit56",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit57(self) -> str | None:
        """Target ID of the Bit57 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit57")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit57.setter
    def bit57(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit57 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit57")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit57",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit58(self) -> str | None:
        """Target ID of the Bit58 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit58")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit58.setter
    def bit58(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit58 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit58")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit58",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit59(self) -> str | None:
        """Target ID of the Bit59 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit59")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit59.setter
    def bit59(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit59 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit59")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit59",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit60(self) -> str | None:
        """Target ID of the Bit60 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit60")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit60.setter
    def bit60(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit60 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit60")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit60",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit61(self) -> str | None:
        """Target ID of the Bit61 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit61")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit61.setter
    def bit61(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit61 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit61")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit61",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit62(self) -> str | None:
        """Target ID of the Bit62 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit62")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit62.setter
    def bit62(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit62 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit62")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit62",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def bit63(self) -> str | None:
        """Target ID of the Bit63 reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("Bit63")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit63.setter
    def bit63(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Bit63 reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit63")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit63",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

