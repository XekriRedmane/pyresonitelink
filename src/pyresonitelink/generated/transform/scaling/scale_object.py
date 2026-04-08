"""Generated component: ScaleObject."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.scale_object_manager import ScaleObjectManager
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleObject(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaleObject.

    Category: Transform/Scaling
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleObject"

    def __init__(self, manager: str | ScaleObjectManager | None = None, scale_power: primitives.Float | None = None, scale_position: primitives.Float3 | None = None, override_far_transition_offset: primitives.Float3 | None = None, custom_transition: primitives.Bool | None = None, transition_lerp: primitives.Float | None = None, active: str | IField[primitives.Bool] | None = None, position: str | IField[primitives.Float3] | None = None, scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            manager: Initial value for Manager.
            scale_power: Initial value for ScalePower.
            scale_position: Initial value for ScalePosition.
            override_far_transition_offset: Initial value for OverrideFarTransitionOffset.
            custom_transition: Initial value for CustomTransition.
            transition_lerp: Initial value for TransitionLerp.
            active: Initial value for _active.
            position: Initial value for _position.
            scale: Initial value for _scale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if manager is not None:
            self.manager = manager
        if scale_power is not None:
            self.scale_power = scale_power
        if scale_position is not None:
            self.scale_position = scale_position
        if override_far_transition_offset is not None:
            self.override_far_transition_offset = override_far_transition_offset
        if custom_transition is not None:
            self.custom_transition = custom_transition
        if transition_lerp is not None:
            self.transition_lerp = transition_lerp
        if active is not None:
            self.active = active
        if position is not None:
            self.position = position
        if scale is not None:
            self.scale = scale

    @property
    def manager(self) -> str | None:
        """Target ID of the Manager reference (targets ScaleObjectManager)."""
        member = self.get_member("Manager")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @manager.setter
    def manager(self, target: str | ScaleObjectManager | None) -> None:
        """Set the Manager reference by target ID or ScaleObjectManager instance."""
        target_id: str | None = target.id if isinstance(target, ScaleObjectManager) else target  # type: ignore[assignment]
        member = self.get_member("Manager")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Manager",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScaleObjectManager'),
            )

    @property
    def scale_power(self) -> primitives.Float | None:
        """The ScalePower field value."""
        member = self.get_member("ScalePower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_power.setter
    def scale_power(self, value: primitives.Float) -> None:
        """Set the ScalePower field value."""
        member = self.get_member("ScalePower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScalePower", fields.FieldFloat(value=value)
            )

    @property
    def scale_position(self) -> primitives.Float3 | None:
        """The ScalePosition field value."""
        member = self.get_member("ScalePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_position.setter
    def scale_position(self, value: primitives.Float3) -> None:
        """Set the ScalePosition field value."""
        member = self.get_member("ScalePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScalePosition", fields.FieldFloat3(value=value)
            )

    @property
    def override_far_transition_offset(self) -> primitives.Float3 | None:
        """The OverrideFarTransitionOffset field value."""
        member = self.get_member("OverrideFarTransitionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_far_transition_offset.setter
    def override_far_transition_offset(self, value: primitives.Float3) -> None:
        """Set the OverrideFarTransitionOffset field value."""
        member = self.get_member("OverrideFarTransitionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideFarTransitionOffset", fields.FieldNullableFloat3(value=value)
            )

    @property
    def custom_transition(self) -> primitives.Bool | None:
        """The CustomTransition field value."""
        member = self.get_member("CustomTransition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @custom_transition.setter
    def custom_transition(self, value: primitives.Bool) -> None:
        """Set the CustomTransition field value."""
        member = self.get_member("CustomTransition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CustomTransition", fields.FieldBool(value=value)
            )

    @property
    def transition_lerp(self) -> primitives.Float | None:
        """The TransitionLerp field value."""
        member = self.get_member("TransitionLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_lerp.setter
    def transition_lerp(self, value: primitives.Float) -> None:
        """Set the TransitionLerp field value."""
        member = self.get_member("TransitionLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TransitionLerp", fields.FieldFloat(value=value)
            )

    @property
    def active(self) -> str | None:
        """Target ID of the _active reference (targets IField[primitives.Bool])."""
        member = self.get_member("_active")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active.setter
    def active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _active reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_active")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_active",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def position(self) -> str | None:
        """Target ID of the _position reference (targets IField[primitives.Float3])."""
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def scale(self) -> str | None:
        """Target ID of the _scale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

