"""Generated component: ObjectSlicerTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectSlicerTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ObjectSlicerTool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectSlicerTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, apply_to_object_root: primitives.Bool | None = None, edge_color: primitives.ColorX | None = None, edge_start: primitives.Float | None = None, edge_end: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            apply_to_object_root: Initial value for ApplyToObjectRoot.
            edge_color: Initial value for EdgeColor.
            edge_start: Initial value for EdgeStart.
            edge_end: Initial value for EdgeEnd.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tip_reference is not None:
            self.tip_reference = tip_reference
        if block_grip_equip is not None:
            self.block_grip_equip = block_grip_equip
        if block_remote_equip is not None:
            self.block_remote_equip = block_remote_equip
        if equip_name is not None:
            self.equip_name = equip_name
        if override_active_tool is not None:
            self.override_active_tool = override_active_tool
        if grip_poses_generated is not None:
            self.grip_poses_generated = grip_poses_generated
        if apply_to_object_root is not None:
            self.apply_to_object_root = apply_to_object_root
        if edge_color is not None:
            self.edge_color = edge_color
        if edge_start is not None:
            self.edge_start = edge_start
        if edge_end is not None:
            self.edge_end = edge_end

    @property
    def equip_link(self) -> members.EmptyElement | None:
        """The _equipLink member."""
        member = self.get_member("_equipLink")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @equip_link.setter
    def equip_link(self, value: members.EmptyElement) -> None:
        """Set the _equipLink member."""
        self.set_member("_equipLink", value)

    @property
    def tip_reference(self) -> str | None:
        """Target ID of the TipReference reference (targets Slot)."""
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_reference.setter
    def tip_reference(self, target: str | Slot | None) -> None:
        """Set the TipReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def block_grip_equip(self) -> primitives.Bool | None:
        """The BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_grip_equip.setter
    def block_grip_equip(self, value: primitives.Bool) -> None:
        """Set the BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockGripEquip", fields.FieldBool(value=value)
            )

    @property
    def block_remote_equip(self) -> primitives.Bool | None:
        """The BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_remote_equip.setter
    def block_remote_equip(self, value: primitives.Bool) -> None:
        """Set the BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockRemoteEquip", fields.FieldBool(value=value)
            )

    @property
    def equip_name(self) -> primitives.String | None:
        """The EquipName field value."""
        member = self.get_member("EquipName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_name.setter
    def equip_name(self, value: primitives.String) -> None:
        """Set the EquipName field value."""
        member = self.get_member("EquipName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquipName", fields.FieldString(value=value)
            )

    @property
    def override_active_tool(self) -> str | None:
        """Target ID of the _overrideActiveTool reference (targets InteractionHandler)."""
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_active_tool.setter
    def override_active_tool(self, target: str | InteractionHandler | None) -> None:
        """Set the _overrideActiveTool reference by target ID or InteractionHandler instance."""
        target_id: str | None = target.id if isinstance(target, InteractionHandler) else target  # type: ignore[assignment]
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overrideActiveTool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

    @property
    def grip_poses_generated(self) -> primitives.Bool | None:
        """The _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_poses_generated.setter
    def grip_poses_generated(self, value: primitives.Bool) -> None:
        """Set the _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_gripPosesGenerated", fields.FieldBool(value=value)
            )

    @property
    def apply_to_object_root(self) -> primitives.Bool | None:
        """The ApplyToObjectRoot field value."""
        member = self.get_member("ApplyToObjectRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @apply_to_object_root.setter
    def apply_to_object_root(self, value: primitives.Bool) -> None:
        """Set the ApplyToObjectRoot field value."""
        member = self.get_member("ApplyToObjectRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ApplyToObjectRoot", fields.FieldBool(value=value)
            )

    @property
    def edge_color(self) -> primitives.ColorX | None:
        """The EdgeColor field value."""
        member = self.get_member("EdgeColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_color.setter
    def edge_color(self, value: primitives.ColorX) -> None:
        """Set the EdgeColor field value."""
        member = self.get_member("EdgeColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeColor", fields.FieldColorX(value=value)
            )

    @property
    def edge_start(self) -> primitives.Float | None:
        """The EdgeStart field value."""
        member = self.get_member("EdgeStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_start.setter
    def edge_start(self, value: primitives.Float) -> None:
        """Set the EdgeStart field value."""
        member = self.get_member("EdgeStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeStart", fields.FieldFloat(value=value)
            )

    @property
    def edge_end(self) -> primitives.Float | None:
        """The EdgeEnd field value."""
        member = self.get_member("EdgeEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_end.setter
    def edge_end(self, value: primitives.Float) -> None:
        """Set the EdgeEnd field value."""
        member = self.get_member("EdgeEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeEnd", fields.FieldFloat(value=value)
            )

    @property
    def slicers(self) -> members.SyncList | None:
        """The _slicers member."""
        member = self.get_member("_slicers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @slicers.setter
    def slicers(self, value: members.SyncList) -> None:
        """Set the _slicers member."""
        self.set_member("_slicers", value)

    @property
    def slice_materials(self) -> members.SyncList | None:
        """The _sliceMaterials member."""
        member = self.get_member("_sliceMaterials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @slice_materials.setter
    def slice_materials(self, value: members.SyncList) -> None:
        """Set the _sliceMaterials member."""
        self.set_member("_sliceMaterials", value)

