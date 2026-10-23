"""Users in Dergflux expressions.

A flow driven by Update runs on every user's machine, and each machine
writes what its own run computes. A flow that moves something, such as a
simulated ball, should run on one machine only, and the host's is the
usual choice.

    with g.Under(slot):
        with g.If(users.local_user_is_host()):
            ...
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr
from pyresonitelink.generated._types import user


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
