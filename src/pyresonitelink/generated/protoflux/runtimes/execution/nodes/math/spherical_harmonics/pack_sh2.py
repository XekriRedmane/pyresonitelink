"""Generated component: PackSH2."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PackSH2(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Pack SH2 node takes in values and returns the SphericalHarmonicsL2 type.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Spherical Harmonics

    Parameterize with a value type::

        PackSH2[primitives.Float]
        PackSH2[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<>"

    def __init__(self, sh0: str | INodeValueOutput[T] | None = None, sh1: str | INodeValueOutput[T] | None = None, sh2: str | INodeValueOutput[T] | None = None, sh3: str | INodeValueOutput[T] | None = None, sh4: str | INodeValueOutput[T] | None = None, sh5: str | INodeValueOutput[T] | None = None, sh6: str | INodeValueOutput[T] | None = None, sh7: str | INodeValueOutput[T] | None = None, sh8: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
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

