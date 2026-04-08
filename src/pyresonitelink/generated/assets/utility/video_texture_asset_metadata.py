"""Generated component: VideoTextureAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.video_texture import VideoTexture
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoTextureAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VideoTextureAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoTextureAssetMetadata"

    def __init__(self, texture: str | IAssetProvider[VideoTexture] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Texture reference (targets IAssetProvider[VideoTexture])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[VideoTexture] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[VideoTexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.VideoTexture>'),
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

    @property
    def has_alpha(self) -> members.EmptyElement | None:
        """The HasAlpha member."""
        member = self.get_member("HasAlpha")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_alpha.setter
    def has_alpha(self, value: members.EmptyElement) -> None:
        """Set the HasAlpha member."""
        self.set_member("HasAlpha", value)

    @property
    def length(self) -> members.EmptyElement | None:
        """The Length member."""
        member = self.get_member("Length")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @length.setter
    def length(self, value: members.EmptyElement) -> None:
        """Set the Length member."""
        self.set_member("Length", value)

    @property
    def playback_engine(self) -> members.EmptyElement | None:
        """The PlaybackEngine member."""
        member = self.get_member("PlaybackEngine")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @playback_engine.setter
    def playback_engine(self, value: members.EmptyElement) -> None:
        """Set the PlaybackEngine member."""
        self.set_member("PlaybackEngine", value)

