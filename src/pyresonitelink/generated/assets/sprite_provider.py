"""Generated component: SpriteProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SpriteProvider(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """A SpriteProvider defines a slice of a Texture2D as a Sprite that may be used by other components e.g. UIX Images to display graphics or produce backgrounds.

    Category: Assets

    **Behavior**: Sprite providers due to the current Unity implementation at the time of writing this have issues with switching images very quickly. They will often flash white, causing a health hazard to photo sensitive users. Having all the sprites on UIX elements at once and switching their ``OrderOffset`` to change which element renders on top will remove the flashing and is currently the only way to combat this issue.

Using SpriteProvider to break up a sprite-sheet of iconography:

By combining multiple icons/elements in a grid-like texture, you can reduce the size of your objects and improve load performance by reusing the same texture for multiple sprites. Please note that the ``Rect`` values are floating point percentages of the texture were 1 would equal 100%, so 1/4 or 25% would be 0.25 in floating point value. 

The ``Rect`` first x,y values are from the LOWER LEFT of the texture being 0.0, 0.0, where the total inclusion of the cut out texture sprite is a percentage of the width and height in the second x,y values. 

Example: Given if you take a 1024x1024 px sprite sheet texture.
* Divide the height and width by 4 to make 12 equal sprite slots of 256x256 px chunks
* A sprite texture on the second column from the left and on the third row from the bottom would be ``Rect``: x: 0.25 y: 0.50 x: 0.25 y: 0.25

See attached example diagram for help.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SpriteProvider"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, texture: str | IAssetProvider[ITexture2D] | None = None, rect: primitives.Rect | None = None, borders: primitives.Float4 | None = None, scale: primitives.Float | None = None, fixed_size: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            texture: Initial value for Texture.
            rect: Initial value for Rect.
            borders: Initial value for Borders.
            scale: Initial value for Scale.
            fixed_size: Initial value for FixedSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if texture is not None:
            self.texture = texture
        if rect is not None:
            self.rect = rect
        if borders is not None:
            self.borders = borders
        if scale is not None:
            self.scale = scale
        if fixed_size is not None:
            self.fixed_size = fixed_size

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def texture(self) -> str | None:
        """The sprite to provide."""
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
    def rect(self) -> primitives.Rect | None:
        """The rectangle within the sprite to render. Note that the second x and y are actually the width and height of the Rect. The values are proportions of the width and height of the image in the Texture property."""
        member = self.get_member("Rect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect.setter
    def rect(self, value: primitives.Rect) -> None:
        """Set the Rect field value."""
        member = self.get_member("Rect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rect", fields.FieldRect(value=value)
            )

    @property
    def borders(self) -> primitives.Float4 | None:
        """Border widths for 9-slice scaling. The XYZW components set the left, bottom, right, and top borders respectively."""
        member = self.get_member("Borders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @borders.setter
    def borders(self, value: primitives.Float4) -> None:
        """Set the Borders field value."""
        member = self.get_member("Borders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Borders", fields.FieldFloat4(value=value)
            )

    @property
    def scale(self) -> primitives.Float | None:
        """Effects the center size when 9 slicing."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat(value=value)
            )

    @property
    def fixed_size(self) -> primitives.Float | None:
        """Effects the center size when 9 slicing."""
        member = self.get_member("FixedSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fixed_size.setter
    def fixed_size(self, value: primitives.Float) -> None:
        """Set the FixedSize field value."""
        member = self.get_member("FixedSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixedSize", fields.FieldFloat(value=value)
            )

