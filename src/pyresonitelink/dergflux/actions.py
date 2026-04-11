"""Prebuilt ActionDef definitions for common ProtoFlux action nodes.

Import these and pass them to ``g.Action()``::

    from pyresonitelink.dergflux import actions

    with g.Action(actions.RaycastOne, origin=s.pos, direction=s.dir) as r:
        with r.on_hit():
            s.distance = r.hit_distance
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux._action import ActionDef, InputDef, OutputDef
from pyresonitelink.generated._types.slot import Slot as _SlotType


RaycastOne = ActionDef(
    import_path="protoflux.physics",
    class_name="RaycastOne",
    inputs={
        "origin": InputDef("origin", primitives.Float3),
        "direction": InputDef("direction", primitives.Float3),
        "max_distance": InputDef("max_distance", primitives.Float),
        "hit_triggers": InputDef("hit_triggers", primitives.Bool),
        "users_only": InputDef("users_only", primitives.Bool),
        "debug_duration": InputDef("debug_duration", primitives.Float),
        "root": InputDef("root"),
    },
    flow_outputs=["on_hit", "on_miss"],
    value_outputs={
        "hit_point": OutputDef("HitPoint", primitives.Float3),
        "hit_normal": OutputDef("HitNormal", primitives.Float3),
        "hit_distance": OutputDef("HitDistance", primitives.Float),
        "hit_triangle_index": OutputDef("HitTriangleIndex", primitives.Int),
    },
)

PlayOneShot = ActionDef(
    import_path="protoflux.audio",
    class_name="PlayOneShot",
    inputs={
        "clip": InputDef(
            "clip",
            ref_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>",
        ),
        "volume": InputDef("volume", primitives.Float),
        "speed": InputDef("speed", primitives.Float),
        "spatialize": InputDef("spatialize", primitives.Bool),
        "spatial_blend": InputDef("spatial_blend", primitives.Float),
        "point": InputDef("point", primitives.Float3),
        "root": InputDef("root"),
        "parent_under_root": InputDef("parent_under_root", primitives.Bool),
        "priority": InputDef("priority", primitives.Int),
        "local_only": InputDef("local_only", primitives.Bool),
    },
    flow_outputs=["on_started_playing"],
    value_outputs={},
)

# =========================================================================
# Data source nodes — value outputs only, no flow
# =========================================================================

StandardController = ActionDef(
    import_path="protoflux.devices.controllers",
    class_name="StandardController",
    inputs={
        "user": InputDef("user"),
        "node": InputDef("node"),
    },
    flow_outputs=[],
    value_outputs={
        "is_active": OutputDef("IsActive", primitives.Bool),
        "battery_level": OutputDef("BatteryLevel", primitives.Float),
        "is_battery_charging": OutputDef("IsBatteryCharging", primitives.Bool),
        "primary": OutputDef("Primary", primitives.Bool),
        "secondary": OutputDef("Secondary", primitives.Bool),
        "grab": OutputDef("Grab", primitives.Float),
        "menu": OutputDef("Menu", primitives.Bool),
        "strength": OutputDef("Strength", primitives.Float),
        "axis": OutputDef("Axis", primitives.Float2),
    },
)

IndexController = ActionDef(
    import_path="protoflux.devices.controllers",
    class_name="IndexController",
    inputs={
        "user": InputDef("user"),
        "node": InputDef("node"),
    },
    flow_outputs=[],
    value_outputs={
        "is_active": OutputDef("IsActive", primitives.Bool),
        "battery_level": OutputDef("BatteryLevel", primitives.Float),
        "is_battery_charging": OutputDef("IsBatteryCharging", primitives.Bool),
        "button_a": OutputDef("ButtonA", primitives.Bool),
        "button_b": OutputDef("ButtonB", primitives.Bool),
        "button_a_touch": OutputDef("ButtonATouch", primitives.Bool),
        "button_b_touch": OutputDef("ButtonBTouch", primitives.Bool),
        "grip": OutputDef("Grip", primitives.Float),
        "grip_touch": OutputDef("GripTouch", primitives.Bool),
        "trigger": OutputDef("Trigger", primitives.Float),
        "trigger_touch": OutputDef("TriggerTouch", primitives.Bool),
        "thumbstick_x": OutputDef("ThumbstickX", primitives.Float),
        "thumbstick_y": OutputDef("ThumbstickY", primitives.Float),
        "thumbstick_touch": OutputDef("ThumbstickTouch", primitives.Bool),
        "thumbstick_press": OutputDef("ThumbstickPress", primitives.Bool),
        "trackpad_x": OutputDef("TrackpadX", primitives.Float),
        "trackpad_y": OutputDef("TrackpadY", primitives.Float),
        "trackpad_touch": OutputDef("TrackpadTouch", primitives.Bool),
        "trackpad_press": OutputDef("TrackpadPress", primitives.Bool),
    },
)

TouchController = ActionDef(
    import_path="protoflux.devices.controllers",
    class_name="TouchController",
    inputs={
        "user": InputDef("user"),
        "node": InputDef("node"),
    },
    flow_outputs=[],
    value_outputs={
        "is_active": OutputDef("IsActive", primitives.Bool),
        "battery_level": OutputDef("BatteryLevel", primitives.Float),
        "is_battery_charging": OutputDef("IsBatteryCharging", primitives.Bool),
        "button_a": OutputDef("ButtonA", primitives.Bool),
        "button_b": OutputDef("ButtonB", primitives.Bool),
        "button_a_touch": OutputDef("ButtonATouch", primitives.Bool),
        "button_b_touch": OutputDef("ButtonBTouch", primitives.Bool),
        "grip": OutputDef("Grip", primitives.Float),
        "trigger": OutputDef("Trigger", primitives.Float),
        "trigger_touch": OutputDef("TriggerTouch", primitives.Bool),
        "thumbstick_x": OutputDef("ThumbstickX", primitives.Float),
        "thumbstick_y": OutputDef("ThumbstickY", primitives.Float),
        "thumbstick_touch": OutputDef("ThumbstickTouch", primitives.Bool),
        "thumbstick_press": OutputDef("ThumbstickPress", primitives.Bool),
    },
)

ViveController = ActionDef(
    import_path="protoflux.devices.controllers",
    class_name="ViveController",
    inputs={
        "user": InputDef("user"),
        "node": InputDef("node"),
    },
    flow_outputs=[],
    value_outputs={
        "is_active": OutputDef("IsActive", primitives.Bool),
        "battery_level": OutputDef("BatteryLevel", primitives.Float),
        "is_battery_charging": OutputDef("IsBatteryCharging", primitives.Bool),
        "menu": OutputDef("Menu", primitives.Bool),
        "grip": OutputDef("Grip", primitives.Bool),
        "trigger": OutputDef("Trigger", primitives.Float),
        "trigger_hair": OutputDef("TriggerHair", primitives.Bool),
        "trigger_click": OutputDef("TriggerClick", primitives.Bool),
        "trackpad_x": OutputDef("TrackpadX", primitives.Float),
        "trackpad_y": OutputDef("TrackpadY", primitives.Float),
        "trackpad_touch": OutputDef("TrackpadTouch", primitives.Bool),
        "trackpad_press": OutputDef("TrackpadPress", primitives.Bool),
    },
)

SlotChildrenEvents = ActionDef(
    import_path="protoflux.slots",
    class_name="SlotChildrenEvents",
    inputs={
        "instance": InputDef(
            "instance",
            global_type="[FrooxEngine]FrooxEngine.Slot",
        ),
    },
    flow_outputs=["on_child_added", "on_child_removed"],
    value_outputs={
        "child": OutputDef("Child", _SlotType),
    },
    is_event_source=True,
)

# =========================================================================
# Event sources — fire impulses on their own, no trigger needed
# =========================================================================

FireOnTrue = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnTrue",
    inputs={
        "condition": InputDef("condition", primitives.Bool),
    },
    flow_outputs=["on_changed"],
    is_event_source=True,
)

FireOnFalse = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnFalse",
    inputs={
        "condition": InputDef("condition", primitives.Bool),
    },
    flow_outputs=["on_changed"],
    is_event_source=True,
)

FireOnLocalTrue = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnLocalTrue",
    inputs={
        "condition": InputDef("condition", primitives.Bool),
    },
    flow_outputs=["on_change"],
    is_event_source=True,
)

FireOnLocalFalse = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnLocalFalse",
    inputs={
        "condition": InputDef("condition", primitives.Bool),
    },
    flow_outputs=["on_change"],
    is_event_source=True,
)

FireOnValueChange = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnValueChange",
    inputs={
        "value": InputDef("value", object),  # generic value expression
    },
    flow_outputs=["on_changed"],
    is_event_source=True,
)

FireOnLocalValueChange = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnLocalValueChange",
    inputs={
        "value": InputDef("value", object),
    },
    flow_outputs=["on_change"],
    is_event_source=True,
)

FireOnObjectValueChange = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnObjectValueChange",
    inputs={
        "value": InputDef("value"),  # reference — pass component ID
    },
    flow_outputs=["on_changed"],
    is_event_source=True,
)

FireOnLocalObjectChange = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnLocalObjectChange",
    inputs={
        "value": InputDef("value"),  # reference — pass component ID
    },
    flow_outputs=["on_change"],
    is_event_source=True,
)

FireOnRefChange = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnRefChange",
    inputs={
        "value": InputDef("value"),  # reference — pass component ID
    },
    flow_outputs=["on_changed"],
    is_event_source=True,
)

FireOnTypeChange = ActionDef(
    import_path="protoflux.flow",
    class_name="FireOnTypeChange",
    inputs={
        "value": InputDef("value"),  # reference — pass component ID
    },
    flow_outputs=["on_changed"],
    is_event_source=True,
)

FireWhileTrue = ActionDef(
    import_path="protoflux.flow",
    class_name="FireWhileTrue",
    inputs={
        "condition": InputDef("condition", primitives.Bool),
    },
    flow_outputs=["on_update"],
    is_event_source=True,
)

LocalFireWhileTrue = ActionDef(
    import_path="protoflux.flow",
    class_name="LocalFireWhileTrue",
    inputs={
        "condition": InputDef("condition", primitives.Bool),
    },
    flow_outputs=["on_update"],
    is_event_source=True,
)

# =========================================================================
# Lifecycle events — fire once on specific lifecycle events
# =========================================================================

OnActivated = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnActivated",
    inputs={
        "only_host": InputDef("only_host", primitives.Bool),
    },
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnDeactivated = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnDeactivated",
    inputs={
        "only_host": InputDef("only_host", primitives.Bool),
    },
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnStart = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnStart",
    inputs={
        "only_host": InputDef("only_host", primitives.Bool),
    },
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnDestroy = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnDestroy",
    inputs={
        "only_host": InputDef("only_host", primitives.Bool),
    },
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnDestroying = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnDestroying",
    inputs={},
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnLoaded = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnLoaded",
    inputs={},
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnDuplicate = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnDuplicate",
    inputs={},
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnPaste = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnPaste",
    inputs={},
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnSaving = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnSaving",
    inputs={},
    flow_outputs=["trigger"],
    is_event_source=True,
)

OnPackageImported = ActionDef(
    import_path="protoflux.flow.events",
    class_name="OnPackageImported",
    inputs={},
    flow_outputs=["trigger"],
    is_event_source=True,
)

UpdatesTimer = ActionDef(
    import_path="protoflux.flow",
    class_name="UpdatesTimer",
    inputs={
        "interval": InputDef("interval", primitives.Int),
    },
    flow_outputs=["on_update"],
    is_event_source=True,
)

SecondsTimer = ActionDef(
    import_path="protoflux.flow",
    class_name="SecondsTimer",
    inputs={
        "interval": InputDef("interval", primitives.Float),
    },
    flow_outputs=["on_update"],
    is_event_source=True,
)

# =========================================================================
# Async actions — suspend across frames
# =========================================================================

DelaySecondsFloat = ActionDef(
    import_path="protoflux.flow",
    class_name="DelaySecondsFloat",
    inputs={
        "duration": InputDef("duration", primitives.Float),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

DelaySecondsDouble = ActionDef(
    import_path="protoflux.flow",
    class_name="DelaySecondsDouble",
    inputs={
        "duration": InputDef("duration", primitives.Double),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

DelaySecondsInt = ActionDef(
    import_path="protoflux.flow",
    class_name="DelaySecondsInt",
    inputs={
        "duration": InputDef("duration", primitives.Int),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

DelayUpdates = ActionDef(
    import_path="generated.protoflux.runtimes.execution.nodes.flow.async",
    class_name="DelayUpdates",
    inputs={
        "updates": InputDef("updates", primitives.Int),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

DelayUpdatesOrSecondsFloat = ActionDef(
    import_path="generated.protoflux.runtimes.execution.nodes.flow.async",
    class_name="DelayUpdatesOrSecondsFloat",
    inputs={
        "updates": InputDef("updates", primitives.Int),
        "duration": InputDef("duration", primitives.Float),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

DelayUpdatesOrSecondsDouble = ActionDef(
    import_path="generated.protoflux.runtimes.execution.nodes.flow.async",
    class_name="DelayUpdatesOrSecondsDouble",
    inputs={
        "updates": InputDef("updates", primitives.Int),
        "duration": InputDef("duration", primitives.Double),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

DelayUpdatesOrSecondsInt = ActionDef(
    import_path="generated.protoflux.runtimes.execution.nodes.flow.async",
    class_name="DelayUpdatesOrSecondsInt",
    inputs={
        "updates": InputDef("updates", primitives.Int),
        "duration": InputDef("duration", primitives.Int),
    },
    flow_outputs=["next", "on_triggered"],
    is_async=True,
)

# =========================================================================
# Impulse-triggered actions
# =========================================================================

PlayOneShotAndWait = ActionDef(
    import_path="protoflux.audio",
    class_name="PlayOneShotAndWait",
    inputs={
        "clip": InputDef(
            "clip",
            ref_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>",
        ),
        "volume": InputDef("volume", primitives.Float),
        "speed": InputDef("speed", primitives.Float),
        "spatialize": InputDef("spatialize", primitives.Bool),
        "spatial_blend": InputDef("spatial_blend", primitives.Float),
        "point": InputDef("point", primitives.Float3),
        "root": InputDef("root"),
        "parent_under_root": InputDef("parent_under_root", primitives.Bool),
        "priority": InputDef("priority", primitives.Int),
        "local_only": InputDef("local_only", primitives.Bool),
    },
    flow_outputs=["on_started_playing", "on_finished_playing"],
    value_outputs={},
    is_async=True,
)
