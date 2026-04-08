"""Generated component: TextureCharacterControllerModifier."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureCharacterControllerModifier(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextureCharacterControllerModifier.

    Category: Locomotion/Modifiers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureCharacterControllerModifier"

    def __init__(self, min_value: np.float32 | None = None, max_value: np.float32 | None = None, texture: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            texture: Initial value for Texture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if texture is not None:
            self.texture = texture

    @property
    def parameter(self) -> members.FieldEnum | None:
        """The Parameter member."""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @parameter.setter
    def parameter(self, value: members.FieldEnum) -> None:
        """Set the Parameter member."""
        self.set_member("Parameter", value)

    @property
    def modification_mode(self) -> members.FieldEnum | None:
        """The ModificationMode member."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @modification_mode.setter
    def modification_mode(self, value: members.FieldEnum) -> None:
        """Set the ModificationMode member."""
        self.set_member("ModificationMode", value)

    @property
    def min_value(self) -> np.float32 | None:
        """The MinValue field value."""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: np.float32) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldFloat(value=value)
            )

    @property
    def max_value(self) -> np.float32 | None:
        """The MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: np.float32) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldFloat(value=value)
            )

    @property
    def channel(self) -> members.FieldEnum | None:
        """The Channel member."""
        member = self.get_member("Channel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @channel.setter
    def channel(self, value: members.FieldEnum) -> None:
        """Set the Channel member."""
        self.set_member("Channel", value)

    @property
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets IAssetProvider[Texture2D])."""
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

