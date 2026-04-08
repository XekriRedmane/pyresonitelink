"""Generated component: DynamicBonePlayerColliders."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBonePlayerColliders(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicBonePlayerColliders.

    Category: Physics/Dynamic Bones
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBonePlayerColliders"

    def __init__(self, visualize_colliders: bool | None = None, disable_default_head_colliders: bool | None = None, disable_default_body_colliders: bool | None = None, disable_default_left_hand_colliders: bool | None = None, disable_default_right_hand_colliders: bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def visualize_colliders(self) -> bool | None:
        """The VisualizeColliders field value."""
        member = self.get_member("VisualizeColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visualize_colliders.setter
    def visualize_colliders(self, value: bool) -> None:
        """Set the VisualizeColliders field value."""
        member = self.get_member("VisualizeColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualizeColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_head_colliders(self) -> bool | None:
        """The DisableDefaultHeadColliders field value."""
        member = self.get_member("DisableDefaultHeadColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_head_colliders.setter
    def disable_default_head_colliders(self, value: bool) -> None:
        """Set the DisableDefaultHeadColliders field value."""
        member = self.get_member("DisableDefaultHeadColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultHeadColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_body_colliders(self) -> bool | None:
        """The DisableDefaultBodyColliders field value."""
        member = self.get_member("DisableDefaultBodyColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_body_colliders.setter
    def disable_default_body_colliders(self, value: bool) -> None:
        """Set the DisableDefaultBodyColliders field value."""
        member = self.get_member("DisableDefaultBodyColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultBodyColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_left_hand_colliders(self) -> bool | None:
        """The DisableDefaultLeftHandColliders field value."""
        member = self.get_member("DisableDefaultLeftHandColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_left_hand_colliders.setter
    def disable_default_left_hand_colliders(self, value: bool) -> None:
        """Set the DisableDefaultLeftHandColliders field value."""
        member = self.get_member("DisableDefaultLeftHandColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableDefaultLeftHandColliders", fields.FieldBool(value=value)
            )

    @property
    def disable_default_right_hand_colliders(self) -> bool | None:
        """The DisableDefaultRightHandColliders field value."""
        member = self.get_member("DisableDefaultRightHandColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_default_right_hand_colliders.setter
    def disable_default_right_hand_colliders(self, value: bool) -> None:
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
        """The Colliders member."""
        member = self.get_member("Colliders")
        if isinstance(member, members.SyncList):
            return member
        return None

    @colliders.setter
    def colliders(self, value: members.SyncList) -> None:
        """Set the Colliders member."""
        self.set_member("Colliders", value)

