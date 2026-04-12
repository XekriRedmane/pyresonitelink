"""Generated component: ClipboardImporter."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ClipboardImporter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Clipboard importer is used by the game as a manager for pasting items and text from the clipboard. Without it, pasting text isn't possible in a world until it is added back to the world.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ClipboardImporter"

    pass

