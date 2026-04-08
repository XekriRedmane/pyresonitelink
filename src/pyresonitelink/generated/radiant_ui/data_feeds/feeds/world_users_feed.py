"""Generated component: WorldUsersFeed."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldUsersFeed(GeneratedComponent, IDataFeedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldUsersFeed.

    Category: Radiant UI/Data Feeds/Feeds
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldUsersFeed"

    pass

