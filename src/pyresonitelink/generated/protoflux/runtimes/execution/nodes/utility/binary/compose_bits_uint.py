"""Generated component: ComposeBits_uint."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ComposeBits_uint(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_uint.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility/Binary
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_uint"

    def __init__(self, bit0: str | INodeValueOutput[bool] | None = None, bit1: str | INodeValueOutput[bool] | None = None, bit2: str | INodeValueOutput[bool] | None = None, bit3: str | INodeValueOutput[bool] | None = None, bit4: str | INodeValueOutput[bool] | None = None, bit5: str | INodeValueOutput[bool] | None = None, bit6: str | INodeValueOutput[bool] | None = None, bit7: str | INodeValueOutput[bool] | None = None, bit8: str | INodeValueOutput[bool] | None = None, bit9: str | INodeValueOutput[bool] | None = None, bit10: str | INodeValueOutput[bool] | None = None, bit11: str | INodeValueOutput[bool] | None = None, bit12: str | INodeValueOutput[bool] | None = None, bit13: str | INodeValueOutput[bool] | None = None, bit14: str | INodeValueOutput[bool] | None = None, bit15: str | INodeValueOutput[bool] | None = None, bit16: str | INodeValueOutput[bool] | None = None, bit17: str | INodeValueOutput[bool] | None = None, bit18: str | INodeValueOutput[bool] | None = None, bit19: str | INodeValueOutput[bool] | None = None, bit20: str | INodeValueOutput[bool] | None = None, bit21: str | INodeValueOutput[bool] | None = None, bit22: str | INodeValueOutput[bool] | None = None, bit23: str | INodeValueOutput[bool] | None = None, bit24: str | INodeValueOutput[bool] | None = None, bit25: str | INodeValueOutput[bool] | None = None, bit26: str | INodeValueOutput[bool] | None = None, bit27: str | INodeValueOutput[bool] | None = None, bit28: str | INodeValueOutput[bool] | None = None, bit29: str | INodeValueOutput[bool] | None = None, bit30: str | INodeValueOutput[bool] | None = None, bit31: str | INodeValueOutput[bool] | None = None, *, component: workers.Component | None = None) -> None:
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

    @property
    def bit0(self) -> str | None:
        """Target ID of the Bit0 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit0.setter
    def bit0(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit0 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit1 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit1.setter
    def bit1(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit1 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit2 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit2.setter
    def bit2(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit2 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit3 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit3.setter
    def bit3(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit3 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit4 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit4")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit4.setter
    def bit4(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit4 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit5 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit5")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit5.setter
    def bit5(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit5 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit6 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit6")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit6.setter
    def bit6(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit6 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit7 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit7")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit7.setter
    def bit7(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit7 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit8 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit8")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit8.setter
    def bit8(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit8 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit9 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit9")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit9.setter
    def bit9(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit9 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit10 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit10")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit10.setter
    def bit10(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit10 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit11 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit11")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit11.setter
    def bit11(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit11 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit12 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit12")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit12.setter
    def bit12(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit12 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit13 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit13")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit13.setter
    def bit13(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit13 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit14 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit14")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit14.setter
    def bit14(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit14 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit15 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit15")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit15.setter
    def bit15(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit15 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit16 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit16")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit16.setter
    def bit16(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit16 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit17 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit17")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit17.setter
    def bit17(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit17 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit18 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit18")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit18.setter
    def bit18(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit18 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit19 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit19")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit19.setter
    def bit19(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit19 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit20 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit20")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit20.setter
    def bit20(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit20 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit21 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit21")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit21.setter
    def bit21(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit21 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit22 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit22")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit22.setter
    def bit22(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit22 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit23 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit23")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit23.setter
    def bit23(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit23 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit24 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit24")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit24.setter
    def bit24(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit24 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit25 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit25")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit25.setter
    def bit25(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit25 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit26 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit26")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit26.setter
    def bit26(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit26 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit27 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit27")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit27.setter
    def bit27(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit27 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit28 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit28")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit28.setter
    def bit28(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit28 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit29 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit29")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit29.setter
    def bit29(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit29 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit30 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit30")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit30.setter
    def bit30(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit30 reference by target ID or INodeValueOutput[bool] instance."""
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
        """Target ID of the Bit31 reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Bit31")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bit31.setter
    def bit31(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Bit31 reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bit31")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bit31",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

