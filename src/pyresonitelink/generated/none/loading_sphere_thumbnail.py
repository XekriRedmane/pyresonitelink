"""Generated component: LoadingSphereThumbnail."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LoadingSphereThumbnail(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Loading Sphere Thumbnail component is used to provide a texture for when the thumbnail for the preview of a world is not yet made or is still loading.

    Not used by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LoadingSphereThumbnail"

    pass

