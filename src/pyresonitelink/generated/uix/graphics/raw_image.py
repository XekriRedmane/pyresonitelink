"""Generated component: RawImage."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.rect_orientation import RectOrientation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RawImage(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The RawImage component takes in a ITexture2D and takes in parameters to alter this texture image.

}}

    Category: UIX/Graphics

    This component acts more like a holder for a texture image to be used by
    other components.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RawImage"

    def __init__(self, texture: str | IAssetProvider[ITexture2D] | None = None, material: str | IAssetProvider[Material] | None = None, tint: primitives.ColorX | None = None, uv_rect: primitives.Rect | None = None, orientation: RectOrientation | str | None = None, preserve_aspect: primitives.Bool | None = None, interaction_target: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            material: Initial value for Material.
            tint: Initial value for Tint.
            uv_rect: Initial value for UVRect.
            orientation: Initial value for Orientation.
            preserve_aspect: Initial value for PreserveAspect.
            interaction_target: Initial value for InteractionTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if material is not None:
            self.material = material
        if tint is not None:
            self.tint = tint
        if uv_rect is not None:
            self.uv_rect = uv_rect
        if orientation is not None:
            self.orientation = orientation
        if preserve_aspect is not None:
            self.preserve_aspect = preserve_aspect
        if interaction_target is not None:
            self.interaction_target = interaction_target

    @property
    def texture(self) -> str | None:
        """The texture image itself."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def material(self) -> str | None:
        """The material to use as the texture from."""
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
    def tint(self) -> primitives.ColorX | None:
        """The tint color for this raw image."""
        member = self.get_member("Tint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint.setter
    def tint(self, value: primitives.ColorX) -> None:
        """Set the Tint field value."""
        member = self.get_member("Tint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tint", fields.FieldColorX(value=value)
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
    def preserve_aspect(self) -> primitives.Bool | None:
        """If this raw graphic should preserve its aspect ratio."""
        member = self.get_member("PreserveAspect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_aspect.setter
    def preserve_aspect(self, value: primitives.Bool) -> None:
        """Set the PreserveAspect field value."""
        member = self.get_member("PreserveAspect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveAspect", fields.FieldBool(value=value)
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

