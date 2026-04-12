"""Generated component: LocomotionAnimationColliderBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionAnimationColliderBlock(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This component can be used in combination with the LocomotionAnimationBodyCollider component to control which colliders on an avatar should be avoided by the avatar's hands.

    Category: Users/Common Avatar System/Animation

    Add this component to the top of a hierarchy of any colliders on your
    avatar that you don't want your hands colliding with. This component can
    also be added to environment colliders if you want feet collisions to
    ignore them.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionAnimationColliderBlock"

    pass

