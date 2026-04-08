"""Generated component: GaussianSplatTool."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.box_interface import BoxInterface
from pyresonitelink.generated._types.sphere_interface import SphereInterface
from pyresonitelink.generated._types.cylinder_interface import CylinderInterface
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatTool(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatTool.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatTool"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, box_selection_template: str | BoxInterface | None = None, sphere_selection_template: str | SphereInterface | None = None, cylinder_selection_template: str | CylinderInterface | None = None, active_box: str | BoxInterface | None = None, active_sphere: str | SphereInterface | None = None, active_cylinder: str | CylinderInterface | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            box_selection_template: Initial value for BoxSelectionTemplate.
            sphere_selection_template: Initial value for SphereSelectionTemplate.
            cylinder_selection_template: Initial value for CylinderSelectionTemplate.
            active_box: Initial value for _activeBox.
            active_sphere: Initial value for _activeSphere.
            active_cylinder: Initial value for _activeCylinder.
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
        if box_selection_template is not None:
            self.box_selection_template = box_selection_template
        if sphere_selection_template is not None:
            self.sphere_selection_template = sphere_selection_template
        if cylinder_selection_template is not None:
            self.cylinder_selection_template = cylinder_selection_template
        if active_box is not None:
            self.active_box = active_box
        if active_sphere is not None:
            self.active_sphere = active_sphere
        if active_cylinder is not None:
            self.active_cylinder = active_cylinder

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
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

    @property
    def box_selection_template(self) -> str | None:
        """Target ID of the BoxSelectionTemplate reference (targets BoxInterface)."""
        member = self.get_member("BoxSelectionTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @box_selection_template.setter
    def box_selection_template(self, target: str | BoxInterface | None) -> None:
        """Set the BoxSelectionTemplate reference by target ID or BoxInterface instance."""
        target_id: str | None = target.id if isinstance(target, BoxInterface) else target  # type: ignore[assignment]
        member = self.get_member("BoxSelectionTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BoxSelectionTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GaussianSplatTool+BoxInterface'),
            )

    @property
    def sphere_selection_template(self) -> str | None:
        """Target ID of the SphereSelectionTemplate reference (targets SphereInterface)."""
        member = self.get_member("SphereSelectionTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sphere_selection_template.setter
    def sphere_selection_template(self, target: str | SphereInterface | None) -> None:
        """Set the SphereSelectionTemplate reference by target ID or SphereInterface instance."""
        target_id: str | None = target.id if isinstance(target, SphereInterface) else target  # type: ignore[assignment]
        member = self.get_member("SphereSelectionTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SphereSelectionTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GaussianSplatTool+SphereInterface'),
            )

    @property
    def cylinder_selection_template(self) -> str | None:
        """Target ID of the CylinderSelectionTemplate reference (targets CylinderInterface)."""
        member = self.get_member("CylinderSelectionTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cylinder_selection_template.setter
    def cylinder_selection_template(self, target: str | CylinderInterface | None) -> None:
        """Set the CylinderSelectionTemplate reference by target ID or CylinderInterface instance."""
        target_id: str | None = target.id if isinstance(target, CylinderInterface) else target  # type: ignore[assignment]
        member = self.get_member("CylinderSelectionTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CylinderSelectionTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GaussianSplatTool+CylinderInterface'),
            )

    @property
    def active_box(self) -> str | None:
        """Target ID of the _activeBox reference (targets BoxInterface)."""
        member = self.get_member("_activeBox")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_box.setter
    def active_box(self, target: str | BoxInterface | None) -> None:
        """Set the _activeBox reference by target ID or BoxInterface instance."""
        target_id: str | None = target.id if isinstance(target, BoxInterface) else target  # type: ignore[assignment]
        member = self.get_member("_activeBox")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeBox",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GaussianSplatTool+BoxInterface'),
            )

    @property
    def active_sphere(self) -> str | None:
        """Target ID of the _activeSphere reference (targets SphereInterface)."""
        member = self.get_member("_activeSphere")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_sphere.setter
    def active_sphere(self, target: str | SphereInterface | None) -> None:
        """Set the _activeSphere reference by target ID or SphereInterface instance."""
        target_id: str | None = target.id if isinstance(target, SphereInterface) else target  # type: ignore[assignment]
        member = self.get_member("_activeSphere")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeSphere",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GaussianSplatTool+SphereInterface'),
            )

    @property
    def active_cylinder(self) -> str | None:
        """Target ID of the _activeCylinder reference (targets CylinderInterface)."""
        member = self.get_member("_activeCylinder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_cylinder.setter
    def active_cylinder(self, target: str | CylinderInterface | None) -> None:
        """Set the _activeCylinder reference by target ID or CylinderInterface instance."""
        target_id: str | None = target.id if isinstance(target, CylinderInterface) else target  # type: ignore[assignment]
        member = self.get_member("_activeCylinder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeCylinder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GaussianSplatTool+CylinderInterface'),
            )

