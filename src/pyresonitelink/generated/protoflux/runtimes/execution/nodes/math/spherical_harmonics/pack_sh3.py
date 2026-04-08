"""Generated component: PackSH3."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PackSH3(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Pack SH3 node takes in values and returns the SphericalHarmonicsL3 type.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Spherical Harmonics

    Parameterize with a value type::

        PackSH3[primitives.Float]
        PackSH3[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<>"

    def __init__(self, sh0: str | INodeValueOutput[T] | None = None, sh1: str | INodeValueOutput[T] | None = None, sh2: str | INodeValueOutput[T] | None = None, sh3: str | INodeValueOutput[T] | None = None, sh4: str | INodeValueOutput[T] | None = None, sh5: str | INodeValueOutput[T] | None = None, sh6: str | INodeValueOutput[T] | None = None, sh7: str | INodeValueOutput[T] | None = None, sh8: str | INodeValueOutput[T] | None = None, sh9: str | INodeValueOutput[T] | None = None, sh10: str | INodeValueOutput[T] | None = None, sh11: str | INodeValueOutput[T] | None = None, sh12: str | INodeValueOutput[T] | None = None, sh13: str | INodeValueOutput[T] | None = None, sh14: str | INodeValueOutput[T] | None = None, sh15: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sh0: Initial value for SH0.
            sh1: Initial value for SH1.
            sh2: Initial value for SH2.
            sh3: Initial value for SH3.
            sh4: Initial value for SH4.
            sh5: Initial value for SH5.
            sh6: Initial value for SH6.
            sh7: Initial value for SH7.
            sh8: Initial value for SH8.
            sh9: Initial value for SH9.
            sh10: Initial value for SH10.
            sh11: Initial value for SH11.
            sh12: Initial value for SH12.
            sh13: Initial value for SH13.
            sh14: Initial value for SH14.
            sh15: Initial value for SH15.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sh0 is not None:
            self.sh0 = sh0
        if sh1 is not None:
            self.sh1 = sh1
        if sh2 is not None:
            self.sh2 = sh2
        if sh3 is not None:
            self.sh3 = sh3
        if sh4 is not None:
            self.sh4 = sh4
        if sh5 is not None:
            self.sh5 = sh5
        if sh6 is not None:
            self.sh6 = sh6
        if sh7 is not None:
            self.sh7 = sh7
        if sh8 is not None:
            self.sh8 = sh8
        if sh9 is not None:
            self.sh9 = sh9
        if sh10 is not None:
            self.sh10 = sh10
        if sh11 is not None:
            self.sh11 = sh11
        if sh12 is not None:
            self.sh12 = sh12
        if sh13 is not None:
            self.sh13 = sh13
        if sh14 is not None:
            self.sh14 = sh14
        if sh15 is not None:
            self.sh15 = sh15

    @property
    def sh0(self) -> str | None:
        """Target ID of the SH0 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh0.setter
    def sh0(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH0 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh1(self) -> str | None:
        """Target ID of the SH1 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh1.setter
    def sh1(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH1 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh2(self) -> str | None:
        """Target ID of the SH2 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh2.setter
    def sh2(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH2 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh3(self) -> str | None:
        """Target ID of the SH3 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh3.setter
    def sh3(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH3 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH3")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH3",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh4(self) -> str | None:
        """Target ID of the SH4 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH4")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh4.setter
    def sh4(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH4 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH4")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH4",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh5(self) -> str | None:
        """Target ID of the SH5 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH5")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh5.setter
    def sh5(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH5 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH5")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH5",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh6(self) -> str | None:
        """Target ID of the SH6 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH6")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh6.setter
    def sh6(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH6 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH6")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH6",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh7(self) -> str | None:
        """Target ID of the SH7 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH7")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh7.setter
    def sh7(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH7 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH7")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH7",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh8(self) -> str | None:
        """Target ID of the SH8 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH8")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh8.setter
    def sh8(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH8 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH8")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH8",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh9(self) -> str | None:
        """Target ID of the SH9 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH9")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh9.setter
    def sh9(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH9 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH9")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH9",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh10(self) -> str | None:
        """Target ID of the SH10 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH10")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh10.setter
    def sh10(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH10 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH10")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH10",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh11(self) -> str | None:
        """Target ID of the SH11 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH11")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh11.setter
    def sh11(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH11 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH11")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH11",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh12(self) -> str | None:
        """Target ID of the SH12 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH12")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh12.setter
    def sh12(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH12 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH12")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH12",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh13(self) -> str | None:
        """Target ID of the SH13 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH13")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh13.setter
    def sh13(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH13 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH13")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH13",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh14(self) -> str | None:
        """Target ID of the SH14 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH14")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh14.setter
    def sh14(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH14 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH14")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH14",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def sh15(self) -> str | None:
        """Target ID of the SH15 reference (targets INodeValueOutput[T])."""
        member = self.get_member("SH15")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh15.setter
    def sh15(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the SH15 reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH15")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH15",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

