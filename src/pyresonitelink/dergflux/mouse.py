"""The local user's mouse in Dergflux expressions.

Each function reads the mouse of the machine that evaluates the node,
through ProtoFlux's mouse nodes, which read Resonite's input directly.
They see every click, including one that the laser also delivers to
whatever is under the crosshair, and one in the dash. A flow that acts on
the mouse should run on one user's machine only, and should usually
ignore the mouse while that user's dash is open (users.is_dash_open).

pressed and released are true in the one engine update in which the
button went down or came up, and held is true in every update in
between.

    with g.If(mouse.left_pressed() & ~users.is_dash_open(users.local_user())):
        ...

In desktop mode, Resonite itself uses the left button to press and use
things under the laser, the right button to grab, and the middle button
to open the context menu (KeyboardAndMouseBindingGenerator).
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr

_MODULE = "protoflux.devices.mouse"


def _button(class_name: str) -> _expr.ExprProxy:
    """Returns the Bool output of one of the mouse button nodes."""
    return _expr.node_output({}, primitives.Bool, module=_MODULE, class_name=class_name)


def left_pressed() -> _expr.ExprProxy:
    """Returns a Bool that is true in the update in which the left button went down."""
    return _button("LeftMousePressed")


def left_held() -> _expr.ExprProxy:
    """Returns a Bool that is true while the left button is down."""
    return _button("LeftMouseHeld")


def left_released() -> _expr.ExprProxy:
    """Returns a Bool that is true in the update in which the left button came up."""
    return _button("LeftMouseReleased")


def right_pressed() -> _expr.ExprProxy:
    """Returns a Bool that is true in the update in which the right button went down."""
    return _button("RightMousePressed")


def right_held() -> _expr.ExprProxy:
    """Returns a Bool that is true while the right button is down."""
    return _button("RightMouseHeld")


def right_released() -> _expr.ExprProxy:
    """Returns a Bool that is true in the update in which the right button came up."""
    return _button("RightMouseReleased")


def scroll_delta() -> _expr.ExprProxy:
    """Returns how far the scroll wheel turned in this update, a Float.

    It is positive for a turn away from the user. Its unit is the
    platform's, and it isn't known how many units one notch gives, so a
    flow that counts notches should act on the update in which the
    scrolling starts.
    """
    return _expr.node_output({}, primitives.Float, module=_MODULE, class_name="MouseScrollDelta")
