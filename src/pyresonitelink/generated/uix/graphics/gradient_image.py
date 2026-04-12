"""Generated component: GradientImage."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.nine_slice_sizing import NineSliceSizing
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GradientImage(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """The GradiantImage component takes in a SpriteProvider or Material and controls the image color using the four corners of the image, then gradients them into the image.

}}

    Category: UIX/Graphics

    You can make fancy effects and icons using this component, especially if
    your hue shifting the different color corners.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.GradientImage"

    def __init__(self, sprite: str | IAssetProvider[Sprite] | None = None, material: str | IAssetProvider[Material] | None = None, preserve_aspect: primitives.Bool | None = None, nine_slice_sizing: NineSliceSizing | str | None = None, flip_horizontally: primitives.Bool | None = None, flip_vertically: primitives.Bool | None = None, interaction_target: primitives.Bool | None = None, fill_rect: primitives.Rect | None = None, legacy_zwrite: primitives.Bool | None = None, tint_top_left: primitives.ColorX | None = None, tint_top_right: primitives.ColorX | None = None, tint_bottom_right: primitives.ColorX | None = None, tint_bottom_left: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sprite: Initial value for Sprite.
            material: Initial value for Material.
            preserve_aspect: Initial value for PreserveAspect.
            nine_slice_sizing: Initial value for NineSliceSizing.
            flip_horizontally: Initial value for FlipHorizontally.
            flip_vertically: Initial value for FlipVertically.
            interaction_target: Initial value for InteractionTarget.
            fill_rect: Initial value for FillRect.
            legacy_zwrite: Initial value for __legacyZWrite.
            tint_top_left: Initial value for TintTopLeft.
            tint_top_right: Initial value for TintTopRight.
            tint_bottom_right: Initial value for TintBottomRight.
            tint_bottom_left: Initial value for TintBottomLeft.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sprite is not None:
            self.sprite = sprite
        if material is not None:
            self.material = material
        if preserve_aspect is not None:
            self.preserve_aspect = preserve_aspect
        if nine_slice_sizing is not None:
            self.nine_slice_sizing = nine_slice_sizing
        if flip_horizontally is not None:
            self.flip_horizontally = flip_horizontally
        if flip_vertically is not None:
            self.flip_vertically = flip_vertically
        if interaction_target is not None:
            self.interaction_target = interaction_target
        if fill_rect is not None:
            self.fill_rect = fill_rect
        if legacy_zwrite is not None:
            self.legacy_zwrite = legacy_zwrite
        if tint_top_left is not None:
            self.tint_top_left = tint_top_left
        if tint_top_right is not None:
            self.tint_top_right = tint_top_right
        if tint_bottom_right is not None:
            self.tint_bottom_right = tint_bottom_right
        if tint_bottom_left is not None:
            self.tint_bottom_left = tint_bottom_left

    @property
    def sprite(self) -> str | None:
        """The sprite to use as the image."""
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
        """The Material to use as the image."""
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
    def preserve_aspect(self) -> primitives.Bool | None:
        """Preserves the aspect ratio of this image provided."""
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
    def nine_slice_sizing(self) -> NineSliceSizing | None:
        """Tells how the image gets 9-sliced on this UIX."""
        member = self.get_member("NineSliceSizing")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return NineSliceSizing(member.value)
        return None

    @nine_slice_sizing.setter
    def nine_slice_sizing(self, value: NineSliceSizing | str) -> None:
        """Set NineSliceSizing. Tells how the image gets 9-sliced on this UIX."""
        member = self.get_member("NineSliceSizing")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "NineSliceSizing",
                members.FieldEnum(value=str(value)),
            )

    @property
    def flip_horizontally(self) -> primitives.Bool | None:
        """Flips the image horizontally (but not the color)."""
        member = self.get_member("FlipHorizontally")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_horizontally.setter
    def flip_horizontally(self, value: primitives.Bool) -> None:
        """Set the FlipHorizontally field value."""
        member = self.get_member("FlipHorizontally")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipHorizontally", fields.FieldBool(value=value)
            )

    @property
    def flip_vertically(self) -> primitives.Bool | None:
        """Flips the image vertically (but not the color)."""
        member = self.get_member("FlipVertically")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_vertically.setter
    def flip_vertically(self, value: primitives.Bool) -> None:
        """Set the FlipVertically field value."""
        member = self.get_member("FlipVertically")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipVertically", fields.FieldBool(value=value)
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
    def legacy_zwrite(self) -> primitives.Bool | None:
        """The legacy Z writing for this image."""
        member = self.get_member("__legacyZWrite")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_zwrite.setter
    def legacy_zwrite(self, value: primitives.Bool) -> None:
        """Set the __legacyZWrite field value."""
        member = self.get_member("__legacyZWrite")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyZWrite", fields.FieldBool(value=value)
            )

    @property
    def tint_top_left(self) -> primitives.ColorX | None:
        """The color of this top left corner."""
        member = self.get_member("TintTopLeft")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_top_left.setter
    def tint_top_left(self, value: primitives.ColorX) -> None:
        """Set the TintTopLeft field value."""
        member = self.get_member("TintTopLeft")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintTopLeft", fields.FieldColorX(value=value)
            )

    @property
    def tint_top_right(self) -> primitives.ColorX | None:
        """The color of this top right corner."""
        member = self.get_member("TintTopRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_top_right.setter
    def tint_top_right(self, value: primitives.ColorX) -> None:
        """Set the TintTopRight field value."""
        member = self.get_member("TintTopRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintTopRight", fields.FieldColorX(value=value)
            )

    @property
    def tint_bottom_right(self) -> primitives.ColorX | None:
        """The color of this bottom right corner."""
        member = self.get_member("TintBottomRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_bottom_right.setter
    def tint_bottom_right(self, value: primitives.ColorX) -> None:
        """Set the TintBottomRight field value."""
        member = self.get_member("TintBottomRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintBottomRight", fields.FieldColorX(value=value)
            )

    @property
    def tint_bottom_left(self) -> primitives.ColorX | None:
        """The color of this bottom left corner."""
        member = self.get_member("TintBottomLeft")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_bottom_left.setter
    def tint_bottom_left(self, value: primitives.ColorX) -> None:
        """Set the TintBottomLeft field value."""
        member = self.get_member("TintBottomLeft")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintBottomLeft", fields.FieldColorX(value=value)
            )

