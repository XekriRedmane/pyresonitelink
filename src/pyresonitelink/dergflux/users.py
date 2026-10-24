"""Users in Dergflux expressions.

A flow driven by Update runs on every user's machine, and each machine
writes what its own run computes. A flow that moves something, such as a
simulated ball, should run on one machine only, and the host's is the
usual choice.

    with g.Under(slot):
        with g.If(users.local_user_is_host()):
            ...

A flow that reads one user's input, such as the mouse, runs on that
user's machine. A model variable can hold that user's machine ID, and
the flow can compare it with the local user's, so that only that
machine runs the flow.

    with g.If(s.player == users.machine_id(users.local_user())):
        ...
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr
from pyresonitelink.generated._types import user
from pyresonitelink.generated._types import user_root as _user_root


def local_user() -> _expr.ExprProxy:
    """Returns the user whose machine evaluates the node, a User expression."""
    return _expr.node_output({}, user.User, module="protoflux.users", class_name="LocalUser")


def is_host(u: object) -> _expr.ExprProxy:
    """Returns a Bool that is true if a user is the session's host.

    Args:
        u: The user, as a User expression such as local_user().
    """
    return _expr.node_output(
        {"User": u}, primitives.Bool,
        module="protoflux.users.status", class_name="IsUserHost",
    )


def local_user_is_host() -> _expr.ExprProxy:
    """Returns a Bool that is true on the host's machine and false on the others."""
    return is_host(local_user())


def machine_id(u: object) -> _expr.ExprProxy:
    """Returns the ID of the machine that a user joined from, a String.

    Each user in a session has a different machine ID, including a user
    who isn't signed in and so has no user ID.

    Args:
        u: The user, as a User expression such as local_user().
    """
    return _expr.node_output(
        {"User": u}, primitives.String,
        module="protoflux.users", class_name="UserMachineID",
    )


def is_vr_active(u: object) -> _expr.ExprProxy:
    """Returns a Bool that is true while a user is in VR, and false in desktop mode.

    Args:
        u: The user, as a User expression such as local_user().
    """
    return _expr.node_output(
        {"User": u}, primitives.Bool,
        module="protoflux.users.info", class_name="UserVR_Active",
    )


def is_dash_open(u: object) -> _expr.ExprProxy:
    """Returns a Bool that is true while a user's dash is open.

    In desktop mode the dash frees the cursor, and the mouse buttons
    then click in the dash.

    Args:
        u: The user, as a User expression such as local_user().
    """
    return _expr.node_output(
        {"User": u}, primitives.Bool,
        module="protoflux.users.status", class_name="IsAppDashOpened",
    )


def view_position() -> _expr.ExprProxy:
    """Returns the local user's view position in world space, a Float3.

    In desktop mode this is the camera's position. Each machine computes
    its own user's view.
    """
    return _expr.node_output(
        {}, primitives.Float3, module="protoflux.users.local_output", class_name="ViewPosition",
    )


def view_rotation() -> _expr.ExprProxy:
    """Returns the local user's view rotation in world space, a FloatQ.

    The view looks along +Z of this rotation, so in desktop mode the
    crosshair is on the ray along view_rotation() * (0, 0, 1).
    """
    return _expr.node_output(
        {}, primitives.FloatQ, module="protoflux.users.local_output", class_name="ViewRotation",
    )


def desktop_fov() -> _expr.ExprProxy:
    """Returns the local user's desktop field of view, a Float in degrees.

    It is the vertical angle of the view, and the window's aspect ratio
    sets the horizontal one (MathX.UVToPerspectiveCameraDirection). It
    is 75 by default, and Resonite keeps it from 0.0001 to 179. In VR it
    is still the desktop setting, which a headset doesn't use.
    """
    return _expr.node_output(
        {}, primitives.Float, module="protoflux.users.local_output", class_name="DesktopFOV",
    )


def window_resolution() -> _expr.ExprProxy:
    """Returns the size of the local machine's Resonite window in pixels, an Int2.

    The aspect ratio of the desktop view is its x over its y.
    """
    return _expr.node_output(
        {}, primitives.Int2, module="protoflux.devices.display", class_name="LocalWindowResolution",
    )


def username(u: object) -> _expr.ExprProxy:
    """Returns a user's name, a String, or null for a null user.

    Args:
        u: The user, as a User expression such as local_user().
    """
    return _expr.node_output(
        {"User": u}, primitives.String,
        module="protoflux.users", class_name="UserUsername",
    )


def local_user_root() -> _expr.ExprProxy:
    """Returns the local user's UserRoot, for g.SetFeetPosition."""
    return _expr.node_output(
        {}, _user_root.UserRoot, module="protoflux.users", class_name="LocalUserRoot",
    )
