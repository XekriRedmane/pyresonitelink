"""Generated enum: ColliderType."""

from enum import StrEnum


class ColliderType(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.ColliderType."""

    no_collision = "NoCollision"
    static = "Static"
    trigger = "Trigger"
    static_trigger = "StaticTrigger"
    static_trigger_auto = "StaticTriggerAuto"
    active = "Active"
    character_controller = "CharacterController"
    haptic_trigger = "HapticTrigger"
    haptic_static_trigger = "HapticStaticTrigger"
    haptic_static_trigger_auto = "HapticStaticTriggerAuto"
    haptic_sampler = "HapticSampler"

