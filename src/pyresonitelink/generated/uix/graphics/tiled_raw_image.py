"""Generated component: TiledRawImage."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TiledRawImage(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.TiledRawImage.

    Category: UIX/Graphics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.TiledRawImage"

    def __init__(self, texture: str | IAssetProvider[ITexture2D] | None = None, material: str | IAssetProvider[Material] | None = None, tint: primitives.ColorX | None = None, tile_size: primitives.Float2 | None = None, tile_offset: primitives.Float2 | None = None, interaction_target: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            material: Initial value for Material.
            tint: Initial value for Tint.
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
        if tile_size is not None:
            self.tile_size = tile_size
        if tile_offset is not None:
            self.tile_offset = tile_offset
        if interaction_target is not None:
            self.interaction_target = interaction_target

    @property
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets IAssetProvider[ITexture2D])."""
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
    def tint(self) -> primitives.ColorX | None:
        """The Tint field value."""
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
    def size_basis(self) -> members.FieldEnum | None:
        """The SizeBasis member."""
        member = self.get_member("SizeBasis")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @size_basis.setter
    def size_basis(self, value: members.FieldEnum) -> None:
        """Set the SizeBasis member."""
        self.set_member("SizeBasis", value)

    @property
    def tile_size(self) -> primitives.Float2 | None:
        """The TileSize field value."""
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
        """The TileOffset field value."""
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
        """The InteractionTarget field value."""
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

