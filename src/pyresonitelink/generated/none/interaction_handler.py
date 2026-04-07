"""Generated component: InteractionHandler."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.locomotion_controller import LocomotionController
from pyresonitelink.generated._types.interaction_handler_stream_driver import InteractionHandlerStreamDriver
from pyresonitelink.generated._types.context_menu_item import ContextMenuItem
from pyresonitelink.generated._types.context_menu import ContextMenu
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.interaction_laser import InteractionLaser
from pyresonitelink.generated._types.ring_mesh import RingMesh
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.link_target import LinkTarget
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.grip_pose_reference import GripPoseReference
from pyresonitelink.generated._types.fresnel_material import FresnelMaterial
from pyresonitelink.generated._types.item_shelf import ItemShelf
from pyresonitelink.generated._types.ivibration_device_component import IVibrationDeviceComponent
from pyresonitelink.generated._types.ilocomotion_reference import ILocomotionReference
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.ihand_target_info_source import IHandTargetInfoSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionHandler(GeneratedComponent, IVibrationDeviceComponent, ILocomotionReference, IInputUpdateReceiver, IHandTargetInfoSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractionHandler.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractionHandler"

    def __init__(self, locomotion_controller: str | LocomotionController | None = None, grab_smoothing: np.float32 | None = None, stream_driver: str | InteractionHandlerStreamDriver | None = None, undo_item: str | ContextMenuItem | None = None, redo_item: str | ContextMenuItem | None = None, context_menu: str | ContextMenu | None = None, equipping_enabled: bool | None = None, menu_enabled: bool | None = None, user_scaling_enabled: bool | None = None, visual_enabled: bool | None = None, pointing_grab: bool | None = None, pointing_touch: bool | None = None, tool_root: str | Slot | None = None, laser_slot: str | Slot | None = None, laser_position: str | IField[primitives.Float3] | None = None, laser_rotation: str | IField[primitives.FloatQ] | None = None, interaction_laser: str | InteractionLaser | None = None, laser_enabled: bool | None = None, grab_toggle: bool | None = None, holder_pos: str | IField[primitives.Float3] | None = None, holder_rot: str | IField[primitives.FloatQ] | None = None, holder_axis_offset: np.float32 | None = None, holder_rotation_offset: primitives.FloatQ | None = None, holder_rotation_reference: primitives.FloatQ | None = None, original_twist_offset: np.float32 | None = None, userspace_toggle_indicator: str | RingMesh | None = None, tool_holder: str | Slot | None = None, show_interaction_hints: bool | None = None, grabber_sphere_active: str | IField[bool] | None = None, grab_ignore_root: str | Slot | None = None, grabber: str | Grabber | None = None, active_tool_link: str | LinkTarget[ITool] | None = None, active_tool_grip_pose_reference: str | GripPoseReference | None = None, tool_locked: bool | None = None, grab_material: str | FresnelMaterial | None = None, item_shelf_slot: str | Slot | None = None, item_shelf: str | ItemShelf | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            locomotion_controller: Initial value for LocomotionController.
            grab_smoothing: Initial value for GrabSmoothing.
            stream_driver: Initial value for _streamDriver.
            undo_item: Initial value for _undoItem.
            redo_item: Initial value for _redoItem.
            context_menu: Initial value for ContextMenu.
            equipping_enabled: Initial value for EquippingEnabled.
            menu_enabled: Initial value for MenuEnabled.
            user_scaling_enabled: Initial value for UserScalingEnabled.
            visual_enabled: Initial value for VisualEnabled.
            pointing_grab: Initial value for PointingGrab.
            pointing_touch: Initial value for PointingTouch.
            tool_root: Initial value for _toolRoot.
            laser_slot: Initial value for _laserSlot.
            laser_position: Initial value for _laserPosition.
            laser_rotation: Initial value for _laserRotation.
            interaction_laser: Initial value for _interactionLaser.
            laser_enabled: Initial value for _laserEnabled.
            grab_toggle: Initial value for _grabToggle.
            holder_pos: Initial value for _holderPos.
            holder_rot: Initial value for _holderRot.
            holder_axis_offset: Initial value for _holderAxisOffset.
            holder_rotation_offset: Initial value for _holderRotationOffset.
            holder_rotation_reference: Initial value for _holderRotationReference.
            original_twist_offset: Initial value for _originalTwistOffset.
            userspace_toggle_indicator: Initial value for _userspaceToggleIndicator.
            tool_holder: Initial value for ToolHolder.
            show_interaction_hints: Initial value for ShowInteractionHints.
            grabber_sphere_active: Initial value for _grabberSphereActive.
            grab_ignore_root: Initial value for _grabIgnoreRoot.
            grabber: Initial value for _grabber.
            active_tool_link: Initial value for ActiveToolLink.
            active_tool_grip_pose_reference: Initial value for _activeToolGripPoseReference.
            tool_locked: Initial value for _toolLocked.
            grab_material: Initial value for _grabMaterial.
            item_shelf_slot: Initial value for _itemShelfSlot.
            item_shelf: Initial value for _itemShelf.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if locomotion_controller is not None:
            self.locomotion_controller = locomotion_controller
        if grab_smoothing is not None:
            self.grab_smoothing = grab_smoothing
        if stream_driver is not None:
            self.stream_driver = stream_driver
        if undo_item is not None:
            self.undo_item = undo_item
        if redo_item is not None:
            self.redo_item = redo_item
        if context_menu is not None:
            self.context_menu = context_menu
        if equipping_enabled is not None:
            self.equipping_enabled = equipping_enabled
        if menu_enabled is not None:
            self.menu_enabled = menu_enabled
        if user_scaling_enabled is not None:
            self.user_scaling_enabled = user_scaling_enabled
        if visual_enabled is not None:
            self.visual_enabled = visual_enabled
        if pointing_grab is not None:
            self.pointing_grab = pointing_grab
        if pointing_touch is not None:
            self.pointing_touch = pointing_touch
        if tool_root is not None:
            self.tool_root = tool_root
        if laser_slot is not None:
            self.laser_slot = laser_slot
        if laser_position is not None:
            self.laser_position = laser_position
        if laser_rotation is not None:
            self.laser_rotation = laser_rotation
        if interaction_laser is not None:
            self.interaction_laser = interaction_laser
        if laser_enabled is not None:
            self.laser_enabled = laser_enabled
        if grab_toggle is not None:
            self.grab_toggle = grab_toggle
        if holder_pos is not None:
            self.holder_pos = holder_pos
        if holder_rot is not None:
            self.holder_rot = holder_rot
        if holder_axis_offset is not None:
            self.holder_axis_offset = holder_axis_offset
        if holder_rotation_offset is not None:
            self.holder_rotation_offset = holder_rotation_offset
        if holder_rotation_reference is not None:
            self.holder_rotation_reference = holder_rotation_reference
        if original_twist_offset is not None:
            self.original_twist_offset = original_twist_offset
        if userspace_toggle_indicator is not None:
            self.userspace_toggle_indicator = userspace_toggle_indicator
        if tool_holder is not None:
            self.tool_holder = tool_holder
        if show_interaction_hints is not None:
            self.show_interaction_hints = show_interaction_hints
        if grabber_sphere_active is not None:
            self.grabber_sphere_active = grabber_sphere_active
        if grab_ignore_root is not None:
            self.grab_ignore_root = grab_ignore_root
        if grabber is not None:
            self.grabber = grabber
        if active_tool_link is not None:
            self.active_tool_link = active_tool_link
        if active_tool_grip_pose_reference is not None:
            self.active_tool_grip_pose_reference = active_tool_grip_pose_reference
        if tool_locked is not None:
            self.tool_locked = tool_locked
        if grab_material is not None:
            self.grab_material = grab_material
        if item_shelf_slot is not None:
            self.item_shelf_slot = item_shelf_slot
        if item_shelf is not None:
            self.item_shelf = item_shelf

    @property
    def side(self) -> members.FieldEnum | None:
        """The Side member."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @side.setter
    def side(self, value: members.FieldEnum) -> None:
        """Set the Side member."""
        self.set_member("Side", value)

    @property
    def locomotion_controller(self) -> str | None:
        """Target ID of the LocomotionController reference (targets LocomotionController)."""
        member = self.get_member("LocomotionController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locomotion_controller.setter
    def locomotion_controller(self, target: str | LocomotionController | None) -> None:
        """Set the LocomotionController reference by target ID or LocomotionController instance."""
        target_id: str | None = target.id if isinstance(target, LocomotionController) else target  # type: ignore[assignment]
        member = self.get_member("LocomotionController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocomotionController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LocomotionController'),
            )

    @property
    def grab_smoothing(self) -> np.float32 | None:
        """The GrabSmoothing field value."""
        member = self.get_member("GrabSmoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_smoothing.setter
    def grab_smoothing(self, value: np.float32) -> None:
        """Set the GrabSmoothing field value."""
        member = self.get_member("GrabSmoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabSmoothing", fields.FieldFloat(value=value)
            )

    @property
    def stream_driver(self) -> str | None:
        """Target ID of the _streamDriver reference (targets InteractionHandlerStreamDriver)."""
        member = self.get_member("_streamDriver")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream_driver.setter
    def stream_driver(self, target: str | InteractionHandlerStreamDriver | None) -> None:
        """Set the _streamDriver reference by target ID or InteractionHandlerStreamDriver instance."""
        target_id: str | None = target.id if isinstance(target, InteractionHandlerStreamDriver) else target  # type: ignore[assignment]
        member = self.get_member("_streamDriver")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_streamDriver",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandlerStreamDriver'),
            )

    @property
    def undo_item(self) -> str | None:
        """Target ID of the _undoItem reference (targets ContextMenuItem)."""
        member = self.get_member("_undoItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @undo_item.setter
    def undo_item(self, target: str | ContextMenuItem | None) -> None:
        """Set the _undoItem reference by target ID or ContextMenuItem instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItem) else target  # type: ignore[assignment]
        member = self.get_member("_undoItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_undoItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItem'),
            )

    @property
    def redo_item(self) -> str | None:
        """Target ID of the _redoItem reference (targets ContextMenuItem)."""
        member = self.get_member("_redoItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @redo_item.setter
    def redo_item(self, target: str | ContextMenuItem | None) -> None:
        """Set the _redoItem reference by target ID or ContextMenuItem instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItem) else target  # type: ignore[assignment]
        member = self.get_member("_redoItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_redoItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItem'),
            )

    @property
    def context_menu(self) -> str | None:
        """Target ID of the ContextMenu reference (targets ContextMenu)."""
        member = self.get_member("ContextMenu")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @context_menu.setter
    def context_menu(self, target: str | ContextMenu | None) -> None:
        """Set the ContextMenu reference by target ID or ContextMenu instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenu) else target  # type: ignore[assignment]
        member = self.get_member("ContextMenu")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ContextMenu",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenu'),
            )

    @property
    def equipping_enabled(self) -> bool | None:
        """The EquippingEnabled field value."""
        member = self.get_member("EquippingEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equipping_enabled.setter
    def equipping_enabled(self, value: bool) -> None:
        """Set the EquippingEnabled field value."""
        member = self.get_member("EquippingEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquippingEnabled", fields.FieldBool(value=value)
            )

    @property
    def menu_enabled(self) -> bool | None:
        """The MenuEnabled field value."""
        member = self.get_member("MenuEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @menu_enabled.setter
    def menu_enabled(self, value: bool) -> None:
        """Set the MenuEnabled field value."""
        member = self.get_member("MenuEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MenuEnabled", fields.FieldBool(value=value)
            )

    @property
    def user_scaling_enabled(self) -> bool | None:
        """The UserScalingEnabled field value."""
        member = self.get_member("UserScalingEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_scaling_enabled.setter
    def user_scaling_enabled(self, value: bool) -> None:
        """Set the UserScalingEnabled field value."""
        member = self.get_member("UserScalingEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserScalingEnabled", fields.FieldBool(value=value)
            )

    @property
    def visual_enabled(self) -> bool | None:
        """The VisualEnabled field value."""
        member = self.get_member("VisualEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visual_enabled.setter
    def visual_enabled(self, value: bool) -> None:
        """Set the VisualEnabled field value."""
        member = self.get_member("VisualEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualEnabled", fields.FieldBool(value=value)
            )

    @property
    def pointing_grab(self) -> bool | None:
        """The PointingGrab field value."""
        member = self.get_member("PointingGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pointing_grab.setter
    def pointing_grab(self, value: bool) -> None:
        """Set the PointingGrab field value."""
        member = self.get_member("PointingGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PointingGrab", fields.FieldBool(value=value)
            )

    @property
    def pointing_touch(self) -> bool | None:
        """The PointingTouch field value."""
        member = self.get_member("PointingTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pointing_touch.setter
    def pointing_touch(self, value: bool) -> None:
        """Set the PointingTouch field value."""
        member = self.get_member("PointingTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PointingTouch", fields.FieldBool(value=value)
            )

    @property
    def tool_root(self) -> str | None:
        """Target ID of the _toolRoot reference (targets Slot)."""
        member = self.get_member("_toolRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool_root.setter
    def tool_root(self, target: str | Slot | None) -> None:
        """Set the _toolRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_toolRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_toolRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def laser_slot(self) -> str | None:
        """Target ID of the _laserSlot reference (targets Slot)."""
        member = self.get_member("_laserSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_slot.setter
    def laser_slot(self, target: str | Slot | None) -> None:
        """Set the _laserSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_laserSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def laser_position(self) -> str | None:
        """Target ID of the _laserPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_laserPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_position.setter
    def laser_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _laserPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_laserPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def laser_rotation(self) -> str | None:
        """Target ID of the _laserRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_laserRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laser_rotation.setter
    def laser_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _laserRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_laserRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_laserRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def interaction_laser(self) -> str | None:
        """Target ID of the _interactionLaser reference (targets InteractionLaser)."""
        member = self.get_member("_interactionLaser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interaction_laser.setter
    def interaction_laser(self, target: str | InteractionLaser | None) -> None:
        """Set the _interactionLaser reference by target ID or InteractionLaser instance."""
        target_id: str | None = target.id if isinstance(target, InteractionLaser) else target  # type: ignore[assignment]
        member = self.get_member("_interactionLaser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_interactionLaser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionLaser'),
            )

    @property
    def laser_enabled(self) -> bool | None:
        """The _laserEnabled field value."""
        member = self.get_member("_laserEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laser_enabled.setter
    def laser_enabled(self, value: bool) -> None:
        """Set the _laserEnabled field value."""
        member = self.get_member("_laserEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_laserEnabled", fields.FieldBool(value=value)
            )

    @property
    def hand_grab_type(self) -> members.FieldEnum | None:
        """The _handGrabType member."""
        member = self.get_member("_handGrabType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hand_grab_type.setter
    def hand_grab_type(self, value: members.FieldEnum) -> None:
        """Set the _handGrabType member."""
        self.set_member("_handGrabType", value)

    @property
    def grab_toggle(self) -> bool | None:
        """The _grabToggle field value."""
        member = self.get_member("_grabToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_toggle.setter
    def grab_toggle(self, value: bool) -> None:
        """Set the _grabToggle field value."""
        member = self.get_member("_grabToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_grabToggle", fields.FieldBool(value=value)
            )

    @property
    def holder_pos(self) -> str | None:
        """Target ID of the _holderPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_holderPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @holder_pos.setter
    def holder_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _holderPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_holderPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holderPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def holder_rot(self) -> str | None:
        """Target ID of the _holderRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_holderRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @holder_rot.setter
    def holder_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _holderRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_holderRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holderRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def laser_rotation_type(self) -> members.FieldEnum | None:
        """The _laserRotationType member."""
        member = self.get_member("_laserRotationType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @laser_rotation_type.setter
    def laser_rotation_type(self, value: members.FieldEnum) -> None:
        """Set the _laserRotationType member."""
        self.set_member("_laserRotationType", value)

    @property
    def holder_axis_offset(self) -> np.float32 | None:
        """The _holderAxisOffset field value."""
        member = self.get_member("_holderAxisOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @holder_axis_offset.setter
    def holder_axis_offset(self, value: np.float32) -> None:
        """Set the _holderAxisOffset field value."""
        member = self.get_member("_holderAxisOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_holderAxisOffset", fields.FieldFloat(value=value)
            )

    @property
    def holder_rotation_offset(self) -> primitives.FloatQ | None:
        """The _holderRotationOffset field value."""
        member = self.get_member("_holderRotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @holder_rotation_offset.setter
    def holder_rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the _holderRotationOffset field value."""
        member = self.get_member("_holderRotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_holderRotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def holder_rotation_reference(self) -> primitives.FloatQ | None:
        """The _holderRotationReference field value."""
        member = self.get_member("_holderRotationReference")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @holder_rotation_reference.setter
    def holder_rotation_reference(self, value: primitives.FloatQ) -> None:
        """Set the _holderRotationReference field value."""
        member = self.get_member("_holderRotationReference")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_holderRotationReference", fields.FieldNullableFloatQ(value=value)
            )

    @property
    def original_twist_offset(self) -> np.float32 | None:
        """The _originalTwistOffset field value."""
        member = self.get_member("_originalTwistOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_twist_offset.setter
    def original_twist_offset(self, value: np.float32) -> None:
        """Set the _originalTwistOffset field value."""
        member = self.get_member("_originalTwistOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalTwistOffset", fields.FieldFloat(value=value)
            )

    @property
    def userspace_toggle_indicator(self) -> str | None:
        """Target ID of the _userspaceToggleIndicator reference (targets RingMesh)."""
        member = self.get_member("_userspaceToggleIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @userspace_toggle_indicator.setter
    def userspace_toggle_indicator(self, target: str | RingMesh | None) -> None:
        """Set the _userspaceToggleIndicator reference by target ID or RingMesh instance."""
        target_id: str | None = target.id if isinstance(target, RingMesh) else target  # type: ignore[assignment]
        member = self.get_member("_userspaceToggleIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userspaceToggleIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RingMesh'),
            )

    @property
    def tool_holder(self) -> str | None:
        """Target ID of the ToolHolder reference (targets Slot)."""
        member = self.get_member("ToolHolder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool_holder.setter
    def tool_holder(self, target: str | Slot | None) -> None:
        """Set the ToolHolder reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ToolHolder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ToolHolder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def show_interaction_hints(self) -> bool | None:
        """The ShowInteractionHints field value."""
        member = self.get_member("ShowInteractionHints")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_interaction_hints.setter
    def show_interaction_hints(self, value: bool) -> None:
        """Set the ShowInteractionHints field value."""
        member = self.get_member("ShowInteractionHints")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowInteractionHints", fields.FieldBool(value=value)
            )

    @property
    def grabber_sphere_active(self) -> str | None:
        """Target ID of the _grabberSphereActive reference (targets IField[bool])."""
        member = self.get_member("_grabberSphereActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber_sphere_active.setter
    def grabber_sphere_active(self, target: str | IField[bool] | None) -> None:
        """Set the _grabberSphereActive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_grabberSphereActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabberSphereActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def grab_ignore_root(self) -> str | None:
        """Target ID of the _grabIgnoreRoot reference (targets Slot)."""
        member = self.get_member("_grabIgnoreRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grab_ignore_root.setter
    def grab_ignore_root(self, target: str | Slot | None) -> None:
        """Set the _grabIgnoreRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_grabIgnoreRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabIgnoreRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def grabber(self) -> str | None:
        """Target ID of the _grabber reference (targets Grabber)."""
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber.setter
    def grabber(self, target: str | Grabber | None) -> None:
        """Set the _grabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def current_grab_type(self) -> members.FieldEnum | None:
        """The _currentGrabType member."""
        member = self.get_member("_currentGrabType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @current_grab_type.setter
    def current_grab_type(self, value: members.FieldEnum) -> None:
        """Set the _currentGrabType member."""
        self.set_member("_currentGrabType", value)

    @property
    def active_tool_link(self) -> str | None:
        """Target ID of the ActiveToolLink reference (targets LinkTarget[ITool])."""
        member = self.get_member("ActiveToolLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_tool_link.setter
    def active_tool_link(self, target: str | LinkTarget[ITool] | None) -> None:
        """Set the ActiveToolLink reference by target ID or LinkTarget[ITool] instance."""
        target_id: str | None = target.id if isinstance(target, LinkTarget) else target  # type: ignore[assignment]
        member = self.get_member("ActiveToolLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ActiveToolLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LinkTarget<[FrooxEngine]FrooxEngine.ITool>'),
            )

    @property
    def active_tool_grip_pose_reference(self) -> str | None:
        """Target ID of the _activeToolGripPoseReference reference (targets GripPoseReference)."""
        member = self.get_member("_activeToolGripPoseReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_tool_grip_pose_reference.setter
    def active_tool_grip_pose_reference(self, target: str | GripPoseReference | None) -> None:
        """Set the _activeToolGripPoseReference reference by target ID or GripPoseReference instance."""
        target_id: str | None = target.id if isinstance(target, GripPoseReference) else target  # type: ignore[assignment]
        member = self.get_member("_activeToolGripPoseReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeToolGripPoseReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.GripPoseReference'),
            )

    @property
    def tool_locked(self) -> bool | None:
        """The _toolLocked field value."""
        member = self.get_member("_toolLocked")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tool_locked.setter
    def tool_locked(self, value: bool) -> None:
        """Set the _toolLocked field value."""
        member = self.get_member("_toolLocked")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_toolLocked", fields.FieldBool(value=value)
            )

    @property
    def grab_material(self) -> str | None:
        """Target ID of the _grabMaterial reference (targets FresnelMaterial)."""
        member = self.get_member("_grabMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grab_material.setter
    def grab_material(self, target: str | FresnelMaterial | None) -> None:
        """Set the _grabMaterial reference by target ID or FresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, FresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_grabMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FresnelMaterial'),
            )

    @property
    def item_shelf_slot(self) -> str | None:
        """Target ID of the _itemShelfSlot reference (targets Slot)."""
        member = self.get_member("_itemShelfSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_shelf_slot.setter
    def item_shelf_slot(self, target: str | Slot | None) -> None:
        """Set the _itemShelfSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_itemShelfSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_itemShelfSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def item_shelf(self) -> str | None:
        """Target ID of the _itemShelf reference (targets ItemShelf)."""
        member = self.get_member("_itemShelf")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_shelf.setter
    def item_shelf(self, target: str | ItemShelf | None) -> None:
        """Set the _itemShelf reference by target ID or ItemShelf instance."""
        target_id: str | None = target.id if isinstance(target, ItemShelf) else target  # type: ignore[assignment]
        member = self.get_member("_itemShelf")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_itemShelf",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ItemShelf'),
            )

