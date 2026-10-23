"""The local user's keyboard in Dergflux expressions.

Each function reads the keyboard of the machine that evaluates the node,
through ProtoFlux's KeyHeld, KeyPressed, and KeyReleased nodes. They read
false while a text field has the keyboard (FrooxEngineContext's
CanReadKeyboard), so typing in a field doesn't trigger them.

    with g.If(keyboard.pressed("Backspace")):
        ...

In desktop mode Resonite binds a number of keys itself, among them W, A,
S, D, Space, Shift, Control, Alt, E, F, R, T, C, X, Z, Y, V, I, M, P,
Escape, Delete, the arrow keys, PageUp, and PageDown
(KeyboardAndMouseBindingGenerator). Tab and Backspace are not among
them.
"""

from pyresonitelink.data import primitives
from pyresonitelink.dergflux import _expr
from pyresonitelink.generated._enums import key as _key

KEY_TYPE = "[Renderite.Shared]Renderite.Shared.Key"
_MODULE = "protoflux.devices.keyboard"


def key(name: str | _key.Key) -> _expr.ExprProxy:
    """Returns a Key constant, for the inputs of the keyboard nodes.

    Args:
        name: The key, as a Key member or as its name in Resonite, such
            as "Tab" or "Backspace".

    Raises:
        ValueError: There is no key by that name.
    """
    value = _key.Key(name)
    return _expr.ExprProxy(_expr.EnumConstNode(KEY_TYPE, value.value, _key.Key))


def _status(class_name: str, name: str | _key.Key) -> _expr.ExprProxy:
    """Returns the Bool output of one of the keyboard nodes for a key."""
    return _expr.node_output(
        {"Key": key(name)}, primitives.Bool, module=_MODULE, class_name=class_name,
    )


def held(name: str | _key.Key) -> _expr.ExprProxy:
    """Returns a Bool that is true while a key is down."""
    return _status("KeyHeld", name)


def pressed(name: str | _key.Key) -> _expr.ExprProxy:
    """Returns a Bool that is true in the update in which a key went down."""
    return _status("KeyPressed", name)


def released(name: str | _key.Key) -> _expr.ExprProxy:
    """Returns a Bool that is true in the update in which a key came up."""
    return _status("KeyReleased", name)
