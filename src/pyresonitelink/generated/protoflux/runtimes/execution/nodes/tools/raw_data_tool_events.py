"""Generated component: RawDataToolEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.raw_data_tool import RawDataTool
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawDataToolEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Raw Data Tool Events node takes in a referenced raw data tool, and depending on the actions or inputs from the user, this node will fire specific events. This can let the user make a custom tool to run any custom flux when connected from this node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Tools
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.RawDataToolEvents"

    def __init__(self, tool: str | IGlobalValueProxy[RawDataTool] | None = None, equipped: str | ISyncNodeOperation | None = None, dequipped: str | ISyncNodeOperation | None = None, tool_update: str | ISyncNodeOperation | None = None, primary_pressed: str | ISyncNodeOperation | None = None, primary_held: str | ISyncNodeOperation | None = None, primary_released: str | ISyncNodeOperation | None = None, secondary_pressed: str | ISyncNodeOperation | None = None, secondary_held: str | ISyncNodeOperation | None = None, secondary_released: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tool: Initial value for Tool.
            equipped: Initial value for Equipped.
            dequipped: Initial value for Dequipped.
            tool_update: Initial value for ToolUpdate.
            primary_pressed: Initial value for PrimaryPressed.
            primary_held: Initial value for PrimaryHeld.
            primary_released: Initial value for PrimaryReleased.
            secondary_pressed: Initial value for SecondaryPressed.
            secondary_held: Initial value for SecondaryHeld.
            secondary_released: Initial value for SecondaryReleased.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tool is not None:
            self.tool = tool
        if equipped is not None:
            self.equipped = equipped
        if dequipped is not None:
            self.dequipped = dequipped
        if tool_update is not None:
            self.tool_update = tool_update
        if primary_pressed is not None:
            self.primary_pressed = primary_pressed
        if primary_held is not None:
            self.primary_held = primary_held
        if primary_released is not None:
            self.primary_released = primary_released
        if secondary_pressed is not None:
            self.secondary_pressed = secondary_pressed
        if secondary_held is not None:
            self.secondary_held = secondary_held
        if secondary_released is not None:
            self.secondary_released = secondary_released

    @property
    def tool(self) -> str | None:
        """Target ID of the Tool reference (targets IGlobalValueProxy[RawDataTool])."""
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool.setter
    def tool(self, target: str | IGlobalValueProxy[RawDataTool] | None) -> None:
        """Set the Tool reference by target ID or IGlobalValueProxy[RawDataTool] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.RawDataTool>'),
            )

    @property
    def equipped(self) -> str | None:
        """Target ID of the Equipped reference (targets ISyncNodeOperation)."""
        member = self.get_member("Equipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipped.setter
    def equipped(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Equipped reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Equipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Equipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def dequipped(self) -> str | None:
        """Target ID of the Dequipped reference (targets ISyncNodeOperation)."""
        member = self.get_member("Dequipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dequipped.setter
    def dequipped(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Dequipped reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Dequipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dequipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def tool_update(self) -> str | None:
        """Target ID of the ToolUpdate reference (targets ISyncNodeOperation)."""
        member = self.get_member("ToolUpdate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool_update.setter
    def tool_update(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the ToolUpdate reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("ToolUpdate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ToolUpdate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def primary_pressed(self) -> str | None:
        """Target ID of the PrimaryPressed reference (targets ISyncNodeOperation)."""
        member = self.get_member("PrimaryPressed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_pressed.setter
    def primary_pressed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the PrimaryPressed reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("PrimaryPressed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PrimaryPressed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def primary_held(self) -> str | None:
        """Target ID of the PrimaryHeld reference (targets ISyncNodeOperation)."""
        member = self.get_member("PrimaryHeld")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_held.setter
    def primary_held(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the PrimaryHeld reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("PrimaryHeld")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PrimaryHeld",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def primary_released(self) -> str | None:
        """Target ID of the PrimaryReleased reference (targets ISyncNodeOperation)."""
        member = self.get_member("PrimaryReleased")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_released.setter
    def primary_released(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the PrimaryReleased reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("PrimaryReleased")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PrimaryReleased",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def secondary_pressed(self) -> str | None:
        """Target ID of the SecondaryPressed reference (targets ISyncNodeOperation)."""
        member = self.get_member("SecondaryPressed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_pressed.setter
    def secondary_pressed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the SecondaryPressed reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryPressed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryPressed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def secondary_held(self) -> str | None:
        """Target ID of the SecondaryHeld reference (targets ISyncNodeOperation)."""
        member = self.get_member("SecondaryHeld")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_held.setter
    def secondary_held(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the SecondaryHeld reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryHeld")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryHeld",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def secondary_released(self) -> str | None:
        """Target ID of the SecondaryReleased reference (targets ISyncNodeOperation)."""
        member = self.get_member("SecondaryReleased")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_released.setter
    def secondary_released(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the SecondaryReleased reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryReleased")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryReleased",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

