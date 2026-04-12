"""Generated component: LegacySettingsData."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacySettingsData(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Legacy Settings Data component was used in the old settings menu before the settings were updated in the settings update series.

    Not used directly by the user. Used in legacy content.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacySettingsData"

    pass

