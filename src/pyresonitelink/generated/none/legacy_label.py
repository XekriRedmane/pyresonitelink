"""Generated component: LegacyLabel."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.ilegacy_ui_element import ILegacyUIElement
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyLabel(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyLabel.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyLabel"

    def __init__(self, text_renderer: str | TextRenderer | None = None, base_color: primitives.ColorX | None = None, base_color_element: str | ILegacyUIElement | None = None, brightness: np.float32 | None = None, lerp_ratio: np.float32 | None = None, lerp_color: primitives.ColorX | None = None, text_color: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text_renderer: Initial value for TextRenderer.
            base_color: Initial value for BaseColor.
            base_color_element: Initial value for BaseColorElement.
            brightness: Initial value for Brightness.
            lerp_ratio: Initial value for LerpRatio.
            lerp_color: Initial value for LerpColor.
            text_color: Initial value for _textColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text_renderer is not None:
            self.text_renderer = text_renderer
        if base_color is not None:
            self.base_color = base_color
        if base_color_element is not None:
            self.base_color_element = base_color_element
        if brightness is not None:
            self.brightness = brightness
        if lerp_ratio is not None:
            self.lerp_ratio = lerp_ratio
        if lerp_color is not None:
            self.lerp_color = lerp_color
        if text_color is not None:
            self.text_color = text_color

    @property
    def text_renderer(self) -> str | None:
        """Target ID of the TextRenderer reference (targets TextRenderer)."""
        member = self.get_member("TextRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_renderer.setter
    def text_renderer(self, target: str | TextRenderer | None) -> None:
        """Set the TextRenderer reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("TextRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TextRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def base_color(self) -> primitives.ColorX | None:
        """The BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_color.setter
    def base_color(self, value: primitives.ColorX) -> None:
        """Set the BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseColor", fields.FieldColorX(value=value)
            )

    @property
    def base_color_element(self) -> str | None:
        """Target ID of the BaseColorElement reference (targets ILegacyUIElement)."""
        member = self.get_member("BaseColorElement")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @base_color_element.setter
    def base_color_element(self, target: str | ILegacyUIElement | None) -> None:
        """Set the BaseColorElement reference by target ID or ILegacyUIElement instance."""
        target_id: str | None = target.id if isinstance(target, ILegacyUIElement) else target  # type: ignore[assignment]
        member = self.get_member("BaseColorElement")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BaseColorElement",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ILegacyUIElement'),
            )

    @property
    def brightness(self) -> np.float32 | None:
        """The Brightness field value."""
        member = self.get_member("Brightness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @brightness.setter
    def brightness(self, value: np.float32) -> None:
        """Set the Brightness field value."""
        member = self.get_member("Brightness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Brightness", fields.FieldFloat(value=value)
            )

    @property
    def lerp_ratio(self) -> np.float32 | None:
        """The LerpRatio field value."""
        member = self.get_member("LerpRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_ratio.setter
    def lerp_ratio(self, value: np.float32) -> None:
        """Set the LerpRatio field value."""
        member = self.get_member("LerpRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpRatio", fields.FieldFloat(value=value)
            )

    @property
    def lerp_color(self) -> primitives.ColorX | None:
        """The LerpColor field value."""
        member = self.get_member("LerpColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_color.setter
    def lerp_color(self, value: primitives.ColorX) -> None:
        """Set the LerpColor field value."""
        member = self.get_member("LerpColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpColor", fields.FieldColorX(value=value)
            )

    @property
    def text_color(self) -> str | None:
        """Target ID of the _textColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_textColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_color.setter
    def text_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _textColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

