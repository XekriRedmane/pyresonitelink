"""Example of a golf ball that a ProtoFlux graph moves, on a small course with a club.

Resonite moves nothing by physics except characters, and its colliders
have no friction or bounciness. So the graph that this script builds
moves the ball itself, once per engine update, and finds what the ball
touches with ray casts. Every surface, the ball, and the club head carry
their own physical properties as dynamic variables, so the ball bounces
high off concrete, dies in the sand, and rolls far on the green.

The course is built on the floor 2 m in front of the user, running away
from them. From the tee it has a fairway with a ramp, a bunker sunk 3 cm
into the fairway, more fairway, and a green, with low concrete walls
along the sides and a tall concrete backstop at the far end. Next to the
tee are a club and a "Tee" button, which puts the ball back on the tee.
In VR the club can be grabbed by its grip and swung, and the ball can be
picked up, placed, and thrown.

Desktop shots
-------------

A desktop user can't swing the club by hand, so a shot takes three
steps with the mouse.

1. Click the ball while it is at rest. This addresses the ball, and an
   arrow on the ground shows where the shot will go. A gauge in front of
   the view shows the club, which the scroll wheel changes.
2. Look at where the ball should go. The arrow points from the ball to
   the spot on the ground under the crosshair, or along the view when
   that spot is farther than MAX_AIM_DISTANCE.
3. Press and hold the left button. The aim stops following the view,
   and the gauge fills and empties again every FILL_TIME seconds.
   Release it to swing the club along the arrow, with a head speed that
   rises with the square of the gauge's fill. A release within TAP_TIME
   of the press, or with the gauge nearly empty, swings nothing, and the
   ball stays addressed.

A right click, or a click on the ball, lets go of the ball, so that the
left button presses things again. Grabbing the ball, or the ball moving,
also lets go of it.

The mouse is read on the desktop user's machine, by a flow that runs only
where the local user's machine ID matches the "golfer" model variable.
That flow passes the swing to the host's flow through model variables,
and the host swings the club.

Physical properties
-------------------

Each course piece's slot has a DynamicVariableSpace named "Physics" with
float variables Restitution, Friction, and Rolling. The ball's slot has
the same three and Mass, and the club head's has Restitution and Mass.
The graph reads them while it runs, so they can be changed in the
inspector. A collider whose slot and ancestors have no Physics space gets
DEFAULT_SURFACE.

When the ball touches a surface, the two restitutions multiply, and the
two friction and rolling coefficients combine as their geometric mean,
as Box2D combines friction. The ball's own values are BALL.

What the graph does in each engine update
-----------------------------------------

The graph runs on the host only, since every user's machine runs an
Update node and they would otherwise all move the ball.

While the ball is held, the graph only measures its velocity from how
far it moved since the last update, so a thrown ball flies on at the
hand's velocity.

Otherwise, in this order:

1. If a desktop user released a shot, the club is posed at the top of
   its backswing, facing along the shot, and in later updates it turns
   about a pivot above the ball until its follow-through.
2. The ball's center is found in the club head's space. If it crossed
   the plane of the face, within the face's bounds, since the last
   update, while the ball and the face moved toward each other, the ball
   is hit. Comparing positions in the head's own space catches a fast
   swing that moves the face past the ball within one update. The hit
   changes the ball's velocity along the face normal by the impulse
   between two bodies of the ball's and the head's masses. A ball sent
   back to the tee starts its history in the head's space again, so that
   the jump doesn't count as a crossing.
3. Gravity is added to the velocity.
4. A ray from the ball's center straight down, one radius and PROBE_SKIN
   long, finds the ground the ball rests on. A ball falling onto it
   faster than BOUNCE_SPEED bounces, and one moving more slowly rolls
   along it, slowed by rolling resistance.
5. A ray from the ball's center along its velocity, as long as one
   update's travel plus a radius, finds anything the ball reaches in this
   update. The ball stops against it, touching it, and bounces or slides.
   Otherwise the ball moves on.

A bounce reverses the velocity's part along the surface normal and scales
it by the restitution. Coulomb friction slows the part along the surface
by up to the friction times the normal impulse. A ball that wasn't
spinning can't lose more than 2/7 of that part this way, because once
its spin catches up with its speed it rolls instead of sliding, and a
solid sphere then keeps 5/7 of the speed it slid with. For the same
reason, a rolling ball speeds up down a slope at 5/7 of the rate of a
sliding one.

Limits
------

The ball doesn't spin, so it has no backspin, hook, or slice. The rays
start at the ball's center, so where the ball meets an edge rather than
a face, it can stop up to a radius away from the true point of contact.
The club's head has no collider, and the ball goes through its back and
sides. A ball that falls 3 m below the course goes back to the tee. Each
run deletes the course from the previous run.

The aiming spot is where the view meets the level plane through the
ball's center, so on the ramp it is off from the true spot under the
crosshair by the ramp's height. Whoever clicks the ball takes it over
from a desktop user who is aiming, so a user who leaves the session
while aiming doesn't keep the ball from everyone else.

Recording
---------

The graph records the ball's velocity before and after each bounce and
each hit of the club, the club head's velocity at a hit, and the ball's
position and velocity at the end of each update, with a
utils.recorder.Recorder named "trace". It records nothing until a script
starts it by writing the number of lines to record to the "trace_left"
model variable, under the ProtoFlux slot, and then reads the lines from
"trace_log".

Usage:
    python examples/dergflux_golf.py [port]

If the port is omitted, the session is found from its LAN announcement.
Requires a running Resonite session with ResoniteLink enabled.
"""

import asyncio
import dataclasses
import math
import sys
from typing import Any

from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux import interaction
from pyresonitelink.dergflux import math as dm
from pyresonitelink.dergflux import mouse
from pyresonitelink.dergflux import slots
from pyresonitelink.dergflux import time
from pyresonitelink.dergflux import transform
from pyresonitelink.dergflux import users
from pyresonitelink.dergflux import variables
from pyresonitelink.generated.assets.materials import pbs_metallic
from pyresonitelink.generated.assets.procedural_meshes import arrow_mesh
from pyresonitelink.generated.assets.procedural_meshes import box_mesh
from pyresonitelink.generated.assets.procedural_meshes import cylinder_mesh
from pyresonitelink.generated.assets.procedural_meshes import ring_mesh
from pyresonitelink.generated.assets.procedural_meshes import sphere_mesh
from pyresonitelink.generated.data.dynamic import dynamic_value_variable
from pyresonitelink.generated.data.dynamic import dynamic_variable_space
from pyresonitelink.generated.physics.colliders import box_collider
from pyresonitelink.generated.physics.colliders import sphere_collider
from pyresonitelink.generated.rendering import text_renderer
from pyresonitelink.generated.transform.interaction import grabbable
from pyresonitelink.generated.transform.interaction import touch_button
from pyresonitelink.utils import materials
from pyresonitelink.utils import placement
from pyresonitelink.utils import recorder
from pyresonitelink.utils import rendering
from pyresonitelink.utils import slots as slot_utils

SLOT_NAME = "Dergflux Golf Example"
DISTANCE = 2.0  # meters from the user's feet to the tee
TOP = 0.1  # meters from the floor to the course's playing surface
BUNKER_DEPTH = 0.03  # meters from the playing surface down to the sand

GRAVITY = 9.81  # m/s^2
# The longest time step the graph takes, so that a stalled frame doesn't
# throw the ball through the course.
MAX_STEP = 1 / 20  # seconds
# How far below the ball's surface the ground ray looks, so that a ball
# rolling over small bumps stays on the ground.
PROBE_SKIN = 0.005  # meters
# The speed along a surface's normal below which the ball stops bouncing
# and rolls. It is more than GRAVITY * MAX_STEP, so that the speed that
# gravity adds in one update to a resting ball doesn't make it bounce.
BOUNCE_SPEED = 0.6  # m/s
# The share of its speed that a solid sphere keeps when it goes from
# sliding to rolling, which is also the share of a sliding sphere's
# acceleration down a slope that a rolling one has.
ROLLING_SHARE = 5 / 7
# How far in front of the club face a hit ball is put, so that the next
# update doesn't find it crossing the face again.
FACE_CLEARANCE = 0.001  # meters
# How far below the course a ball goes back to the tee.
LOST_DEPTH = 3.0  # meters


@dataclasses.dataclass(frozen=True)
class Physics:
    """Represents the physical properties that a slot's Physics space holds.

    Attributes:
        restitution (float): The ratio of the speed away from a surface
            after a bounce to the speed toward it before, from 0 to 1, as
            a property of this body alone. A contact multiplies the two
            bodies' values.
        friction (float): The Coulomb friction coefficient. A contact
            uses the geometric mean of the two bodies' values.
        rolling (float): The rolling resistance coefficient, the ratio of
            the force that slows a rolling ball to its weight. A contact
            uses the geometric mean of the two bodies' values.
        mass (float): The mass in kilograms, for bodies that collide with
            each other, or 0 for surfaces that don't move.
    """

    restitution: float
    friction: float = 0.0
    rolling: float = 0.0
    mass: float = 0.0


# The Rules of Golf set a 42.67 mm minimum diameter and a 45.93 g maximum
# mass.
BALL_RADIUS = 0.02135  # meters
BALL = Physics(restitution=0.9, friction=0.5, rolling=0.1, mass=0.04593)

# A contact with these values and BALL's gives the ball a restitution of
# 0.36, a friction coefficient of 0.55, and a rolling resistance
# coefficient of 0.14, which slows a rolling ball by 1.4 m/s^2.
FAIRWAY = Physics(restitution=0.4, friction=0.6, rolling=0.2)
# A rolling ball slows by 0.54 m/s^2, so that one rolled at 1.83 m/s goes
# 3.1 m, which is a 10 on the Stimpmeter.
GREEN = Physics(restitution=0.3, friction=0.6, rolling=0.03)
BUNKER = Physics(restitution=0.08, friction=0.9, rolling=4.0)
CONCRETE = Physics(restitution=0.85, friction=0.7, rolling=0.02)
WOOD = Physics(restitution=0.6, friction=0.4, rolling=0.03)
DEFAULT_SURFACE = Physics(restitution=0.5, friction=0.5, rolling=0.2)

# A club head with this restitution gives a ball with BALL's a
# coefficient of restitution of 0.83, the limit that the Rules of Golf
# set for drivers.
CLUB_HEAD = Physics(restitution=0.92, mass=0.2)

# The club, in its own space, has its grip's center at the origin, the
# shaft down -Y, and the face toward +Z.
GRIP_LENGTH = 0.26  # meters
GRIP_RADIUS = 0.013  # meters
SHAFT_RADIUS = 0.0055  # meters
HEAD_DROP = 0.9  # meters from the grip's center down to the head's center
# The head is a box, heel to toe along X, sole to top along Y, and back to
# face along Z, tilted back by the selected club's loft so the face looks
# upward.
HEAD_SIZE = (0.075, 0.045, 0.02)  # meters

# A desktop swing turns the club about a pivot this far above the ball's
# center, so the head's center is this far from the pivot and passes
# through the ball's center at the bottom of the swing.
PIVOT_HEIGHT = 1.4  # meters


@dataclasses.dataclass(frozen=True)
class Club:
    """Represents one of the clubs that the club head can be.

    A ball leaves a head with CLUB_HEAD's and BALL's values at about 1.5
    times the head's speed, along the face normal, at the loft above
    level.

    Attributes:
        name (str): The name that the gauge shows.
        loft (float): The face's angle back from vertical, in degrees.
        speed (float): The head's speed at the bottom of a desktop swing
            with the gauge full, in m/s.
        backswing (float): How far back a desktop swing with the gauge
            full starts, in degrees about the pivot. It only changes how
            the swing looks, since the head's speed is set separately.
    """

    name: str
    loft: float
    speed: float
    backswing: float


# The clubs in the order that the scroll wheel steps through them. The
# first is the one the club starts as. A full iron shot lands about 13 m
# away on level ground, and a full putt rolls about 5 m on the green.
CLUBS = [
    Club("7 Iron", loft=30.0, speed=8.0, backswing=100.0),
    Club("Wedge", loft=50.0, speed=7.0, backswing=90.0),
    Club("Putter", loft=3.0, speed=1.6, backswing=25.0),
]
# The share of a club's full head speed and backswing that an empty
# gauge gives. The speed rises with the square of the fill, so that short
# shots are easier to judge.
MIN_SPEED_SHARE = 0.1
MIN_BACKSWING_SHARE = 0.2
FILL_TIME = 1.2  # seconds for the gauge to fill from empty
# A shot released with the gauge below this fill, or this soon after the
# press, swings nothing. Without TAP_TIME a quick click would swing, since
# the gauge fills by an eighth in 0.15 s.
CANCEL_FILL = 0.03
TAP_TIME = 0.2  # seconds

# The crosshair is on the ball when the view's ray passes within this
# distance of the ball's center, and the ball is no farther than REACH.
CLICK_RADIUS = 0.06  # meters
REACH = 5.0  # meters
# A ball slower than this is at rest and can be addressed.
REST_SPEED = 0.05  # m/s
# The aiming spot is used only when the view looks down by at least this
# much (the sine of the angle below level) and the spot is no farther
# than MAX_AIM_DISTANCE. The arrow keeps its direction while the spot is
# closer to the ball than MIN_AIM_DISTANCE.
MIN_LOOK_DOWN = 0.05
MAX_AIM_DISTANCE = 30.0  # meters
MIN_AIM_DISTANCE = 0.1  # meters
# The arrow's length is ARROW_LENGTH, plus ARROW_GROWTH times the gauge's
# fill.
ARROW_LENGTH = 0.5  # meters
ARROW_GROWTH = 0.8  # meters
ARROW_LIFT = 0.005  # meters from the ball's center up to the arrow

# The gauge, in the view's space, with the view looking along +Z.
GAUGE_AT = (0.0, -0.1, 0.45)  # meters
GAUGE_RADIUS = 0.05  # meters, to the outside of the ring
GAUGE_WIDTH = 0.008  # meters
# TextRenderer sizes. A Size is about 6.5 times the letter height, so
# these make letters about 1.3 cm and 0.6 cm tall, seen from 0.45 m.
CLUB_LABEL_SIZE = 0.085
HINT_SIZE = 0.04
HINT = "Look to aim, hold left to swing\nScroll for a club, right-click to let go"


@dataclasses.dataclass(frozen=True)
class Piece:
    """Represents one box of the course.

    Attributes:
        name (str): The slot's name.
        size (tuple[float, float, float]): The box's width, height, and
            length in meters.
        center (tuple[float, float, float]): The box's center in the
            course's space, with the floor at Y = 0 and the tee at the
            origin's X and Z.
        finish (str): The key of the box's material in FINISHES.
        physics (Physics): The box's physical properties.
        tilt (float): The box's rotation about X in degrees. A positive
            tilt turns +Y toward +Z.
    """

    name: str
    size: tuple[float, float, float]
    center: tuple[float, float, float]
    finish: str
    physics: Physics
    tilt: float = 0.0


FINISHES = {
    "Fairway": materials.Finish((0.05, 0.25, 0.03), metallic=0.0, smoothness=0.15),
    "Green": materials.Finish((0.08, 0.45, 0.06), metallic=0.0, smoothness=0.25),
    "Sand": materials.Finish((0.65, 0.52, 0.3), metallic=0.0, smoothness=0.05),
    "Concrete": materials.Finish((0.35, 0.35, 0.33), metallic=0.0, smoothness=0.2),
    "Wood": materials.Finish((0.4, 0.2, 0.08), metallic=0.0, smoothness=0.4),
    "Ball": materials.Finish((0.9, 0.9, 0.9), metallic=0.0, smoothness=0.7),
    "Steel": materials.Finish((0.6, 0.6, 0.62), metallic=0.9, smoothness=0.75),
    "Grip": materials.Finish((0.02, 0.02, 0.02), metallic=0.0, smoothness=0.3),
    "Button": materials.Finish((0.1, 0.2, 0.5), metallic=0.2, smoothness=0.5),
    # The arrow and the gauge glow, so that they show in any light.
    "Aim": materials.Finish((0.9, 0.8, 0.1), metallic=0.0, smoothness=0.3,
                            emissive=(0.6, 0.5, 0.05)),
    "Gauge": materials.Finish((0.1, 0.1, 0.1), metallic=0.0, smoothness=0.3,
                              emissive=(0.08, 0.08, 0.08)),
    "Power": materials.Finish((0.9, 0.35, 0.05), metallic=0.0, smoothness=0.3,
                              emissive=(0.9, 0.35, 0.05)),
}


def _slab(name: str, x: tuple[float, float], z: tuple[float, float], top: float,
          finish: str, physics: Physics) -> Piece:
    """Returns a level 0.1 m slab covering a rectangle, with its top at a height."""
    return Piece(
        name, (x[1] - x[0], 0.1, z[1] - z[0]),
        ((x[0] + x[1]) / 2, top - 0.05, (z[0] + z[1]) / 2), finish, physics,
    )


def _ramp(name: str, x: float, z: float, length: float, angle: float) -> Piece:
    """Returns a 4 cm thick wooden ramp that rises toward +Z from the playing surface.

    Args:
        name: The slot's name.
        x: The ramp's center across the course.
        z: Where the ramp's top surface meets the playing surface.
        length: The length of the ramp's top surface.
        angle: How steeply the ramp rises, in degrees.
    """
    thickness = 0.04
    a = math.radians(angle)
    # The top surface's normal leans back toward -Z, and the middle of the
    # top surface is half the length up the slope from z.
    top_center = (x, TOP + length / 2 * math.sin(a), z + length / 2 * math.cos(a))
    normal = (0.0, math.cos(a), -math.sin(a))
    center = tuple(c - n * thickness / 2 for c, n in zip(top_center, normal))
    return Piece(name, (0.6, thickness, length), center, "Wood", WOOD, tilt=-angle)  # type: ignore[arg-type]


COURSE = [
    _slab("Tee Fairway", (-1.5, 1.5), (-1.0, 4.0), TOP, "Fairway", FAIRWAY),
    _ramp("Ramp", 0.8, 1.5, 1.2, 10.0),
    _slab("Bunker", (-1.5, 0.0), (4.0, 6.0), TOP - BUNKER_DEPTH, "Sand", BUNKER),
    _slab("Fairway Beside Bunker", (0.0, 1.5), (4.0, 6.0), TOP, "Fairway", FAIRWAY),
    _slab("Fairway", (-1.5, 1.5), (6.0, 9.0), TOP, "Fairway", FAIRWAY),
    _slab("Green", (-1.5, 1.5), (9.0, 13.0), TOP, "Green", GREEN),
    Piece("Left Wall", (0.15, 0.3, 14.15), (-1.575, 0.15, 6.075), "Concrete", CONCRETE),
    Piece("Right Wall", (0.15, 0.3, 14.15), (1.575, 0.15, 6.075), "Concrete", CONCRETE),
    Piece("Backstop", (3.3, 2.5, 0.15), (0.0, 1.25, 13.075), "Concrete", CONCRETE),
]

TEE = (0.0, TOP + BALL_RADIUS, 0.0)  # the ball's center on the tee
CLUB_START = (0.35, TOP + HEAD_DROP + 0.05, -0.15)  # the club's grip
BUTTON_AT = (-0.9, 1.0, -0.8)  # the Tee button's center
BUTTON_SIZE = (0.14, 0.07, 0.02)  # meters
LABEL_SIZE = 0.18  # the TextRenderer's Size, which makes letters about 3 cm tall
# A positive tilt turns the button's face, toward -Z, up toward the user's
# eyes.
BUTTON_TILT = 30.0  # degrees


async def add_physics(resolink: client.Client, slot: workers.Slot, physics: Physics) -> None:
    """Gives a slot a Physics space with a body's physical properties.

    Mass is added only for bodies that move.
    """
    await dynamic_variable_space.DynamicVariableSpace(
        space_name="Physics", only_direct_binding=False,
    ).add_to_slot(resolink, slot)
    values = {
        "Restitution": physics.restitution,
        "Friction": physics.friction,
        "Rolling": physics.rolling,
    }
    if physics.mass > 0:
        values["Mass"] = physics.mass
    for name, value in values.items():
        await dynamic_value_variable.DynamicValueVariable[primitives.Float](
            variable_name=f"Physics/{name}", value=primitives.Float(value),
        ).add_to_slot(resolink, slot)


async def add_box(
    resolink: client.Client,
    parent: workers.Slot,
    name: str,
    size: tuple[float, float, float],
    material: pbs_metallic.PBS_Metallic,
    *,
    position: tuple[float, float, float] = (0.0, 0.0, 0.0),
    tilt: float = 0.0,
    collider: bool = True,
) -> workers.Slot:
    """Adds a slot with a box mesh, and a box collider of the same size.

    Args:
        resolink: The connected client.
        parent: The slot to add the box under.
        name: The new slot's name.
        size: The box's size along X, Y, and Z in meters.
        material: The box's material.
        position: The box's center in the parent's space.
        tilt: The box's rotation about X in degrees.
        collider: Whether to add a collider.

    Returns:
        The new slot.
    """
    a = math.radians(tilt)
    slot = await resolink.add_slot(
        parent=parent, name=name, position=position,
        rotation=(math.sin(a / 2), 0, 0, math.cos(a / 2)),
    )
    mesh = box_mesh.BoxMesh(size=primitives.Float3(*size))
    await mesh.add_to_slot(resolink, slot)
    await rendering.add_renderer(resolink, slot, mesh, [material])
    if collider:
        await box_collider.BoxCollider(size=primitives.Float3(*size)).add_to_slot(resolink, slot)
    return slot


async def add_cylinder(
    resolink: client.Client,
    parent: workers.Slot,
    name: str,
    radius: float,
    height: float,
    material: pbs_metallic.PBS_Metallic,
    position: tuple[float, float, float],
) -> workers.Slot:
    """Adds a slot with a cylinder mesh along Y and no collider."""
    slot = await resolink.add_slot(parent=parent, name=name, position=position)
    mesh = cylinder_mesh.CylinderMesh(
        radius=primitives.Float(radius), height=primitives.Float(height),
    )
    await mesh.add_to_slot(resolink, slot)
    await rendering.add_renderer(resolink, slot, mesh, [material])
    return slot


@dataclasses.dataclass
class AimVisuals:
    """Represents the arrow and the gauge of desktop shots.

    Both are under a slot whose world transform is the identity, so that
    the graph can drive their positions and rotations in world space.

    Attributes:
        arrow: The arrow's slot, at its tail.
        arrow_mesh: The arrow's mesh, whose Vector is the arrow in world
            space.
        gauge: The gauge's slot, at the ring's center, facing the user
            from -Z.
        fill: The ring that shows how full the gauge is. Its Arc runs
            from the left end over the top, in degrees.
        club_labels: The slots of the clubs' names, one per club in
            CLUBS, of which the graph shows only the selected one.
    """

    arrow: workers.Slot
    arrow_mesh: arrow_mesh.ArrowMesh
    gauge: workers.Slot
    fill: ring_mesh.RingMesh
    club_labels: list[workers.Slot]


@dataclasses.dataclass
class Scene:
    """Represents the slots and components that the graph uses.

    Attributes:
        course: The example's root slot, whose space is the course's.
        graph: The slot for the ProtoFlux nodes.
        ball: The ball's slot.
        ball_grab: The ball's Grabbable.
        club: The club's slot, at the grip's center.
        head: The club head's slot, at the head's center, with the face
            toward +Z.
        pivot: The pivot of desktop swings, which turns about Y to face
            along the shot.
        arm: The pivot's child, which turns about X to swing the club.
        mount: Where the club goes during a desktop swing.
        tee_button: The Tee button's TouchButton.
        aim: The visuals of desktop shots.
    """

    course: workers.Slot
    graph: workers.Slot
    ball: workers.Slot
    ball_grab: grabbable.Grabbable
    club: workers.Slot
    head: workers.Slot
    pivot: workers.Slot
    arm: workers.Slot
    mount: workers.Slot
    tee_button: touch_button.TouchButton
    aim: AimVisuals


async def build_scene(resolink: client.Client) -> Scene:
    """Builds the course, the ball, the club, and the Tee button in front of the user.

    A slot under Root named SLOT_NAME, from a previous run, is deleted
    first.
    """
    for old in await workers.Slot(id=workers.Slot.ROOT_SLOT_ID).remove_children_named(
        resolink, SLOT_NAME,
    ):
        print(f"Deleted old slot {old}.")
    world = await placement.on_floor_in_front_of_head(resolink, DISTANCE)
    course = await slot_utils.add_slot_at(resolink, world, name=SLOT_NAME)
    print(f"Created slot {course.id}.")
    mats = await materials.add_materials(resolink, course, FINISHES)

    for piece in COURSE:
        slot = await add_box(
            resolink, course, piece.name, piece.size, mats[piece.finish],
            position=piece.center, tilt=piece.tilt,
        )
        await add_physics(resolink, slot, piece.physics)
    print(f"Built {len(COURSE)} course pieces.")

    ball = await resolink.add_slot(parent=course, name="Ball", position=TEE)
    mesh = sphere_mesh.SphereMesh(radius=primitives.Float(BALL_RADIUS))
    await mesh.add_to_slot(resolink, ball)
    await rendering.add_renderer(resolink, ball, mesh, [mats["Ball"]])
    await sphere_collider.SphereCollider(radius=primitives.Float(BALL_RADIUS)).add_to_slot(
        resolink, ball,
    )
    ball_grab = grabbable.Grabbable()
    await ball_grab.add_to_slot(resolink, ball)
    await add_physics(resolink, ball, BALL)

    club = await resolink.add_slot(parent=course, name="Club", position=CLUB_START)
    await grabbable.Grabbable().add_to_slot(resolink, club)
    # The grip is the club's only collider, so a hand grabs the club there
    # and the ball's rays meet nothing else of it.
    await add_box(
        resolink, club, "Grip", (2 * GRIP_RADIUS, GRIP_LENGTH, 2 * GRIP_RADIUS),
        mats["Grip"],
    )
    shaft_top = -GRIP_LENGTH / 2
    shaft_bottom = -HEAD_DROP + HEAD_SIZE[1] / 2
    await add_cylinder(
        resolink, club, "Shaft", SHAFT_RADIUS, shaft_top - shaft_bottom, mats["Steel"],
        (0.0, (shaft_top + shaft_bottom) / 2, 0.0),
    )
    # The loft turns the face's normal, +Z, up toward +Y, which is a
    # negative angle about X. The graph drives the head's rotation from
    # the selected club.
    head = await add_box(
        resolink, club, "Head", HEAD_SIZE, mats["Steel"],
        position=(0.0, -HEAD_DROP, 0.0), tilt=-CLUBS[0].loft, collider=False,
    )
    await add_physics(resolink, head, CLUB_HEAD)

    pivot = await resolink.add_slot(parent=course, name="Swing Pivot")
    arm = await resolink.add_slot(parent=pivot, name="Swing Arm")
    mount = await resolink.add_slot(
        parent=arm, name="Club Mount", position=(0.0, -(PIVOT_HEIGHT - HEAD_DROP), 0.0),
    )

    graph = await resolink.add_slot(parent=course, name="ProtoFlux")
    tee_button = await add_button(resolink, course, "Tee", mats["Button"])
    aim = await add_aim_visuals(resolink, course, mats)
    print("Built the ball, the club, the Tee button, and the aiming visuals.")
    return Scene(course, graph, ball, ball_grab, club, head, pivot, arm, mount, tee_button, aim)


async def add_text(
    resolink: client.Client,
    parent: workers.Slot,
    name: str,
    text: str,
    size: float,
    position: tuple[float, float, float],
) -> workers.Slot:
    """Adds a slot with white text, which reads from the slot's -Z side.

    Returns:
        The new slot.
    """
    slot = await resolink.add_slot(parent=parent, name=name, position=position)
    await text_renderer.TextRenderer(
        text=text, size=primitives.Float(size),
        color=primitives.ColorX(1, 1, 1, 1, "sRGB"),
    ).add_to_slot(resolink, slot)
    return slot


async def add_button(
    resolink: client.Client,
    course: workers.Slot,
    label: str,
    material: pbs_metallic.PBS_Metallic,
) -> touch_button.TouchButton:
    """Adds a labeled button next to the tee, facing the user.

    Returns:
        The button's TouchButton.
    """
    slot = await add_box(
        resolink, course, f"{label} Button", BUTTON_SIZE, material,
        position=BUTTON_AT, tilt=BUTTON_TILT,
    )
    button = touch_button.TouchButton()
    await button.add_to_slot(resolink, slot)
    # The label sits just in front of the face toward the user, at -Z.
    # A size of 0.04 made letters about 6 mm tall, so the size is about
    # 6.5 times the letter height (seen on screen, 23 Oct 2026).
    await add_text(
        resolink, slot, "Label", label, LABEL_SIZE, (0.0, 0.0, -BUTTON_SIZE[2] / 2 - 0.001),
    )
    return button


async def add_ring(
    resolink: client.Client,
    parent: workers.Slot,
    name: str,
    arc: float,
    material: pbs_metallic.PBS_Metallic,
    z: float = 0.0,
) -> ring_mesh.RingMesh:
    """Adds a slot with one of the gauge's rings, in the slot's XY plane.

    Args:
        resolink: The connected client.
        parent: The gauge's slot.
        name: The new slot's name.
        arc: How much of the ring to draw, in degrees, from the left end
            over the top.
        material: The ring's material.
        z: The slot's position along the gauge's Z, so that one ring can
            sit in front of another.

    Returns:
        The ring's mesh.
    """
    slot = await resolink.add_slot(parent=parent, name=name, position=(0.0, 0.0, z))
    mesh = ring_mesh.RingMesh(
        arc=primitives.Float(arc), segments=primitives.Int(48),
        inner_radius=primitives.Float(GAUGE_RADIUS - GAUGE_WIDTH),
        outer_radius=primitives.Float(GAUGE_RADIUS),
    )
    await mesh.add_to_slot(resolink, slot)
    await rendering.add_renderer(resolink, slot, mesh, [material])
    return mesh


async def add_aim_visuals(
    resolink: client.Client,
    course: workers.Slot,
    mats: dict[str, pbs_metallic.PBS_Metallic],
) -> AimVisuals:
    """Adds the arrow and the gauge of desktop shots, hidden until the graph shows them."""
    world = await slot_utils.add_slot_at(
        resolink, transforms.Transform(), name="Aim Visuals", parent=course,
    )
    arrow = await resolink.add_slot(parent=world, name="Aim Arrow", isActive=False)
    arrow_shape = arrow_mesh.ArrowMesh(
        vector=primitives.Float3(0, 0, ARROW_LENGTH),
        body_radius=primitives.Float(0.004), head_radius=primitives.Float(0.012),
        head_length=primitives.Float(0.035),
    )
    await arrow_shape.add_to_slot(resolink, arrow)
    await rendering.add_renderer(resolink, arrow, arrow_shape, [mats["Aim"]])

    gauge = await resolink.add_slot(parent=world, name="Gauge", isActive=False)
    await add_ring(resolink, gauge, "Gauge Back", 180.0, mats["Gauge"])
    fill = await add_ring(resolink, gauge, "Gauge Fill", 0.0, mats["Power"], z=-0.001)
    labels = [
        await add_text(resolink, gauge, f"{club.name} Label", club.name, CLUB_LABEL_SIZE,
                       (0.0, 0.015, 0.0))
        for club in CLUBS
    ]
    await add_text(resolink, gauge, "Hint", HINT, HINT_SIZE, (0.0, -0.02, 0.0))
    return AimVisuals(arrow, arrow_shape, gauge, fill, labels)


async def build_graph(resolink: client.Client, scene: Scene) -> None:
    """Builds the Dergflux graph that moves the ball, swings the club, and takes desktop shots."""
    g = Graph()
    s = g.Space(scene.graph, space_name="Golf")
    s.v = s.Float3ModelVar("velocity")  # the ball's, in world space, in m/s
    # The ball's center in the head's space, the head's center in world
    # space, and the ball's center in world space, as they were at the
    # end of the last update.
    s.prev_q = s.Float3ModelVar("prev_in_head")
    s.prev_head = s.Float3ModelVar("prev_head")
    s.prev_ball = s.Float3ModelVar("prev_ball")
    s.tee_request = s.BoolModelVar("tee_request")
    s.swing_request = s.BoolModelVar("swing_request")
    s.swinging = s.BoolModelVar("swinging")
    s.swing_angle = s.FloatModelVar("swing_angle")  # degrees about the arm's X
    s.swing_back = s.FloatModelVar("swing_back")  # degrees
    s.swing_rate = s.FloatModelVar("swing_rate")  # degrees per second
    s.swing_yaw = s.FloatModelVar("swing_yaw")  # degrees about the course's Y
    # The machine ID of the desktop user who addressed the ball, or an
    # empty string while nobody has.
    s.golfer = s.StringModelVar("golfer", "")
    # The machine ID of a desktop user who pressed the left button on the
    # ball, until the button comes up and addresses the ball.
    s.presser = s.StringModelVar("presser", "")
    s.club = s.IntModelVar("club", 0)  # the index of the club in CLUBS
    s.aim = s.Float3ModelVar("aim")  # the shot's direction, level, in world space
    s.charging = s.BoolModelVar("charging")  # whether the golfer holds the left button
    s.charge_time = s.FloatModelVar("charge_time")  # seconds since it went down
    s.fill = s.FloatModelVar("fill")  # the gauge's fill, from 0 to 1
    s.was_scrolling = s.BoolModelVar("was_scrolling")
    # Records the ball's velocity around each bounce, and its position and
    # velocity at the end of each update, while a script asks for it.
    trace = recorder.Recorder(g, s, "trace")

    course = slots.ref(scene.course)
    ball = slots.ref(scene.ball)
    club = slots.ref(scene.club)
    head = slots.ref(scene.head)
    pivot = slots.ref(scene.pivot)
    arm = slots.ref(scene.arm)
    mount = slots.ref(scene.mount)

    def ball_value(name: str) -> Any:
        return variables.read(ball, f"Physics/{name}", primitives.Float).value

    def head_value(name: str) -> Any:
        return variables.read(head, f"Physics/{name}", primitives.Float).value

    dt = dm.min_(time.delta_time(), MAX_STEP)
    p = transform.global_position(ball)
    head_pos = transform.global_position(head)
    q = transform.global_point_to_local(head, p)
    prev_q = s.prev_q
    up = primitives.Float3(0, 1, 0)
    down = primitives.Float3(0, -1, 0)
    gravity = primitives.Float3(0, -GRAVITY, 0)
    face = HEAD_SIZE[2] / 2 + BALL_RADIUS  # the ball center's Z on the face
    swing_rotation = dm.axis_angle(primitives.Float3(1, 0, 0), s.swing_angle)

    def by_club(values: list[float]) -> Any:
        """Returns the value for the selected club, from one value per club in CLUBS."""
        chosen: Any = values[-1]
        for i in reversed(range(len(values) - 1)):
            chosen = dm.conditional(s.club == i, values[i], chosen)
        return chosen

    def surface_of(hit: Any) -> tuple[Any, Any, Any]:
        """Returns the restitution, friction, and rolling coefficients of a contact."""
        where = slots.of_component(hit.hit_collider)

        def value(name: str, default: float) -> Any:
            r = variables.read(where, f"Physics/{name}", primitives.Float)
            return dm.conditional(r.found, r.value, default)

        return (
            ball_value("Restitution") * value("Restitution", DEFAULT_SURFACE.restitution),
            dm.sqrt(ball_value("Friction") * value("Friction", DEFAULT_SURFACE.friction)),
            dm.sqrt(ball_value("Rolling") * value("Rolling", DEFAULT_SURFACE.rolling)),
        )

    def bounce(where: str, n: Any, restitution: Any, friction: Any) -> None:
        """Bounces the ball off a surface with normal n that it moves into."""
        trace.record(where=f"{where}_in", v=s.v, e=restitution)
        vn = dm.dot(s.v, n)
        along = s.v - n * vn
        # Friction removes up to friction * (1 + e) * |vn| of the speed
        # along the surface, but no more than a rolling ball would lose.
        keep = dm.max_(
            ROLLING_SHARE,
            1 - friction * (1 + restitution) * -vn / dm.max_(dm.magnitude(along), 1e-4),
        )
        s.v = along * keep - n * (vn * restitution)
        trace.record(where=f"{where}_out", v=s.v)

    with g.Under(scene.graph):
        with g.ButtonEvents(button=scene.tee_button) as e:
            with e.pressed():
                s.tee_request = True

    build_desktop_shots(g, s, scene, by_club)

    with g.Under(scene.graph):
        with g.If(users.local_user_is_host()):
            with g.If(interaction.is_grabbed(scene.ball_grab)):
                s.v = (p - s.prev_ball) / dt
            with g.Else():
                lost = transform.global_point_to_local(course, p).y < -LOST_DEPTH
                with g.If(s.tee_request | lost):
                    s.tee_request = False
                    s.v = primitives.Float3(0, 0, 0)
                    g.SetGlobalPosition(ball, transform.local_point_to_global(
                        course, primitives.Float3(*TEE)))
                    # The ball jumped, so its history in the head's space
                    # starts again here. Otherwise a jump across the face
                    # would count as a hit.
                    s.prev_q = q

                # 1. The desktop swing.
                with g.If(s.swing_request):
                    s.swing_request = False
                    s.swing_angle = s.swing_back
                    s.swinging = True
                    g.SetGlobalPosition(pivot, p + primitives.Float3(0, PIVOT_HEIGHT, 0))
                    g.SetLocalRotation(
                        pivot, dm.axis_angle(primitives.Float3(0, 1, 0), s.swing_yaw))
                    g.SetLocalRotation(arm, swing_rotation)
                    g.SetGlobalPositionRotation(
                        club, transform.global_position(mount), transform.global_rotation(mount),
                    )
                    # The club jumped, so its history starts again here.
                    s.prev_head = head_pos
                    s.prev_q = q
                with g.Else():
                    with g.If(s.swinging):
                        s.swing_angle = s.swing_angle - s.swing_rate * dt
                        g.SetLocalRotation(arm, swing_rotation)
                        g.SetGlobalPositionRotation(
                            club, transform.global_position(mount),
                            transform.global_rotation(mount),
                        )
                        with g.If(s.swing_angle < -s.swing_back):
                            s.swinging = False

                # 2. The club's hit. The face is at Z = face in the head's
                # space, and the ball crossed it if it was in front before
                # and is behind now. It is a hit only if the ball and the
                # face are moving toward each other.
                with g.If((prev_q.z >= face) & (q.z < face)):
                    t = (prev_q.z - face) / (prev_q.z - q.z)
                    crossing = prev_q + (q - prev_q) * t
                    n = transform.local_direction_to_global(head, primitives.Float3(0, 0, 1))
                    club_v = (head_pos - s.prev_head) / dt
                    approach = dm.dot(s.v - club_v, n)
                    on_face = ((abs(crossing.x) <= HEAD_SIZE[0] / 2 + BALL_RADIUS)
                               & (abs(crossing.y) <= HEAD_SIZE[1] / 2 + BALL_RADIUS)
                               & (approach < 0))
                    with g.If(on_face):
                        e = ball_value("Restitution") * head_value("Restitution")
                        ball_mass = ball_value("Mass")
                        head_mass = head_value("Mass")
                        trace.record(where="club_in", v=s.v, club=club_v)
                        s.v = s.v - n * (approach * (1 + e) * head_mass / (head_mass + ball_mass))
                        trace.record(where="club_out", v=s.v)
                        g.SetGlobalPosition(ball, transform.local_point_to_global(
                            head, dm.pack(crossing.x, crossing.y, face + FACE_CLEARANCE)))

                # 3. Gravity.
                s.v = s.v + gravity * dt

                # 4. The ground under the ball.
                with g.RaycastOne(origin=p, direction=down,
                                  max_distance=BALL_RADIUS + PROBE_SKIN,
                                  ignore_hierarchy=scene.ball) as ground:
                    with ground.on_hit():
                        n = ground.hit_normal
                        vn = dm.dot(s.v, n)
                        restitution, friction, rolling = surface_of(ground)
                        with g.If(vn < -BOUNCE_SPEED):
                            bounce("ground", n, restitution, friction)
                        with g.Else():
                            with g.If(vn < BOUNCE_SPEED):
                                # Rolling. The velocity loses its part along
                                # the normal, and 2/7 of the gravity along the
                                # surface that was added in step 3.
                                along_g = (n * n.y - up) * GRAVITY
                                rolled = s.v - n * vn - along_g * ((1 - ROLLING_SHARE) * dt)
                                slowing = rolling * GRAVITY * n.y * dt
                                s.v = rolled * dm.max_(
                                    0, 1 - slowing / dm.max_(dm.magnitude(rolled), 1e-4))
                                # The ray went straight down, so the ball's
                                # center is hit_distance * n.y from the
                                # surface's plane. This puts it one radius
                                # from it.
                                g.SetGlobalPosition(
                                    ball, p + n * (BALL_RADIUS - ground.hit_distance * n.y))

                # 5. What the ball reaches in this update. A ray with no
                # direction ends the flow, so a ball at rest casts none.
                # RaycastOne measures its maximum distance in lengths of
                # its direction, so the direction is normalized.
                step = s.v * dt
                with g.If(dm.magnitude(s.v) > 1e-4):
                    with g.RaycastOne(origin=p, direction=dm.normalized(s.v),
                                      max_distance=dm.magnitude(step) + BALL_RADIUS,
                                      ignore_hierarchy=scene.ball) as hit:
                        with hit.on_hit():
                            n = hit.hit_normal
                            vn = dm.dot(s.v, n)
                            with g.If(vn < 0):
                                restitution, friction, _ = surface_of(hit)
                                g.SetGlobalPosition(ball, hit.hit_point + n * BALL_RADIUS)
                                with g.If(vn < -BOUNCE_SPEED):
                                    bounce("sweep", n, restitution, friction)
                                with g.Else():
                                    s.v = s.v - n * vn
                            with g.Else():
                                g.SetGlobalPosition(ball, p + step)
                        with hit.on_miss():
                            g.SetGlobalPosition(ball, p + step)

            s.prev_q = q
            s.prev_head = head_pos
            s.prev_ball = p
            trace.record(where="end", p=p, v=s.v)
    await g.build(resolink)


def build_desktop_shots(g: Graph, s: Any, scene: Scene, by_club: Any) -> None:
    """Adds the flow and the bindings that let a desktop user address, aim, and hit the ball.

    The flow runs on every machine, and each machine reads its own user's
    mouse and view. Only the golfer's machine writes the shot's model
    variables, apart from the press that addresses the ball. The arrow
    is shown to everyone, and the gauge only to the golfer.

    Args:
        g: The graph.
        s: The graph's Space, with the variables that build_graph declares.
        scene: The slots and components of the course.
        by_club: Returns the value for the selected club, from one value
            per club in CLUBS.
    """
    ball = slots.ref(scene.ball)
    course = slots.ref(scene.course)
    p = transform.global_position(ball)
    local = users.local_user()
    me = users.machine_id(local)
    mine = s.golfer == me
    dash_open = users.is_dash_open(local)
    in_vr = users.is_vr_active(local)
    eye = users.view_position()
    view = users.view_rotation()
    forward = view * primitives.Float3(0, 0, 1)

    # The crosshair is on the ball when the view's ray passes close to the
    # ball's center, in front of the view.
    to_ball = p - eye
    depth = dm.dot(to_ball, forward)
    on_ball = ((depth > 0) & (depth < REACH)
               & (dm.magnitude(to_ball - forward * depth) < CLICK_RADIUS))
    at_rest = ((dm.magnitude(s.v) < REST_SPEED)
               & ~interaction.is_grabbed(scene.ball_grab))

    # The spot is where the view's ray meets the level plane through the
    # ball's center.
    look_down = -forward.y
    reach = (eye.y - p.y) / dm.max_(look_down, MIN_LOOK_DOWN)
    to_spot = eye + forward * reach - p
    to_spot_level = dm.pack(to_spot.x, 0, to_spot.z)
    facing = dm.pack(forward.x, 0, forward.z)

    def let_go() -> None:
        s.golfer = ""
        s.charging = False
        s.fill = 0.0

    with g.Under(scene.graph):
        with g.If(~dash_open):
            with g.If(mine):
                with g.If(mouse.right_pressed() | ~at_rest | in_vr):
                    let_go()
                with g.Else():
                    # One club per turn of the wheel, counted when the
                    # scrolling starts.
                    scroll = mouse.scroll_delta()
                    scrolling = scroll != 0
                    with g.If(scrolling & ~s.was_scrolling):
                        s.club = (s.club + dm.to_int(dm.sign(scroll)) + len(CLUBS)) % len(CLUBS)
                    s.was_scrolling = scrolling

                    with g.If(s.charging):
                        # The fill rises to 1 in FILL_TIME and falls back to
                        # 0 in as long again, over and over.
                        s.charge_time = s.charge_time + time.delta_time()
                        s.fill = 1 - abs(1 - (s.charge_time / FILL_TIME) % 2)
                        with g.If(mouse.left_released()):
                            s.charging = False
                            with g.If((s.fill >= CANCEL_FILL) & (s.charge_time >= TAP_TIME)):
                                level = transform.global_direction_to_local(course, s.aim)
                                speed = by_club([c.speed for c in CLUBS]) * (
                                    MIN_SPEED_SHARE + (1 - MIN_SPEED_SHARE) * s.fill * s.fill)
                                s.swing_yaw = dm.atan2(level.x, level.z) * math.degrees(1)
                                s.swing_back = by_club([c.backswing for c in CLUBS]) * (
                                    MIN_BACKSWING_SHARE + (1 - MIN_BACKSWING_SHARE) * s.fill)
                                s.swing_rate = speed * math.degrees(1 / PIVOT_HEIGHT)
                                s.swing_request = True
                                s.golfer = ""
                            s.fill = 0.0
                    with g.Else():
                        with g.If((look_down > MIN_LOOK_DOWN) & (reach < MAX_AIM_DISTANCE)):
                            # Near the ball the direction to the spot turns
                            # quickly, so the arrow keeps its direction there.
                            with g.If(dm.magnitude(to_spot_level) > MIN_AIM_DISTANCE):
                                s.aim = dm.normalized(to_spot_level)
                        with g.Else():
                            s.aim = dm.normalized(facing)
                        with g.If(mouse.left_pressed()):
                            with g.If(on_ball):
                                let_go()
                            with g.Else():
                                s.charging = True
                                s.charge_time = 0.0
            with g.Else():
                with g.If(~in_vr):
                    with g.If(mouse.left_pressed() & on_ball & at_rest):
                        s.presser = me
                    # The ball is addressed when the button comes up, so
                    # that the press that addresses it doesn't also start a
                    # swing.
                    with g.If(mouse.left_released() & (s.presser == me)):
                        s.presser = ""
                        s.golfer = me
                        s.charging = False
                        s.fill = 0.0
                        s.aim = dm.normalized(facing)
        with g.Else():
            # The left button may come up in the dash, where the flow
            # doesn't see it, so a swing in progress stops.
            with g.If(mine & s.charging):
                s.charging = False
                s.fill = 0.0

    aim = scene.aim
    g.Bind(s.golfer != "", aim.arrow, "IsActive", slot=scene.graph)
    g.Bind(p + primitives.Float3(0, ARROW_LIFT, 0), aim.arrow, "Position", slot=scene.graph)
    g.Bind(s.aim * (ARROW_LENGTH + ARROW_GROWTH * s.fill), aim.arrow_mesh, "Vector",
           slot=scene.graph)
    # A drive computes on each machine, so the gauge shows only on the
    # golfer's, in front of the golfer's own view.
    g.Bind(mine & ~dash_open, aim.gauge, "IsActive", slot=scene.graph)
    g.Bind(eye + view * primitives.Float3(*GAUGE_AT), aim.gauge, "Position", slot=scene.graph)
    g.Bind(view, aim.gauge, "Rotation", slot=scene.graph)
    g.Bind(s.fill * 180, aim.fill, "Arc", slot=scene.graph)
    for i, label in enumerate(aim.club_labels):
        g.Bind(s.club == i, label, "IsActive", slot=scene.graph)
    g.Bind(dm.axis_angle(primitives.Float3(1, 0, 0), -by_club([c.loft for c in CLUBS])),
           scene.head, "Rotation", slot=scene.graph)


async def main(port: int | None) -> None:
    """Builds the course and the graph in front of the user.

    Args:
        port (int | None): The ResoniteLink port, or None to find the
            session from its LAN announcement.
    """
    if port is None:
        session = await discovery.find_session()
        print(f"Found {session.name!r} on port {session.port}.")
        port = session.port
    resolink = client.Client()
    await resolink.connect(port)
    scene = await build_scene(resolink)
    await build_graph(resolink, scene)
    print("The course is ready. Click the ball to aim a shot, or grab the club and swing it.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
