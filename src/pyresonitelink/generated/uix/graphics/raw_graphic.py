"""Generated component: RawGraphic."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.rect_orientation import RectOrientation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.material_property_block import MaterialPropertyBlock
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawGraphic(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The RawGraphic component takes in a Material or a Material Property Block component, then shows the raw graphic image onto the UIX.

}}

    Category: UIX/Graphics

    Use this component when the Image component does not have what your
    looking for in your UIX design.

    **Related Components**: * MainTexturePropertyBlock
* Projection360PropertyBlock
* MainAndMaskTexturePropertyBlock
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RawGraphic"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, property_block: str | IAssetProvider[MaterialPropertyBlock] | None = None, fill_rect: primitives.Rect | None = None, color: primitives.ColorX | None = None, uv_rect: primitives.Rect | None = None, orientation: RectOrientation | str | None = None, normal: primitives.Float3 | None = None, tangent: primitives.Float4 | None = None, hide_with_no_material: primitives.Bool | None = None, preserve_uv_aspect_ratio: primitives.Bool | None = None, interaction_target: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            property_block: Initial value for PropertyBlock.
            fill_rect: Initial value for FillRect.
            color: Initial value for Color.
            uv_rect: Initial value for UVRect.
            orientation: Initial value for Orientation.
            normal: Initial value for Normal.
            tangent: Initial value for Tangent.
            hide_with_no_material: Initial value for HideWithNoMaterial.
            preserve_uv_aspect_ratio: Initial value for PreserveUVAspectRatio.
            interaction_target: Initial value for InteractionTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if property_block is not None:
            self.property_block = property_block
        if fill_rect is not None:
            self.fill_rect = fill_rect
        if color is not None:
            self.color = color
        if uv_rect is not None:
            self.uv_rect = uv_rect
        if orientation is not None:
            self.orientation = orientation
        if normal is not None:
            self.normal = normal
        if tangent is not None:
            self.tangent = tangent
        if hide_with_no_material is not None:
            self.hide_with_no_material = hide_with_no_material
        if preserve_uv_aspect_ratio is not None:
            self.preserve_uv_aspect_ratio = preserve_uv_aspect_ratio
        if interaction_target is not None:
            self.interaction_target = interaction_target

    @property
    def material(self) -> str | None:
        """The material to take the raw graphic from."""
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

    @property
    def property_block(self) -> str | None:
        """The image within a literal image block."""
        member = self.get_member("PropertyBlock")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @property_block.setter
    def property_block(self, target: str | IAssetProvider[MaterialPropertyBlock] | None) -> None:
        """Set the PropertyBlock reference by target ID or IAssetProvider[MaterialPropertyBlock] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PropertyBlock")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PropertyBlock",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.MaterialPropertyBlock>'),
            )

    @property
    def fill_rect(self) -> primitives.Rect | None:
        """The filling rect for this image."""
        member = self.get_member("FillRect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_rect.setter
    def fill_rect(self, value: primitives.Rect) -> None:
        """Set the FillRect field value."""
        member = self.get_member("FillRect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillRect", fields.FieldRect(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """Changes the color of the image."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def uv_rect(self) -> primitives.Rect | None:
        """Shifts the UV of the raw image."""
        member = self.get_member("UVRect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_rect.setter
    def uv_rect(self, value: primitives.Rect) -> None:
        """Set the UVRect field value."""
        member = self.get_member("UVRect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVRect", fields.FieldRect(value=value)
            )

    @property
    def orientation(self) -> RectOrientation | None:
        """Rotates the raw image and respects aspect ratio."""
        member = self.get_member("Orientation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RectOrientation(member.value)
        return None

    @orientation.setter
    def orientation(self, value: RectOrientation | str) -> None:
        """Set Orientation. Rotates the raw image and respects aspect ratio."""
        member = self.get_member("Orientation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Orientation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def normal(self) -> primitives.Float3 | None:
        """The normal for this raw graphic."""
        member = self.get_member("Normal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal.setter
    def normal(self, value: primitives.Float3) -> None:
        """Set the Normal field value."""
        member = self.get_member("Normal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Normal", fields.FieldNullableFloat3(value=value)
            )

    @property
    def tangent(self) -> primitives.Float4 | None:
        """The tangent for this raw graphic."""
        member = self.get_member("Tangent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tangent.setter
    def tangent(self, value: primitives.Float4) -> None:
        """Set the Tangent field value."""
        member = self.get_member("Tangent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tangent", fields.FieldNullableFloat4(value=value)
            )

    @property
    def hide_with_no_material(self) -> primitives.Bool | None:
        """If there is no material, hid this raw image."""
        member = self.get_member("HideWithNoMaterial")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_with_no_material.setter
    def hide_with_no_material(self, value: primitives.Bool) -> None:
        """Set the HideWithNoMaterial field value."""
        member = self.get_member("HideWithNoMaterial")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideWithNoMaterial", fields.FieldBool(value=value)
            )

    @property
    def preserve_uv_aspect_ratio(self) -> primitives.Bool | None:
        """If this raw graphic should preserve its aspect ratio."""
        member = self.get_member("PreserveUVAspectRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_uv_aspect_ratio.setter
    def preserve_uv_aspect_ratio(self, value: primitives.Bool) -> None:
        """Set the PreserveUVAspectRatio field value."""
        member = self.get_member("PreserveUVAspectRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUVAspectRatio", fields.FieldBool(value=value)
            )

    @property
    def interaction_target(self) -> primitives.Bool | None:
        """Makes this image as the interaction target for this UIX."""
        member = self.get_member("InteractionTarget")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interaction_target.setter
    def interaction_target(self, value: primitives.Bool) -> None:
        """Set the InteractionTarget field value."""
        member = self.get_member("InteractionTarget")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InteractionTarget", fields.FieldBool(value=value)
            )

