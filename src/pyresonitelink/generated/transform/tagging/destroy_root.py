"""Generated component: DestroyRoot."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idestroy_root import IDestroyRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyRoot(GeneratedComponent, IDestroyRoot, IWorldEventReceiver):
    """The Destroy Root component marks the slot tagged with the component where an object's root is for destroying grabbed objects if the game cannot find an object root component above the grabbed object.

Keep in mind, the grabber checks for object roots and destroy roots after releasing the object, which depending on the object and it's position will put it back where it was before it was grabbed. meaning this component can destroy the root object if a sub grabbed object is destroyed.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyRoot"

    pass

