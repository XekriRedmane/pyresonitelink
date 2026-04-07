"""Generated component: WavelengthColor."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WavelengthColor(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.WavelengthColor.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Colors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.WavelengthColor"

    def __init__(self, wavelength: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            wavelength: Initial value for Wavelength.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if wavelength is not None:
            self.wavelength = wavelength

    @property
    def wavelength(self) -> str | None:
        """Target ID of the Wavelength reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Wavelength")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @wavelength.setter
    def wavelength(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Wavelength reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Wavelength")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Wavelength",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

