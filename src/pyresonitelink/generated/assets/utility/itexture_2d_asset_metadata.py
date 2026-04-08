"""Generated component: ITexture2DAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ITexture2DAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ITexture2DAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ITexture2DAssetMetadata"

    def __init__(self, texture: str | IAssetProvider[ITexture2D] | None = None, *, component: workers.Component | None = None) -> None:
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
    def size(self) -> members.EmptyElement | None:
        """The Size member."""
        member = self.get_member("Size")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @size.setter
    def size(self, value: members.EmptyElement) -> None:
        """Set the Size member."""
        self.set_member("Size", value)

    @property
    def width(self) -> members.EmptyElement | None:
        """The Width member."""
        member = self.get_member("Width")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @width.setter
    def width(self, value: members.EmptyElement) -> None:
        """Set the Width member."""
        self.set_member("Width", value)

    @property
    def height(self) -> members.EmptyElement | None:
        """The Height member."""
        member = self.get_member("Height")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @height.setter
    def height(self, value: members.EmptyElement) -> None:
        """Set the Height member."""
        self.set_member("Height", value)

