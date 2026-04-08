"""Generated component: Texture3DAssetMetadata."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
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

    def __init__(self, texture: str | IAssetProvider[Texture3D] | None = None, size: primitives.Int3 | None = None, width: np.int32 | None = None, height: np.int32 | None = None, depth: np.int32 | None = None, memory_bytes: np.int64 | None = None, formatted_memory_bytes: str | None = None, actual_loaded_variant: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            size: Initial value for Size.
            width: Initial value for Width.
            height: Initial value for Height.
            depth: Initial value for Depth.
            memory_bytes: Initial value for MemoryBytes.
            formatted_memory_bytes: Initial value for FormattedMemoryBytes.
            actual_loaded_variant: Initial value for ActualLoadedVariant.
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
        if depth is not None:
            self.depth = depth
        if memory_bytes is not None:
            self.memory_bytes = memory_bytes
        if formatted_memory_bytes is not None:
            self.formatted_memory_bytes = formatted_memory_bytes
        if actual_loaded_variant is not None:
            self.actual_loaded_variant = actual_loaded_variant

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
    def size(self) -> primitives.Int3 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Int3) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt3(value=value)
            )

    @property
    def width(self) -> np.int32 | None:
        """The Width field value."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: np.int32) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldInt(value=value)
            )

    @property
    def height(self) -> np.int32 | None:
        """The Height field value."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: np.int32) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldInt(value=value)
            )

    @property
    def depth(self) -> np.int32 | None:
        """The Depth field value."""
        member = self.get_member("Depth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth.setter
    def depth(self, value: np.int32) -> None:
        """Set the Depth field value."""
        member = self.get_member("Depth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Depth", fields.FieldInt(value=value)
            )

    @property
    def memory_bytes(self) -> np.int64 | None:
        """The MemoryBytes field value."""
        member = self.get_member("MemoryBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @memory_bytes.setter
    def memory_bytes(self, value: np.int64) -> None:
        """Set the MemoryBytes field value."""
        member = self.get_member("MemoryBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MemoryBytes", fields.FieldLong(value=value)
            )

    @property
    def formatted_memory_bytes(self) -> str | None:
        """The FormattedMemoryBytes field value."""
        member = self.get_member("FormattedMemoryBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @formatted_memory_bytes.setter
    def formatted_memory_bytes(self, value: str) -> None:
        """Set the FormattedMemoryBytes field value."""
        member = self.get_member("FormattedMemoryBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormattedMemoryBytes", fields.FieldString(value=value)
            )

    @property
    def format_(self) -> members.FieldEnum | None:
        """The Format member."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @format_.setter
    def format_(self, value: members.FieldEnum) -> None:
        """Set the Format member."""
        self.set_member("Format", value)

    @property
    def actual_loaded_variant(self) -> str | None:
        """The ActualLoadedVariant field value."""
        member = self.get_member("ActualLoadedVariant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_loaded_variant.setter
    def actual_loaded_variant(self, value: str) -> None:
        """Set the ActualLoadedVariant field value."""
        member = self.get_member("ActualLoadedVariant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActualLoadedVariant", fields.FieldString(value=value)
            )

    @property
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

