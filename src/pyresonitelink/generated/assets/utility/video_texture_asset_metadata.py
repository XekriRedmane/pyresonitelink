"""Generated component: VideoTextureAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.video_texture import VideoTexture
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoTextureAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The VideoTextureAssetMetadata component turns the data at the bottom of an inspector on a video asset Type component into usable values which can be used elsewhere.

    Category: Assets/Utility

    Attach to a slot and provide a ``Texture`` to get information on in
    order for it to work.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoTextureAssetMetadata"

    def __init__(self, texture: str | IAssetProvider[VideoTexture] | None = None, size: primitives.Int2 | None = None, width: primitives.Int | None = None, height: primitives.Int | None = None, has_alpha: primitives.Bool | None = None, length: primitives.Double | None = None, playback_engine: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            size: Initial value for Size.
            width: Initial value for Width.
            height: Initial value for Height.
            has_alpha: Initial value for HasAlpha.
            length: Initial value for Length.
            playback_engine: Initial value for PlaybackEngine.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if size is not None:
            self.size = size
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if has_alpha is not None:
            self.has_alpha = has_alpha
        if length is not None:
            self.length = length
        if playback_engine is not None:
            self.playback_engine = playback_engine

    @property
    def texture(self) -> str | None:
        """The video texture to get information on."""
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
    def size(self) -> primitives.Int2 | None:
        """The size of the ``Texture`` in pixels."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Int2) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt2(value=value)
            )

    @property
    def width(self) -> primitives.Int | None:
        """The width of ``Texture`` in pixels."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Int) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldInt(value=value)
            )

    @property
    def height(self) -> primitives.Int | None:
        """The height of ``Texture`` in pixels."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Int) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldInt(value=value)
            )

    @property
    def has_alpha(self) -> primitives.Bool | None:
        """Whether ``Texture`` is transparent."""
        member = self.get_member("HasAlpha")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_alpha.setter
    def has_alpha(self, value: primitives.Bool) -> None:
        """Set the HasAlpha field value."""
        member = self.get_member("HasAlpha")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasAlpha", fields.FieldBool(value=value)
            )

    @property
    def length(self) -> primitives.Double | None:
        """The duration of ``Texture``."""
        member = self.get_member("Length")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @length.setter
    def length(self, value: primitives.Double) -> None:
        """Set the Length field value."""
        member = self.get_member("Length")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Length", fields.FieldDouble(value=value)
            )

    @property
    def playback_engine(self) -> primitives.String | None:
        """The playback engine ``Texture`` is using."""
        member = self.get_member("PlaybackEngine")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @playback_engine.setter
    def playback_engine(self, value: primitives.String) -> None:
        """Set the PlaybackEngine field value."""
        member = self.get_member("PlaybackEngine")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PlaybackEngine", fields.FieldString(value=value)
            )

