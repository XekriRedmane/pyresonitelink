"""Generated component: TrackingOffsetCompensator."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrackingOffsetCompensator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TrackingOffsetCompensator counteracts changes to tracking offset to all trackers at once, so this one doesn't move when all others do. usually due to a tracking offset component or seated mode.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackingOffsetCompensator"

    pass

