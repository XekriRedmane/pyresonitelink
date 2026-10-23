"""Finds the user's head, and places things in front of it.

The user's head is the "Head" slot under the user's root slot, which is the
child of Root that has a UserRoot component. If several users are in the
session, find_head and in_front_of_head use the first user root under Root.

A typical use places a new slot 2 m in front of the head, facing the head,
with slots.add_slot_at.

    world = await placement.in_front_of_head(resolink, 2.0, turn=placement.HALF_TURN)
    slot = await slots.add_slot_at(resolink, world, name="Example")
"""

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import transforms
from pyresonitelink.data import workers

USER_ROOT_TYPE = "[FrooxEngine]FrooxEngine.UserRoot"

# Half a turn about Y. Turning a transform from in_front_of_head by this
# makes its +Z axis point back at the head.
HALF_TURN = primitives.FloatQ(0, 1, 0, 0)


async def find_head(resolink: client.Client) -> str:
    """Finds the slot ID of the first user's head.

    Args:
        resolink (client.Client): The connected client.

    Returns:
        The ID of the user root's child named "Head".

    Raises:
        LookupError: No user root or no head slot was found.
    """
    root = (await resolink.get_slot(workers.Slot.ROOT_SLOT_ID, depth=1)).data
    assert root is not None
    # Without includeComponentData, the children still list their
    # components' types.
    user_root = next(
        (child for child in root.children
         if any(c.componentType == USER_ROOT_TYPE for c in child.components)),
        None,
    )
    if user_root is None:
        raise LookupError("No child of Root has a UserRoot component.")
    assert user_root.id is not None
    user = (await resolink.get_slot(user_root.id, depth=1)).data
    assert user is not None
    for child in user.children:
        if child.name is not None and child.name.value == "Head":
            assert child.id is not None
            return child.id
    raise LookupError(f"The user root {user_root.id} has no Head slot.")


async def in_front_of_head(
    resolink: client.Client,
    distance: float,
    *,
    turn: primitives.FloatQ | None = None,
    scale: float = 1.0,
) -> transforms.Transform:
    """Returns a world transform at a distance in front of the first user's head.

    The transform's axes are the head's axes, turned by turn if it is given.
    +Z is forward in Resonite, so without a turn the transform's +Z axis
    points away from the head, and with HALF_TURN it points back at it.

    Args:
        resolink (client.Client): The connected client.
        distance (float): How far in front of the head, in meters, along
            the head's +Z axis.
        turn (primitives.FloatQ | None): A rotation applied after the
            head's, i.e. about the transform's own axes, or None for none.
        scale (float): The transform's uniform scale in world space.

    Returns:
        The transform, in world space.

    Raises:
        LookupError: The head wasn't found (see find_head).
    """
    head = await resolink.get_global_transform(await find_head(resolink))
    forward = transforms.rotate(head.rotation, primitives.Float3(0, 0, 1))
    return transforms.Transform(
        position=primitives.Float3(
            head.position.x + distance * forward.x,
            head.position.y + distance * forward.y,
            head.position.z + distance * forward.z,
        ),
        rotation=head.rotation if turn is None else transforms.multiply(head.rotation, turn),
        scale=primitives.Float3(scale, scale, scale),
    )

