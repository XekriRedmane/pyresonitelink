"""Generated component: DynamicBonePlayerColliders."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBonePlayerColliders(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This component is used in the Resonite hair dryer, and allows for dynamic bone colliders specified in the ``Colliders`` list to automatically collide with Dynamic Bone Chains. 

Can also be used in disabling the automatic dynamic bone colliders that Resonite generates incase you want to manually specify them.

    Category: Physics/Dynamic Bones

    **Behavior**: Only works while the component has an active user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBonePlayerColliders"

    def __init__(self, visualize_colliders: primitives.Bool | None = None, disable_default_head_colliders: primitives.Bool | None = None, disable_default_body_colliders: primitives.Bool | None = None, disable_default_left_hand_colliders: primitives.Bool | None = None, disable_default_right_hand_colliders: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            visualize_colliders: Initial value for VisualizeColliders.
            disable_default_head_colliders: Initial value for DisableDefaultHeadColliders.
            disable_default_body_colliders: Initial value for DisableDefaultBodyColliders.
            disable_default_left_hand_colliders: Initial value for DisableDefaultLeftHandColliders.
            disable_default_right_hand_colliders: Initial value for DisableDefaultRightHandColliders.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if visualize_colliders is not None:
            self.visualize_colliders = visualize_colliders
        if disable_default_head_colliders is not None:
            self.disable_default_head_colliders = disable_default_head_colliders
        if disable_default_body_colliders is not None:
            self.disable_default_body_colliders = disable_default_body_colliders
        if disable_default_left_hand_colliders is not None:
            self.disable_default_left_hand_colliders = disable_default_left_hand_colliders
        if disable_default_right_hand_colliders is not None:
            self.disable_default_right_hand_colliders = disable_default_right_hand_colliders

    @property
    def visualize_colliders(self) -> primitives.Bool | None:
        """Visualize all the colliders in ``Colliders`` that are currently colliding against a Dynamic Bone Chain. Automatically updates the collider visuals every frame server side."""
        member = self.get_member("VisualizeColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visualize_colliders.setter
    def visualize_colliders(self, value: primitives.Bool) -> None:
        """Set the VisualizeColliders field value."""
        member = self.get_member("VisualizeColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualizeColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_head_colliders(self) -> primitives.Bool | None:
        """Whether to not use the default head collider made by the engine."""
        member = self.get_member("DisableDefaultHeadColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_head_colliders.setter
    def disable_default_head_colliders(self, value: primitives.Bool) -> None:
        """Set the DisableDefaultHeadColliders field value."""
        member = self.get_member("DisableDefaultHeadColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultHeadColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_body_colliders(self) -> primitives.Bool | None:
        """Whether to not use the body colliders made by the engine."""
        member = self.get_member("DisableDefaultBodyColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_body_colliders.setter
    def disable_default_body_colliders(self, value: primitives.Bool) -> None:
        """Set the DisableDefaultBodyColliders field value."""
        member = self.get_member("DisableDefaultBodyColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultBodyColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_left_hand_colliders(self) -> primitives.Bool | None:
        """Whether to not use the left hand collider made by the engine."""
        member = self.get_member("DisableDefaultLeftHandColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_left_hand_colliders.setter
    def disable_default_left_hand_colliders(self, value: primitives.Bool) -> None:
        """Set the DisableDefaultLeftHandColliders field value."""
        member = self.get_member("DisableDefaultLeftHandColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultLeftHandColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_right_hand_colliders(self) -> primitives.Bool | None:
        """Whether to not use the right hand collider made by the engine."""
        member = self.get_member("DisableDefaultRightHandColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_right_hand_colliders.setter
    def disable_default_right_hand_colliders(self, value: primitives.Bool) -> None:
        """Set the DisableDefaultRightHandColliders field value."""
        member = self.get_member("DisableDefaultRightHandColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultRightHandColliders", fields.FieldBool(value=value)
            )

    @property
    def colliders(self) -> members.SyncList | None:
        """A list of colliders to enable collision for all Dynamic bone chains in a world."""
        member = self.get_member("Colliders")
        if isinstance(member, members.SyncList):
            return member
        return None

    @colliders.setter
    def colliders(self, value: members.SyncList) -> None:
        """Set Colliders. A list of colliders to enable collision for all Dynamic bone chains in a world."""
        self.set_member("Colliders", value)

