"""Generated component: ContextMenu."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.arc_layout import ArcLayout
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.outlined_arc import OutlinedArc
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.ui_circle_segment import UI_CircleSegment
from pyresonitelink.generated._types.ui_text_unlit_material import UI_TextUnlitMaterial
from pyresonitelink.generated._types.ui_unlit_material import UI_UnlitMaterial
from pyresonitelink.generated._types.ztest import ZTest
from pyresonitelink.generated._types.zwrite import ZWrite
from pyresonitelink.generated._types.context_menu_item import ContextMenuItem
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContextMenu(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ContextMenu.

    Category: Radiant UI/Context Menu
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContextMenu"

    def __init__(self, owner: str | User | None = None, pointer: str | Slot | None = None, separation: np.float32 | None = None, label_size: primitives.Float2 | None = None, radius_ratio: np.float32 | None = None, current_summoner: str | IWorldElement | None = None, canvas: str | Canvas | None = None, arc_layout: str | ArcLayout | None = None, canvas_active: str | IField[bool] | None = None, collider_enabled: str | IField[bool] | None = None, icon_image: str | Image | None = None, separation: str | IField[np.float32] | None = None, offset_min: str | IField[primitives.Float2] | None = None, offset_max: str | IField[primitives.Float2] | None = None, inner_circle: str | OutlinedArc | None = None, inner_circle_button: str | Button | None = None, inner_circle_anchor_min: str | IField[primitives.Float2] | None = None, inner_circle_anchor_max: str | IField[primitives.Float2] | None = None, items_root: str | Slot | None = None, arc_material: str | UI_CircleSegment | None = None, font_material: str | UI_TextUnlitMaterial | None = None, sprite_material: str | UI_UnlitMaterial | None = None, arc_overlay: str | IField[bool] | None = None, font_overlay: str | IField[bool] | None = None, sprite_overlay: str | IField[bool] | None = None, arc_ztest: str | IField[ZTest] | None = None, font_ztest: str | IField[ZTest] | None = None, sprite_ztest: str | IField[ZTest] | None = None, zwrite_arc: str | IField[ZWrite] | None = None, zwrite_text: str | IField[ZWrite] | None = None, arc_render_queue: str | IField[np.int32] | None = None, font_render_queue: str | IField[np.int32] | None = None, sprite_render_queue: str | IField[np.int32] | None = None, canvas_offset: str | IField[np.int32] | None = None, fill_fade: str | IField[primitives.ColorX] | None = None, outline_fade: str | IField[primitives.ColorX] | None = None, text_fade: str | IField[primitives.ColorX] | None = None, icon_fade: str | IField[primitives.ColorX] | None = None, lerp: np.float32 | None = None, flick_mode_active: bool | None = None, flick_enabled: bool | None = None, hidden: bool | None = None, selected_item: str | ContextMenuItem | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            owner: Initial value for Owner.
            pointer: Initial value for Pointer.
            separation: Initial value for Separation.
            label_size: Initial value for LabelSize.
            radius_ratio: Initial value for RadiusRatio.
            current_summoner: Initial value for _currentSummoner.
            canvas: Initial value for _canvas.
            arc_layout: Initial value for _arcLayout.
            canvas_active: Initial value for _canvasActive.
            collider_enabled: Initial value for _colliderEnabled.
            icon_image: Initial value for _iconImage.
            separation: Initial value for _separation.
            offset_min: Initial value for _offsetMin.
            offset_max: Initial value for _offsetMax.
            inner_circle: Initial value for _innerCircle.
            inner_circle_button: Initial value for _innerCircleButton.
            inner_circle_anchor_min: Initial value for _innerCircleAnchorMin.
            inner_circle_anchor_max: Initial value for _innerCircleAnchorMax.
            items_root: Initial value for _itemsRoot.
            arc_material: Initial value for _arcMaterial.
            font_material: Initial value for _fontMaterial.
            sprite_material: Initial value for _spriteMaterial.
            arc_overlay: Initial value for _arcOverlay.
            font_overlay: Initial value for _fontOverlay.
            sprite_overlay: Initial value for _spriteOverlay.
            arc_ztest: Initial value for _arcZTest.
            font_ztest: Initial value for _fontZTest.
            sprite_ztest: Initial value for _spriteZTest.
            zwrite_arc: Initial value for _zwriteArc.
            zwrite_text: Initial value for _zwriteText.
            arc_render_queue: Initial value for _arcRenderQueue.
            font_render_queue: Initial value for _fontRenderQueue.
            sprite_render_queue: Initial value for _spriteRenderQueue.
            canvas_offset: Initial value for _canvasOffset.
            fill_fade: Initial value for _fillFade.
            outline_fade: Initial value for _outlineFade.
            text_fade: Initial value for _textFade.
            icon_fade: Initial value for _iconFade.
            lerp: Initial value for _lerp.
            flick_mode_active: Initial value for _flickModeActive.
            flick_enabled: Initial value for _flickEnabled.
            hidden: Initial value for _hidden.
            selected_item: Initial value for _selectedItem.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if owner is not None:
            self.owner = owner
        if pointer is not None:
            self.pointer = pointer
        if separation is not None:
            self.separation = separation
        if label_size is not None:
            self.label_size = label_size
        if radius_ratio is not None:
            self.radius_ratio = radius_ratio
        if current_summoner is not None:
            self.current_summoner = current_summoner
        if canvas is not None:
            self.canvas = canvas
        if arc_layout is not None:
            self.arc_layout = arc_layout
        if canvas_active is not None:
            self.canvas_active = canvas_active
        if collider_enabled is not None:
            self.collider_enabled = collider_enabled
        if icon_image is not None:
            self.icon_image = icon_image
        if separation is not None:
            self.separation = separation
        if offset_min is not None:
            self.offset_min = offset_min
        if offset_max is not None:
            self.offset_max = offset_max
        if inner_circle is not None:
            self.inner_circle = inner_circle
        if inner_circle_button is not None:
            self.inner_circle_button = inner_circle_button
        if inner_circle_anchor_min is not None:
            self.inner_circle_anchor_min = inner_circle_anchor_min
        if inner_circle_anchor_max is not None:
            self.inner_circle_anchor_max = inner_circle_anchor_max
        if items_root is not None:
            self.items_root = items_root
        if arc_material is not None:
            self.arc_material = arc_material
        if font_material is not None:
            self.font_material = font_material
        if sprite_material is not None:
            self.sprite_material = sprite_material
        if arc_overlay is not None:
            self.arc_overlay = arc_overlay
        if font_overlay is not None:
            self.font_overlay = font_overlay
        if sprite_overlay is not None:
            self.sprite_overlay = sprite_overlay
        if arc_ztest is not None:
            self.arc_ztest = arc_ztest
        if font_ztest is not None:
            self.font_ztest = font_ztest
        if sprite_ztest is not None:
            self.sprite_ztest = sprite_ztest
        if zwrite_arc is not None:
            self.zwrite_arc = zwrite_arc
        if zwrite_text is not None:
            self.zwrite_text = zwrite_text
        if arc_render_queue is not None:
            self.arc_render_queue = arc_render_queue
        if font_render_queue is not None:
            self.font_render_queue = font_render_queue
        if sprite_render_queue is not None:
            self.sprite_render_queue = sprite_render_queue
        if canvas_offset is not None:
            self.canvas_offset = canvas_offset
        if fill_fade is not None:
            self.fill_fade = fill_fade
        if outline_fade is not None:
            self.outline_fade = outline_fade
        if text_fade is not None:
            self.text_fade = text_fade
        if icon_fade is not None:
            self.icon_fade = icon_fade
        if lerp is not None:
            self.lerp = lerp
        if flick_mode_active is not None:
            self.flick_mode_active = flick_mode_active
        if flick_enabled is not None:
            self.flick_enabled = flick_enabled
        if hidden is not None:
            self.hidden = hidden
        if selected_item is not None:
            self.selected_item = selected_item

    @property
    def owner(self) -> str | None:
        """Target ID of the Owner reference (targets User)."""
        member = self.get_member("Owner")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @owner.setter
    def owner(self, target: str | User | None) -> None:
        """Set the Owner reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("Owner")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Owner",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def pointer(self) -> str | None:
        """Target ID of the Pointer reference (targets Slot)."""
        member = self.get_member("Pointer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pointer.setter
    def pointer(self, target: str | Slot | None) -> None:
        """Set the Pointer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Pointer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pointer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def separation(self) -> np.float32 | None:
        """The Separation field value."""
        member = self.get_member("Separation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separation.setter
    def separation(self, value: np.float32) -> None:
        """Set the Separation field value."""
        member = self.get_member("Separation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Separation", fields.FieldFloat(value=value)
            )

    @property
    def label_size(self) -> primitives.Float2 | None:
        """The LabelSize field value."""
        member = self.get_member("LabelSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_size.setter
    def label_size(self, value: primitives.Float2) -> None:
        """Set the LabelSize field value."""
        member = self.get_member("LabelSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelSize", fields.FieldFloat2(value=value)
            )

    @property
    def radius_ratio(self) -> np.float32 | None:
        """The RadiusRatio field value."""
        member = self.get_member("RadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_ratio.setter
    def radius_ratio(self, value: np.float32) -> None:
        """Set the RadiusRatio field value."""
        member = self.get_member("RadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusRatio", fields.FieldFloat(value=value)
            )

    @property
    def current_summoner(self) -> str | None:
        """Target ID of the _currentSummoner reference (targets IWorldElement)."""
        member = self.get_member("_currentSummoner")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_summoner.setter
    def current_summoner(self, target: str | IWorldElement | None) -> None:
        """Set the _currentSummoner reference by target ID or IWorldElement instance."""
        target_id: str | None = target.id if isinstance(target, IWorldElement) else target  # type: ignore[assignment]
        member = self.get_member("_currentSummoner")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentSummoner",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldElement'),
            )

    @property
    def canvas(self) -> str | None:
        """Target ID of the _canvas reference (targets Canvas)."""
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas.setter
    def canvas(self, target: str | Canvas | None) -> None:
        """Set the _canvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def arc_layout(self) -> str | None:
        """Target ID of the _arcLayout reference (targets ArcLayout)."""
        member = self.get_member("_arcLayout")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arc_layout.setter
    def arc_layout(self, target: str | ArcLayout | None) -> None:
        """Set the _arcLayout reference by target ID or ArcLayout instance."""
        target_id: str | None = target.id if isinstance(target, ArcLayout) else target  # type: ignore[assignment]
        member = self.get_member("_arcLayout")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arcLayout",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.ArcLayout'),
            )

    @property
    def canvas_active(self) -> str | None:
        """Target ID of the _canvasActive reference (targets IField[bool])."""
        member = self.get_member("_canvasActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas_active.setter
    def canvas_active(self, target: str | IField[bool] | None) -> None:
        """Set the _canvasActive reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_canvasActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvasActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def collider_enabled(self) -> str | None:
        """Target ID of the _colliderEnabled reference (targets IField[bool])."""
        member = self.get_member("_colliderEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_enabled.setter
    def collider_enabled(self, target: str | IField[bool] | None) -> None:
        """Set the _colliderEnabled reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def icon_image(self) -> str | None:
        """Target ID of the _iconImage reference (targets Image)."""
        member = self.get_member("_iconImage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_image.setter
    def icon_image(self, target: str | Image | None) -> None:
        """Set the _iconImage reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_iconImage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconImage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def separation(self) -> str | None:
        """Target ID of the _separation reference (targets IField[np.float32])."""
        member = self.get_member("_separation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @separation.setter
    def separation(self, target: str | IField[np.float32] | None) -> None:
        """Set the _separation reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_separation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_separation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def offset_min(self) -> str | None:
        """Target ID of the _offsetMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("_offsetMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset_min.setter
    def offset_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _offsetMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_offsetMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_offsetMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def offset_max(self) -> str | None:
        """Target ID of the _offsetMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("_offsetMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset_max.setter
    def offset_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _offsetMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_offsetMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_offsetMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def inner_circle(self) -> str | None:
        """Target ID of the _innerCircle reference (targets OutlinedArc)."""
        member = self.get_member("_innerCircle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inner_circle.setter
    def inner_circle(self, target: str | OutlinedArc | None) -> None:
        """Set the _innerCircle reference by target ID or OutlinedArc instance."""
        target_id: str | None = target.id if isinstance(target, OutlinedArc) else target  # type: ignore[assignment]
        member = self.get_member("_innerCircle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_innerCircle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.OutlinedArc'),
            )

    @property
    def inner_circle_button(self) -> str | None:
        """Target ID of the _innerCircleButton reference (targets Button)."""
        member = self.get_member("_innerCircleButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inner_circle_button.setter
    def inner_circle_button(self, target: str | Button | None) -> None:
        """Set the _innerCircleButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_innerCircleButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_innerCircleButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def inner_circle_anchor_min(self) -> str | None:
        """Target ID of the _innerCircleAnchorMin reference (targets IField[primitives.Float2])."""
        member = self.get_member("_innerCircleAnchorMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inner_circle_anchor_min.setter
    def inner_circle_anchor_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _innerCircleAnchorMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_innerCircleAnchorMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_innerCircleAnchorMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def inner_circle_anchor_max(self) -> str | None:
        """Target ID of the _innerCircleAnchorMax reference (targets IField[primitives.Float2])."""
        member = self.get_member("_innerCircleAnchorMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inner_circle_anchor_max.setter
    def inner_circle_anchor_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _innerCircleAnchorMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_innerCircleAnchorMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_innerCircleAnchorMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def items_root(self) -> str | None:
        """Target ID of the _itemsRoot reference (targets Slot)."""
        member = self.get_member("_itemsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @items_root.setter
    def items_root(self, target: str | Slot | None) -> None:
        """Set the _itemsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_itemsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_itemsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def arc_material(self) -> str | None:
        """Target ID of the _arcMaterial reference (targets UI_CircleSegment)."""
        member = self.get_member("_arcMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arc_material.setter
    def arc_material(self, target: str | UI_CircleSegment | None) -> None:
        """Set the _arcMaterial reference by target ID or UI_CircleSegment instance."""
        target_id: str | None = target.id if isinstance(target, UI_CircleSegment) else target  # type: ignore[assignment]
        member = self.get_member("_arcMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arcMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_CircleSegment'),
            )

    @property
    def font_material(self) -> str | None:
        """Target ID of the _fontMaterial reference (targets UI_TextUnlitMaterial)."""
        member = self.get_member("_fontMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font_material.setter
    def font_material(self, target: str | UI_TextUnlitMaterial | None) -> None:
        """Set the _fontMaterial reference by target ID or UI_TextUnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UI_TextUnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_fontMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fontMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_TextUnlitMaterial'),
            )

    @property
    def sprite_material(self) -> str | None:
        """Target ID of the _spriteMaterial reference (targets UI_UnlitMaterial)."""
        member = self.get_member("_spriteMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_material.setter
    def sprite_material(self, target: str | UI_UnlitMaterial | None) -> None:
        """Set the _spriteMaterial reference by target ID or UI_UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UI_UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_spriteMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spriteMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_UnlitMaterial'),
            )

    @property
    def arc_overlay(self) -> str | None:
        """Target ID of the _arcOverlay reference (targets IField[bool])."""
        member = self.get_member("_arcOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arc_overlay.setter
    def arc_overlay(self, target: str | IField[bool] | None) -> None:
        """Set the _arcOverlay reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arcOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arcOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def font_overlay(self) -> str | None:
        """Target ID of the _fontOverlay reference (targets IField[bool])."""
        member = self.get_member("_fontOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font_overlay.setter
    def font_overlay(self, target: str | IField[bool] | None) -> None:
        """Set the _fontOverlay reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_fontOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fontOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def sprite_overlay(self) -> str | None:
        """Target ID of the _spriteOverlay reference (targets IField[bool])."""
        member = self.get_member("_spriteOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_overlay.setter
    def sprite_overlay(self, target: str | IField[bool] | None) -> None:
        """Set the _spriteOverlay reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_spriteOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spriteOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def arc_ztest(self) -> str | None:
        """Target ID of the _arcZTest reference (targets IField[ZTest])."""
        member = self.get_member("_arcZTest")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arc_ztest.setter
    def arc_ztest(self, target: str | IField[ZTest] | None) -> None:
        """Set the _arcZTest reference by target ID or IField[ZTest] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arcZTest")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arcZTest",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ZTest>'),
            )

    @property
    def font_ztest(self) -> str | None:
        """Target ID of the _fontZTest reference (targets IField[ZTest])."""
        member = self.get_member("_fontZTest")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font_ztest.setter
    def font_ztest(self, target: str | IField[ZTest] | None) -> None:
        """Set the _fontZTest reference by target ID or IField[ZTest] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_fontZTest")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fontZTest",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ZTest>'),
            )

    @property
    def sprite_ztest(self) -> str | None:
        """Target ID of the _spriteZTest reference (targets IField[ZTest])."""
        member = self.get_member("_spriteZTest")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_ztest.setter
    def sprite_ztest(self, target: str | IField[ZTest] | None) -> None:
        """Set the _spriteZTest reference by target ID or IField[ZTest] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_spriteZTest")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spriteZTest",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ZTest>'),
            )

    @property
    def zwrite_arc(self) -> str | None:
        """Target ID of the _zwriteArc reference (targets IField[ZWrite])."""
        member = self.get_member("_zwriteArc")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @zwrite_arc.setter
    def zwrite_arc(self, target: str | IField[ZWrite] | None) -> None:
        """Set the _zwriteArc reference by target ID or IField[ZWrite] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_zwriteArc")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zwriteArc",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ZWrite>'),
            )

    @property
    def zwrite_text(self) -> str | None:
        """Target ID of the _zwriteText reference (targets IField[ZWrite])."""
        member = self.get_member("_zwriteText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @zwrite_text.setter
    def zwrite_text(self, target: str | IField[ZWrite] | None) -> None:
        """Set the _zwriteText reference by target ID or IField[ZWrite] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_zwriteText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zwriteText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ZWrite>'),
            )

    @property
    def arc_render_queue(self) -> str | None:
        """Target ID of the _arcRenderQueue reference (targets IField[np.int32])."""
        member = self.get_member("_arcRenderQueue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arc_render_queue.setter
    def arc_render_queue(self, target: str | IField[np.int32] | None) -> None:
        """Set the _arcRenderQueue reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arcRenderQueue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arcRenderQueue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def font_render_queue(self) -> str | None:
        """Target ID of the _fontRenderQueue reference (targets IField[np.int32])."""
        member = self.get_member("_fontRenderQueue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font_render_queue.setter
    def font_render_queue(self, target: str | IField[np.int32] | None) -> None:
        """Set the _fontRenderQueue reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_fontRenderQueue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fontRenderQueue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def sprite_render_queue(self) -> str | None:
        """Target ID of the _spriteRenderQueue reference (targets IField[np.int32])."""
        member = self.get_member("_spriteRenderQueue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_render_queue.setter
    def sprite_render_queue(self, target: str | IField[np.int32] | None) -> None:
        """Set the _spriteRenderQueue reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_spriteRenderQueue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spriteRenderQueue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def canvas_offset(self) -> str | None:
        """Target ID of the _canvasOffset reference (targets IField[np.int32])."""
        member = self.get_member("_canvasOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas_offset.setter
    def canvas_offset(self, target: str | IField[np.int32] | None) -> None:
        """Set the _canvasOffset reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_canvasOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvasOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def fill_fade(self) -> str | None:
        """Target ID of the _fillFade reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_fillFade")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fill_fade.setter
    def fill_fade(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _fillFade reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_fillFade")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fillFade",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def outline_fade(self) -> str | None:
        """Target ID of the _outlineFade reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_outlineFade")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outline_fade.setter
    def outline_fade(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _outlineFade reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_outlineFade")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_outlineFade",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def text_fade(self) -> str | None:
        """Target ID of the _textFade reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_textFade")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_fade.setter
    def text_fade(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _textFade reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textFade")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textFade",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def icon_fade(self) -> str | None:
        """Target ID of the _iconFade reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_iconFade")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_fade.setter
    def icon_fade(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _iconFade reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_iconFade")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconFade",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def lerp(self) -> np.float32 | None:
        """The _lerp field value."""
        member = self.get_member("_lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: np.float32) -> None:
        """Set the _lerp field value."""
        member = self.get_member("_lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lerp", fields.FieldFloat(value=value)
            )

    @property
    def state(self) -> members.FieldEnum | None:
        """The _state member."""
        member = self.get_member("_state")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @state.setter
    def state(self, value: members.FieldEnum) -> None:
        """Set the _state member."""
        self.set_member("_state", value)

    @property
    def flick_mode_active(self) -> bool | None:
        """The _flickModeActive field value."""
        member = self.get_member("_flickModeActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flick_mode_active.setter
    def flick_mode_active(self, value: bool) -> None:
        """Set the _flickModeActive field value."""
        member = self.get_member("_flickModeActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_flickModeActive", fields.FieldBool(value=value)
            )

    @property
    def flick_enabled(self) -> bool | None:
        """The _flickEnabled field value."""
        member = self.get_member("_flickEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flick_enabled.setter
    def flick_enabled(self, value: bool) -> None:
        """Set the _flickEnabled field value."""
        member = self.get_member("_flickEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_flickEnabled", fields.FieldBool(value=value)
            )

    @property
    def hidden(self) -> bool | None:
        """The _hidden field value."""
        member = self.get_member("_hidden")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hidden.setter
    def hidden(self, value: bool) -> None:
        """Set the _hidden field value."""
        member = self.get_member("_hidden")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_hidden", fields.FieldBool(value=value)
            )

    @property
    def selected_item(self) -> str | None:
        """Target ID of the _selectedItem reference (targets ContextMenuItem)."""
        member = self.get_member("_selectedItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_item.setter
    def selected_item(self, target: str | ContextMenuItem | None) -> None:
        """Set the _selectedItem reference by target ID or ContextMenuItem instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenuItem) else target  # type: ignore[assignment]
        member = self.get_member("_selectedItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selectedItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenuItem'),
            )

