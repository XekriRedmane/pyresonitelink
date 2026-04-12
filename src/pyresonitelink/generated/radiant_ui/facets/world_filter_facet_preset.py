"""Generated component: WorldFilterFacetPreset."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldFilterFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The WorldFilterFacetPreset component loads the World Filter facet when it's not ``_fullyLoaded``. It does this by loading the facet from the cloud, and using that loaded data to make the preset

    Category: Radiant UI/Facets

    used in the main dash. no need to be used by the user unless they are
    missing the World Filter facet.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldFilterFacetPreset"

    pass

