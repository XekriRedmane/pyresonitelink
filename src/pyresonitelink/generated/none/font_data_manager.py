"""Generated component: FontDataManager."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FontDataManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The FontDataManager component handles the mapping of Font data and parameters to font based materials during rendering.

    Not used by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FontDataManager"

    pass

