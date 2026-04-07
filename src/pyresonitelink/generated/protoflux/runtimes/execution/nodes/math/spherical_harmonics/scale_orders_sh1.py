"""Generated component: ScaleOrdersSH1."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.spherical_harmonics_l1 import SphericalHarmonicsL1
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleOrdersSH1(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Spherical Harmonics

    Parameterize with a value type::

        ScaleOrdersSH1[np.float32]
        ScaleOrdersSH1[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<>"

    def __init__(self, sh: str | INodeValueOutput[SphericalHarmonicsL1[T]] | None = None, order0: str | INodeValueOutput[np.float32] | None = None, order1: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sh: Initial value for SH.
            order0: Initial value for Order0.
            order1: Initial value for Order1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sh is not None:
            self.sh = sh
        if order0 is not None:
            self.order0 = order0
        if order1 is not None:
            self.order1 = order1

    @property
    def sh(self) -> str | None:
        """Target ID of the SH reference (targets INodeValueOutput[SphericalHarmonicsL1[T]])."""
        member = self.get_member("SH")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sh.setter
    def sh(self, target: str | INodeValueOutput[SphericalHarmonicsL1[T]] | None) -> None:
        """Set the SH reference by target ID or INodeValueOutput[SphericalHarmonicsL1[T]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SH")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SH",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Elements.Core]Elements.Core.SphericalHarmonicsL1<T>>'),
            )

    @property
    def order0(self) -> str | None:
        """Target ID of the Order0 reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Order0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @order0.setter
    def order0(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Order0 reference by target ID or INodeValueOutput[np.float32] instance."""
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
        """Target ID of the Order1 reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Order1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @order1.setter
    def order1(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Order1 reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Order1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Order1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

