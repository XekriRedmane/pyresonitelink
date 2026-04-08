"""Generated component: ExtractBits_long."""

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


class ExtractBits_long(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_long.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_long"

    def __init__(self, integer: str | INodeValueOutput[primitives.Long] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            integer: Initial value for Integer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if integer is not None:
            self.integer = integer

    @property
    def integer(self) -> str | None:
        """Target ID of the Integer reference (targets INodeValueOutput[primitives.Long])."""
        member = self.get_member("Integer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @integer.setter
    def integer(self, target: str | INodeValueOutput[primitives.Long] | None) -> None:
        """Set the Integer reference by target ID or INodeValueOutput[primitives.Long] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Integer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Integer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<long>'),
            )

    @property
    def bit0(self) -> members.EmptyElement | None:
        """The Bit0 member."""
        member = self.get_member("Bit0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit0.setter
    def bit0(self, value: members.EmptyElement) -> None:
        """Set the Bit0 member."""
        self.set_member("Bit0", value)

    @property
    def bit1(self) -> members.EmptyElement | None:
        """The Bit1 member."""
        member = self.get_member("Bit1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit1.setter
    def bit1(self, value: members.EmptyElement) -> None:
        """Set the Bit1 member."""
        self.set_member("Bit1", value)

    @property
    def bit2(self) -> members.EmptyElement | None:
        """The Bit2 member."""
        member = self.get_member("Bit2")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit2.setter
    def bit2(self, value: members.EmptyElement) -> None:
        """Set the Bit2 member."""
        self.set_member("Bit2", value)

    @property
    def bit3(self) -> members.EmptyElement | None:
        """The Bit3 member."""
        member = self.get_member("Bit3")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit3.setter
    def bit3(self, value: members.EmptyElement) -> None:
        """Set the Bit3 member."""
        self.set_member("Bit3", value)

    @property
    def bit4(self) -> members.EmptyElement | None:
        """The Bit4 member."""
        member = self.get_member("Bit4")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit4.setter
    def bit4(self, value: members.EmptyElement) -> None:
        """Set the Bit4 member."""
        self.set_member("Bit4", value)

    @property
    def bit5(self) -> members.EmptyElement | None:
        """The Bit5 member."""
        member = self.get_member("Bit5")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit5.setter
    def bit5(self, value: members.EmptyElement) -> None:
        """Set the Bit5 member."""
        self.set_member("Bit5", value)

    @property
    def bit6(self) -> members.EmptyElement | None:
        """The Bit6 member."""
        member = self.get_member("Bit6")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit6.setter
    def bit6(self, value: members.EmptyElement) -> None:
        """Set the Bit6 member."""
        self.set_member("Bit6", value)

    @property
    def bit7(self) -> members.EmptyElement | None:
        """The Bit7 member."""
        member = self.get_member("Bit7")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit7.setter
    def bit7(self, value: members.EmptyElement) -> None:
        """Set the Bit7 member."""
        self.set_member("Bit7", value)

    @property
    def bit8(self) -> members.EmptyElement | None:
        """The Bit8 member."""
        member = self.get_member("Bit8")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit8.setter
    def bit8(self, value: members.EmptyElement) -> None:
        """Set the Bit8 member."""
        self.set_member("Bit8", value)

    @property
    def bit9(self) -> members.EmptyElement | None:
        """The Bit9 member."""
        member = self.get_member("Bit9")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit9.setter
    def bit9(self, value: members.EmptyElement) -> None:
        """Set the Bit9 member."""
        self.set_member("Bit9", value)

    @property
    def bit10(self) -> members.EmptyElement | None:
        """The Bit10 member."""
        member = self.get_member("Bit10")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit10.setter
    def bit10(self, value: members.EmptyElement) -> None:
        """Set the Bit10 member."""
        self.set_member("Bit10", value)

    @property
    def bit11(self) -> members.EmptyElement | None:
        """The Bit11 member."""
        member = self.get_member("Bit11")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit11.setter
    def bit11(self, value: members.EmptyElement) -> None:
        """Set the Bit11 member."""
        self.set_member("Bit11", value)

    @property
    def bit12(self) -> members.EmptyElement | None:
        """The Bit12 member."""
        member = self.get_member("Bit12")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit12.setter
    def bit12(self, value: members.EmptyElement) -> None:
        """Set the Bit12 member."""
        self.set_member("Bit12", value)

    @property
    def bit13(self) -> members.EmptyElement | None:
        """The Bit13 member."""
        member = self.get_member("Bit13")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit13.setter
    def bit13(self, value: members.EmptyElement) -> None:
        """Set the Bit13 member."""
        self.set_member("Bit13", value)

    @property
    def bit14(self) -> members.EmptyElement | None:
        """The Bit14 member."""
        member = self.get_member("Bit14")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit14.setter
    def bit14(self, value: members.EmptyElement) -> None:
        """Set the Bit14 member."""
        self.set_member("Bit14", value)

    @property
    def bit15(self) -> members.EmptyElement | None:
        """The Bit15 member."""
        member = self.get_member("Bit15")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit15.setter
    def bit15(self, value: members.EmptyElement) -> None:
        """Set the Bit15 member."""
        self.set_member("Bit15", value)

    @property
    def bit16(self) -> members.EmptyElement | None:
        """The Bit16 member."""
        member = self.get_member("Bit16")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit16.setter
    def bit16(self, value: members.EmptyElement) -> None:
        """Set the Bit16 member."""
        self.set_member("Bit16", value)

    @property
    def bit17(self) -> members.EmptyElement | None:
        """The Bit17 member."""
        member = self.get_member("Bit17")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit17.setter
    def bit17(self, value: members.EmptyElement) -> None:
        """Set the Bit17 member."""
        self.set_member("Bit17", value)

    @property
    def bit18(self) -> members.EmptyElement | None:
        """The Bit18 member."""
        member = self.get_member("Bit18")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit18.setter
    def bit18(self, value: members.EmptyElement) -> None:
        """Set the Bit18 member."""
        self.set_member("Bit18", value)

    @property
    def bit19(self) -> members.EmptyElement | None:
        """The Bit19 member."""
        member = self.get_member("Bit19")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit19.setter
    def bit19(self, value: members.EmptyElement) -> None:
        """Set the Bit19 member."""
        self.set_member("Bit19", value)

    @property
    def bit20(self) -> members.EmptyElement | None:
        """The Bit20 member."""
        member = self.get_member("Bit20")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit20.setter
    def bit20(self, value: members.EmptyElement) -> None:
        """Set the Bit20 member."""
        self.set_member("Bit20", value)

    @property
    def bit21(self) -> members.EmptyElement | None:
        """The Bit21 member."""
        member = self.get_member("Bit21")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit21.setter
    def bit21(self, value: members.EmptyElement) -> None:
        """Set the Bit21 member."""
        self.set_member("Bit21", value)

    @property
    def bit22(self) -> members.EmptyElement | None:
        """The Bit22 member."""
        member = self.get_member("Bit22")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit22.setter
    def bit22(self, value: members.EmptyElement) -> None:
        """Set the Bit22 member."""
        self.set_member("Bit22", value)

    @property
    def bit23(self) -> members.EmptyElement | None:
        """The Bit23 member."""
        member = self.get_member("Bit23")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit23.setter
    def bit23(self, value: members.EmptyElement) -> None:
        """Set the Bit23 member."""
        self.set_member("Bit23", value)

    @property
    def bit24(self) -> members.EmptyElement | None:
        """The Bit24 member."""
        member = self.get_member("Bit24")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit24.setter
    def bit24(self, value: members.EmptyElement) -> None:
        """Set the Bit24 member."""
        self.set_member("Bit24", value)

    @property
    def bit25(self) -> members.EmptyElement | None:
        """The Bit25 member."""
        member = self.get_member("Bit25")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit25.setter
    def bit25(self, value: members.EmptyElement) -> None:
        """Set the Bit25 member."""
        self.set_member("Bit25", value)

    @property
    def bit26(self) -> members.EmptyElement | None:
        """The Bit26 member."""
        member = self.get_member("Bit26")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit26.setter
    def bit26(self, value: members.EmptyElement) -> None:
        """Set the Bit26 member."""
        self.set_member("Bit26", value)

    @property
    def bit27(self) -> members.EmptyElement | None:
        """The Bit27 member."""
        member = self.get_member("Bit27")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit27.setter
    def bit27(self, value: members.EmptyElement) -> None:
        """Set the Bit27 member."""
        self.set_member("Bit27", value)

    @property
    def bit28(self) -> members.EmptyElement | None:
        """The Bit28 member."""
        member = self.get_member("Bit28")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit28.setter
    def bit28(self, value: members.EmptyElement) -> None:
        """Set the Bit28 member."""
        self.set_member("Bit28", value)

    @property
    def bit29(self) -> members.EmptyElement | None:
        """The Bit29 member."""
        member = self.get_member("Bit29")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit29.setter
    def bit29(self, value: members.EmptyElement) -> None:
        """Set the Bit29 member."""
        self.set_member("Bit29", value)

    @property
    def bit30(self) -> members.EmptyElement | None:
        """The Bit30 member."""
        member = self.get_member("Bit30")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit30.setter
    def bit30(self, value: members.EmptyElement) -> None:
        """Set the Bit30 member."""
        self.set_member("Bit30", value)

    @property
    def bit31(self) -> members.EmptyElement | None:
        """The Bit31 member."""
        member = self.get_member("Bit31")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit31.setter
    def bit31(self, value: members.EmptyElement) -> None:
        """Set the Bit31 member."""
        self.set_member("Bit31", value)

    @property
    def bit32(self) -> members.EmptyElement | None:
        """The Bit32 member."""
        member = self.get_member("Bit32")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit32.setter
    def bit32(self, value: members.EmptyElement) -> None:
        """Set the Bit32 member."""
        self.set_member("Bit32", value)

    @property
    def bit33(self) -> members.EmptyElement | None:
        """The Bit33 member."""
        member = self.get_member("Bit33")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit33.setter
    def bit33(self, value: members.EmptyElement) -> None:
        """Set the Bit33 member."""
        self.set_member("Bit33", value)

    @property
    def bit34(self) -> members.EmptyElement | None:
        """The Bit34 member."""
        member = self.get_member("Bit34")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit34.setter
    def bit34(self, value: members.EmptyElement) -> None:
        """Set the Bit34 member."""
        self.set_member("Bit34", value)

    @property
    def bit35(self) -> members.EmptyElement | None:
        """The Bit35 member."""
        member = self.get_member("Bit35")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit35.setter
    def bit35(self, value: members.EmptyElement) -> None:
        """Set the Bit35 member."""
        self.set_member("Bit35", value)

    @property
    def bit36(self) -> members.EmptyElement | None:
        """The Bit36 member."""
        member = self.get_member("Bit36")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit36.setter
    def bit36(self, value: members.EmptyElement) -> None:
        """Set the Bit36 member."""
        self.set_member("Bit36", value)

    @property
    def bit37(self) -> members.EmptyElement | None:
        """The Bit37 member."""
        member = self.get_member("Bit37")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit37.setter
    def bit37(self, value: members.EmptyElement) -> None:
        """Set the Bit37 member."""
        self.set_member("Bit37", value)

    @property
    def bit38(self) -> members.EmptyElement | None:
        """The Bit38 member."""
        member = self.get_member("Bit38")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit38.setter
    def bit38(self, value: members.EmptyElement) -> None:
        """Set the Bit38 member."""
        self.set_member("Bit38", value)

    @property
    def bit39(self) -> members.EmptyElement | None:
        """The Bit39 member."""
        member = self.get_member("Bit39")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit39.setter
    def bit39(self, value: members.EmptyElement) -> None:
        """Set the Bit39 member."""
        self.set_member("Bit39", value)

    @property
    def bit40(self) -> members.EmptyElement | None:
        """The Bit40 member."""
        member = self.get_member("Bit40")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit40.setter
    def bit40(self, value: members.EmptyElement) -> None:
        """Set the Bit40 member."""
        self.set_member("Bit40", value)

    @property
    def bit41(self) -> members.EmptyElement | None:
        """The Bit41 member."""
        member = self.get_member("Bit41")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit41.setter
    def bit41(self, value: members.EmptyElement) -> None:
        """Set the Bit41 member."""
        self.set_member("Bit41", value)

    @property
    def bit42(self) -> members.EmptyElement | None:
        """The Bit42 member."""
        member = self.get_member("Bit42")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit42.setter
    def bit42(self, value: members.EmptyElement) -> None:
        """Set the Bit42 member."""
        self.set_member("Bit42", value)

    @property
    def bit43(self) -> members.EmptyElement | None:
        """The Bit43 member."""
        member = self.get_member("Bit43")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit43.setter
    def bit43(self, value: members.EmptyElement) -> None:
        """Set the Bit43 member."""
        self.set_member("Bit43", value)

    @property
    def bit44(self) -> members.EmptyElement | None:
        """The Bit44 member."""
        member = self.get_member("Bit44")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit44.setter
    def bit44(self, value: members.EmptyElement) -> None:
        """Set the Bit44 member."""
        self.set_member("Bit44", value)

    @property
    def bit45(self) -> members.EmptyElement | None:
        """The Bit45 member."""
        member = self.get_member("Bit45")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit45.setter
    def bit45(self, value: members.EmptyElement) -> None:
        """Set the Bit45 member."""
        self.set_member("Bit45", value)

    @property
    def bit46(self) -> members.EmptyElement | None:
        """The Bit46 member."""
        member = self.get_member("Bit46")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit46.setter
    def bit46(self, value: members.EmptyElement) -> None:
        """Set the Bit46 member."""
        self.set_member("Bit46", value)

    @property
    def bit47(self) -> members.EmptyElement | None:
        """The Bit47 member."""
        member = self.get_member("Bit47")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit47.setter
    def bit47(self, value: members.EmptyElement) -> None:
        """Set the Bit47 member."""
        self.set_member("Bit47", value)

    @property
    def bit48(self) -> members.EmptyElement | None:
        """The Bit48 member."""
        member = self.get_member("Bit48")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit48.setter
    def bit48(self, value: members.EmptyElement) -> None:
        """Set the Bit48 member."""
        self.set_member("Bit48", value)

    @property
    def bit49(self) -> members.EmptyElement | None:
        """The Bit49 member."""
        member = self.get_member("Bit49")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit49.setter
    def bit49(self, value: members.EmptyElement) -> None:
        """Set the Bit49 member."""
        self.set_member("Bit49", value)

    @property
    def bit50(self) -> members.EmptyElement | None:
        """The Bit50 member."""
        member = self.get_member("Bit50")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit50.setter
    def bit50(self, value: members.EmptyElement) -> None:
        """Set the Bit50 member."""
        self.set_member("Bit50", value)

    @property
    def bit51(self) -> members.EmptyElement | None:
        """The Bit51 member."""
        member = self.get_member("Bit51")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit51.setter
    def bit51(self, value: members.EmptyElement) -> None:
        """Set the Bit51 member."""
        self.set_member("Bit51", value)

    @property
    def bit52(self) -> members.EmptyElement | None:
        """The Bit52 member."""
        member = self.get_member("Bit52")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit52.setter
    def bit52(self, value: members.EmptyElement) -> None:
        """Set the Bit52 member."""
        self.set_member("Bit52", value)

    @property
    def bit53(self) -> members.EmptyElement | None:
        """The Bit53 member."""
        member = self.get_member("Bit53")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit53.setter
    def bit53(self, value: members.EmptyElement) -> None:
        """Set the Bit53 member."""
        self.set_member("Bit53", value)

    @property
    def bit54(self) -> members.EmptyElement | None:
        """The Bit54 member."""
        member = self.get_member("Bit54")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit54.setter
    def bit54(self, value: members.EmptyElement) -> None:
        """Set the Bit54 member."""
        self.set_member("Bit54", value)

    @property
    def bit55(self) -> members.EmptyElement | None:
        """The Bit55 member."""
        member = self.get_member("Bit55")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit55.setter
    def bit55(self, value: members.EmptyElement) -> None:
        """Set the Bit55 member."""
        self.set_member("Bit55", value)

    @property
    def bit56(self) -> members.EmptyElement | None:
        """The Bit56 member."""
        member = self.get_member("Bit56")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit56.setter
    def bit56(self, value: members.EmptyElement) -> None:
        """Set the Bit56 member."""
        self.set_member("Bit56", value)

    @property
    def bit57(self) -> members.EmptyElement | None:
        """The Bit57 member."""
        member = self.get_member("Bit57")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit57.setter
    def bit57(self, value: members.EmptyElement) -> None:
        """Set the Bit57 member."""
        self.set_member("Bit57", value)

    @property
    def bit58(self) -> members.EmptyElement | None:
        """The Bit58 member."""
        member = self.get_member("Bit58")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit58.setter
    def bit58(self, value: members.EmptyElement) -> None:
        """Set the Bit58 member."""
        self.set_member("Bit58", value)

    @property
    def bit59(self) -> members.EmptyElement | None:
        """The Bit59 member."""
        member = self.get_member("Bit59")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit59.setter
    def bit59(self, value: members.EmptyElement) -> None:
        """Set the Bit59 member."""
        self.set_member("Bit59", value)

    @property
    def bit60(self) -> members.EmptyElement | None:
        """The Bit60 member."""
        member = self.get_member("Bit60")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit60.setter
    def bit60(self, value: members.EmptyElement) -> None:
        """Set the Bit60 member."""
        self.set_member("Bit60", value)

    @property
    def bit61(self) -> members.EmptyElement | None:
        """The Bit61 member."""
        member = self.get_member("Bit61")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit61.setter
    def bit61(self, value: members.EmptyElement) -> None:
        """Set the Bit61 member."""
        self.set_member("Bit61", value)

    @property
    def bit62(self) -> members.EmptyElement | None:
        """The Bit62 member."""
        member = self.get_member("Bit62")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit62.setter
    def bit62(self, value: members.EmptyElement) -> None:
        """Set the Bit62 member."""
        self.set_member("Bit62", value)

    @property
    def bit63(self) -> members.EmptyElement | None:
        """The Bit63 member."""
        member = self.get_member("Bit63")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bit63.setter
    def bit63(self, value: members.EmptyElement) -> None:
        """Set the Bit63 member."""
        self.set_member("Bit63", value)

