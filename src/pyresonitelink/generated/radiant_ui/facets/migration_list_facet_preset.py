"""Generated component: MigrationListFacetPreset."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MigrationListFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The MigrationListFacetPreset component loads the Migration List facet when it's not ``_fullyLoaded``. It does this by loading the facet from the cloud, and using that loaded data to make the preset

    Category: Radiant UI/Facets

    used in the main dash. no need to be used by the user unless they are
    missing the Migration List facet.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MigrationListFacetPreset"

    pass

