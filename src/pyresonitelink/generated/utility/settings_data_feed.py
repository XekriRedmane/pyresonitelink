"""Generated component: SettingsDataFeed."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SettingsDataFeed(GeneratedComponent, IDataFeedComponent, IComponent, IWorldEventReceiver):
    """The SettingsDataFeed component is a data feed that generates a list of settings and their categories.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SettingsDataFeed"

    pass

