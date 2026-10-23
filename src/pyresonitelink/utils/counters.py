"""Dergflux expressions and flows for mechanical counters, such as odometers.

A counter has drums, one per decimal place, and a position, which is the
number of digits that the lowest drum has turned. That is, if the lowest
drum shows hundredths, the position of 12.34 is 1234. drum_turns gives how
many digits each drum has turned for a position. The lowest drum turns with
the position. Each higher drum rests on its digit and rolls to the next one
while the drum below it rolls from 9 to 0, as an odometer's carry gears
make it.

    for place, drum in zip([1, 10, 100, 1000], drums):
        turns = counters.drum_turns(position, place)
        g.Bind(dm.axis_angle(axis, dm.to_float(turns * 36)), drum, "Rotation", slot=slot)

add_detents makes the drums rest on whole digits. It adds a flow that runs
in every engine update and keeps a detent, the whole digit the drums rest
on, and returns a smoothed position that follows it. While the number is
within threshold digits of the detent, the drums lean toward the number by
creep of the way. When the number goes further, the detent moves to the
nearest digit, and the drums snap to it. A threshold of more than half a
digit keeps the drums from snapping back and forth when the number stops
near the middle between two digits. When held is false, the number itself
is set to the detent, as a detent spring pulls a released mechanism into
place.

The smoothed position follows its target through two smoothing stages in
series, each of which closes a fraction rate * dt of its gap in every
update, where dt is the update's length in seconds. The pair starts from
rest, speeds up, and slows down again, so a snap takes about 4 / rate
seconds to cover 90% of the way. A trace of a live odometer, with a rate
of 30, showed snaps of 100 to 135 ms (23 Oct 2026).

    s.value = s.FloatDynVar("value")
    s.held = s.BoolDynVar("held")
    position = counters.add_detents(g, s, slot, "value", scale=100, held=s.held)
"""

from typing import Any

from pyresonitelink.data import workers
from pyresonitelink.dergflux import _expr
from pyresonitelink.dergflux import _graph
from pyresonitelink.dergflux import _space
from pyresonitelink.dergflux import math as dm
from pyresonitelink.dergflux import time

# How close to the detent, in digits, a released number has to be to count
# as already on it. Without it, the flow would set the number every update.
_ON_DETENT = 0.001


def drum_turns(position: Any, place: int) -> _expr.ExprProxy:
    """Returns how many digits a counter's drum has turned, from 0 up to 10.

    If p is the drum's place and n the position, the drum turns by
    floor(n / p) mod 10 digits, plus the fraction of the way that the drums
    below it have gone from p - 1 to p, which is clamp01((n mod p) - (p - 1)).
    For example, at a position of 129.5 the tens drum has turned 2.5
    digits, since the units drum is halfway from 9 to 0. The result is 10
    at the end of a carry from 9, which shows the same digit as 0.

    Args:
        position (Any): The counter's position, a Float or Double
            expression that isn't negative.
        place (int): The drum's place, which is 1 for the lowest drum, 10
            for the one above it, and so on.

    Returns:
        The number of digits turned. Multiply it by 36 for an angle in
        degrees.

    Raises:
        ValueError: place isn't a positive power of 10.
    """
    p = place
    while p > 1 and p % 10 == 0:
        p //= 10
    if p != 1:
        raise ValueError(f"A drum's place is a power of 10, not {place}.")
    if place == 1:
        return position % 10
    return dm.floor(position / place) % 10 + dm.clamp01(position % place - (place - 1))


def add_detents(
    g: _graph.Graph,
    space: _space.Space,
    slot: workers.Slot,
    variable: str,
    *,
    scale: float = 1.0,
    held: Any = None,
    threshold: float = 0.55,
    creep: float = 0.25,
    rate: float = 30.0,
    name: str = "detent",
) -> _expr.ExprProxy:
    """Adds a flow that makes a counter's drums rest on whole digits, and snap between them.

    The flow declares three FloatModelVars in the space: name, which is the
    detent, and name_lag and name_position, which are the two smoothing
    stages. All three count digits of the lowest drum. It runs under slot,
    in every engine update.

    Args:
        g (Graph): The graph to add the flow to.
        space (Space): The space that has the number's variable.
        slot (workers.Slot): The slot to put the flow's nodes on.
        variable (str): The name of the space's Float variable that holds
            the number, as in getattr(space, variable).
        scale (float): The lowest drum's digits per unit of the number,
            e.g. 100 when the lowest drum shows hundredths.
        held (Any): A Bool expression that is true while the number is
            being set, such as while a crank is held. While it is false,
            the flow sets the number to the detent. None leaves the number
            alone.
        threshold (float): How far the number goes from the detent, in
            digits, before the detent moves. It is more than 0.5.
        creep (float): The fraction of the way from the detent to the
            number that the drums lean before they snap.
        rate (float): The rate of each smoothing stage, per second.
        name (str): The prefix of the variables' names.

    Returns:
        The smoothed position, in digits of the lowest drum, to pass to
        drum_turns.

    Raises:
        ValueError: threshold is 0.5 or less, which would make the drums
            snap back after each snap.
    """
    if threshold <= 0.5:
        raise ValueError(f"A threshold of {threshold} digits would snap back after each snap.")
    lag, position = f"{name}_lag", f"{name}_position"
    setattr(space, name, space.FloatModelVar(name))
    setattr(space, lag, space.FloatModelVar(lag))
    setattr(space, position, space.FloatModelVar(position))

    def var(attribute: str) -> Any:
        """Returns the space's variable with the attribute name."""
        return getattr(space, attribute)

    with g.Under(slot):
        n = var(variable) * scale
        with g.If(abs(n - var(name)) > threshold):
            setattr(space, name, dm.round_(n))
        if held is not None:
            with g.If(~held & (abs(n - var(name)) > _ON_DETENT)):
                setattr(space, variable, var(name) / scale)
        target = var(name) + creep * (n - var(name))
        step = dm.clamp01(time.delta_time() * rate)
        setattr(space, lag, var(lag) + (target - var(lag)) * step)
        setattr(space, position, var(position) + (var(lag) - var(position)) * step)
    return var(position)
