"""Generated component: MigrationDetailFacetPreset."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MigrationDetailFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The MigrationDetailFacetPreset component loads the Migration Detail facet when it's not ``_fullyLoaded``. It does this by loading the facet from the cloud, and using that loaded data to make the preset

    Category: Radiant UI/Facets

    used in the main dash. no need to be used by the user unless they are
    missing the Migration Detail facet.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MigrationDetailFacetPreset"

    pass

