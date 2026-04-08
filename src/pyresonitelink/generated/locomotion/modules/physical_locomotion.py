"""Generated component: PhysicalLocomotion."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.locomotion_controller import LocomotionController
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.character_controller import CharacterController
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iphysical_locomotion import IPhysicalLocomotion
from pyresonitelink.generated._types.ifield_of_view_modifier import IFieldOfViewModifier
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PhysicalLocomotion(GeneratedComponent, ICustomInspector, IPhysicalLocomotion, IFieldOfViewModifier, IInputUpdateReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhysicalLocomotion.

    Category: Locomotion/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhysicalLocomotion"

    def __init__(self, icon: str | IAssetProvider[ITexture2D] | None = None, color: primitives.ColorX | None = None, current_controller: str | LocomotionController | None = None, last_default_icon: str | None = None, last_default_color: primitives.ColorX | None = None, min_initialization_delay: np.float32 | None = None, max_initialization_delay: np.float32 | None = None, initialization_collider_root: str | Slot | None = None, use_speed_from_user_settings: bool | None = None, description: str | None = None, grip_on_hold: bool | None = None, grip_radius: np.float32 | None = None, grip_velocity_multiplier: np.float32 | None = None, hand_grip_rotation_smooth_speed: np.float32 | None = None, fall_respawn_position: np.float32 | None = None, make_gravity_character_local: bool | None = None, auto_align_vertical_with_gravity_speed: np.float32 | None = None, manual_align_vertical_with_gravity_speed: np.float32 | None = None, air_deceleration_speed: np.float32 | None = None, grip_scale_delay: np.float32 | None = None, allow_crouch: bool | None = None, maximum_normalized_speed: np.float32 | None = None, default_icon: str | None = None, default_color: primitives.ColorX | None = None, character_controller: str | CharacterController | None = None, legacy_name: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            icon: Initial value for Icon.
            color: Initial value for Color.
            current_controller: Initial value for _currentController.
            last_default_icon: Initial value for _lastDefaultIcon.
            last_default_color: Initial value for _lastDefaultColor.
            min_initialization_delay: Initial value for MinInitializationDelay.
            max_initialization_delay: Initial value for MaxInitializationDelay.
            initialization_collider_root: Initial value for InitializationColliderRoot.
            use_speed_from_user_settings: Initial value for UseSpeedFromUserSettings.
            description: Initial value for Description.
            grip_on_hold: Initial value for GripOnHold.
            grip_radius: Initial value for GripRadius.
            grip_velocity_multiplier: Initial value for GripVelocityMultiplier.
            hand_grip_rotation_smooth_speed: Initial value for HandGripRotationSmoothSpeed.
            fall_respawn_position: Initial value for FallRespawnPosition.
            make_gravity_character_local: Initial value for MakeGravityCharacterLocal.
            auto_align_vertical_with_gravity_speed: Initial value for AutoAlignVerticalWithGravitySpeed.
            manual_align_vertical_with_gravity_speed: Initial value for ManualAlignVerticalWithGravitySpeed.
            air_deceleration_speed: Initial value for AirDecelerationSpeed.
            grip_scale_delay: Initial value for GripScaleDelay.
            allow_crouch: Initial value for AllowCrouch.
            maximum_normalized_speed: Initial value for MaximumNormalizedSpeed.
            default_icon: Initial value for _defaultIcon.
            default_color: Initial value for _defaultColor.
            character_controller: Initial value for _characterController.
            legacy_name: Initial value for __legacyName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if icon is not None:
            self.icon = icon
        if color is not None:
            self.color = color
        if current_controller is not None:
            self.current_controller = current_controller
        if last_default_icon is not None:
            self.last_default_icon = last_default_icon
        if last_default_color is not None:
            self.last_default_color = last_default_color
        if min_initialization_delay is not None:
            self.min_initialization_delay = min_initialization_delay
        if max_initialization_delay is not None:
            self.max_initialization_delay = max_initialization_delay
        if initialization_collider_root is not None:
            self.initialization_collider_root = initialization_collider_root
        if use_speed_from_user_settings is not None:
            self.use_speed_from_user_settings = use_speed_from_user_settings
        if description is not None:
            self.description = description
        if grip_on_hold is not None:
            self.grip_on_hold = grip_on_hold
        if grip_radius is not None:
            self.grip_radius = grip_radius
        if grip_velocity_multiplier is not None:
            self.grip_velocity_multiplier = grip_velocity_multiplier
        if hand_grip_rotation_smooth_speed is not None:
            self.hand_grip_rotation_smooth_speed = hand_grip_rotation_smooth_speed
        if fall_respawn_position is not None:
            self.fall_respawn_position = fall_respawn_position
        if make_gravity_character_local is not None:
            self.make_gravity_character_local = make_gravity_character_local
        if auto_align_vertical_with_gravity_speed is not None:
            self.auto_align_vertical_with_gravity_speed = auto_align_vertical_with_gravity_speed
        if manual_align_vertical_with_gravity_speed is not None:
            self.manual_align_vertical_with_gravity_speed = manual_align_vertical_with_gravity_speed
        if air_deceleration_speed is not None:
            self.air_deceleration_speed = air_deceleration_speed
        if grip_scale_delay is not None:
            self.grip_scale_delay = grip_scale_delay
        if allow_crouch is not None:
            self.allow_crouch = allow_crouch
        if maximum_normalized_speed is not None:
            self.maximum_normalized_speed = maximum_normalized_speed
        if default_icon is not None:
            self.default_icon = default_icon
        if default_color is not None:
            self.default_color = default_color
        if character_controller is not None:
            self.character_controller = character_controller
        if legacy_name is not None:
            self.legacy_name = legacy_name

    @property
    def icon(self) -> str | None:
        """Target ID of the Icon reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Icon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon.setter
    def icon(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Icon reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Icon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Icon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def current_controller(self) -> str | None:
        """Target ID of the _currentController reference (targets LocomotionController)."""
        member = self.get_member("_currentController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_controller.setter
    def current_controller(self, target: str | LocomotionController | None) -> None:
        """Set the _currentController reference by target ID or LocomotionController instance."""
        target_id: str | None = target.id if isinstance(target, LocomotionController) else target  # type: ignore[assignment]
        member = self.get_member("_currentController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LocomotionController'),
            )

    @property
    def last_default_icon(self) -> str | None:
        """The _lastDefaultIcon field value."""
        member = self.get_member("_lastDefaultIcon")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_default_icon.setter
    def last_default_icon(self, value: str) -> None:
        """Set the _lastDefaultIcon field value."""
        member = self.get_member("_lastDefaultIcon")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastDefaultIcon", fields.FieldUri(value=value)
            )

    @property
    def last_default_color(self) -> primitives.ColorX | None:
        """The _lastDefaultColor field value."""
        member = self.get_member("_lastDefaultColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_default_color.setter
    def last_default_color(self, value: primitives.ColorX) -> None:
        """Set the _lastDefaultColor field value."""
        member = self.get_member("_lastDefaultColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastDefaultColor", fields.FieldNullableColorX(value=value)
            )

    @property
    def turn(self) -> members.SyncObject | None:
        """The Turn member."""
        member = self.get_member("Turn")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @turn.setter
    def turn(self, value: members.SyncObject) -> None:
        """Set the Turn member."""
        self.set_member("Turn", value)

    @property
    def archetype(self) -> members.FieldEnum | None:
        """The Archetype member."""
        member = self.get_member("Archetype")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @archetype.setter
    def archetype(self, value: members.FieldEnum) -> None:
        """Set the Archetype member."""
        self.set_member("Archetype", value)

    @property
    def min_initialization_delay(self) -> np.float32 | None:
        """The MinInitializationDelay field value."""
        member = self.get_member("MinInitializationDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_initialization_delay.setter
    def min_initialization_delay(self, value: np.float32) -> None:
        """Set the MinInitializationDelay field value."""
        member = self.get_member("MinInitializationDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinInitializationDelay", fields.FieldFloat(value=value)
            )

    @property
    def max_initialization_delay(self) -> np.float32 | None:
        """The MaxInitializationDelay field value."""
        member = self.get_member("MaxInitializationDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_initialization_delay.setter
    def max_initialization_delay(self, value: np.float32) -> None:
        """Set the MaxInitializationDelay field value."""
        member = self.get_member("MaxInitializationDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxInitializationDelay", fields.FieldFloat(value=value)
            )

    @property
    def initialization_collider_root(self) -> str | None:
        """Target ID of the InitializationColliderRoot reference (targets Slot)."""
        member = self.get_member("InitializationColliderRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @initialization_collider_root.setter
    def initialization_collider_root(self, target: str | Slot | None) -> None:
        """Set the InitializationColliderRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("InitializationColliderRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InitializationColliderRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def use_speed_from_user_settings(self) -> bool | None:
        """The UseSpeedFromUserSettings field value."""
        member = self.get_member("UseSpeedFromUserSettings")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_speed_from_user_settings.setter
    def use_speed_from_user_settings(self, value: bool) -> None:
        """Set the UseSpeedFromUserSettings field value."""
        member = self.get_member("UseSpeedFromUserSettings")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSpeedFromUserSettings", fields.FieldBool(value=value)
            )

    @property
    def description(self) -> str | None:
        """The Description field value."""
        member = self.get_member("Description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: str) -> None:
        """Set the Description field value."""
        member = self.get_member("Description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Description", fields.FieldString(value=value)
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
    def gripping(self) -> members.FieldEnum | None:
        """The Gripping member."""
        member = self.get_member("Gripping")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @gripping.setter
    def gripping(self, value: members.FieldEnum) -> None:
        """Set the Gripping member."""
        self.set_member("Gripping", value)

    @property
    def grip_on_hold(self) -> bool | None:
        """The GripOnHold field value."""
        member = self.get_member("GripOnHold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_on_hold.setter
    def grip_on_hold(self, value: bool) -> None:
        """Set the GripOnHold field value."""
        member = self.get_member("GripOnHold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GripOnHold", fields.FieldBool(value=value)
            )

    @property
    def grip_radius(self) -> np.float32 | None:
        """The GripRadius field value."""
        member = self.get_member("GripRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_radius.setter
    def grip_radius(self, value: np.float32) -> None:
        """Set the GripRadius field value."""
        member = self.get_member("GripRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GripRadius", fields.FieldFloat(value=value)
            )

    @property
    def grip_velocity_multiplier(self) -> np.float32 | None:
        """The GripVelocityMultiplier field value."""
        member = self.get_member("GripVelocityMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_velocity_multiplier.setter
    def grip_velocity_multiplier(self, value: np.float32) -> None:
        """Set the GripVelocityMultiplier field value."""
        member = self.get_member("GripVelocityMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GripVelocityMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def grip_hand_rotation_mode(self) -> members.FieldEnum | None:
        """The GripHandRotationMode member."""
        member = self.get_member("GripHandRotationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @grip_hand_rotation_mode.setter
    def grip_hand_rotation_mode(self, value: members.FieldEnum) -> None:
        """Set the GripHandRotationMode member."""
        self.set_member("GripHandRotationMode", value)

    @property
    def grip_object_rotation_mode(self) -> members.FieldEnum | None:
        """The GripObjectRotationMode member."""
        member = self.get_member("GripObjectRotationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @grip_object_rotation_mode.setter
    def grip_object_rotation_mode(self, value: members.FieldEnum) -> None:
        """Set the GripObjectRotationMode member."""
        self.set_member("GripObjectRotationMode", value)

    @property
    def hand_grip_rotation_smooth_speed(self) -> np.float32 | None:
        """The HandGripRotationSmoothSpeed field value."""
        member = self.get_member("HandGripRotationSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_grip_rotation_smooth_speed.setter
    def hand_grip_rotation_smooth_speed(self, value: np.float32) -> None:
        """Set the HandGripRotationSmoothSpeed field value."""
        member = self.get_member("HandGripRotationSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandGripRotationSmoothSpeed", fields.FieldNullableFloat(value=value)
            )

    @property
    def fall_respawn_position(self) -> np.float32 | None:
        """The FallRespawnPosition field value."""
        member = self.get_member("FallRespawnPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fall_respawn_position.setter
    def fall_respawn_position(self, value: np.float32) -> None:
        """Set the FallRespawnPosition field value."""
        member = self.get_member("FallRespawnPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FallRespawnPosition", fields.FieldFloat(value=value)
            )

    @property
    def make_gravity_character_local(self) -> bool | None:
        """The MakeGravityCharacterLocal field value."""
        member = self.get_member("MakeGravityCharacterLocal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @make_gravity_character_local.setter
    def make_gravity_character_local(self, value: bool) -> None:
        """Set the MakeGravityCharacterLocal field value."""
        member = self.get_member("MakeGravityCharacterLocal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MakeGravityCharacterLocal", fields.FieldBool(value=value)
            )

    @property
    def auto_align_vertical_with_gravity_speed(self) -> np.float32 | None:
        """The AutoAlignVerticalWithGravitySpeed field value."""
        member = self.get_member("AutoAlignVerticalWithGravitySpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_align_vertical_with_gravity_speed.setter
    def auto_align_vertical_with_gravity_speed(self, value: np.float32) -> None:
        """Set the AutoAlignVerticalWithGravitySpeed field value."""
        member = self.get_member("AutoAlignVerticalWithGravitySpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAlignVerticalWithGravitySpeed", fields.FieldFloat(value=value)
            )

    @property
    def manual_align_vertical_with_gravity_speed(self) -> np.float32 | None:
        """The ManualAlignVerticalWithGravitySpeed field value."""
        member = self.get_member("ManualAlignVerticalWithGravitySpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @manual_align_vertical_with_gravity_speed.setter
    def manual_align_vertical_with_gravity_speed(self, value: np.float32) -> None:
        """Set the ManualAlignVerticalWithGravitySpeed field value."""
        member = self.get_member("ManualAlignVerticalWithGravitySpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ManualAlignVerticalWithGravitySpeed", fields.FieldFloat(value=value)
            )

    @property
    def air_deceleration_speed(self) -> np.float32 | None:
        """The AirDecelerationSpeed field value."""
        member = self.get_member("AirDecelerationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @air_deceleration_speed.setter
    def air_deceleration_speed(self, value: np.float32) -> None:
        """Set the AirDecelerationSpeed field value."""
        member = self.get_member("AirDecelerationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AirDecelerationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def grip_scale_delay(self) -> np.float32 | None:
        """The GripScaleDelay field value."""
        member = self.get_member("GripScaleDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_scale_delay.setter
    def grip_scale_delay(self, value: np.float32) -> None:
        """Set the GripScaleDelay field value."""
        member = self.get_member("GripScaleDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GripScaleDelay", fields.FieldFloat(value=value)
            )

    @property
    def allow_crouch(self) -> bool | None:
        """The AllowCrouch field value."""
        member = self.get_member("AllowCrouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_crouch.setter
    def allow_crouch(self, value: bool) -> None:
        """Set the AllowCrouch field value."""
        member = self.get_member("AllowCrouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowCrouch", fields.FieldBool(value=value)
            )

    @property
    def maximum_normalized_speed(self) -> np.float32 | None:
        """The MaximumNormalizedSpeed field value."""
        member = self.get_member("MaximumNormalizedSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_normalized_speed.setter
    def maximum_normalized_speed(self, value: np.float32) -> None:
        """Set the MaximumNormalizedSpeed field value."""
        member = self.get_member("MaximumNormalizedSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumNormalizedSpeed", fields.FieldFloat(value=value)
            )

    @property
    def default_icon(self) -> str | None:
        """The _defaultIcon field value."""
        member = self.get_member("_defaultIcon")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_icon.setter
    def default_icon(self, value: str) -> None:
        """Set the _defaultIcon field value."""
        member = self.get_member("_defaultIcon")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_defaultIcon", fields.FieldUri(value=value)
            )

    @property
    def default_color(self) -> primitives.ColorX | None:
        """The _defaultColor field value."""
        member = self.get_member("_defaultColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_color.setter
    def default_color(self, value: primitives.ColorX) -> None:
        """Set the _defaultColor field value."""
        member = self.get_member("_defaultColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_defaultColor", fields.FieldColorX(value=value)
            )

    @property
    def character_controller(self) -> str | None:
        """Target ID of the _characterController reference (targets CharacterController)."""
        member = self.get_member("_characterController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @character_controller.setter
    def character_controller(self, target: str | CharacterController | None) -> None:
        """Set the _characterController reference by target ID or CharacterController instance."""
        target_id: str | None = target.id if isinstance(target, CharacterController) else target  # type: ignore[assignment]
        member = self.get_member("_characterController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_characterController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CharacterController'),
            )

    @property
    def legacy_name(self) -> str | None:
        """The __legacyName field value."""
        member = self.get_member("__legacyName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_name.setter
    def legacy_name(self, value: str) -> None:
        """Set the __legacyName field value."""
        member = self.get_member("__legacyName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyName", fields.FieldString(value=value)
            )

