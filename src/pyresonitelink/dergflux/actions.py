"""Prebuilt ActionDef definitions for common ProtoFlux action nodes.

Import these and pass them to ``g.Action()``::

    from pyresonitelink.dergflux import actions

    with g.Action(actions.RaycastOne, origin=s.pos, direction=s.dir) as r:
        with r.on_hit():
            s.distance = r.hit_distance
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux._action import ActionDef, InputDef, OutputDef


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
        "clip": InputDef("clip"),
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

PlayOneShotAndWait = ActionDef(
    import_path="protoflux.audio",
    class_name="PlayOneShotAndWait",
    inputs={
        "clip": InputDef("clip"),
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
)
