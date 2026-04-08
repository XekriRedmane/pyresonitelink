"""Generated component: ExtractBits_int."""

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


class ExtractBits_int(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_int.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_int"

    def __init__(self, integer: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Integer reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Integer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @integer.setter
    def integer(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Integer reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Integer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Integer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
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

