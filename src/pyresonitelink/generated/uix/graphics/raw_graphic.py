"""Generated component: RawGraphic."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.material_property_block import MaterialPropertyBlock
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawGraphic(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.RawGraphic.

    Category: UIX/Graphics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RawGraphic"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, property_block: str | IAssetProvider[MaterialPropertyBlock] | None = None, fill_rect: primitives.Rect | None = None, color: primitives.ColorX | None = None, uv_rect: primitives.Rect | None = None, normal: primitives.Float3 | None = None, tangent: primitives.Float4 | None = None, hide_with_no_material: bool | None = None, preserve_uv_aspect_ratio: bool | None = None, interaction_target: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            property_block: Initial value for PropertyBlock.
            fill_rect: Initial value for FillRect.
            color: Initial value for Color.
            uv_rect: Initial value for UVRect.
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

    @property
    def property_block(self) -> str | None:
        """Target ID of the PropertyBlock reference (targets IAssetProvider[MaterialPropertyBlock])."""
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
        """The FillRect field value."""
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
        """The Color field value."""
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
        """The UVRect field value."""
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
    def orientation(self) -> members.FieldEnum | None:
        """The Orientation member."""
        member = self.get_member("Orientation")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @orientation.setter
    def orientation(self, value: members.FieldEnum) -> None:
        """Set the Orientation member."""
        self.set_member("Orientation", value)

    @property
    def normal(self) -> primitives.Float3 | None:
        """The Normal field value."""
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
        """The Tangent field value."""
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
    def hide_with_no_material(self) -> bool | None:
        """The HideWithNoMaterial field value."""
        member = self.get_member("HideWithNoMaterial")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_with_no_material.setter
    def hide_with_no_material(self, value: bool) -> None:
        """Set the HideWithNoMaterial field value."""
        member = self.get_member("HideWithNoMaterial")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideWithNoMaterial", fields.FieldBool(value=value)
            )

    @property
    def preserve_uv_aspect_ratio(self) -> bool | None:
        """The PreserveUVAspectRatio field value."""
        member = self.get_member("PreserveUVAspectRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_uv_aspect_ratio.setter
    def preserve_uv_aspect_ratio(self, value: bool) -> None:
        """Set the PreserveUVAspectRatio field value."""
        member = self.get_member("PreserveUVAspectRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUVAspectRatio", fields.FieldBool(value=value)
            )

    @property
    def interaction_target(self) -> bool | None:
        """The InteractionTarget field value."""
        member = self.get_member("InteractionTarget")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interaction_target.setter
    def interaction_target(self, value: bool) -> None:
        """Set the InteractionTarget field value."""
        member = self.get_member("InteractionTarget")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InteractionTarget", fields.FieldBool(value=value)
            )

