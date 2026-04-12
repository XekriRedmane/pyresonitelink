"""Generated component: EquipTool."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EquipTool(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Equip Tool node equips a tool to the user, optionally dequipping an existing tool.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Tools
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.EquipTool"

    def __init__(self, tool: str | INodeObjectOutput[ITool] | None = None, user: str | INodeObjectOutput[User] | None = None, side: str | INodeValueOutput[Chirality] | None = None, dequip_existing: str | INodeValueOutput[primitives.Bool] | None = None, on_equipped: str | INodeOperation | None = None, on_equip_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tool: Initial value for Tool.
            user: Initial value for User.
            side: Initial value for Side.
            dequip_existing: Initial value for DequipExisting.
            on_equipped: Initial value for OnEquipped.
            on_equip_fail: Initial value for OnEquipFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tool is not None:
            self.tool = tool
        if user is not None:
            self.user = user
        if side is not None:
            self.side = side
        if dequip_existing is not None:
            self.dequip_existing = dequip_existing
        if on_equipped is not None:
            self.on_equipped = on_equipped
        if on_equip_fail is not None:
            self.on_equip_fail = on_equip_fail

    @property
    def tool(self) -> str | None:
        """The tool to equip.

If the tool is null or the tool is already equipped ``OnEquipFail`` will fire."""
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool.setter
    def tool(self, target: str | INodeObjectOutput[ITool] | None) -> None:
        """Set the Tool reference by target ID or INodeObjectOutput[ITool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.ITool>'),
            )

    @property
    def user(self) -> str | None:
        """The user to equip the tool to.

If the user is null then the execution context's local user will be used, and if that local user is null then ``OnEquipFail`` will fire."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the User reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def side(self) -> str | None:
        """The chirality of the user to equip this tool.

If an interaction handler for the side can not be found then ``OnEquipFail`` will fire."""
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side.setter
    def side(self, target: str | INodeValueOutput[Chirality] | None) -> None:
        """Set the Side reference by target ID or INodeValueOutput[Chirality] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Side",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>'),
            )

    @property
    def dequip_existing(self) -> str | None:
        """Should this tool dequip an already held tool.

If an another tool is already equipped and ``DequipExisting`` is false then ``OnEquipFail`` will fire."""
        member = self.get_member("DequipExisting")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dequip_existing.setter
    def dequip_existing(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the DequipExisting reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DequipExisting")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DequipExisting",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_equipped(self) -> str | None:
        """Fires if the tool successfully equips to a user."""
        member = self.get_member("OnEquipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_equipped.setter
    def on_equipped(self, target: str | INodeOperation | None) -> None:
        """Set the OnEquipped reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnEquipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnEquipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_equip_fail(self) -> str | None:
        """Fires if the tool fails to equip."""
        member = self.get_member("OnEquipFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_equip_fail.setter
    def on_equip_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnEquipFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnEquipFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnEquipFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

