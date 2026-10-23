"""The 18 holes of the golf example, as data.

Each hole is described in its own space, with X across the hole, Z from
the tee toward the cup, and Y up from the ground that the course stands
on. Most holes have a felt floor whose top is FLOOR above the ground,
with rails around it. A raised part is a box from the ground up to its
top, so its sides are walls.

A hole is made of boxes and cylinders, each with a surface whose
physical properties the ball's graph reads, zones that do something to
a ball that rolls over them, and movers, groups of boxes that a binding
turns or slides with the world's time.

dergflux_golf.py builds the holes from this module and moves the balls
on them.
"""

import dataclasses
import math

FLOOR = 0.1  # meters from the ground to the top of a hole's main floor
RAIL_HEIGHT = 0.09  # meters from a floor to the top of the rail beside it
RAIL_THICKNESS = 0.05  # meters
# The Rules of Golf set a 42.67 mm minimum diameter.
BALL_RADIUS = 0.02135  # meters
GRAVITY = 9.81  # m/s^2
# The Rules of Golf set a 108 mm diameter for the cup.
CUP_RADIUS = 0.054  # meters
# A zone is a trigger box this tall, standing on the floor. The ball's
# graph finds it with a ray from just above the ball's center.
ZONE_HEIGHT = 0.03  # meters

# The kinds of zone, as the ball's graph reads them from Zone/Kind.
CUP = 1  # the ball drops in if it is slow enough
BOOST = 2  # the ball's velocity along the floor becomes Direction * Speed
LAUNCH = 3  # the ball is put at the zone's center and fired at Direction * Speed
WARP = 4  # the ball is put at Target and sent along Direction at Speed or faster
WATER = 5  # a stroke is added and the ball goes back to where it was hit from


@dataclasses.dataclass(frozen=True)
class Physics:
    """Represents the physical properties that a slot's Physics space holds.

    Attributes:
        restitution (float): The ratio of the speed away from a surface
            after a bounce to the speed toward it before, as a property of
            this body alone. A contact multiplies the two bodies' values,
            so a value above 1 makes a bumper that kicks the ball.
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


# The Rules of Golf set a 45.93 g maximum mass.
BALL = Physics(restitution=0.9, friction=0.5, rolling=0.1, mass=0.04593)

# The surfaces, by name. A contact of felt with BALL's values slows a
# rolling ball by 0.88 m/s^2, so one rolled at 3 m/s goes 5.1 m.
SURFACES = {
    "felt": Physics(restitution=0.3, friction=0.6, rolling=0.08),
    "rail": Physics(restitution=0.75, friction=0.3, rolling=0.02),
    # A contact restitution of 1.17 sends the ball away faster than it came.
    "bumper": Physics(restitution=1.3, friction=0.2, rolling=0.02),
    "wood": Physics(restitution=0.5, friction=0.4, rolling=0.05),
    "stone": Physics(restitution=0.6, friction=0.5, rolling=0.05),
    "sand": Physics(restitution=0.08, friction=0.9, rolling=4.0),
    # A rolling ball slows by only 0.2 m/s^2 on ice.
    "ice": Physics(restitution=0.2, friction=0.02, rolling=0.004),
    "water": Physics(restitution=0.1, friction=0.9, rolling=4.0),
    # The floor of a tunnel. With BALL's values, a ball rolls down it on
    # any slope steeper than 2.5 degrees, where felt needs 7.1.
    "chute": Physics(restitution=0.3, friction=0.3, rolling=0.01),
    # Zone pads and other things that the ball never touches.
    "none": Physics(restitution=0.5),
}


@dataclasses.dataclass(frozen=True)
class Box:
    """Represents a box of a hole.

    Attributes:
        center (tuple[float, float, float]): The center in the hole's
            space, or in a mover's space for a mover's part.
        size (tuple[float, float, float]): The size along X, Y, and Z
            before the rotation, in meters.
        surface (str): The key of the box's physical properties in
            SURFACES.
        finish (str | None): The key of its material in the example's
            FINISHES, or None for the one named like the surface.
        rotation (tuple[float, float, float]): Euler angles in degrees,
            as floatQ.Euler takes them.
        collider (bool): Whether the box has a collider.
    """

    center: tuple[float, float, float]
    size: tuple[float, float, float]
    surface: str
    finish: str | None = None
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0)
    collider: bool = True


@dataclasses.dataclass(frozen=True)
class Cylinder:
    """Represents an upright cylinder of a hole.

    Attributes:
        center (tuple[float, float, float]): The center in the hole's space.
        radius (float): The radius in meters.
        height (float): The height in meters.
        surface (str): The key of its physical properties in SURFACES.
        finish (str | None): The key of its material, or None for the
            one named like the surface.
        collider (bool): Whether the cylinder has a collider.
    """

    center: tuple[float, float, float]
    radius: float
    height: float
    surface: str
    finish: str | None = None
    collider: bool = True


@dataclasses.dataclass(frozen=True)
class Zone:
    """Represents a place on a floor that does something to a ball over it.

    The zone's slot is at center, unrotated in the hole's space, so a
    direction or a point in the zone's space is the same as in the
    hole's, measured from center.

    Attributes:
        kind (int): CUP, BOOST, LAUNCH, WARP, or WATER.
        center (tuple[float, float, float]): The middle of the zone's
            bottom, on the floor, in the hole's space.
        size (tuple[float, float]): The extent along X and Z, or the
            diameter twice for a round zone.
        round (bool): Whether the zone is a disc rather than a rectangle.
        direction (tuple[float, float, float]): A unit vector, for BOOST,
            LAUNCH, and WARP.
        speed (float): The speed in m/s, for BOOST, LAUNCH, and WARP.
        target (tuple[float, float, float]): Where a WARP puts the ball's
            center, in the hole's space.
    """

    kind: int
    center: tuple[float, float, float]
    size: tuple[float, float]
    round: bool = False
    direction: tuple[float, float, float] = (0.0, 0.0, 1.0)
    speed: float = 0.0
    target: tuple[float, float, float] = (0.0, 0.0, 0.0)


@dataclasses.dataclass(frozen=True)
class Mover:
    """Represents boxes that turn or slide together, with the world's time.

    Attributes:
        pivot (tuple[float, float, float]): The point the boxes turn
            about, or their middle position, in the hole's space.
        parts (list[Box]): The boxes, in the pivot's space.
        surface (str): The key of the boxes' physical properties.
        axis (tuple[float, float, float]): The axis of the turn, or the
            direction of the slide.
        speed (float): Degrees per second of the turn, or 0 for a slide.
        amplitude (float): How far a slide goes either way, in meters.
        period (float): The seconds of one slide there and back.
        phase (float): Seconds added to the world's time, so that two
            movers don't move together.
    """

    pivot: tuple[float, float, float]
    parts: list[Box]
    surface: str
    axis: tuple[float, float, float]
    speed: float = 0.0
    amplitude: float = 0.0
    period: float = 1.0
    phase: float = 0.0


@dataclasses.dataclass(frozen=True)
class Hole:
    """Represents one hole.

    Attributes:
        number (int): From 1 to 18.
        name (str): The name on the hole's sign.
        par (int): The strokes that a good player takes.
        tee (tuple[float, float, float]): The ball's center on the tee,
            in the hole's space.
        pieces (list[Box | Cylinder]): The floors, rails, and obstacles.
        zones (list[Zone]): The cup and every other zone.
        movers (list[Mover]): The moving obstacles.
    """

    number: int
    name: str
    par: int
    tee: tuple[float, float, float]
    pieces: list[Box | Cylinder]
    zones: list[Zone]
    movers: list[Mover] = dataclasses.field(default_factory=list)

    @property
    def cup(self) -> Zone:
        """The hole's cup."""
        return next(z for z in self.zones if z.kind == CUP)

    def bounds(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """Returns the corners of the box that a ball in play stays inside.

        It spans the floors and rails along X and Z, with 5 cm to spare,
        and from 5 cm below the lowest floor's top up. A ball whose center
        leaves it is out of bounds.
        """
        boxes = [p for p in self.pieces if isinstance(p, Box)]
        floors = [b for b in boxes if b.surface in ("felt", "ice", "sand", "water", "wood")]
        xs, zs = [], []
        for b in boxes:
            # The extents of a box turned about Y, which is how rails turn.
            yaw = math.radians(b.rotation[1])
            half_x = (abs(math.cos(yaw)) * b.size[0] + abs(math.sin(yaw)) * b.size[2]) / 2
            half_z = (abs(math.sin(yaw)) * b.size[0] + abs(math.cos(yaw)) * b.size[2]) / 2
            xs += [b.center[0] - half_x, b.center[0] + half_x]
            zs += [b.center[2] - half_z, b.center[2] + half_z]
        lowest = min(b.center[1] + b.size[1] / 2 for b in floors if b.rotation == (0.0, 0.0, 0.0))
        return (min(xs) - 0.05, lowest - 0.05, min(zs) - 0.05), (max(xs) + 0.05, 10.0, max(zs) + 0.05)


# ---------------------------------------------------------------------------
# The pieces that holes are made of.
# ---------------------------------------------------------------------------


def floor(x0: float, x1: float, z0: float, z1: float, top: float = FLOOR,
          surface: str = "felt") -> Box:
    """Returns a floor over a rectangle, a box from the ground up to its top."""
    return Box(((x0 + x1) / 2, top / 2, (z0 + z1) / 2), (x1 - x0, top, z1 - z0), surface)


def rails(points: list[tuple[float, float]], top: float = FLOOR + RAIL_HEIGHT,
          surface: str = "rail") -> list[Box]:
    """Returns rails along a path of points (x, z), from the ground up to top.

    Each rail is centered on its segment and runs half a thickness past
    both ends, so that the rails meet at the corners.
    """
    boxes = []
    for (xa, za), (xb, zb) in zip(points, points[1:]):
        length = math.hypot(xb - xa, zb - za)
        # A turn about Y by this angle points the box's +Z along the segment.
        yaw = math.degrees(math.atan2(xb - xa, zb - za))
        boxes.append(Box(
            ((xa + xb) / 2, top / 2, (za + zb) / 2),
            (RAIL_THICKNESS, top, length + RAIL_THICKNESS), surface, rotation=(0.0, yaw, 0.0),
        ))
    return boxes


def fence(x0: float, x1: float, z0: float, z1: float,
          top: float = FLOOR + RAIL_HEIGHT) -> list[Box]:
    """Returns rails around the outside of a rectangle."""
    h = RAIL_THICKNESS / 2
    return rails([(x0 - h, z0 - h), (x0 - h, z1 + h), (x1 + h, z1 + h), (x1 + h, z0 - h),
                  (x0 - h, z0 - h)], top)


def block(x: float, z: float, sx: float, sz: float, height: float = RAIL_HEIGHT,
          base: float = FLOOR, surface: str = "stone") -> Box:
    """Returns an obstacle standing height above a floor, a box from the ground up."""
    top = base + height
    return Box((x, top / 2, z), (sx, top, sz), surface)


def post(x: float, z: float, radius: float = 0.07, height: float = RAIL_HEIGHT,
         surface: str = "bumper") -> Cylinder:
    """Returns a round post standing height above the floor, from the ground up."""
    top = FLOOR + height
    return Cylinder((x, top / 2, z), radius, top, surface)


def roof(x0: float, x1: float, z0: float, z1: float, bottom: float, top: float,
         surface: str = "stone") -> Box:
    """Returns a box between two heights, over a tunnel."""
    return Box(((x0 + x1) / 2, (bottom + top) / 2, (z0 + z1) / 2),
               (x1 - x0, top - bottom, z1 - z0), surface)


RAMP_THICKNESS = 0.04  # meters


def ramp(x0: float, x1: float, z0: float, z1: float, y0: float, y1: float,
         surface: str = "felt") -> Box:
    """Returns a slab whose top rises along Z, from y0 at z0 to y1 at z1."""
    a = math.atan2(y1 - y0, z1 - z0)
    length = math.hypot(z1 - z0, y1 - y0)
    # The top's normal leans back toward -Z for a slab that rises toward
    # +Z, and the slab's center is half a thickness below the top's middle.
    normal = (0.0, math.cos(a), -math.sin(a))
    top = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)
    center = tuple(c - n * RAMP_THICKNESS / 2 for c, n in zip(top, normal))
    # A positive angle about X turns +Y toward +Z, so the rise is a
    # negative angle.
    return Box(center, (x1 - x0, RAMP_THICKNESS, length), surface,  # type: ignore[arg-type]
               rotation=(-math.degrees(a), 0.0, 0.0))


def ramp_x(x0: float, x1: float, z0: float, z1: float, y0: float, y1: float,
           surface: str = "felt") -> Box:
    """Returns a slab whose top rises along X, from y0 at x0 to y1 at x1."""
    a = math.atan2(y1 - y0, x1 - x0)
    length = math.hypot(x1 - x0, y1 - y0)
    normal = (-math.sin(a), math.cos(a), 0.0)
    top = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)
    center = tuple(c - n * RAMP_THICKNESS / 2 for c, n in zip(top, normal))
    # A positive angle about Z turns +X toward +Y, which is the rise.
    return Box(center, (length, RAMP_THICKNESS, z1 - z0), surface,  # type: ignore[arg-type]
               rotation=(0.0, 0.0, math.degrees(a)))


def cup(x: float, z: float, top: float = FLOOR) -> Zone:
    """Returns the cup at a point on a floor whose top is at top."""
    return Zone(CUP, (x, top, z), (2 * CUP_RADIUS, 2 * CUP_RADIUS), round=True)


def tee(x: float, z: float, top: float = FLOOR) -> tuple[float, float, float]:
    """Returns the ball's center on a tee at a point on a floor whose top is at top."""
    return (x, top + BALL_RADIUS, z)


def boost(x: float, z: float, sx: float, sz: float, speed: float,
          direction: tuple[float, float, float] = (0.0, 0.0, 1.0), top: float = FLOOR) -> Zone:
    """Returns a pad that sends the ball along direction at speed."""
    return Zone(BOOST, (x, top, z), (sx, sz), direction=direction, speed=speed)


def launch(x: float, z: float, sx: float, sz: float, target: tuple[float, float, float],
           angle: float, top: float = FLOOR) -> Zone:
    """Returns a pad that fires the ball from its center to land at target.

    The ball leaves the pad's center at the angle above level, in
    degrees, at the speed that a body with no drag needs to reach
    target, the landing point of the ball's center in the hole's space.
    That speed is the solution of h = d tan(a) - g d^2 / (2 v^2 cos^2(a))
    for v, with d the level distance and h the rise.

    Raises:
        ValueError: The angle is too low to reach the target.
    """
    start = (x, top + BALL_RADIUS, z)
    dx, dz = target[0] - start[0], target[2] - start[2]
    d = math.hypot(dx, dz)
    h = target[1] - start[1]
    a = math.radians(angle)
    if d * math.tan(a) <= h:
        raise ValueError(f"A launch at {angle} degrees can't rise {h} m in {d} m.")
    speed = math.sqrt(GRAVITY * d * d / (2 * math.cos(a) ** 2 * (d * math.tan(a) - h)))
    direction = (dx / d * math.cos(a), math.sin(a), dz / d * math.cos(a))
    return Zone(LAUNCH, (x, top, z), (sx, sz), direction=direction, speed=speed)


def warp(x: float, z: float, exit_x: float, exit_z: float, speed: float,
         direction: tuple[float, float, float] = (0.0, 0.0, 1.0), top: float = FLOOR,
         exit_top: float = FLOOR) -> Zone:
    """Returns a hole in the floor that sends the ball out at another point."""
    return Zone(WARP, (x, top, z), (0.16, 0.16), round=True, direction=direction,
                speed=speed, target=(exit_x, exit_top + BALL_RADIUS, exit_z))


def water(x0: float, x1: float, z0: float, z1: float, top: float = FLOOR) -> list[Box | Zone]:
    """Returns a pond: a floor of water whose top is 1 cm below top, and its zone."""
    pond_top = top - 0.01
    return [floor(x0, x1, z0, z1, pond_top, "water"),
            Zone(WATER, ((x0 + x1) / 2, pond_top, (z0 + z1) / 2), (x1 - x0, z1 - z0))]


def _hole(number: int, name: str, par: int, tee_at: tuple[float, float, float],
          parts: list[Box | Cylinder | Zone | Mover | list]) -> Hole:  # type: ignore[type-arg]
    """Returns a hole from a list of pieces, zones, movers, and lists of them."""
    flat: list[Box | Cylinder | Zone | Mover] = []
    for p in parts:
        flat.extend(p if isinstance(p, list) else [p])
    return Hole(
        number, name, par, tee_at,
        pieces=[p for p in flat if isinstance(p, (Box, Cylinder))],
        zones=[p for p in flat if isinstance(p, Zone)],
        movers=[p for p in flat if isinstance(p, Mover)],
    )


# A tunnel's floor falls this far from its mouth to its exit, so that a
# ball that stops in it rolls out. Over a tunnel 0.6 m long that is a
# slope of 7.6 degrees, and over 0.8 m one of 5.7, both steeper than the
# 2.5 degrees that a chute needs.
TUNNEL_DROP = 0.08  # meters
# The height of a tunnel's roof above its mouth's floor, above the 6 cm
# from the ball's center where the zone ray starts.
TUNNEL_HEIGHT = 0.11  # meters


def _windmill(z: float, gap: float = 0.12, width: float = 0.7, speed: float = 45.0,
              top: float = FLOOR + TUNNEL_DROP) -> list:  # type: ignore[type-arg]
    """Returns a windmill house across a lane, with a tunnel and turning blades in front.

    The house's front is at z, where the floor's top is at top. The
    tunnel's floor falls by TUNNEL_DROP to FLOOR at the house's back. Four
    blades as wide as the tunnel turn in front of it, about a hub above
    the tunnel, and reach down to the floor, so they block the tunnel's
    mouth now and then.
    """
    height = 0.45
    depth = 0.8
    half = gap / 2
    blade_length = 0.48
    hub = (0.0, top + 0.5, z - 0.04)
    blades = [
        Box((blade_length / 2 * math.sin(math.radians(k * 90)),
             -blade_length / 2 * math.cos(math.radians(k * 90)), 0.0),
            (gap + 0.02, blade_length, 0.02), "wood", rotation=(0.0, 0.0, k * 90.0))
        for k in range(4)
    ]
    return [
        block(-(half + width) / 2, z + depth / 2, width - half, depth, height, top),
        block((half + width) / 2, z + depth / 2, width - half, depth, height, top),
        roof(-half, half, z, z + depth, top + TUNNEL_HEIGHT, top + height),
        ramp(-half, half, z, z + depth, top, top - TUNNEL_DROP, "chute"),
        Mover(hub, blades, "wood", (0.0, 0.0, 1.0), speed=speed),
    ]


def _slider(z: float, length: float, amplitude: float, period: float, phase: float) -> Mover:
    """Returns a wall across a lane that slides from side to side."""
    return Mover((0.0, FLOOR, z), [Box((0.0, RAIL_HEIGHT / 2, 0.0), (length, RAIL_HEIGHT, 0.06), "rail")],
                 "rail", (1.0, 0.0, 0.0), amplitude=amplitude, period=period, phase=phase)


def _holes() -> list[Hole]:
    """Returns the 18 holes."""
    up = FLOOR + 0.2  # the top of a raised green
    deck = FLOOR + 0.3  # the top of an upper deck
    finale_green = FLOOR + 0.15
    return [
        _hole(1, "Warm Up", 2, tee(0, 0.5), [
            floor(-0.5, 0.5, 0, 5), fence(-0.5, 0.5, 0, 5), cup(0, 4.3),
        ]),
        _hole(2, "Stepping Stones", 3, tee(0, 0.5), [
            floor(-0.6, 0.6, 0, 6), fence(-0.6, 0.6, 0, 6),
            block(-0.25, 2.4, 0.7, 0.15), block(0.25, 4.0, 0.7, 0.15),
            cup(0, 5.3),
        ]),
        _hole(3, "Hairpin", 3, tee(-0.5, 0.5), [
            floor(-1, 1, 0, 6), fence(-1, 1, 0, 6),
            rails([(0, 0), (0, 4.4)]),
            # Deflectors in the far corners turn the ball around the end
            # of the middle rail.
            rails([(-1, 5.2), (-0.2, 6)]), rails([(0.2, 6), (1, 5.2)]),
            cup(0.5, 0.7),
        ]),
        _hole(4, "Pinball", 3, tee(0, 0.5), [
            floor(-0.9, 0.9, 0, 7), fence(-0.9, 0.9, 0, 7),
            post(-0.45, 2.0), post(0.45, 2.0), post(0, 3.1),
            post(-0.5, 4.2), post(0.5, 4.2), post(0, 5.3),
            cup(0, 6.4),
        ]),
        _hole(5, "Up the Ramp", 2, tee(0, 0.5), [
            floor(-0.6, 0.6, 0, 2.5), ramp(-0.6, 0.6, 2.5, 4.0, FLOOR, up),
            floor(-0.6, 0.6, 4.0, 6.5, up), fence(-0.6, 0.6, 0, 6.5, up + RAIL_HEIGHT),
            cup(0, 5.8, up),
        ]),
        # The lane before the windmill is raised, so that its tunnel falls
        # to the lane behind it.
        _hole(6, "Windmill", 3, tee(0, 0.5, FLOOR + TUNNEL_DROP), [
            floor(-0.7, 0.7, 0, 4.0, FLOOR + TUNNEL_DROP), floor(-0.7, 0.7, 4.8, 8),
            fence(-0.7, 0.7, 0, 8, FLOOR + TUNNEL_DROP + RAIL_HEIGHT),
            _windmill(4.0), cup(0, 7.2),
        ]),
        _hole(7, "Speed Strip", 2, tee(0, 0.5), [
            floor(-0.5, 0.5, 0, 9), fence(-0.5, 0.5, 0, 9),
            boost(0, 2.5, 0.6, 0.5, 2.5), boost(0, 5.5, 0.6, 0.5, 2.5),
            block(-0.3, 4.0, 0.25, 0.1), block(0.3, 7.0, 0.25, 0.1),
            cup(0, 8.3),
        ]),
        _hole(8, "Water Hazard", 3, tee(-0.4, 0.5), [
            floor(-0.9, 0.9, 0, 2.5), floor(-0.9, 0.9, 4.0, 7),
            water(-0.9, 0.35, 2.5, 4.0), water(0.65, 0.9, 2.5, 4.0),
            floor(0.35, 0.65, 2.5, 4.0, surface="wood"),
            fence(-0.9, 0.9, 0, 7), cup(-0.4, 6.3),
        ]),
        _hole(9, "Cannon", 3, tee(0, 0.4), [
            floor(-0.25, 0.25, 0, 2.6),
            rails([(-0.25 - RAIL_THICKNESS / 2, 2.6), (-0.25 - RAIL_THICKNESS / 2, -RAIL_THICKNESS / 2),
                   (0.25 + RAIL_THICKNESS / 2, -RAIL_THICKNESS / 2), (0.25 + RAIL_THICKNESS / 2, 2.6)]),
            launch(0, 2.3, 0.5, 0.4, (0, FLOOR + BALL_RADIUS, 5.6), 60.0),
            floor(-0.8, 0.8, 4.6, 7.5), fence(-0.8, 0.8, 4.6, 7.5),
            cup(0.3, 6.7),
        ]),
        _hole(10, "Warp Zone", 2, tee(-0.45, 0.5), [
            floor(-0.8, 0.8, 0, 7), fence(-0.8, 0.8, 0, 7),
            rails([(-0.8, 3.0), (0.8, 3.0)]),
            warp(0.45, 2.3, -0.45, 3.5, 0.8),
            cup(0.45, 6.0),
        ]),
        _hole(11, "Sliders", 3, tee(0, 0.5), [
            floor(-0.6, 0.6, 0, 7.5), fence(-0.6, 0.6, 0, 7.5),
            _slider(2.6, 0.6, 0.3, 3.0, 0.0), _slider(4.8, 0.6, 0.3, 2.2, 1.0),
            cup(0, 6.8),
        ]),
        _hole(12, "Ice Rink", 3, tee(-0.4, 0.5), [
            floor(-0.8, 0.8, 0, 1.5), floor(-0.8, 0.8, 1.5, 5.5, surface="ice"),
            floor(-0.8, 0.8, 5.5, 7.5), fence(-0.8, 0.8, 0, 7.5),
            rails([(0.15, 6.35), (0.15, 6.85), (0.65, 6.85), (0.65, 6.35)]),
            cup(0.4, 6.6),
        ]),
        # The lane before the wall is raised, so that the tunnels through
        # it fall to the lane behind it.
        _hole(13, "Three Tunnels", 3, tee(0, 0.5, FLOOR + TUNNEL_DROP), [
            floor(-0.9, 0.9, 0, 3.0, FLOOR + TUNNEL_DROP),
            [block((a + b) / 2, 3.3, b - a, 0.6, 0.3)
             for a, b in ((-0.9, -0.67), (-0.53, -0.07), (0.07, 0.53), (0.67, 0.9))],
            [roof(x - 0.07, x + 0.07, 3.0, 3.6, FLOOR + TUNNEL_DROP + TUNNEL_HEIGHT, FLOOR + 0.3)
             for x in (-0.6, 0.0, 0.6)],
            [ramp(x - 0.07, x + 0.07, 3.0, 3.6, FLOOR + TUNNEL_DROP, FLOOR, "chute")
             for x in (-0.6, 0.0, 0.6)],
            floor(-0.9, -0.3, 3.6, 4.6, FLOOR - 0.03, "sand"), floor(0.3, 0.9, 3.6, 4.6, FLOOR - 0.03, "sand"),
            floor(-0.3, 0.3, 3.6, 4.6), floor(-0.9, 0.9, 4.6, 7.5),
            fence(-0.9, 0.9, 0, 7.5, FLOOR + TUNNEL_DROP + RAIL_HEIGHT), cup(0, 6.6),
        ]),
        _hole(14, "The Summit", 3, tee(0, 0.5), [
            floor(-1, 1, 0, 3.4), floor(-1, 1, 5.6, 7),
            ramp(-0.3, 0.3, 3.4, 4.2, FLOOR, up), floor(-0.3, 0.3, 4.2, 4.8, up),
            ramp(-0.3, 0.3, 4.8, 5.6, up, FLOOR),
            # Stone walls on both sides of the ridge, a little higher than
            # its top, keep the ball on it. A ball that overshoots the cup
            # rolls down the far side.
            block(-0.65, 4.5, 0.7, 2.2, up - FLOOR + 0.06), block(0.65, 4.5, 0.7, 2.2, up - FLOOR + 0.06),
            fence(-1, 1, 0, 7), cup(0, 4.5, up),
        ]),
        _hole(15, "Zig Zag", 4, tee(-0.5, 0.5), [
            floor(-1, 1, 0, 9), fence(-1, 1, 0, 9),
            rails([(-1, 2.2), (0.4, 2.2)]), rails([(1, 4.4), (-0.4, 4.4)]), rails([(-1, 6.6), (0.4, 6.6)]),
            cup(-0.5, 8.2),
        ]),
        _hole(16, "Spin Cycle", 3, tee(0, 0.5), [
            floor(-1, 1, 0, 7.5), fence(-1, 1, 0, 7.5),
            Mover((0.0, FLOOR, 3.8), [Box((0.0, RAIL_HEIGHT / 2, 0.0), (1.8, RAIL_HEIGHT, 0.05), "rail")],
                  "rail", (0.0, 1.0, 0.0), speed=50.0),
            Cylinder((0.0, FLOOR + 0.07, 3.8), 0.05, 0.14, "none", "Steel", collider=False),
            cup(0, 6.6),
        ]),
        _hole(17, "Double Decker", 3, tee(0, 0.5, deck), [
            floor(-0.5, 0.5, 0, 3.5, deck), ramp(-0.5, 0.5, 3.5, 5.0, deck, FLOOR),
            rails([(-0.5 - RAIL_THICKNESS / 2, 5.0), (-0.5 - RAIL_THICKNESS / 2, -RAIL_THICKNESS / 2),
                   (0.5 + RAIL_THICKNESS / 2, -RAIL_THICKNESS / 2), (0.5 + RAIL_THICKNESS / 2, 5.0)],
                  deck + RAIL_HEIGHT),
            boost(0, 2.0, 0.5, 0.4, 1.5, top=deck),
            floor(-0.9, 0.9, 5.0, 8.0),
            rails([(-0.5 - RAIL_THICKNESS / 2, 5.0), (-0.9 - RAIL_THICKNESS / 2, 5.0),
                   (-0.9 - RAIL_THICKNESS / 2, 8.0 + RAIL_THICKNESS / 2),
                   (0.9 + RAIL_THICKNESS / 2, 8.0 + RAIL_THICKNESS / 2),
                   (0.9 + RAIL_THICKNESS / 2, 5.0), (0.5 + RAIL_THICKNESS / 2, 5.0)]),
            post(-0.4, 6.2), post(0.4, 6.2),
            cup(0, 7.3),
        ]),
        _hole(18, "Grand Finale", 4, tee(0, 0.5), [
            floor(-1.1, 1.1, 0, 4.0),
            post(-0.6, 1.8), post(0.6, 1.8), post(0, 2.6),
            launch(-0.5, 3.6, 0.4, 0.4, (-0.5, finale_green + BALL_RADIUS, 8.0), 55.0),
            water(-1.1, 0.7, 4.0, 7.0),
            floor(0.7, 1.1, 4.0, 6.0, surface="wood"), ramp(0.7, 1.1, 6.0, 7.0, FLOOR, finale_green, "wood"),
            floor(-1.1, 1.1, 7.0, 10.5, finale_green),
            fence(-1.1, 1.1, 0, 10.5, finale_green + RAIL_HEIGHT),
            cup(0.3, 9.6, finale_green),
        ]),
    ]


HOLES = _holes()
# The par of the whole course.
PAR = sum(h.par for h in HOLES)

# Where each hole's origin is in the course's space. The holes are in
# three rows of six, going back and forth, so that each hole's tee is
# near the last one's.
COLUMN_SPACING = 3.0  # meters
ROW_SPACING = 12.0  # meters


def hole_origin(number: int) -> tuple[float, float, float]:
    """Returns the origin of a hole in the course's space."""
    row, column = divmod(number - 1, 6)
    if row % 2 == 1:
        column = 5 - column
    return (column * COLUMN_SPACING, 0.0, row * ROW_SPACING)
