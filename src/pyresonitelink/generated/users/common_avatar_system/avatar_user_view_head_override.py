"""Generated component: AvatarUserViewHeadOverride."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.render_transform_override import RenderTransformOverride
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.nullable import Nullable
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserViewHeadOverride(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserViewHeadOverride.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserViewHeadOverride"

    def __init__(self, render_transform_override: str | RenderTransformOverride | None = None, override_enabled: str | IField[primitives.Bool] | None = None, pos_override: str | IField[Nullable[primitives.Float3]] | None = None, rot_override: str | IField[Nullable[primitives.FloatQ]] | None = None, equipping_slot: str | AvatarObjectSlot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            render_transform_override: Initial value for RenderTransformOverride.
            override_enabled: Initial value for _overrideEnabled.
            pos_override: Initial value for _posOverride.
            rot_override: Initial value for _rotOverride.
            equipping_slot: Initial value for _equippingSlot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if render_transform_override is not None:
            self.render_transform_override = render_transform_override
        if override_enabled is not None:
            self.override_enabled = override_enabled
        if pos_override is not None:
            self.pos_override = pos_override
        if rot_override is not None:
            self.rot_override = rot_override
        if equipping_slot is not None:
            self.equipping_slot = equipping_slot

    @property
    def render_transform_override(self) -> str | None:
        """Target ID of the RenderTransformOverride reference (targets RenderTransformOverride)."""
        member = self.get_member("RenderTransformOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_transform_override.setter
    def render_transform_override(self, target: str | RenderTransformOverride | None) -> None:
        """Set the RenderTransformOverride reference by target ID or RenderTransformOverride instance."""
        target_id: str | None = target.id if isinstance(target, RenderTransformOverride) else target  # type: ignore[assignment]
        member = self.get_member("RenderTransformOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RenderTransformOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RenderTransformOverride'),
            )

    @property
    def override_enabled(self) -> str | None:
        """Target ID of the _overrideEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_overrideEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_enabled.setter
    def override_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _overrideEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_overrideEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overrideEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def pos_override(self) -> str | None:
        """Target ID of the _posOverride reference (targets IField[Nullable[primitives.Float3]])."""
        member = self.get_member("_posOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pos_override.setter
    def pos_override(self, target: str | IField[Nullable[primitives.Float3]] | None) -> None:
        """Set the _posOverride reference by target ID or IField[Nullable[primitives.Float3]] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_posOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_posOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Nullable<float3>>'),
            )

    @property
    def rot_override(self) -> str | None:
        """Target ID of the _rotOverride reference (targets IField[Nullable[primitives.FloatQ]])."""
        member = self.get_member("_rotOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rot_override.setter
    def rot_override(self, target: str | IField[Nullable[primitives.FloatQ]] | None) -> None:
        """Set the _rotOverride reference by target ID or IField[Nullable[primitives.FloatQ]] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Nullable<floatQ>>'),
            )

    @property
    def equipping_slot(self) -> str | None:
        """Target ID of the _equippingSlot reference (targets AvatarObjectSlot)."""
        member = self.get_member("_equippingSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipping_slot.setter
    def equipping_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the _equippingSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("_equippingSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_equippingSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

