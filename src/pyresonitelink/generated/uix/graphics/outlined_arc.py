"""Generated component: OutlinedArc."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OutlinedArc(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.OutlinedArc.

    Category: UIX/Graphics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.OutlinedArc"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material

    @property
    def arc(self) -> np.float32 | None:
        """The Arc field value."""
        member = self.get_member("Arc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc.setter
    def arc(self, value: np.float32) -> None:
        """Set the Arc field value."""
        member = self.get_member("Arc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Arc", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> np.float32 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: np.float32) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def outer_radius_ratio(self) -> np.float32 | None:
        """The OuterRadiusRatio field value."""
        member = self.get_member("OuterRadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outer_radius_ratio.setter
    def outer_radius_ratio(self, value: np.float32) -> None:
        """Set the OuterRadiusRatio field value."""
        member = self.get_member("OuterRadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OuterRadiusRatio", fields.FieldFloat(value=value)
            )

    @property
    def inner_radius_ratio(self) -> np.float32 | None:
        """The InnerRadiusRatio field value."""
        member = self.get_member("InnerRadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_radius_ratio.setter
    def inner_radius_ratio(self, value: np.float32) -> None:
        """Set the InnerRadiusRatio field value."""
        member = self.get_member("InnerRadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerRadiusRatio", fields.FieldFloat(value=value)
            )

    @property
    def rounded_corner_radius(self) -> np.float32 | None:
        """The RoundedCornerRadius field value."""
        member = self.get_member("RoundedCornerRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rounded_corner_radius.setter
    def rounded_corner_radius(self, value: np.float32) -> None:
        """Set the RoundedCornerRadius field value."""
        member = self.get_member("RoundedCornerRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RoundedCornerRadius", fields.FieldFloat(value=value)
            )

    @property
    def fill_color(self) -> primitives.ColorX | None:
        """The FillColor field value."""
        member = self.get_member("FillColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_color.setter
    def fill_color(self, value: primitives.ColorX) -> None:
        """Set the FillColor field value."""
        member = self.get_member("FillColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillColor", fields.FieldColorX(value=value)
            )

    @property
    def outline_color(self) -> primitives.ColorX | None:
        """The OutlineColor field value."""
        member = self.get_member("OutlineColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_color.setter
    def outline_color(self, value: primitives.ColorX) -> None:
        """Set the OutlineColor field value."""
        member = self.get_member("OutlineColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineColor", fields.FieldColorX(value=value)
            )

    @property
    def outline_thickness(self) -> np.float32 | None:
        """The OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_thickness.setter
    def outline_thickness(self, value: np.float32) -> None:
        """Set the OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineThickness", fields.FieldFloat(value=value)
            )

    @property
    def material(self) -> str | None:
        """Target ID of the Material reference (targets IAssetProvider[Material])."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the Material reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

