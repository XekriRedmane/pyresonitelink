"""Generated component: LegacyColorDialog."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.legacy_slider import LegacySlider
from pyresonitelink.generated._types.color_wheel_triangle_mesh import ColorWheelTriangleMesh
from pyresonitelink.generated._types.legacy_button import LegacyButton
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.ivalue_source import IValueSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyColorDialog(GeneratedComponent, IValueSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyColorDialog.

    Category: UI/Dialogs
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyColorDialog"

    def __init__(self, realtime: bool | None = None, target_field: str | IField[primitives.ColorX] | None = None, original_color: primitives.ColorX | None = None, hue: np.float32 | None = None, saturation: np.float32 | None = None, value: np.float32 | None = None, alpha: np.float32 | None = None, gain: np.float32 | None = None, r_slider: str | LegacySlider | None = None, g_slider: str | LegacySlider | None = None, b_slider: str | LegacySlider | None = None, a_slider: str | LegacySlider | None = None, gain_slider: str | LegacySlider | None = None, r_value: str | IField[np.float32] | None = None, g_value: str | IField[np.float32] | None = None, b_value: str | IField[np.float32] | None = None, a_value: str | IField[np.float32] | None = None, gain_value: str | IField[np.float32] | None = None, color_wheel_mesh: str | ColorWheelTriangleMesh | None = None, ok_button: str | LegacyButton | None = None, cancel_button: str | LegacyButton | None = None, style: str | LegacyUIStyle | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            realtime: Initial value for Realtime.
            target_field: Initial value for TargetField.
            original_color: Initial value for _originalColor.
            hue: Initial value for _hue.
            saturation: Initial value for _saturation.
            value: Initial value for _value.
            alpha: Initial value for _alpha.
            gain: Initial value for _gain.
            r_slider: Initial value for _rSlider.
            g_slider: Initial value for _gSlider.
            b_slider: Initial value for _bSlider.
            a_slider: Initial value for _aSlider.
            gain_slider: Initial value for _gainSlider.
            r_value: Initial value for _rValue.
            g_value: Initial value for _gValue.
            b_value: Initial value for _bValue.
            a_value: Initial value for _aValue.
            gain_value: Initial value for _gainValue.
            color_wheel_mesh: Initial value for _colorWheelMesh.
            ok_button: Initial value for _okButton.
            cancel_button: Initial value for _cancelButton.
            style: Initial value for _style.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if realtime is not None:
            self.realtime = realtime
        if target_field is not None:
            self.target_field = target_field
        if original_color is not None:
            self.original_color = original_color
        if hue is not None:
            self.hue = hue
        if saturation is not None:
            self.saturation = saturation
        if value is not None:
            self.value = value
        if alpha is not None:
            self.alpha = alpha
        if gain is not None:
            self.gain = gain
        if r_slider is not None:
            self.r_slider = r_slider
        if g_slider is not None:
            self.g_slider = g_slider
        if b_slider is not None:
            self.b_slider = b_slider
        if a_slider is not None:
            self.a_slider = a_slider
        if gain_slider is not None:
            self.gain_slider = gain_slider
        if r_value is not None:
            self.r_value = r_value
        if g_value is not None:
            self.g_value = g_value
        if b_value is not None:
            self.b_value = b_value
        if a_value is not None:
            self.a_value = a_value
        if gain_value is not None:
            self.gain_value = gain_value
        if color_wheel_mesh is not None:
            self.color_wheel_mesh = color_wheel_mesh
        if ok_button is not None:
            self.ok_button = ok_button
        if cancel_button is not None:
            self.cancel_button = cancel_button
        if style is not None:
            self.style = style

    @property
    def realtime(self) -> bool | None:
        """The Realtime field value."""
        member = self.get_member("Realtime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @realtime.setter
    def realtime(self, value: bool) -> None:
        """Set the Realtime field value."""
        member = self.get_member("Realtime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Realtime", fields.FieldBool(value=value)
            )

    @property
    def target_field(self) -> str | None:
        """Target ID of the TargetField reference (targets IField[primitives.ColorX])."""
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the TargetField reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def original_color(self) -> primitives.ColorX | None:
        """The _originalColor field value."""
        member = self.get_member("_originalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_color.setter
    def original_color(self, value: primitives.ColorX) -> None:
        """Set the _originalColor field value."""
        member = self.get_member("_originalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalColor", fields.FieldColorX(value=value)
            )

    @property
    def hue(self) -> np.float32 | None:
        """The _hue field value."""
        member = self.get_member("_hue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hue.setter
    def hue(self, value: np.float32) -> None:
        """Set the _hue field value."""
        member = self.get_member("_hue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_hue", fields.FieldFloat(value=value)
            )

    @property
    def saturation(self) -> np.float32 | None:
        """The _saturation field value."""
        member = self.get_member("_saturation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saturation.setter
    def saturation(self, value: np.float32) -> None:
        """Set the _saturation field value."""
        member = self.get_member("_saturation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_saturation", fields.FieldFloat(value=value)
            )

    @property
    def value(self) -> np.float32 | None:
        """The _value field value."""
        member = self.get_member("_value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: np.float32) -> None:
        """Set the _value field value."""
        member = self.get_member("_value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_value", fields.FieldFloat(value=value)
            )

    @property
    def alpha(self) -> np.float32 | None:
        """The _alpha field value."""
        member = self.get_member("_alpha")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha.setter
    def alpha(self, value: np.float32) -> None:
        """Set the _alpha field value."""
        member = self.get_member("_alpha")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_alpha", fields.FieldFloat(value=value)
            )

    @property
    def profile(self) -> members.FieldEnum | None:
        """The _profile member."""
        member = self.get_member("_profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the _profile member."""
        self.set_member("_profile", value)

    @property
    def gain(self) -> np.float32 | None:
        """The _gain field value."""
        member = self.get_member("_gain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gain.setter
    def gain(self, value: np.float32) -> None:
        """Set the _gain field value."""
        member = self.get_member("_gain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_gain", fields.FieldFloat(value=value)
            )

    @property
    def r_slider(self) -> str | None:
        """Target ID of the _rSlider reference (targets LegacySlider)."""
        member = self.get_member("_rSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @r_slider.setter
    def r_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _rSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_rSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def g_slider(self) -> str | None:
        """Target ID of the _gSlider reference (targets LegacySlider)."""
        member = self.get_member("_gSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @g_slider.setter
    def g_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _gSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_gSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_gSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def b_slider(self) -> str | None:
        """Target ID of the _bSlider reference (targets LegacySlider)."""
        member = self.get_member("_bSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b_slider.setter
    def b_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _bSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_bSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def a_slider(self) -> str | None:
        """Target ID of the _aSlider reference (targets LegacySlider)."""
        member = self.get_member("_aSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a_slider.setter
    def a_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _aSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_aSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_aSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def gain_slider(self) -> str | None:
        """Target ID of the _gainSlider reference (targets LegacySlider)."""
        member = self.get_member("_gainSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gain_slider.setter
    def gain_slider(self, target: str | LegacySlider | None) -> None:
        """Set the _gainSlider reference by target ID or LegacySlider instance."""
        target_id: str | None = target.id if isinstance(target, LegacySlider) else target  # type: ignore[assignment]
        member = self.get_member("_gainSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_gainSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacySlider'),
            )

    @property
    def r_value(self) -> str | None:
        """Target ID of the _rValue reference (targets IField[np.float32])."""
        member = self.get_member("_rValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @r_value.setter
    def r_value(self, target: str | IField[np.float32] | None) -> None:
        """Set the _rValue reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def g_value(self) -> str | None:
        """Target ID of the _gValue reference (targets IField[np.float32])."""
        member = self.get_member("_gValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @g_value.setter
    def g_value(self, target: str | IField[np.float32] | None) -> None:
        """Set the _gValue reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_gValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_gValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def b_value(self) -> str | None:
        """Target ID of the _bValue reference (targets IField[np.float32])."""
        member = self.get_member("_bValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b_value.setter
    def b_value(self, target: str | IField[np.float32] | None) -> None:
        """Set the _bValue reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_bValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def a_value(self) -> str | None:
        """Target ID of the _aValue reference (targets IField[np.float32])."""
        member = self.get_member("_aValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a_value.setter
    def a_value(self, target: str | IField[np.float32] | None) -> None:
        """Set the _aValue reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_aValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_aValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def gain_value(self) -> str | None:
        """Target ID of the _gainValue reference (targets IField[np.float32])."""
        member = self.get_member("_gainValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gain_value.setter
    def gain_value(self, target: str | IField[np.float32] | None) -> None:
        """Set the _gainValue reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_gainValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_gainValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def color_wheel_mesh(self) -> str | None:
        """Target ID of the _colorWheelMesh reference (targets ColorWheelTriangleMesh)."""
        member = self.get_member("_colorWheelMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_wheel_mesh.setter
    def color_wheel_mesh(self, target: str | ColorWheelTriangleMesh | None) -> None:
        """Set the _colorWheelMesh reference by target ID or ColorWheelTriangleMesh instance."""
        target_id: str | None = target.id if isinstance(target, ColorWheelTriangleMesh) else target  # type: ignore[assignment]
        member = self.get_member("_colorWheelMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorWheelMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ColorWheelTriangleMesh'),
            )

    @property
    def ok_button(self) -> str | None:
        """Target ID of the _okButton reference (targets LegacyButton)."""
        member = self.get_member("_okButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ok_button.setter
    def ok_button(self, target: str | LegacyButton | None) -> None:
        """Set the _okButton reference by target ID or LegacyButton instance."""
        target_id: str | None = target.id if isinstance(target, LegacyButton) else target  # type: ignore[assignment]
        member = self.get_member("_okButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_okButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyButton'),
            )

    @property
    def cancel_button(self) -> str | None:
        """Target ID of the _cancelButton reference (targets LegacyButton)."""
        member = self.get_member("_cancelButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cancel_button.setter
    def cancel_button(self, target: str | LegacyButton | None) -> None:
        """Set the _cancelButton reference by target ID or LegacyButton instance."""
        target_id: str | None = target.id if isinstance(target, LegacyButton) else target  # type: ignore[assignment]
        member = self.get_member("_cancelButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cancelButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyButton'),
            )

    @property
    def style(self) -> str | None:
        """Target ID of the _style reference (targets LegacyUIStyle)."""
        member = self.get_member("_style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the _style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("_style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

