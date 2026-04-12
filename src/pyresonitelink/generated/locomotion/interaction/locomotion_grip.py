"""Generated component: LocomotionGrip."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionGrip(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocomotionGrip component controls if users can climb on a collider hierarchy. 

For some locomotions, colliders have to specifically be tagged as being climbable. In these cases, this component is used for that purpose.

    Category: Locomotion/Interaction

    While this component is enabled on a slot the hierarchy will be
    climbable, while this component is disabled on a slot the hierarchy will
    not be climbable even if climbing is enabled by default in the
    locomotion.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionGrip"

    pass

