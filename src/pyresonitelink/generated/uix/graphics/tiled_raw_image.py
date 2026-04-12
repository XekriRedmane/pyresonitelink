"""Generated component: TiledRawImage."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.tile_size_basis import TileSizeBasis
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TiledRawImage(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The TiledRawImage component takes in a ITexture2D and renders it to the UIX, and then tiles it if the image provided is too small. There are parameters to control how the tiling behaves for the UIX element that it is in.

}}

    Category: UIX/Graphics

    This can be used to make fancy backgrounds or image effects. And like
    with other images, this can be layered for even more effects.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.TiledRawImage"

    def __init__(self, texture: str | IAssetProvider[ITexture2D] | None = None, material: str | IAssetProvider[Material] | None = None, tint: primitives.ColorX | None = None, size_basis: TileSizeBasis | str | None = None, tile_size: primitives.Float2 | None = None, tile_offset: primitives.Float2 | None = None, interaction_target: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            material: Initial value for Material.
            tint: Initial value for Tint.
            size_basis: Initial value for SizeBasis.
            tile_size: Initial value for TileSize.
            tile_offset: Initial value for TileOffset.
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
        if size_basis is not None:
            self.size_basis = size_basis
        if tile_size is not None:
            self.tile_size = tile_size
        if tile_offset is not None:
            self.tile_offset = tile_offset
        if interaction_target is not None:
            self.interaction_target = interaction_target

    @property
    def texture(self) -> str | None:
        """The tilable image to use."""
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
        """The material that has a tilable image to use."""
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
        """The tint color for this image."""
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
    def size_basis(self) -> TileSizeBasis | None:
        """Changes how the tiling behaves."""
        member = self.get_member("SizeBasis")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TileSizeBasis(member.value)
        return None

    @size_basis.setter
    def size_basis(self, value: TileSizeBasis | str) -> None:
        """Set SizeBasis. Changes how the tiling behaves."""
        member = self.get_member("SizeBasis")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SizeBasis",
                members.FieldEnum(value=str(value)),
            )

    @property
    def tile_size(self) -> primitives.Float2 | None:
        """How large this image is on the ``X`` and ``Y``."""
        member = self.get_member("TileSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tile_size.setter
    def tile_size(self, value: primitives.Float2) -> None:
        """Set the TileSize field value."""
        member = self.get_member("TileSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TileSize", fields.FieldFloat2(value=value)
            )

    @property
    def tile_offset(self) -> primitives.Float2 | None:
        """How much this image should be moved on the ``X`` and ``Y``."""
        member = self.get_member("TileOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tile_offset.setter
    def tile_offset(self, value: primitives.Float2) -> None:
        """Set the TileOffset field value."""
        member = self.get_member("TileOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TileOffset", fields.FieldFloat2(value=value)
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

