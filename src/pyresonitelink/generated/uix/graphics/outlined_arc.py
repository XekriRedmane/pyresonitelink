"""Generated component: OutlinedArc."""

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
    """The OutlinedArc component takes in many parameters to create a circular image or design and can be controlled using those parameters. Then this renders onto the UIX.

}}

    Category: UIX/Graphics

    A user could make fancy effects like a loading circular throbber, or
    menu buttons that arc around.

    **Related Components**: * Context menu components
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.OutlinedArc"

    def __init__(self, arc: primitives.Float | None = None, offset: primitives.Float | None = None, outer_radius_ratio: primitives.Float | None = None, inner_radius_ratio: primitives.Float | None = None, rounded_corner_radius: primitives.Float | None = None, fill_color: primitives.ColorX | None = None, outline_color: primitives.ColorX | None = None, outline_thickness: primitives.Float | None = None, material: str | IAssetProvider[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            arc: Initial value for Arc.
            offset: Initial value for Offset.
            outer_radius_ratio: Initial value for OuterRadiusRatio.
            inner_radius_ratio: Initial value for InnerRadiusRatio.
            rounded_corner_radius: Initial value for RoundedCornerRadius.
            fill_color: Initial value for FillColor.
            outline_color: Initial value for OutlineColor.
            outline_thickness: Initial value for OutlineThickness.
            material: Initial value for Material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if arc is not None:
            self.arc = arc
        if offset is not None:
            self.offset = offset
        if outer_radius_ratio is not None:
            self.outer_radius_ratio = outer_radius_ratio
        if inner_radius_ratio is not None:
            self.inner_radius_ratio = inner_radius_ratio
        if rounded_corner_radius is not None:
            self.rounded_corner_radius = rounded_corner_radius
        if fill_color is not None:
            self.fill_color = fill_color
        if outline_color is not None:
            self.outline_color = outline_color
        if outline_thickness is not None:
            self.outline_thickness = outline_thickness
        if material is not None:
            self.material = material

    @property
    def arc(self) -> primitives.Float | None:
        """The amount to arc around the center."""
        member = self.get_member("Arc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc.setter
    def arc(self, value: primitives.Float) -> None:
        """Set the Arc field value."""
        member = self.get_member("Arc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Arc", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> primitives.Float | None:
        """The amount to rotate around the center."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def outer_radius_ratio(self) -> primitives.Float | None:
        """The outer distance for this arc from the center."""
        member = self.get_member("OuterRadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outer_radius_ratio.setter
    def outer_radius_ratio(self, value: primitives.Float) -> None:
        """Set the OuterRadiusRatio field value."""
        member = self.get_member("OuterRadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OuterRadiusRatio", fields.FieldFloat(value=value)
            )

    @property
    def inner_radius_ratio(self) -> primitives.Float | None:
        """The inner distance for this arc from the center."""
        member = self.get_member("InnerRadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_radius_ratio.setter
    def inner_radius_ratio(self, value: primitives.Float) -> None:
        """Set the InnerRadiusRatio field value."""
        member = self.get_member("InnerRadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerRadiusRatio", fields.FieldFloat(value=value)
            )

    @property
    def rounded_corner_radius(self) -> primitives.Float | None:
        """The amount of how rounded the edges of the arc end points are."""
        member = self.get_member("RoundedCornerRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rounded_corner_radius.setter
    def rounded_corner_radius(self, value: primitives.Float) -> None:
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
        """The inner color (filled in color) of this arc."""
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
        """The outer color (the outline) of this arc."""
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
    def outline_thickness(self) -> primitives.Float | None:
        """The amount to thicken for the outline."""
        member = self.get_member("OutlineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_thickness.setter
    def outline_thickness(self, value: primitives.Float) -> None:
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
        """Uses a material for the arc."""
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

