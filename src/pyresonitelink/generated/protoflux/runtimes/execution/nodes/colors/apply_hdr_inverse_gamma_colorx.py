"""Generated component: ApplyHDRInverseGammaColorX."""

import numpy as np

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


class ApplyHDRInverseGammaColorX(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ApplyHDRInverseGammaColorX.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ApplyHDRInverseGammaColorX"

    def __init__(self, color: str | INodeValueOutput[primitives.ColorX] | None = None, gamma: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            color: Initial value for Color.
            gamma: Initial value for Gamma.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if color is not None:
            self.color = color
        if gamma is not None:
            self.gamma = gamma

    @property
    def color(self) -> str | None:
        """Target ID of the Color reference (targets INodeValueOutput[primitives.ColorX])."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the Color reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def gamma(self) -> str | None:
        """Target ID of the Gamma reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Gamma")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gamma.setter
    def gamma(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Gamma reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Gamma")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Gamma",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

