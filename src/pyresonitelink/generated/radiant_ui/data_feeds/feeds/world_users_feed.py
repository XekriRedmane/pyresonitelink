"""Generated component: WorldUsersFeed."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idata_feed_component import IDataFeedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldUsersFeed(GeneratedComponent, IDataFeedComponent, IComponent, IWorldEventReceiver):
    """The WorldUsersFeed can be used to build systems that need a list of users currently in the session.

    Category: Radiant UI/Data Feeds/Feeds
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldUsersFeed"

    pass

