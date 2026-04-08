"""Generated component: ScaleOrdersSH3."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.spherical_harmonics_l3 import SphericalHarmonicsL3
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleOrdersSH3(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Spherical Harmonics

    Parameterize with a value type::

        ScaleOrdersSH3[primitives.Float]
        ScaleOrdersSH3[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<>"

    def __init__(self, sh: str | INodeValueOutput[SphericalHarmonicsL3[T]] | None = None, order0: str | INodeValueOutput[primitives.Float] | None = None, order1: str | INodeValueOutput[primitives.Float] | None = None, order2: str | INodeValueOutput[primitives.Float] | None = None, order3: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sh: Initial value for SH.
            order0: Initial value for Order0.
            order1: Initial value for Order1.
            order2: Initial value for Order2.
            order3: Initial value for Order3.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sh is not None:
            self.sh = sh
        if order0 is not None:
            self.order0 = order0
        if order1 is not None:
            self.order1 = order1
        if order2 is not None:
            self.order2 = order2
        if order3 is not None:
            self.order3 = order3

    @property
    def sh(self) -> str | None:
        """Target ID of the SH reference (targets INodeValueOutput[SphericalHarmonicsL3[T]])."""
        member = self.get_member("SH")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh.setter
    def sh(self, target: str | INodeValueOutput[SphericalHarmonicsL3[T]] | None) -> None:
        """Set the SH reference by target ID or INodeValueOutput[SphericalHarmonicsL3[T]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Elements.Core]Elements.Core.SphericalHarmonicsL3<T>>'),
            )

    @property
    def order0(self) -> str | None:
        """Target ID of the Order0 reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Order0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @order0.setter
    def order0(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Order0 reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Order0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Order0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def order1(self) -> str | None:
        """Target ID of the Order1 reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Order1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @order1.setter
    def order1(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Order1 reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Order1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Order1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def order2(self) -> str | None:
        """Target ID of the Order2 reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Order2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @order2.setter
    def order2(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Order2 reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Order2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Order2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def order3(self) -> str | None:
        """Target ID of the Order3 reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Order3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @order3.setter
    def order3(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Order3 reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Order3")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Order3",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

