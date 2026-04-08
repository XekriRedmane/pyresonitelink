"""Generated component: LegacyRadioGroup."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.legacy_radio import LegacyRadio
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.iradio_group import IRadioGroup
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyRadioGroup(GeneratedComponent, IRadioGroup, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyRadioGroup.

    Category: UI/Physical
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyRadioGroup"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: bool | None = None, accept_remote_touch: bool | None = None, is_enabled: bool | None = None, selected_option: str | LegacyRadio | None = None, choice_visual: str | Slot | None = None, choice_position: str | IField[primitives.Float3] | None = None, choice_rotation: str | IField[primitives.FloatQ] | None = None, choice_scale: str | IField[primitives.Float3] | None = None, choice_material: str | PBS_RimMetallic | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            is_enabled: Initial value for IsEnabled.
            selected_option: Initial value for _selectedOption.
            choice_visual: Initial value for _choiceVisual.
            choice_position: Initial value for _choicePosition.
            choice_rotation: Initial value for _choiceRotation.
            choice_scale: Initial value for _choiceScale.
            choice_material: Initial value for _choiceMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if selected_option is not None:
            self.selected_option = selected_option
        if choice_visual is not None:
            self.choice_visual = choice_visual
        if choice_position is not None:
            self.choice_position = choice_position
        if choice_rotation is not None:
            self.choice_rotation = choice_rotation
        if choice_scale is not None:
            self.choice_scale = choice_scale
        if choice_material is not None:
            self.choice_material = choice_material

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets LegacyUIStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the Style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def accept_physical_touch(self) -> bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def is_enabled(self) -> bool | None:
        """The IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        """Set the IsEnabled field value."""
        member = self.get_member("IsEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsEnabled", fields.FieldBool(value=value)
            )

    @property
    def selected_option(self) -> str | None:
        """Target ID of the _selectedOption reference (targets LegacyRadio)."""
        member = self.get_member("_selectedOption")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_option.setter
    def selected_option(self, target: str | LegacyRadio | None) -> None:
        """Set the _selectedOption reference by target ID or LegacyRadio instance."""
        target_id: str | None = target.id if isinstance(target, LegacyRadio) else target  # type: ignore[assignment]
        member = self.get_member("_selectedOption")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selectedOption",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyRadio'),
            )

    @property
    def choice_visual(self) -> str | None:
        """Target ID of the _choiceVisual reference (targets Slot)."""
        member = self.get_member("_choiceVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @choice_visual.setter
    def choice_visual(self, target: str | Slot | None) -> None:
        """Set the _choiceVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_choiceVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_choiceVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def choice_position(self) -> str | None:
        """Target ID of the _choicePosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_choicePosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @choice_position.setter
    def choice_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _choicePosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_choicePosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_choicePosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def choice_rotation(self) -> str | None:
        """Target ID of the _choiceRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_choiceRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @choice_rotation.setter
    def choice_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _choiceRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_choiceRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_choiceRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def choice_scale(self) -> str | None:
        """Target ID of the _choiceScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_choiceScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @choice_scale.setter
    def choice_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _choiceScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_choiceScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_choiceScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def choice_material(self) -> str | None:
        """Target ID of the _choiceMaterial reference (targets PBS_RimMetallic)."""
        member = self.get_member("_choiceMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @choice_material.setter
    def choice_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _choiceMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_choiceMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_choiceMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

