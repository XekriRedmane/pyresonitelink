"""Generated component: FormatAsTime."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iformat_provider import IFormatProvider
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FormatAsTime(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatAsTime.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Formatting
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatAsTime"

    def __init__(self, time: str | INodeValueOutput[np.float32] | None = None, decimal_places: str | INodeValueOutput[np.int32] | None = None, format_provider: str | INodeObjectOutput[IFormatProvider] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            time: Initial value for Time.
            decimal_places: Initial value for DecimalPlaces.
            format_provider: Initial value for FormatProvider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if time is not None:
            self.time = time
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if format_provider is not None:
            self.format_provider = format_provider

    @property
    def time(self) -> str | None:
        """Target ID of the Time reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @time.setter
    def time(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Time reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Time")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Time",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def decimal_places(self) -> str | None:
        """Target ID of the DecimalPlaces reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("DecimalPlaces")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @decimal_places.setter
    def decimal_places(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the DecimalPlaces reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DecimalPlaces")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DecimalPlaces",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def format_provider(self) -> str | None:
        """Target ID of the FormatProvider reference (targets INodeObjectOutput[IFormatProvider])."""
        member = self.get_member("FormatProvider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_provider.setter
    def format_provider(self, target: str | INodeObjectOutput[IFormatProvider] | None) -> None:
        """Set the FormatProvider reference by target ID or INodeObjectOutput[IFormatProvider] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FormatProvider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FormatProvider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<IFormatProvider>'),
            )

