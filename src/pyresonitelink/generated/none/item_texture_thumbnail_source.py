"""Generated component: ItemTextureThumbnailSource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.iitem_thumbnail_source import IItemThumbnailSource
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ItemTextureThumbnailSource(GeneratedComponent, IItemThumbnailSource, ICustomInspector, IWorldEventReceiver):
    """The ItemTextureThumbnailSource component can be used to customize the inventory preview of an item, setting it to a texture.

    To work, the component needs to be attached to the object's root slot
    and have an image in its ``Texture``. The ``Ensure single thumbnail
    source`` button can be used to remove all other instances of the
    component in the item's hierarchy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ItemTextureThumbnailSource"

    def __init__(self, texture: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture

    @property
    def texture(self) -> str | None:
        """The texture that should be used as the item's inventory preview. If null, the component will be ignored."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def crop(self) -> members.FieldEnum | None:
        """The rectangle that defines what section of the image to use. (Or null to use the entire image)"""
        member = self.get_member("Crop")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @crop.setter
    def crop(self, value: members.FieldEnum) -> None:
        """Set Crop. The rectangle that defines what section of the image to use. (Or null to use the entire image)"""
        self.set_member("Crop", value)

