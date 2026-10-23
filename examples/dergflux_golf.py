"""Example of an 18-hole minigolf course for several players, whose balls ProtoFlux graphs move.

Resonite moves nothing by physics except characters, and its colliders
have no friction or bounciness. So the graphs that this script builds
move each ball themselves, once per engine update, and find what the
ball touches with ray casts. Every surface, the ball, and the club head
carry their own physical properties as dynamic variables, so the ball
kicks off bumpers, dies in the sand, and slides far on ice.

The course is built on the floor in front of the user, with hole 1 just
ahead. golf_holes.py, beside this script, describes the 18 holes: their
floors, rails, ramps, and obstacles, their zones, which boost, launch,
warp, or drown a ball that rolls over them, and their moving obstacles,
a windmill, sliding walls, and a turning bar. Each hole has a sign with
its number, name, and par. Next to hole 1 is a "Play" button.

Players
-------

Each player plays with a kit of their own: a ball, a club, the aiming
arrow and gauge of desktop shots, a name tag that floats above the ball,
a HUD, a row of the scoreboard, and the graph that moves the ball.
Everyone plays at the same time, each at their own pace, and the balls
pass through each other.

Pressing Play gives the presser a kit by duplicating an inactive
template kit into the "Players" slot. The duplicate's OnDuplicate event
fires only on the presser's machine, where it stores the presser as the
kit's owner and names the kit after the presser's machine ID, which is
how a second press finds the presser's kit instead of making another.
Pressing Play again starts the round again from hole 1. The host
destroys a kit whose owner has left.

Only the owner's machine runs a kit's flows, so only the owner can
address, aim, and hit the ball. On every other machine, the kit's club
can't be grabbed, and its grip has no collider, through drives that
compute differently on each machine. The ball has no collider at all,
so nothing can touch it, and the rays of one ball never meet another.
Another player's club is shown only while it is held or swinging.

A round
-------

The ball starts on hole 1's tee, and the player is moved to stand behind
it. Each club hit is a stroke. A ball that leaves the hole, or falls
into water, costs a stroke and goes back to where it was last hit from,
and Backspace does the same for a ball that is stuck. A ball drops into
the cup when its center is over the cup, it touches the floor, and it is
slower than CAPTURE_SPEED. A player who reaches MAX_OVER_PAR strokes over
par without holing out picks the ball up and scores that.

ADVANCE_DELAY seconds after the ball drops, it goes to the next hole's
tee and the player is moved there. After hole 18 the HUD shows the
round's score until Play is pressed.

The HUD, which only its owner sees, shows the hole, its par, the strokes
taken on it, and the score against par so far. Holding Tab shows the
scoreboard, with every player's strokes on each hole. Each kit draws its
own row, placed by the kit's index under Players, so the board shows as
many rows as there are kits.

Desktop shots
-------------

A desktop user can't swing the club by hand, so a shot takes three
steps with the mouse.

1. Click your ball while it is at rest. This addresses the ball, and an
   arrow on the ground shows where the shot will go. A gauge in front of
   the view shows the club, which the scroll wheel changes. The putter
   comes first.
2. Look at where the ball should go. The arrow points from the ball to
   the spot under the crosshair on the level plane through the ball, or
   along the view when that spot is farther than MAX_AIM_DISTANCE.
3. Press and hold the left button. The aim stops following the view,
   and the gauge fills and empties again every FILL_TIME seconds.
   Release it to swing the club along the arrow, with a head speed that
   rises with the square of the gauge's fill. A release within TAP_TIME
   of the press, or with the gauge nearly empty, swings nothing, and the
   ball stays addressed.

A right click, or a click on the ball, lets go of the ball, so that the
left button presses things again. The ball moving also lets go of it.
Only the owner sees the arrow and the gauge.

Physical properties
-------------------

The surfaces of each hole are grouped under slots named after them, and
each group has a DynamicVariableSpace named "Physics" with float
variables Restitution, Friction, and Rolling. The ball's slot has the
same three and Mass, and the club head's has Restitution and Mass. The
graph reads them while it runs, so they can be changed in the inspector.
A collider whose slot and ancestors have no Physics space gets
DEFAULT_SURFACE.

When the ball touches a surface, the two restitutions multiply, and the
two friction and rolling coefficients combine as their geometric mean,
as Box2D combines friction. A bumper's restitution is above 1, so it
sends the ball away faster than it came.

Each mover's pivot has a space named "Mover" with its Spin, the axis of
its turn in its own space times its speed in degrees per second, and its
Slide, the direction of its slide times its amplitude, with the Period
and the Phase of the slide in seconds. The ball's graph works out the
mover's velocity at a contact from them and the world's time, as the
bindings that move the movers do.

Each hole's slot has a space named "Hole" with its Tee, Par, and the
corners Min and Max of the box a ball in play stays inside, all in the
hole's space. Each zone's slot has a space named "Zone" with its Kind,
Direction, Speed, and Target, in the zone's space.

What a kit's graph does in each engine update
---------------------------------------------

The graph runs on the owner's machine only. Until the ball drops, in
this order:

1. A ball outside its hole's box, or a press of Backspace, costs a
   stroke and puts the ball back where it was last hit from.
2. If the owner released a desktop shot, the club is posed at the top of
   its backswing, facing along the shot, and in later updates it turns
   about a pivot above the ball until its follow-through.
3. The ball's center is found in the club head's space. If it crossed
   the plane of the face, within the face's bounds, since the last
   update, while the ball and the face moved toward each other, the ball
   is hit, and a stroke is added. Comparing positions in the head's own
   space catches a fast swing that moves the face past the ball within
   one update. The hit changes the ball's velocity along the face normal
   by the impulse between two bodies of the ball's and the head's
   masses. A ball that was put somewhere starts its history in the
   head's space again, so that the jump doesn't count as a crossing.
4. Gravity is added to the velocity.
5. A ray from the ball's center straight down, one radius and PROBE_SKIN
   long, finds the ground the ball rests on. A ball falling onto it
   faster than BOUNCE_SPEED bounces, and one moving more slowly rolls
   along it, slowed by rolling resistance.
6. A ray from the ball's center along its velocity, as long as one
   update's travel plus a radius, finds anything the ball reaches in this
   update. The ball stops against it, touching it, and bounces or slides.
   A wall bounces the ball back at any speed above WALL_BOUNCE_SPEED.
   Otherwise the ball moves on.
7. PUSH_RAYS level rays from the ball's center, one radius long, find a
   moving obstacle that overlaps the ball. The ball is put back out to
   touching it, and bounces off it as off a surface that moves with the
   obstacle's velocity at that point, so a turning bar or blade, or a
   sliding wall, pushes and knocks the ball along.
8. A ray straight down from ZONE_PROBE above the ball's center, which
   also meets trigger colliders, finds a zone under the ball, and the
   zone acts on the ball.
9. A ball that has reached its stroke limit and stopped is picked up.

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
A moving obstacle that overlaps the ball by less than its radius pushes
it, but one fast enough to pass more than a radius into the ball in one
update can pass through it, since the push rays are one radius long. The
fastest, the tip of hole 16's bar, moves 1.3 cm in an update at 60 per
second. The push rays are level, so a blade pushes the ball only along
the floor.
The club's head has no collider, and the ball goes through its back and
sides. The cup has no hole in the floor's collider, so a ball too fast
to drop rolls straight across it, where a real cup's edge would deflect
it. The scoreboard's panel has room for MAX_ROWS players. Each run
deletes the course from the previous run, with every kit.

The aiming spot is where the view meets the level plane through the
ball's center, so on a slope it is off from the true spot under the
crosshair. The other players see a kit's ball move with the network's
delay, since only its owner's machine moves it.

Recording
---------

A kit's graph records the ball's velocity before and after each bounce
and each hit of the club, the zones it meets, where a ball went out or
dropped, and the ball's position and velocity at the end of each update,
with a utils.recorder.Recorder named "trace". It records nothing until
a script starts it by writing the number of lines to record to the
"trace_left" model variable, under the kit's ProtoFlux slot, and then
reads the lines from "trace_log".

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

import golf_holes
from pyresonitelink import client
from pyresonitelink import discovery
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers
from pyresonitelink.dergflux import Graph
from pyresonitelink.dergflux import interaction
from pyresonitelink.dergflux import keyboard
from pyresonitelink.dergflux import math as dm
from pyresonitelink.dergflux import mouse
from pyresonitelink.dergflux import slots
from pyresonitelink.dergflux import strings
from pyresonitelink.dergflux import time
from pyresonitelink.dergflux import transform
from pyresonitelink.dergflux import users
from pyresonitelink.dergflux import variables
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated.assets.procedural_meshes import arrow_mesh
from pyresonitelink.generated.assets.procedural_meshes import box_mesh
from pyresonitelink.generated.assets.procedural_meshes import cylinder_mesh
from pyresonitelink.generated.assets.procedural_meshes import ring_mesh
from pyresonitelink.generated.assets.procedural_meshes import sphere_mesh
from pyresonitelink.generated.data.dynamic import dynamic_value_variable
from pyresonitelink.generated.data.dynamic import dynamic_variable_space
from pyresonitelink.generated.physics.colliders import box_collider
from pyresonitelink.generated.physics.colliders import cylinder_collider
from pyresonitelink.generated.rendering import text_renderer
from pyresonitelink.generated.transform.interaction import grabbable
from pyresonitelink.generated.transform.interaction import touch_button
from pyresonitelink.utils import batches
from pyresonitelink.utils import materials
from pyresonitelink.utils import placement
from pyresonitelink.utils import recorder
from pyresonitelink.utils import slots as slot_utils

Physics = golf_holes.Physics
FLOOR = golf_holes.FLOOR
BALL_RADIUS = golf_holes.BALL_RADIUS
GRAVITY = golf_holes.GRAVITY
HOLES = golf_holes.HOLES

SLOT_NAME = "Dergflux Golf Example"
# Meters from the user's feet to hole 1's origin, at the near end of its
# floor.
DISTANCE = 1.5

# The longest time step the graph takes, so that a stalled frame doesn't
# throw the ball through the course.
MAX_STEP = 1 / 20  # seconds
# How far below the ball's surface the ground ray looks, so that a ball
# rolling over small bumps stays on the ground.
PROBE_SKIN = 0.005  # meters
# The speed along a surface's normal below which the ball stops bouncing
# off the ground and rolls. It is more than GRAVITY * MAX_STEP, so that
# the speed that gravity adds in one update to a resting ball doesn't make
# it bounce.
BOUNCE_SPEED = 0.6  # m/s
# A surface whose normal's Y is below WALL_NORMAL_Y is a wall, and a ball
# that hits it faster than WALL_BOUNCE_SPEED bounces, as a ball does off
# a minigolf rail, rather than sliding along it.
WALL_NORMAL_Y = 0.5
WALL_BOUNCE_SPEED = 0.05  # m/s
# The share of its speed that a solid sphere keeps when it goes from
# sliding to rolling, which is also the share of a sliding sphere's
# acceleration down a slope that a rolling one has.
ROLLING_SHARE = 5 / 7
# How far in front of the club face a hit ball is put, so that the next
# update doesn't find it crossing the face again.
FACE_CLEARANCE = 0.001  # meters
# The zone ray starts this far above the ball's center, above a zone's
# top and below the 11 cm roofs of the tunnels.
ZONE_PROBE = 0.06  # meters
# The number of level rays, evenly spread around the ball, that find a
# moving obstacle that overlaps it.
PUSH_RAYS = 8
# A ball over the cup drops in if it is slower than this.
CAPTURE_SPEED = 1.3  # m/s
# How far below the zone's center a dropped ball's center goes, which
# hides it inside the floor under the cup.
CUP_DEPTH = golf_holes.ZONE_HEIGHT / 2 + BALL_RADIUS + 0.005  # meters
# The strokes over par at which a ball that stops is picked up.
MAX_OVER_PAR = 4
# Seconds from the ball dropping to the next hole.
ADVANCE_DELAY = 2.5
# Where the player is put, behind the tee, in the hole's space.
STAND_BACK = 0.8  # meters

DEFAULT_SURFACE = Physics(restitution=0.5, friction=0.5, rolling=0.2)
BALL = golf_holes.BALL
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
# Where the club rests, from the ball's center on the tee, in the hole's
# space.
CLUB_OFFSET = (0.35, HEAD_DROP + 0.05 - BALL_RADIUS, -0.15)

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
# first is the one the club starts as. A full putt rolls about 11 m on
# felt, and the lofted clubs fly over rails.
CLUBS = [
    Club("Putter", loft=3.0, speed=3.0, backswing=30.0),
    Club("7 Iron", loft=30.0, speed=8.0, backswing=100.0),
    Club("Wedge", loft=50.0, speed=7.0, backswing=90.0),
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

# The crosshair is on the ball when the view's ray passes within
# CLICK_RADIUS of the ball's center, or within CLICK_SLOPE times the
# ball's distance for a far ball, which is about 0.7 degrees, and the
# ball is no farther than REACH. A ball 6 m away was out of a 5 m reach
# after one putt on hole 5.
CLICK_RADIUS = 0.06  # meters
CLICK_SLOPE = 0.012
REACH = 15.0  # meters
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

# Things in front of the view, in the view's space, with the view looking
# along +Z. A TextRenderer's Size is about 6.5 times its letter height.
GAUGE_AT = (0.0, -0.1, 0.45)  # meters
GAUGE_RADIUS = 0.05  # meters, to the outside of the ring
GAUGE_WIDTH = 0.008  # meters
CLUB_LABEL_SIZE = 0.085  # letters about 1.3 cm tall
HINT_SIZE = 0.04  # letters about 0.6 cm tall
HINT = "Look to aim, hold left to swing\nScroll for a club, right-click to let go"
# The HUD's slot, at its center. Its status text is at its top left and
# the banner, which names the result of a hole, above its center.
HUD_AT = (0.0, 0.0, 0.6)  # meters
STATUS_AT = (-0.34, 0.17, 0.0)  # meters, in the HUD's space
STATUS_SIZE = 0.09  # letters about 1.4 cm tall
KEYS_AT = (-0.34, 0.125, 0.0)  # meters, in the HUD's space, under the status
KEYS = "Tab: scores    Backspace: replay from the last spot (+1)"
BANNER_AT = (0.0, 0.07, 0.0)  # meters, in the HUD's space
BANNER_SIZE = 0.16

# The scoreboard, in the view's space. Its columns are along its X, and
# its rows go down along its Y.
BOARD_AT = (0.0, 0.05, 0.75)  # meters
NAME_X = -0.44  # meters, where the names start
HOLE_X = -0.2  # meters, the middle of hole 1's column
CELL_WIDTH = 0.03  # meters between holes' columns
TOTAL_X = HOLE_X + 18 * CELL_WIDTH + 0.03
DIFF_X = TOTAL_X + 0.06
TITLE_Y = 0.075  # meters
HEADER_Y = 0.035
PAR_Y = 0.005
FIRST_ROW_Y = -0.03
ROW_STEP = 0.03  # meters from one player's row to the next
MAX_ROWS = 8
BOARD_TEXT_SIZE = 0.075  # letters about 1.2 cm tall

# Text over the ball, the name of its owner.
NAME_TAG_HEIGHT = 0.12  # meters above the ball's center
NAME_TAG_SIZE = 0.12

PLAY_AT = (-0.95, 0.9, -0.5)  # the Play button, in hole 1's space
BUTTON_SIZE = (0.16, 0.08, 0.02)  # meters
LABEL_SIZE = 0.18  # letters about 3 cm tall
# A positive tilt turns the button's face, toward -Z, up toward the user's
# eyes.
BUTTON_TILT = 30.0  # degrees
INSTRUCTIONS = (
    "Press Play to get a ball, or to start again.\n"
    "Click your ball, look where it should go,\n"
    "and hold the left button to swing.\n"
    "Hold Tab for the scores."
)
SIGN_HEIGHT = 0.9  # meters from the ground to the middle of a hole's sign

FINISHES = {
    "felt": materials.Finish((0.05, 0.32, 0.08), metallic=0.0, smoothness=0.1),
    "rail": materials.Finish((0.75, 0.72, 0.65), metallic=0.0, smoothness=0.4),
    "bumper": materials.Finish((0.8, 0.08, 0.08), metallic=0.1, smoothness=0.6,
                               emissive=(0.25, 0.0, 0.0)),
    "wood": materials.Finish((0.45, 0.25, 0.1), metallic=0.0, smoothness=0.4),
    "stone": materials.Finish((0.4, 0.4, 0.42), metallic=0.0, smoothness=0.2),
    "sand": materials.Finish((0.7, 0.58, 0.35), metallic=0.0, smoothness=0.05),
    "ice": materials.Finish((0.75, 0.9, 1.0), metallic=0.1, smoothness=0.95),
    "water": materials.Finish((0.05, 0.25, 0.6), metallic=0.2, smoothness=0.95),
    "chute": materials.Finish((0.3, 0.32, 0.35), metallic=0.3, smoothness=0.8),
    "Cup": materials.Finish((0.01, 0.01, 0.01), metallic=0.0, smoothness=0.0),
    "Flagstick": materials.Finish((0.9, 0.9, 0.85), metallic=0.0, smoothness=0.5),
    "Flag": materials.Finish((0.8, 0.05, 0.05), metallic=0.0, smoothness=0.3),
    "Boost": materials.Finish((0.95, 0.75, 0.05), metallic=0.0, smoothness=0.5,
                              emissive=(0.5, 0.35, 0.0)),
    "Launch": materials.Finish((0.95, 0.3, 0.05), metallic=0.0, smoothness=0.5,
                               emissive=(0.6, 0.15, 0.0)),
    "Warp": materials.Finish((0.45, 0.1, 0.8), metallic=0.0, smoothness=0.5,
                             emissive=(0.3, 0.05, 0.6)),
    "Sign": materials.Finish((0.12, 0.2, 0.35), metallic=0.0, smoothness=0.3),
    "Panel": materials.Finish((0.02, 0.03, 0.05), metallic=0.0, smoothness=0.0,
                              emissive=(0.02, 0.03, 0.05)),
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

# The finish of the pad that shows each kind of zone, or None for none.
ZONE_FINISHES = {
    golf_holes.CUP: "Cup", golf_holes.BOOST: "Boost", golf_holes.LAUNCH: "Launch",
    golf_holes.WARP: "Cup", golf_holes.WATER: None,
}

WHITE = primitives.ColorX(1, 1, 1, 1, "sRGB")


# ---------------------------------------------------------------------------
# Building the scenery.
# ---------------------------------------------------------------------------


def add_variables(batch: batches.SceneBatch, slot: str, space: str,
                  values: dict[str, Any]) -> None:
    """Adds a DynamicVariableSpace and a dynamic variable for each value.

    Args:
        batch: The batch to add them to.
        slot: The slot's ID.
        space: The space's name.
        values: The variables' values, by name. Each value's Python type
            picks the variable's type: a Float3, an int for Int, or a
            float for Float.
    """
    batch.add_component(slot, dynamic_variable_space.DynamicVariableSpace(
        space_name=space, only_direct_binding=False))
    for name, value in values.items():
        if isinstance(value, primitives.Float3):
            variable: GeneratedComponent = dynamic_value_variable.DynamicValueVariable[primitives.Float3](
                variable_name=f"{space}/{name}", value=value)
        elif isinstance(value, int):
            variable = dynamic_value_variable.DynamicValueVariable[primitives.Int](
                variable_name=f"{space}/{name}", value=primitives.Int(value))
        else:
            variable = dynamic_value_variable.DynamicValueVariable[primitives.Float](
                variable_name=f"{space}/{name}", value=primitives.Float(value))
        batch.add_component(slot, variable)


def add_physics(batch: batches.SceneBatch, slot: str, physics: Physics) -> None:
    """Gives a slot a Physics space with a body's physical properties.

    Mass is added only for bodies that move.
    """
    values: dict[str, Any] = {
        "Restitution": physics.restitution,
        "Friction": physics.friction,
        "Rolling": physics.rolling,
    }
    if physics.mass > 0:
        values["Mass"] = physics.mass
    add_variables(batch, slot, "Physics", values)


def add_box(
    batch: batches.SceneBatch,
    parent: str,
    name: str,
    size: tuple[float, float, float],
    material: str,
    *,
    position: tuple[float, float, float] = (0.0, 0.0, 0.0),
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0),
    collider: str | None = "Static",
    active: bool = True,
) -> str:
    """Adds a slot with a box mesh, and a box collider of the same size.

    Args:
        batch: The batch to add it to.
        parent: The parent slot's ID.
        name: The new slot's name.
        size: The box's size along X, Y, and Z in meters.
        material: The material's ID.
        position: The box's center in the parent's space.
        rotation: Euler angles in degrees.
        collider: The collider's type, such as "Static" or
            "StaticTrigger", or None for no collider.
        active: Whether the slot is active.

    Returns:
        The new slot's ID.
    """
    slot = batch.add_slot(parent, name, position=position, rotation=batches.euler(*rotation),
                          active=active)
    mesh = batch.add_component(slot, box_mesh.BoxMesh(size=primitives.Float3(*size)))
    batch.add_renderer(slot, mesh, [material])
    if collider is not None:
        batch.add_component(slot, box_collider.BoxCollider(
            size=primitives.Float3(*size), type_=collider))
    return slot


def add_cylinder(
    batch: batches.SceneBatch,
    parent: str,
    name: str,
    radius: float,
    height: float,
    material: str,
    position: tuple[float, float, float],
    collider: str | None = None,
) -> str:
    """Adds a slot with an upright cylinder mesh, and a collider of the same size if asked.

    Returns:
        The new slot's ID.
    """
    slot = batch.add_slot(parent, name, position=position)
    mesh = batch.add_component(slot, cylinder_mesh.CylinderMesh(
        radius=primitives.Float(radius), height=primitives.Float(height)))
    batch.add_renderer(slot, mesh, [material])
    if collider is not None:
        batch.add_component(slot, cylinder_collider.CylinderCollider(
            radius=primitives.Float(radius), height=primitives.Float(height), type_=collider))
    return slot


def add_text(
    batch: batches.SceneBatch,
    parent: str,
    name: str,
    text: str,
    size: float,
    position: tuple[float, float, float],
    align: str = "Center",
) -> tuple[str, text_renderer.TextRenderer]:
    """Adds a slot with white text, which reads from the slot's -Z side.

    Args:
        batch: The batch to add it to.
        parent: The parent slot's ID.
        name: The new slot's name.
        text: The text.
        size: The TextRenderer's Size, about 6.5 times the letter height.
        position: Where the text is anchored, in the parent's space.
        align: "Left", "Center", or "Right", for where the anchor is.

    Returns:
        The new slot's ID and its TextRenderer.
    """
    slot = batch.add_slot(parent, name, position=position)
    renderer = text_renderer.TextRenderer(
        text=text, size=primitives.Float(size), color=WHITE, horizontal_align=align)
    batch.add_component(slot, renderer)
    return slot, renderer


def add_piece(batch: batches.SceneBatch, parent: str, piece: golf_holes.Box | golf_holes.Cylinder,
              mats: dict[str, str], name: str) -> str:
    """Adds a box or a cylinder of a hole under its surface's group, and returns its slot's ID."""
    material = mats[piece.finish or piece.surface]
    collider = "Static" if piece.collider else None
    if isinstance(piece, golf_holes.Box):
        return add_box(batch, parent, name, piece.size, material, position=piece.center,
                       rotation=piece.rotation, collider=collider)
    return add_cylinder(batch, parent, name, piece.radius, piece.height, material, piece.center,
                        collider)


def add_zone(batch: batches.SceneBatch, parent: str, zone: golf_holes.Zone,
             mats: dict[str, str]) -> None:
    """Adds a zone: a trigger collider, its Zone space, and the pad that shows it.

    The zone's slot is at the middle of the trigger, ZONE_HEIGHT / 2 above
    the floor.
    """
    h = golf_holes.ZONE_HEIGHT
    x, y, z = zone.center
    slot = batch.add_slot(parent, f"Zone {zone.kind}", position=(x, y + h / 2, z))
    sx, sz = zone.size
    if zone.round:
        batch.add_component(slot, cylinder_collider.CylinderCollider(
            radius=primitives.Float(sx / 2), height=primitives.Float(h), type_="StaticTrigger"))
    else:
        batch.add_component(slot, box_collider.BoxCollider(
            size=primitives.Float3(sx, h, sz), type_="StaticTrigger"))
    target = tuple(t - c for t, c in zip(zone.target, (x, y + h / 2, z)))
    add_variables(batch, slot, "Zone", {
        "Kind": zone.kind,
        "Direction": primitives.Float3(*zone.direction),
        "Speed": zone.speed,
        "Target": primitives.Float3(*target),
    })
    finish = ZONE_FINISHES[zone.kind]
    if finish is None:
        return
    # The pad lies a hair above the floor, so that it isn't hidden by it.
    pad_y = -h / 2 + 0.002
    if zone.round:
        add_cylinder(batch, slot, "Pad", sx / 2, 0.004, mats[finish], (0.0, pad_y, 0.0))
    else:
        add_box(batch, slot, "Pad", (sx, 0.004, sz), mats[finish], position=(0.0, pad_y, 0.0),
                collider=None)
    if zone.kind == golf_holes.WARP:
        # A purple ring marks where the ball comes out.
        exit_at = (zone.target[0] - x, zone.target[1] - BALL_RADIUS + 0.002 - (y + h / 2),
                   zone.target[2] - z)
        add_cylinder(batch, slot, "Exit", 0.08, 0.004, mats["Warp"], exit_at)
        add_cylinder(batch, slot, "Ring", sx / 2 + 0.02, 0.003, mats["Warp"], (0.0, pad_y - 0.001, 0.0))


def add_hole(batch: batches.SceneBatch, holes: str, hole: golf_holes.Hole,
             mats: dict[str, str]) -> list[tuple[str, golf_holes.Mover]]:
    """Adds a hole, with its Hole space, its pieces grouped by surface, its zones, flag, and sign.

    Returns:
        The slot ID of each mover's pivot, with the mover.
    """
    slot = batch.add_slot(holes, f"Hole {hole.number}", position=golf_holes.hole_origin(hole.number))
    low, high = hole.bounds()
    add_variables(batch, slot, "Hole", {
        "Tee": primitives.Float3(*hole.tee), "Par": hole.par,
        "Min": primitives.Float3(*low), "Max": primitives.Float3(*high),
    })
    groups: dict[str, str] = {}

    def group(surface: str) -> str:
        if surface not in groups:
            groups[surface] = batch.add_slot(slot, surface.title())
            add_physics(batch, groups[surface], golf_holes.SURFACES[surface])
        return groups[surface]

    for i, piece in enumerate(hole.pieces):
        add_piece(batch, group(piece.surface), piece, mats, f"Piece {i}")
    pivots = []
    for i, mover in enumerate(hole.movers):
        pivot = batch.add_slot(group(mover.surface), f"Mover {i}", position=mover.pivot)
        add_variables(batch, pivot, "Mover", {
            "Spin": primitives.Float3(*(a * mover.speed for a in mover.axis)),
            "Slide": primitives.Float3(*(a * (0.0 if mover.speed else mover.amplitude)
                                         for a in mover.axis)),
            "Period": float(mover.period), "Phase": float(mover.phase),
        })
        for j, part in enumerate(mover.parts):
            add_piece(batch, pivot, part, mats, f"Part {j}")
        pivots.append((pivot, mover))
    zones = batch.add_slot(slot, "Zones")
    for zone in hole.zones:
        add_zone(batch, zones, zone, mats)

    # The flagstick stands at the edge of the cup, so that it doesn't hide
    # a dropped ball's name tag.
    cx, cy, cz = hole.cup.center
    stick_x = cx + golf_holes.CUP_RADIUS + 0.01
    add_cylinder(batch, slot, "Flagstick", 0.006, 1.0, mats["Flagstick"], (stick_x, cy + 0.5, cz))
    add_box(batch, slot, "Flag", (0.22, 0.14, 0.005), mats["Flag"],
            position=(stick_x + 0.11, cy + 0.93, cz), collider=None)

    sign_x = low[0] - 0.3
    sign = batch.add_slot(slot, "Sign", position=(sign_x, 0.0, 0.3))
    add_box(batch, sign, "Post", (0.04, SIGN_HEIGHT, 0.04), mats["Sign"],
            position=(0.0, SIGN_HEIGHT / 2, 0.0), collider=None)
    add_box(batch, sign, "Board", (0.42, 0.24, 0.02), mats["Sign"],
            position=(0.0, SIGN_HEIGHT, 0.0), collider=None)
    add_text(batch, sign, "Label", f"{hole.number}. {hole.name}\nPar {hole.par}", 0.14,
             (0.0, SIGN_HEIGHT, -0.012))
    return pivots


@dataclasses.dataclass
class AimVisuals:
    """Represents the things of a kit that the graph shows and moves in world space.

    They are under a slot whose world transform is the identity, so that
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
        name_tag: The name tag's slot, at the text's center.
        name_text: The name tag's TextRenderer.
        hud: The HUD's slot.
        status: The HUD's text of the hole, par, strokes, and score.
        banner: The slot of the HUD's text that names a hole's result.
        banner_text: Its TextRenderer.
        row: The slot of the kit's row of the scoreboard.
        row_name: The row's TextRenderer of the player's name.
        row_holes: The row's TextRenderers of the strokes on each hole.
        row_total: The row's TextRenderer of the total strokes.
        row_diff: The row's TextRenderer of the score against par.
    """

    arrow: workers.Slot
    arrow_mesh: arrow_mesh.ArrowMesh
    gauge: workers.Slot
    fill: ring_mesh.RingMesh
    club_labels: list[workers.Slot]
    name_tag: workers.Slot
    name_text: text_renderer.TextRenderer
    hud: workers.Slot
    status: text_renderer.TextRenderer
    banner: workers.Slot
    banner_text: text_renderer.TextRenderer
    row: workers.Slot
    row_name: text_renderer.TextRenderer
    row_holes: list[text_renderer.TextRenderer]
    row_total: text_renderer.TextRenderer
    row_diff: text_renderer.TextRenderer


@dataclasses.dataclass
class Kit:
    """Represents the slots and components of one player's kit.

    The script builds the template kit, and the graph duplicates it for
    each player, so these are the template's.

    Attributes:
        root: The kit's slot, at the course's origin, named after its
            owner's machine ID once it is duplicated.
        graph: The slot for the kit's ProtoFlux nodes.
        ball: The ball's slot.
        club: The club's slot, at the grip's center.
        club_grab: The club's Grabbable.
        grip_collider: The grip's BoxCollider, the club's only collider.
        head: The club head's slot, at the head's center, with the face
            toward +Z.
        pivot: The pivot of desktop swings, which turns about Y to face
            along the shot.
        arm: The pivot's child, which turns about X to swing the club.
        mount: Where the club goes during a desktop swing.
        aim: The things that the graph shows and moves in world space.
    """

    root: workers.Slot
    graph: workers.Slot
    ball: workers.Slot
    club: workers.Slot
    club_grab: grabbable.Grabbable
    grip_collider: box_collider.BoxCollider
    head: workers.Slot
    pivot: workers.Slot
    arm: workers.Slot
    mount: workers.Slot
    aim: AimVisuals


@dataclasses.dataclass
class Course:
    """Represents the slots and components that every player shares.

    Attributes:
        root: The example's root slot, whose space is the course's.
        holes: The slot whose children are the holes, "Hole 1" to
            "Hole 18".
        graph: The slot for the ProtoFlux nodes that every player shares.
        players: The slot that the players' kits go under.
        play_button: The Play button's TouchButton.
        board: The slot of the scoreboard's panel and headings.
        movers: The slot of each mover's pivot, with the mover.
        kit: The template kit, which is inactive.
    """

    root: workers.Slot
    holes: workers.Slot
    graph: workers.Slot
    players: workers.Slot
    play_button: touch_button.TouchButton
    board: workers.Slot
    movers: list[tuple[workers.Slot, golf_holes.Mover]]
    kit: Kit


def add_board(batch: batches.SceneBatch, frame: str, mats: dict[str, str]) -> str:
    """Adds the scoreboard's panel and headings, hidden until the graph shows them.

    Returns:
        The board's slot ID.
    """
    board = batch.add_slot(frame, "Scoreboard", active=False)
    top = TITLE_Y + 0.03
    bottom = FIRST_ROW_Y - (MAX_ROWS - 1) * ROW_STEP - 0.02
    left, right = NAME_X - 0.03, DIFF_X + 0.04
    add_box(batch, board, "Panel", (right - left, top - bottom, 0.004), mats["Panel"],
            position=((left + right) / 2, (top + bottom) / 2, 0.006), collider=None)
    add_text(batch, board, "Title", "Scores", BOARD_TEXT_SIZE * 1.5, (0.0, TITLE_Y, 0.0))
    add_text(batch, board, "Hole", "Hole", BOARD_TEXT_SIZE, (NAME_X, HEADER_Y, 0.0), "Left")
    add_text(batch, board, "Par", "Par", BOARD_TEXT_SIZE, (NAME_X, PAR_Y, 0.0), "Left")
    for hole in HOLES:
        x = HOLE_X + (hole.number - 1) * CELL_WIDTH
        add_text(batch, board, f"Hole {hole.number}", str(hole.number), BOARD_TEXT_SIZE,
                 (x, HEADER_Y, 0.0))
        add_text(batch, board, f"Par {hole.number}", str(hole.par), BOARD_TEXT_SIZE, (x, PAR_Y, 0.0))
    add_text(batch, board, "Total", "Total", BOARD_TEXT_SIZE, (TOTAL_X, HEADER_Y, 0.0))
    add_text(batch, board, "Par Total", str(golf_holes.PAR), BOARD_TEXT_SIZE, (TOTAL_X, PAR_Y, 0.0))
    add_text(batch, board, "Diff", "+/-", BOARD_TEXT_SIZE, (DIFF_X, HEADER_Y, 0.0))
    return board


async def build_course(resolink: client.Client) -> Course:
    """Builds the 18 holes, the Play button, the scoreboard, and the template kit in front of the user.

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
    assert course.id is not None
    mats = {k: m.id for k, m in (await materials.add_materials(resolink, course, FINISHES)).items()}
    assert all(mats.values())
    mat_ids: dict[str, str] = {k: v for k, v in mats.items() if v is not None}

    batch = batches.SceneBatch(resolink)
    holes = batch.add_slot(course.id, "Holes")
    movers: list[tuple[workers.Slot, golf_holes.Mover]] = []
    for hole in HOLES:
        movers += [(workers.Slot(id=p), m) for p, m in add_hole(batch, holes, hole, mat_ids)]
    graph = batch.add_slot(course.id, "ProtoFlux")
    players = batch.add_slot(course.id, "Players")

    play_slot = add_box(batch, course.id, "Play Button", BUTTON_SIZE, mat_ids["Button"],
                        position=PLAY_AT, rotation=(BUTTON_TILT, 0.0, 0.0))
    play_button = touch_button.TouchButton()
    batch.add_component(play_slot, play_button)
    add_text(batch, play_slot, "Label", "Play", LABEL_SIZE, (0.0, 0.0, -BUTTON_SIZE[2] / 2 - 0.001))
    add_text(batch, course.id, "Instructions", INSTRUCTIONS, 0.09,
             (PLAY_AT[0], PLAY_AT[1] + 0.3, PLAY_AT[2]))

    # A slot whose world transform is the identity, for things whose
    # world transform a binding drives.
    identity = transforms.relative_to(world, transforms.Transform())
    frame = batch.add_slot(course.id, "World Frame", position=_tuple(identity.position),
                           rotation=identity.rotation, scale=_tuple(identity.scale))
    board = add_board(batch, frame, mat_ids)
    kit = add_kit(batch, course.id, identity, mat_ids)
    await batch.flush()
    print(f"Built {len(HOLES)} holes, the Play button, the scoreboard, and the template kit.")
    for component in _components_to_refresh(kit, play_button):
        await component.refresh(resolink)
    return Course(
        course, workers.Slot(id=holes), workers.Slot(id=graph), workers.Slot(id=players),
        play_button, workers.Slot(id=board), movers, kit,
    )


def _tuple(v: primitives.Float3) -> tuple[float, float, float]:
    """Returns a Float3 as a tuple of floats."""
    return (float(v.x), float(v.y), float(v.z))


def _components_to_refresh(kit: Kit, play_button: touch_button.TouchButton) -> list[GeneratedComponent]:
    """Returns the components that bindings drive, which need their members' IDs from the server."""
    aim = kit.aim
    return [
        play_button, kit.club_grab, kit.grip_collider, aim.arrow_mesh, aim.fill, aim.name_text,
        aim.status, aim.banner_text, aim.row_name, *aim.row_holes, aim.row_total, aim.row_diff,
    ]


def add_kit(batch: batches.SceneBatch, course: str, identity: transforms.Transform,
            mats: dict[str, str]) -> Kit:
    """Adds the inactive template kit at the course's origin.

    Args:
        batch: The batch to add it to.
        course: The course's slot ID.
        identity: The local transform, under the course, that has the
            identity world transform. The kit is at the course's origin,
            so a slot under it with this transform has it too.
        mats: The materials' IDs, by key in FINISHES.
    """
    root = batch.add_slot(course, "Kit Template", active=False)
    first_tee = golf_holes.hole_origin(1)
    tee = tuple(o + t for o, t in zip(first_tee, HOLES[0].tee))
    ball = batch.add_slot(root, "Ball", position=tee)
    mesh = batch.add_component(ball, sphere_mesh.SphereMesh(radius=primitives.Float(BALL_RADIUS)))
    batch.add_renderer(ball, mesh, [mats["Ball"]])
    add_physics(batch, ball, BALL)

    club = batch.add_slot(root, "Club", position=tuple(t + o for t, o in zip(tee, CLUB_OFFSET)))
    club_grab = grabbable.Grabbable()
    batch.add_component(club, club_grab)
    # The grip is the club's only collider, so a hand grabs the club there
    # and the ball's rays meet nothing else of it.
    grip_size = (2 * GRIP_RADIUS, GRIP_LENGTH, 2 * GRIP_RADIUS)
    grip = add_box(batch, club, "Grip", grip_size, mats["Grip"], collider=None)
    grip_collider = box_collider.BoxCollider(size=primitives.Float3(*grip_size))
    batch.add_component(grip, grip_collider)
    shaft_top = -GRIP_LENGTH / 2
    shaft_bottom = -HEAD_DROP + HEAD_SIZE[1] / 2
    add_cylinder(batch, club, "Shaft", SHAFT_RADIUS, shaft_top - shaft_bottom, mats["Steel"],
                 (0.0, (shaft_top + shaft_bottom) / 2, 0.0))
    # The loft turns the face's normal, +Z, up toward +Y, which is a
    # negative angle about X. The graph drives the head's rotation from
    # the selected club.
    head = add_box(batch, club, "Head", HEAD_SIZE, mats["Steel"], position=(0.0, -HEAD_DROP, 0.0),
                   rotation=(-CLUBS[0].loft, 0.0, 0.0), collider=None)
    add_physics(batch, head, CLUB_HEAD)

    pivot = batch.add_slot(root, "Swing Pivot")
    arm = batch.add_slot(pivot, "Swing Arm")
    mount = batch.add_slot(arm, "Club Mount", position=(0.0, -(PIVOT_HEIGHT - HEAD_DROP), 0.0))
    graph = batch.add_slot(root, "ProtoFlux")
    aim = add_aim_visuals(batch, root, identity, mats)
    return Kit(
        workers.Slot(id=root), workers.Slot(id=graph), workers.Slot(id=ball), workers.Slot(id=club),
        club_grab, grip_collider, workers.Slot(id=head), workers.Slot(id=pivot),
        workers.Slot(id=arm), workers.Slot(id=mount), aim,
    )


def add_ring(batch: batches.SceneBatch, parent: str, name: str, arc: float, material: str,
             z: float = 0.0) -> ring_mesh.RingMesh:
    """Adds a slot with one of the gauge's rings, in the slot's XY plane.

    Args:
        batch: The batch to add it to.
        parent: The gauge's slot ID.
        name: The new slot's name.
        arc: How much of the ring to draw, in degrees, from the left end
            over the top.
        material: The ring's material's ID.
        z: The slot's position along the gauge's Z, so that one ring can
            sit in front of another.

    Returns:
        The ring's mesh.
    """
    slot = batch.add_slot(parent, name, position=(0.0, 0.0, z))
    mesh = ring_mesh.RingMesh(
        arc=primitives.Float(arc), segments=primitives.Int(48),
        inner_radius=primitives.Float(GAUGE_RADIUS - GAUGE_WIDTH),
        outer_radius=primitives.Float(GAUGE_RADIUS),
    )
    mesh_id = batch.add_component(slot, mesh)
    batch.add_renderer(slot, mesh_id, [material])
    return mesh


def add_aim_visuals(batch: batches.SceneBatch, kit: str, identity: transforms.Transform,
                    mats: dict[str, str]) -> AimVisuals:
    """Adds a kit's arrow, gauge, name tag, HUD, and scoreboard row, which the graph shows and moves."""
    world = batch.add_slot(kit, "World Frame", position=_tuple(identity.position),
                           rotation=identity.rotation, scale=_tuple(identity.scale))
    arrow = batch.add_slot(world, "Aim Arrow", active=False)
    arrow_shape = arrow_mesh.ArrowMesh(
        vector=primitives.Float3(0, 0, ARROW_LENGTH),
        body_radius=primitives.Float(0.004), head_radius=primitives.Float(0.012),
        head_length=primitives.Float(0.035),
    )
    arrow_id = batch.add_component(arrow, arrow_shape)
    batch.add_renderer(arrow, arrow_id, [mats["Aim"]])

    gauge = batch.add_slot(world, "Gauge", active=False)
    add_ring(batch, gauge, "Gauge Back", 180.0, mats["Gauge"])
    fill = add_ring(batch, gauge, "Gauge Fill", 0.0, mats["Power"], z=-0.001)
    labels = [
        add_text(batch, gauge, f"{club.name} Label", club.name, CLUB_LABEL_SIZE, (0.0, 0.015, 0.0))[0]
        for club in CLUBS
    ]
    add_text(batch, gauge, "Hint", HINT, HINT_SIZE, (0.0, -0.02, 0.0))

    name_tag, name_text = add_text(batch, world, "Name Tag", "", NAME_TAG_SIZE, (0.0, 0.0, 0.0))

    hud = batch.add_slot(world, "HUD", active=False)
    _, status = add_text(batch, hud, "Status", "", STATUS_SIZE, STATUS_AT, "Left")
    add_text(batch, hud, "Keys", KEYS, HINT_SIZE, KEYS_AT, "Left")
    banner, banner_text = add_text(batch, hud, "Banner", "", BANNER_SIZE, BANNER_AT)

    row = batch.add_slot(world, "Score Row", active=False)
    _, row_name = add_text(batch, row, "Name", "", BOARD_TEXT_SIZE, (NAME_X, 0.0, 0.0), "Left")
    row_holes = [
        add_text(batch, row, f"Hole {h.number}", "", BOARD_TEXT_SIZE,
                 (HOLE_X + (h.number - 1) * CELL_WIDTH, 0.0, 0.0))[1]
        for h in HOLES
    ]
    _, row_total = add_text(batch, row, "Total", "", BOARD_TEXT_SIZE, (TOTAL_X, 0.0, 0.0))
    _, row_diff = add_text(batch, row, "Diff", "", BOARD_TEXT_SIZE, (DIFF_X, 0.0, 0.0))
    return AimVisuals(
        workers.Slot(id=arrow), arrow_shape, workers.Slot(id=gauge), fill,
        [workers.Slot(id=label) for label in labels], workers.Slot(id=name_tag), name_text,
        workers.Slot(id=hud), status, workers.Slot(id=banner), banner_text,
        workers.Slot(id=row), row_name, row_holes, row_total, row_diff,
    )


# ---------------------------------------------------------------------------
# The kit's graph.
# ---------------------------------------------------------------------------


@dataclasses.dataclass
class KitRefs:
    """Represents the expressions that the parts of a kit's graph share.

    Attributes:
        s: The kit's Space.
        trace: The recorder of the kit's ball.
        mine: A Bool, true on the owner's machine.
        hole: The slot of the owner's current hole.
        tee: The ball's center on the current hole's tee, in the hole's
            space.
        par: The current hole's par, an Int.
        by_club: Returns the value for the selected club, from one value
            per club in CLUBS.
    """

    s: Any
    trace: recorder.Recorder
    mine: Any
    hole: Any
    tee: Any
    par: Any
    by_club: Any


def to_par(diff: Any) -> Any:
    """Returns a score against par as a String, such as "+3", "E", or "-1"."""
    return dm.conditional(diff > 0, "+" + strings.to_string(diff),
                          dm.conditional(diff == 0, "E", strings.to_string(diff)))


def build_kit_graph(kit: Kit, course: Course) -> Graph:
    """Returns the Dergflux graph of the template kit, which each duplicate gets a copy of.

    The graph references slots inside the kit and the course outside it.
    A duplicate's references to slots inside it point to its own copies,
    and its references to the course stay as they are.
    """
    g = Graph()
    s = g.Space(kit.graph, space_name="Golf")
    # The user who pressed Play for this kit, which is null in the
    # template and once the user has left.
    s.owner = s.UserModelVar("owner")
    s.claimed = s.BoolModelVar("claimed")  # whether the kit has had an owner
    s.hole = s.IntModelVar("hole", 0)  # the index of the current hole in HOLES
    s.strokes = s.IntModelVar("strokes", 0)  # on the current hole
    s.holed = s.BoolModelVar("holed")  # whether the current hole is done
    s.holed_at = s.DoubleModelVar("holed_at")  # the world time it was done
    s.picked_up = s.BoolModelVar("picked_up")  # whether it ended at the stroke limit
    s.finish_request = s.BoolModelVar("finish_request")
    s.finished = s.BoolModelVar("finished")  # whether the round is over
    s.result = s.StringModelVar("result", "")  # the name of the last hole's result
    s.total = s.IntModelVar("total", 0)  # strokes on the holes done
    s.par_total = s.IntModelVar("par_total", 0)  # par of the holes done
    for hole in HOLES:
        setattr(s, f"score{hole.number}", s.IntModelVar(f"score{hole.number}", 0))
    # Where the ball was last hit from, in world space.
    s.last_spot = s.Float3ModelVar("last_spot")
    s.v = s.Float3ModelVar("velocity")  # the ball's, in world space, in m/s
    # The ball's center in the head's space and the head's center in
    # world space, as they were at the end of the last update.
    s.prev_q = s.Float3ModelVar("prev_in_head")
    s.prev_head = s.Float3ModelVar("prev_head")
    s.tee_request = s.BoolModelVar("tee_request")  # put the ball on the current tee
    s.teleport_request = s.BoolModelVar("teleport_request")  # move the owner behind it
    s.swing_request = s.BoolModelVar("swing_request")
    s.swinging = s.BoolModelVar("swinging")
    s.swing_angle = s.FloatModelVar("swing_angle")  # degrees about the arm's X
    s.swing_back = s.FloatModelVar("swing_back")  # degrees
    s.swing_rate = s.FloatModelVar("swing_rate")  # degrees per second
    s.swing_yaw = s.FloatModelVar("swing_yaw")  # degrees about the course's Y
    s.addressed = s.BoolModelVar("addressed")
    # Whether the left button went down with the crosshair on the ball,
    # until it comes up and addresses the ball.
    s.pressed_on_ball = s.BoolModelVar("pressed_on_ball")
    s.club = s.IntModelVar("club", 0)  # the index of the club in CLUBS
    s.aim = s.Float3ModelVar("aim")  # the shot's direction, level, in world space
    s.charging = s.BoolModelVar("charging")  # whether the left button is held for a shot
    s.charge_time = s.FloatModelVar("charge_time")  # seconds since it went down
    s.fill = s.FloatModelVar("fill")  # the gauge's fill, from 0 to 1
    s.was_scrolling = s.BoolModelVar("was_scrolling")
    # Records the ball's velocity around each bounce, and its position and
    # velocity at the end of each update, while a script asks for it.
    trace = recorder.Recorder(g, s, "trace")

    local = users.local_user()
    hole = slots.find_child(course.holes, "Hole " + strings.to_string(s.hole + 1))
    refs = KitRefs(
        s=s, trace=trace, mine=s.owner == local, hole=hole,
        tee=variables.read(hole, "Hole/Tee", primitives.Float3).value,
        par=variables.read(hole, "Hole/Par", primitives.Int).value,
        by_club=None,
    )

    def by_club(values: list[float]) -> Any:
        """Returns the value for the selected club, from one value per club in CLUBS."""
        chosen: Any = values[-1]
        for i in reversed(range(len(values) - 1)):
            chosen = dm.conditional(s.club == i, values[i], chosen)
        return chosen

    refs.by_club = by_club
    root = slots.ref(kit.root)

    with g.Under(kit.graph):
        # Only the machine that duplicated the kit gets this event.
        with g.OnDuplicate() as e:
            with e.trigger():
                s.owner = local
                s.claimed = True
                g.SetSlotName(root, users.machine_id(local))
                s.tee_request = True
                s.teleport_request = True

    with g.Under(kit.graph):
        with g.If(users.local_user_is_host() & s.claimed & dm.is_null(s.owner)):
            g.DestroySlot(root)

    with g.Under(kit.graph):
        with g.ButtonEvents(button=course.play_button) as e:
            with e.pressed():
                with g.If(refs.mine):
                    s.hole = 0
                    s.strokes = 0
                    s.total = 0
                    s.par_total = 0
                    for h in HOLES:
                        setattr(s, f"score{h.number}", 0)
                    s.holed = False
                    s.finished = False
                    s.picked_up = False
                    s.finish_request = False
                    s.result = ""
                    s.addressed = False
                    s.charging = False
                    s.fill = 0.0
                    s.tee_request = True
                    s.teleport_request = True

    add_ball_flow(g, kit, course, refs)
    add_desktop_shots(g, kit, course, refs)
    add_bindings(g, kit, refs)
    return g


def add_ball_flow(g: Graph, kit: Kit, course: Course, refs: KitRefs) -> None:
    """Adds the flow that moves the owner's ball, swings the club, and keeps the score."""
    s, trace = refs.s, refs.trace
    ball = slots.ref(kit.ball)
    club = slots.ref(kit.club)
    head = slots.ref(kit.head)
    pivot = slots.ref(kit.pivot)
    arm = slots.ref(kit.arm)
    mount = slots.ref(kit.mount)
    hole = refs.hole

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
    zero = primitives.Float3(0, 0, 0)
    gravity = primitives.Float3(0, -GRAVITY, 0)
    face = HEAD_SIZE[2] / 2 + BALL_RADIUS  # the ball center's Z on the face
    swing_rotation = dm.axis_angle(primitives.Float3(1, 0, 0), s.swing_angle)
    tee_world = transform.local_point_to_global(hole, refs.tee)
    in_hole = transform.global_point_to_local(hole, p)
    low = variables.read(hole, "Hole/Min", primitives.Float3).value
    high = variables.read(hole, "Hole/Max", primitives.Float3).value
    out_of_bounds = ((in_hole.x < low.x) | (in_hole.x > high.x) | (in_hole.y < low.y)
                     | (in_hole.z < low.z) | (in_hole.z > high.z))
    local = users.local_user()
    replay = keyboard.pressed("Backspace") & ~users.is_dash_open(local) & ~s.addressed

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

    def penalty(where: str) -> None:
        """Adds a stroke and puts the ball back where it was last hit from."""
        trace.record(where=where, p=p)
        s.strokes = s.strokes + 1
        s.v = zero
        g.SetGlobalPosition(ball, s.last_spot)
        s.prev_q = q

    with g.Under(kit.graph):
        with g.If(refs.mine):
            with g.If(s.tee_request):
                s.tee_request = False
                s.v = zero
                s.last_spot = tee_world
                g.SetGlobalPosition(ball, tee_world)
                g.SetGlobalPositionRotation(
                    club, transform.local_point_to_global(hole, refs.tee + primitives.Float3(*CLUB_OFFSET)),
                    transform.global_rotation(hole),
                )
                # The ball and the club jumped, so their history starts
                # again here. Otherwise a jump across the face would count
                # as a hit.
                s.prev_q = q
                s.prev_head = head_pos
            with g.If(s.teleport_request):
                s.teleport_request = False
                g.SetFeetPosition(users.local_user_root(), transform.local_point_to_global(
                    hole, dm.pack(refs.tee.x, 0, refs.tee.z - STAND_BACK)))

            with g.If(~s.holed):
                # 1. Out of bounds, and a replay from the last spot.
                with g.If(out_of_bounds | replay):
                    penalty("out")

                # 2. The desktop swing.
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

                # 3. The club's hit. The face is at Z = face in the head's
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
                        s.strokes = s.strokes + 1
                        s.last_spot = p
                        s.v = s.v - n * (approach * (1 + e) * head_mass / (head_mass + ball_mass))
                        trace.record(where="club_out", v=s.v)
                        g.SetGlobalPosition(ball, transform.local_point_to_global(
                            head, dm.pack(crossing.x, crossing.y, face + FACE_CLEARANCE)))

                # 4. Gravity.
                s.v = s.v + gravity * dt

                # 5. The ground under the ball.
                with g.RaycastOne(origin=p, direction=down,
                                  max_distance=BALL_RADIUS + PROBE_SKIN,
                                  ignore_hierarchy=kit.ball) as ground:
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
                                # surface that was added in step 4.
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

                # 6. What the ball reaches in this update. A ray with no
                # direction ends the flow, so a ball at rest casts none.
                # RaycastOne measures its maximum distance in lengths of
                # its direction, so the direction is normalized.
                step = s.v * dt
                with g.If(dm.magnitude(s.v) > 1e-4):
                    with g.RaycastOne(origin=p, direction=dm.normalized(s.v),
                                      max_distance=dm.magnitude(step) + BALL_RADIUS,
                                      ignore_hierarchy=kit.ball) as hit:
                        with hit.on_hit():
                            n = hit.hit_normal
                            vn = dm.dot(s.v, n)
                            with g.If(vn < 0):
                                restitution, friction, _ = surface_of(hit)
                                g.SetGlobalPosition(ball, hit.hit_point + n * BALL_RADIUS)
                                wall = (n.y < WALL_NORMAL_Y) & (vn < -WALL_BOUNCE_SPEED)
                                with g.If((vn < -BOUNCE_SPEED) | wall):
                                    bounce("sweep", n, restitution, friction)
                                with g.Else():
                                    s.v = s.v - n * vn
                            with g.Else():
                                g.SetGlobalPosition(ball, p + step)
                        with hit.on_miss():
                            g.SetGlobalPosition(ball, p + step)

                # 7. Moving obstacles that overlap the ball.
                add_pushes(g, kit, refs, p, surface_of)

                # 8. The zone under the ball, if any.
                add_zones(g, kit, refs, p, q, penalty)

                # 9. The stroke limit.
                limit = refs.par + MAX_OVER_PAR
                with g.If(~s.finish_request & (s.strokes >= limit)
                          & (dm.magnitude(s.v) < REST_SPEED) & ~s.swinging):
                    s.picked_up = True
                    s.finish_request = True

                with g.If(s.finish_request):
                    finish_hole(g, refs)

            with g.Else():
                # The hole is done. The next one starts ADVANCE_DELAY
                # seconds later, or the round is over.
                with g.If(~s.finished & (time.world_time() - s.holed_at > ADVANCE_DELAY)):
                    with g.If(s.hole < len(HOLES) - 1):
                        s.hole = s.hole + 1
                        s.strokes = 0
                        s.holed = False
                        s.picked_up = False
                        s.result = ""
                        s.tee_request = True
                        s.teleport_request = True
                    with g.Else():
                        s.finished = True

            s.prev_q = q
            s.prev_head = head_pos
            trace.record(where="end", p=p, v=s.v)


def add_pushes(g: Graph, kit: Kit, refs: KitRefs, p: Any, surface_of: Any) -> None:
    """Adds the flow that lets a moving obstacle that overlaps the ball push it.

    Each of PUSH_RAYS level rays from the ball's center, one radius long,
    may meet a collider under a slot with a Mover space. The obstacle's
    velocity at the contact is the turn's angular velocity across the
    contact's offset from the pivot, plus the slide's velocity, the
    derivative of the binding's amplitude * sin(2 pi (t + phase) / period).
    The ball is put back out to touching the obstacle, and if it moves
    into the obstacle relative to that velocity, it bounces off it.
    """
    s, trace = refs.s, refs.trace
    ball = slots.ref(kit.ball)
    with g.For(PUSH_RAYS) as loop:
        with loop.OnIterate() as i:
            angle = dm.to_float(i) * (2 * math.pi / PUSH_RAYS)
            direction = dm.pack(dm.sin(angle), 0, dm.cos(angle))
            with g.RaycastOne(origin=p, direction=direction, max_distance=BALL_RADIUS,
                              ignore_hierarchy=kit.ball) as hit:
                with hit.on_hit():
                    where = slots.of_component(hit.hit_collider)
                    period = variables.read(where, "Mover/Period", primitives.Float)
                    with g.If(period.found):
                        pivot = slots.parent(where)
                        spin = variables.read(where, "Mover/Spin", primitives.Float3).value
                        slide = variables.read(where, "Mover/Slide", primitives.Float3).value
                        phase = variables.read(where, "Mover/Phase", primitives.Float).value
                        # The slide's phase angle, in radians, from the
                        # world's time, as the binding computes it.
                        cycle = dm.to_float((time.world_time() + phase) % period.value) / period.value
                        rate = 2 * math.pi / period.value
                        omega = transform.local_direction_to_global(pivot, spin) * (math.pi / 180)
                        surface_v = (
                            dm.cross(omega, hit.hit_point - transform.global_position(pivot))
                            + transform.local_direction_to_global(pivot, slide)
                            * (rate * dm.cos(cycle * (2 * math.pi)))
                        )
                        n = hit.hit_normal
                        overlap = BALL_RADIUS - dm.dot(p - hit.hit_point, n)
                        with g.If(overlap > 0):
                            g.SetGlobalPosition(ball, p + n * overlap)
                        approach = dm.dot(s.v - surface_v, n)
                        with g.If(approach < 0):
                            restitution, _, _ = surface_of(hit)
                            trace.record(where="push_in", v=s.v)
                            s.v = s.v - n * (approach * (1 + restitution))
                            trace.record(where="push_out", v=s.v)


def add_zones(g: Graph, kit: Kit, refs: KitRefs, p: Any, q: Any, penalty: Any) -> None:
    """Adds the flow that finds the zone under the ball and acts on the ball."""
    s, trace = refs.s, refs.trace
    ball = slots.ref(kit.ball)
    h = golf_holes.ZONE_HEIGHT
    with g.RaycastOne(origin=p + primitives.Float3(0, ZONE_PROBE, 0),
                      direction=primitives.Float3(0, -1, 0),
                      max_distance=ZONE_PROBE + BALL_RADIUS,
                      hit_triggers=True, ignore_hierarchy=kit.ball) as found:
        with found.on_hit():
            zone = slots.of_component(found.hit_collider)
            kind = variables.read(zone, "Zone/Kind", primitives.Int).value
            center = transform.global_position(zone)
            direction = transform.local_direction_to_global(
                zone, variables.read(zone, "Zone/Direction", primitives.Float3).value)
            speed = variables.read(zone, "Zone/Speed", primitives.Float).value
            # One kind at a time, as an else-if chain, whose paths add up
            # rather than multiply.
            with g.If(kind == golf_holes.CUP):
                with g.If(dm.magnitude(s.v) < CAPTURE_SPEED):
                    trace.record(where="cup", p=p, v=s.v)
                    g.SetGlobalPosition(ball, center - primitives.Float3(0, CUP_DEPTH, 0))
                    s.v = primitives.Float3(0, 0, 0)
                    s.finish_request = True
            with g.Else():
                with g.If(kind == golf_holes.BOOST):
                    trace.record(where="boost", v=s.v)
                    s.v = direction * speed + dm.pack(0, s.v.y, 0)
                with g.Else():
                    with g.If(kind == golf_holes.LAUNCH):
                        trace.record(where="launch", p=p)
                        g.SetGlobalPosition(ball, center + primitives.Float3(0, BALL_RADIUS - h / 2, 0))
                        s.v = direction * speed
                    with g.Else():
                        with g.If(kind == golf_holes.WARP):
                            trace.record(where="warp", p=p)
                            target = transform.local_point_to_global(
                                zone, variables.read(zone, "Zone/Target", primitives.Float3).value)
                            s.v = direction * dm.max_(dm.magnitude(s.v), speed)
                            g.SetGlobalPosition(ball, target)
                            s.prev_q = q
                        with g.Else():
                            with g.If(kind == golf_holes.WATER):
                                penalty("water")


def finish_hole(g: Graph, refs: KitRefs) -> None:
    """Records the current hole's strokes on the card and names the result."""
    s = refs.s
    s.finish_request = False
    s.holed = True
    s.holed_at = time.world_time()
    s.addressed = False
    # A write of each hole's score, of the strokes on the current hole or
    # of its old value, rather than an If per hole. Each If would double
    # the paths that ProtoFlux's ImpulseValidator walks.
    for hole in HOLES:
        score = getattr(s, f"score{hole.number}")
        setattr(s, f"score{hole.number}", dm.conditional(s.hole == hole.number - 1, s.strokes, score))
    s.total = s.total + s.strokes
    s.par_total = s.par_total + refs.par
    d = s.strokes - refs.par
    named = dm.conditional(
        s.strokes == 1, "Hole in one!", dm.conditional(
            d <= -2, "Eagle!", dm.conditional(
                d == -1, "Birdie!", dm.conditional(
                    d == 0, "Par", dm.conditional(
                        d == 1, "Bogey", dm.conditional(
                            d == 2, "Double bogey", "+" + strings.to_string(d)))))))
    s.result = dm.conditional(s.picked_up, "Picked up at " + strings.to_string(s.strokes), named)


def add_desktop_shots(g: Graph, kit: Kit, course: Course, refs: KitRefs) -> None:
    """Adds the flow that lets the owner, in desktop mode, address, aim, and hit the ball.

    The flow reads the mouse and the view of the machine that runs it,
    so it runs only on the owner's.
    """
    s = refs.s
    ball = slots.ref(kit.ball)
    course_ref = slots.ref(course.root)
    p = transform.global_position(ball)
    local = users.local_user()
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
               & (dm.magnitude(to_ball - forward * depth)
                  < dm.max_(CLICK_RADIUS, depth * CLICK_SLOPE)))
    at_rest = dm.magnitude(s.v) < REST_SPEED

    # The spot is where the view's ray meets the level plane through the
    # ball's center.
    look_down = -forward.y
    reach = (eye.y - p.y) / dm.max_(look_down, MIN_LOOK_DOWN)
    to_spot = eye + forward * reach - p
    to_spot_level = dm.pack(to_spot.x, 0, to_spot.z)
    facing = dm.pack(forward.x, 0, forward.z)

    def let_go() -> None:
        s.addressed = False
        s.charging = False
        s.fill = 0.0

    with g.Under(kit.graph):
        with g.If(refs.mine & ~dash_open):
            with g.If(s.addressed):
                with g.If(mouse.right_pressed() | ~at_rest | in_vr | s.holed):
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
                                level = transform.global_direction_to_local(course_ref, s.aim)
                                speed = refs.by_club([c.speed for c in CLUBS]) * (
                                    MIN_SPEED_SHARE + (1 - MIN_SPEED_SHARE) * s.fill * s.fill)
                                s.swing_yaw = dm.atan2(level.x, level.z) * math.degrees(1)
                                s.swing_back = refs.by_club([c.backswing for c in CLUBS]) * (
                                    MIN_BACKSWING_SHARE + (1 - MIN_BACKSWING_SHARE) * s.fill)
                                s.swing_rate = speed * math.degrees(1 / PIVOT_HEIGHT)
                                s.swing_request = True
                                s.addressed = False
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
                with g.If(~in_vr & ~s.holed):
                    with g.If(mouse.left_pressed() & on_ball & at_rest):
                        s.pressed_on_ball = True
                    # The ball is addressed when the button comes up, so
                    # that the press that addresses it doesn't also start a
                    # swing.
                    with g.If(mouse.left_released()):
                        with g.If(s.pressed_on_ball):
                            s.addressed = True
                            s.charging = False
                            s.fill = 0.0
                            s.aim = dm.normalized(facing)
                        s.pressed_on_ball = False
        # The left button may come up in the dash, where the flow doesn't
        # see it, so a swing in progress stops.
        with g.If(refs.mine & dash_open & s.charging):
            s.charging = False
            s.fill = 0.0


def add_bindings(g: Graph, kit: Kit, refs: KitRefs) -> None:
    """Binds what each machine shows of the kit, and what it lets its user touch.

    A drive computes on each machine, so the owner's machine and the
    others' can show and allow different things.
    """
    s, mine = refs.s, refs.mine
    p = transform.global_position(slots.ref(kit.ball))
    local = users.local_user()
    dash_open = users.is_dash_open(local)
    eye = users.view_position()
    view = users.view_rotation()
    aim = kit.aim
    at = kit.graph

    def in_view(offset: Any) -> Any:
        """Returns a point in world space that is at an offset in the view's space."""
        return eye + view * offset

    g.Bind(mine, kit.club_grab, "Enabled", slot=at)
    g.Bind(mine, kit.grip_collider, "Enabled", slot=at)
    g.Bind(mine | interaction.is_grabbed(kit.club_grab) | s.swinging, kit.club, "IsActive",
           slot=at)
    g.Bind(dm.axis_angle(primitives.Float3(1, 0, 0), -refs.by_club([c.loft for c in CLUBS])),
           kit.head, "Rotation", slot=at)

    g.Bind(mine & s.addressed, aim.arrow, "IsActive", slot=at)
    g.Bind(p + primitives.Float3(0, ARROW_LIFT, 0), aim.arrow, "Position", slot=at)
    g.Bind(s.aim * (ARROW_LENGTH + ARROW_GROWTH * s.fill), aim.arrow_mesh, "Vector", slot=at)

    g.Bind(mine & s.addressed & ~dash_open, aim.gauge, "IsActive", slot=at)
    g.Bind(in_view(primitives.Float3(*GAUGE_AT)), aim.gauge, "Position", slot=at)
    g.Bind(view, aim.gauge, "Rotation", slot=at)
    g.Bind(s.fill * 180, aim.fill, "Arc", slot=at)
    for i, label in enumerate(aim.club_labels):
        g.Bind(s.club == i, label, "IsActive", slot=at)

    # The name tag turns to face each viewer.
    g.Bind(p + primitives.Float3(0, NAME_TAG_HEIGHT, 0), aim.name_tag, "Position", slot=at)
    g.Bind(view, aim.name_tag, "Rotation", slot=at)
    g.Bind(users.username(s.owner), aim.name_text, "Text", slot=at)

    score = to_par(s.total - s.par_total)
    # The HUD hides while the scoreboard shows.
    g.Bind(mine & ~dash_open & s.claimed & ~keyboard.held("Tab"), aim.hud, "IsActive", slot=at)
    g.Bind(in_view(primitives.Float3(*HUD_AT)), aim.hud, "Position", slot=at)
    g.Bind(view, aim.hud, "Rotation", slot=at)
    g.Bind(
        "Hole " + strings.to_string(s.hole + 1) + "    Par " + strings.to_string(refs.par)
        + "\nStrokes " + strings.to_string(s.strokes) + "\nScore " + score,
        aim.status, "Text", slot=at,
    )
    g.Bind(s.holed, aim.banner, "IsActive", slot=at)
    g.Bind(dm.conditional(
        s.finished,
        "Round complete!\n" + strings.to_string(s.total) + " strokes, " + score
        + "\nPress Play to play again",
        s.result,
    ), aim.banner_text, "Text", slot=at)

    # The row of the scoreboard follows the view of whoever holds Tab.
    row_y = FIRST_ROW_Y - ROW_STEP * slots.child_index(slots.ref(kit.root))
    g.Bind(keyboard.held("Tab") & ~dash_open & s.claimed, aim.row, "IsActive", slot=at)
    # The row is a millimeter nearer than the panel, so that the panel
    # doesn't hide it.
    g.Bind(in_view(primitives.Float3(*BOARD_AT) + dm.pack(0, row_y, -0.001)),
           aim.row, "Position", slot=at)
    g.Bind(view, aim.row, "Rotation", slot=at)
    g.Bind(dm.conditional(mine, "> ", "") + users.username(s.owner), aim.row_name, "Text", slot=at)
    for h, cell in zip(HOLES, aim.row_holes):
        strokes = getattr(s, f"score{h.number}")
        g.Bind(dm.conditional(strokes == 0, "", strings.to_string(strokes)), cell, "Text", slot=at)
    g.Bind(strings.to_string(s.total), aim.row_total, "Text", slot=at)
    g.Bind(score, aim.row_diff, "Text", slot=at)


# ---------------------------------------------------------------------------
# The graph that every player shares.
# ---------------------------------------------------------------------------


def build_course_graph(course: Course) -> Graph:
    """Returns the graph of the Play button, the moving obstacles, and the scoreboard's headings.

    A press of Play gives the presser a kit if they have none. It runs on
    the presser's machine, since a button's events fire only there, so
    the duplicate's OnDuplicate event fires there too.
    """
    g = Graph()
    with g.Under(course.graph):
        with g.ButtonEvents(button=course.play_button) as e:
            with e.pressed():
                mine = slots.find_child(course.players, users.machine_id(users.local_user()))
                with g.If(dm.is_null(mine)):
                    kit = g.DuplicateSlot(course.kit.root, course.players)
                    g.SetSlotActiveSelf(kit, True)

    # The movers follow the world's time, which every user's machine
    # shares, so they are in the same place for everyone.
    now = time.world_time()
    for pivot, mover in course.movers:
        t = now + mover.phase
        axis = primitives.Float3(*mover.axis)
        if mover.speed:
            angle = dm.to_float((t * mover.speed) % 360)
            g.Bind(dm.axis_angle(axis, angle), pivot, "Rotation", slot=course.graph)
        else:
            offset = dm.to_float(dm.sin(t * (2 * math.pi / mover.period))) * mover.amplitude
            g.Bind(primitives.Float3(*mover.pivot) + axis * offset, pivot, "Position",
                   slot=course.graph)

    local = users.local_user()
    view = users.view_rotation()
    g.Bind(keyboard.held("Tab") & ~users.is_dash_open(local), course.board, "IsActive",
           slot=course.graph)
    g.Bind(users.view_position() + view * primitives.Float3(*BOARD_AT), course.board, "Position",
           slot=course.graph)
    g.Bind(view, course.board, "Rotation", slot=course.graph)
    return g


async def main(port: int | None) -> None:
    """Builds the course and the graphs in front of the user.

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
    course = await build_course(resolink)
    await build_course_graph(course).build(resolink)
    print("Built the graph of the Play button, the movers, and the scoreboard.")
    await build_kit_graph(course.kit, course).build(resolink)
    print("The course is ready. Press Play to get a ball.")
    await resolink.close()


if __name__ == "__main__":
    asyncio.run(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
