"""Generated component: Texture3DAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Texture3DAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Texture3DAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Texture3DAssetMetadata"

    def __init__(self, texture: str | IAssetProvider[Texture3D] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Texture reference (targets IAssetProvider[Texture3D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
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
    def depth(self) -> members.EmptyElement | None:
        """The Depth member."""
        member = self.get_member("Depth")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @depth.setter
    def depth(self, value: members.EmptyElement) -> None:
        """Set the Depth member."""
        self.set_member("Depth", value)

    @property
    def memory_bytes(self) -> members.EmptyElement | None:
        """The MemoryBytes member."""
        member = self.get_member("MemoryBytes")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @memory_bytes.setter
    def memory_bytes(self, value: members.EmptyElement) -> None:
        """Set the MemoryBytes member."""
        self.set_member("MemoryBytes", value)

    @property
    def formatted_memory_bytes(self) -> members.EmptyElement | None:
        """The FormattedMemoryBytes member."""
        member = self.get_member("FormattedMemoryBytes")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @formatted_memory_bytes.setter
    def formatted_memory_bytes(self, value: members.EmptyElement) -> None:
        """Set the FormattedMemoryBytes member."""
        self.set_member("FormattedMemoryBytes", value)

    @property
    def format_(self) -> members.EmptyElement | None:
        """The Format member."""
        member = self.get_member("Format")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @format_.setter
    def format_(self, value: members.EmptyElement) -> None:
        """Set the Format member."""
        self.set_member("Format", value)

    @property
    def actual_loaded_variant(self) -> members.EmptyElement | None:
        """The ActualLoadedVariant member."""
        member = self.get_member("ActualLoadedVariant")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @actual_loaded_variant.setter
    def actual_loaded_variant(self, value: members.EmptyElement) -> None:
        """Set the ActualLoadedVariant member."""
        self.set_member("ActualLoadedVariant", value)

    @property
    def profile(self) -> members.EmptyElement | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @profile.setter
    def profile(self, value: members.EmptyElement) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

