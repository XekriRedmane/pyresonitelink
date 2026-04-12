"""Generated component: ChildrenSaveBlocker."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ChildrenSaveBlocker(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ChildrenSaveBlocker component prevents the slot's children from being saved with the slot.

    Category: Utility

    When attached to a slot, the children of the slot will not be saved when
    the slot is part of an item being saved. The slot itself will still be
    saved.

    **See also**: * GrabbableSaveBlock for blocking saves of grabbable items.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ChildrenSaveBlocker"

    pass

