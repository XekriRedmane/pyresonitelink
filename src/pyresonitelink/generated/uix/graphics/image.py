"""Generated component: Image."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Image(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Image.

    Category: UIX/Graphics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Image"

    def __init__(self, sprite: str | IAssetProvider[Sprite] | None = None, material: str | IAssetProvider[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sprite: Initial value for Sprite.
            material: Initial value for Material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sprite is not None:
            self.sprite = sprite
        if material is not None:
            self.material = material

    @property
    def sprite(self) -> str | None:
        """Target ID of the Sprite reference (targets IAssetProvider[Sprite])."""
        member = self.get_member("Sprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite.setter
    def sprite(self, target: str | IAssetProvider[Sprite] | None) -> None:
        """Set the Sprite reference by target ID or IAssetProvider[Sprite] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Sprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Sprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Sprite>'),
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
    def preserve_aspect(self) -> bool | None:
        """The PreserveAspect field value."""
        member = self.get_member("PreserveAspect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_aspect.setter
    def preserve_aspect(self, value: bool) -> None:
        """Set the PreserveAspect field value."""
        member = self.get_member("PreserveAspect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveAspect", fields.FieldBool(value=value)
            )

    @property
    def nine_slice_sizing(self) -> members.FieldEnum | None:
        """The NineSliceSizing member."""
        member = self.get_member("NineSliceSizing")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @nine_slice_sizing.setter
    def nine_slice_sizing(self, value: members.FieldEnum) -> None:
        """Set the NineSliceSizing member."""
        self.set_member("NineSliceSizing", value)

    @property
    def flip_horizontally(self) -> bool | None:
        """The FlipHorizontally field value."""
        member = self.get_member("FlipHorizontally")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_horizontally.setter
    def flip_horizontally(self, value: bool) -> None:
        """Set the FlipHorizontally field value."""
        member = self.get_member("FlipHorizontally")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipHorizontally", fields.FieldBool(value=value)
            )

    @property
    def flip_vertically(self) -> bool | None:
        """The FlipVertically field value."""
        member = self.get_member("FlipVertically")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_vertically.setter
    def flip_vertically(self, value: bool) -> None:
        """Set the FlipVertically field value."""
        member = self.get_member("FlipVertically")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipVertically", fields.FieldBool(value=value)
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
    def legacy_zwrite(self) -> bool | None:
        """The __legacyZWrite field value."""
        member = self.get_member("__legacyZWrite")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_zwrite.setter
    def legacy_zwrite(self, value: bool) -> None:
        """Set the __legacyZWrite field value."""
        member = self.get_member("__legacyZWrite")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyZWrite", fields.FieldBool(value=value)
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

