"""Generated component: UnpackSH4."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.spherical_harmonics_l4 import SphericalHarmonicsL4
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnpackSH4(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Spherical Harmonics

    Parameterize with a value type::

        UnpackSH4[np.float32]
        UnpackSH4[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<>"

    def __init__(self, sh: str | INodeValueOutput[SphericalHarmonicsL4[T]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sh: Initial value for SH.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sh is not None:
            self.sh = sh

    @property
    def sh(self) -> str | None:
        """Target ID of the SH reference (targets INodeValueOutput[SphericalHarmonicsL4[T]])."""
        member = self.get_member("SH")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh.setter
    def sh(self, target: str | INodeValueOutput[SphericalHarmonicsL4[T]] | None) -> None:
        """Set the SH reference by target ID or INodeValueOutput[SphericalHarmonicsL4[T]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Elements.Core]Elements.Core.SphericalHarmonicsL4<T>>'),
            )

    @property
    def sh0(self) -> members.EmptyElement | None:
        """The SH0 member."""
        member = self.get_member("SH0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh0.setter
    def sh0(self, value: members.EmptyElement) -> None:
        """Set the SH0 member."""
        self.set_member("SH0", value)

    @property
    def sh1(self) -> members.EmptyElement | None:
        """The SH1 member."""
        member = self.get_member("SH1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh1.setter
    def sh1(self, value: members.EmptyElement) -> None:
        """Set the SH1 member."""
        self.set_member("SH1", value)

    @property
    def sh2(self) -> members.EmptyElement | None:
        """The SH2 member."""
        member = self.get_member("SH2")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh2.setter
    def sh2(self, value: members.EmptyElement) -> None:
        """Set the SH2 member."""
        self.set_member("SH2", value)

    @property
    def sh3(self) -> members.EmptyElement | None:
        """The SH3 member."""
        member = self.get_member("SH3")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh3.setter
    def sh3(self, value: members.EmptyElement) -> None:
        """Set the SH3 member."""
        self.set_member("SH3", value)

    @property
    def sh4(self) -> members.EmptyElement | None:
        """The SH4 member."""
        member = self.get_member("SH4")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh4.setter
    def sh4(self, value: members.EmptyElement) -> None:
        """Set the SH4 member."""
        self.set_member("SH4", value)

    @property
    def sh5(self) -> members.EmptyElement | None:
        """The SH5 member."""
        member = self.get_member("SH5")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh5.setter
    def sh5(self, value: members.EmptyElement) -> None:
        """Set the SH5 member."""
        self.set_member("SH5", value)

    @property
    def sh6(self) -> members.EmptyElement | None:
        """The SH6 member."""
        member = self.get_member("SH6")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh6.setter
    def sh6(self, value: members.EmptyElement) -> None:
        """Set the SH6 member."""
        self.set_member("SH6", value)

    @property
    def sh7(self) -> members.EmptyElement | None:
        """The SH7 member."""
        member = self.get_member("SH7")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh7.setter
    def sh7(self, value: members.EmptyElement) -> None:
        """Set the SH7 member."""
        self.set_member("SH7", value)

    @property
    def sh8(self) -> members.EmptyElement | None:
        """The SH8 member."""
        member = self.get_member("SH8")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh8.setter
    def sh8(self, value: members.EmptyElement) -> None:
        """Set the SH8 member."""
        self.set_member("SH8", value)

    @property
    def sh9(self) -> members.EmptyElement | None:
        """The SH9 member."""
        member = self.get_member("SH9")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh9.setter
    def sh9(self, value: members.EmptyElement) -> None:
        """Set the SH9 member."""
        self.set_member("SH9", value)

    @property
    def sh10(self) -> members.EmptyElement | None:
        """The SH10 member."""
        member = self.get_member("SH10")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh10.setter
    def sh10(self, value: members.EmptyElement) -> None:
        """Set the SH10 member."""
        self.set_member("SH10", value)

    @property
    def sh11(self) -> members.EmptyElement | None:
        """The SH11 member."""
        member = self.get_member("SH11")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh11.setter
    def sh11(self, value: members.EmptyElement) -> None:
        """Set the SH11 member."""
        self.set_member("SH11", value)

    @property
    def sh12(self) -> members.EmptyElement | None:
        """The SH12 member."""
        member = self.get_member("SH12")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh12.setter
    def sh12(self, value: members.EmptyElement) -> None:
        """Set the SH12 member."""
        self.set_member("SH12", value)

    @property
    def sh13(self) -> members.EmptyElement | None:
        """The SH13 member."""
        member = self.get_member("SH13")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh13.setter
    def sh13(self, value: members.EmptyElement) -> None:
        """Set the SH13 member."""
        self.set_member("SH13", value)

    @property
    def sh14(self) -> members.EmptyElement | None:
        """The SH14 member."""
        member = self.get_member("SH14")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh14.setter
    def sh14(self, value: members.EmptyElement) -> None:
        """Set the SH14 member."""
        self.set_member("SH14", value)

    @property
    def sh15(self) -> members.EmptyElement | None:
        """The SH15 member."""
        member = self.get_member("SH15")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh15.setter
    def sh15(self, value: members.EmptyElement) -> None:
        """Set the SH15 member."""
        self.set_member("SH15", value)

    @property
    def sh16(self) -> members.EmptyElement | None:
        """The SH16 member."""
        member = self.get_member("SH16")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh16.setter
    def sh16(self, value: members.EmptyElement) -> None:
        """Set the SH16 member."""
        self.set_member("SH16", value)

    @property
    def sh17(self) -> members.EmptyElement | None:
        """The SH17 member."""
        member = self.get_member("SH17")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh17.setter
    def sh17(self, value: members.EmptyElement) -> None:
        """Set the SH17 member."""
        self.set_member("SH17", value)

    @property
    def sh18(self) -> members.EmptyElement | None:
        """The SH18 member."""
        member = self.get_member("SH18")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh18.setter
    def sh18(self, value: members.EmptyElement) -> None:
        """Set the SH18 member."""
        self.set_member("SH18", value)

    @property
    def sh19(self) -> members.EmptyElement | None:
        """The SH19 member."""
        member = self.get_member("SH19")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh19.setter
    def sh19(self, value: members.EmptyElement) -> None:
        """Set the SH19 member."""
        self.set_member("SH19", value)

    @property
    def sh20(self) -> members.EmptyElement | None:
        """The SH20 member."""
        member = self.get_member("SH20")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh20.setter
    def sh20(self, value: members.EmptyElement) -> None:
        """Set the SH20 member."""
        self.set_member("SH20", value)

    @property
    def sh21(self) -> members.EmptyElement | None:
        """The SH21 member."""
        member = self.get_member("SH21")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh21.setter
    def sh21(self, value: members.EmptyElement) -> None:
        """Set the SH21 member."""
        self.set_member("SH21", value)

    @property
    def sh22(self) -> members.EmptyElement | None:
        """The SH22 member."""
        member = self.get_member("SH22")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh22.setter
    def sh22(self, value: members.EmptyElement) -> None:
        """Set the SH22 member."""
        self.set_member("SH22", value)

    @property
    def sh23(self) -> members.EmptyElement | None:
        """The SH23 member."""
        member = self.get_member("SH23")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh23.setter
    def sh23(self, value: members.EmptyElement) -> None:
        """Set the SH23 member."""
        self.set_member("SH23", value)

    @property
    def sh24(self) -> members.EmptyElement | None:
        """The SH24 member."""
        member = self.get_member("SH24")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sh24.setter
    def sh24(self, value: members.EmptyElement) -> None:
        """Set the SH24 member."""
        self.set_member("SH24", value)

