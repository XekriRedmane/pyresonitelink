"""Generated component: UVW_ProceduralTexture3D."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_provider import ITextureProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UVW_ProceduralTexture3D(GeneratedComponent, ITextureProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UVW_ProceduralTexture3D.

    Category: Assets/Procedural Texture3Ds
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UVW_ProceduralTexture3D"

    def __init__(self, high_priority_integration: bool | None = None, anisotropic_level: np.int32 | None = None, size: primitives.Int3 | None = None, value_offset: primitives.Float3 | None = None, value_multiplier: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            anisotropic_level: Initial value for AnisotropicLevel.
            size: Initial value for Size.
            value_offset: Initial value for ValueOffset.
            value_multiplier: Initial value for ValueMultiplier.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if size is not None:
            self.size = size
        if value_offset is not None:
            self.value_offset = value_offset
        if value_multiplier is not None:
            self.value_multiplier = value_multiplier

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def filter_mode(self) -> members.FieldEnum | None:
        """The FilterMode member."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @filter_mode.setter
    def filter_mode(self, value: members.FieldEnum) -> None:
        """Set the FilterMode member."""
        self.set_member("FilterMode", value)

    @property
    def anisotropic_level(self) -> np.int32 | None:
        """The AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anisotropic_level.setter
    def anisotropic_level(self, value: np.int32) -> None:
        """Set the AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnisotropicLevel", fields.FieldInt(value=value)
            )

    @property
    def wrap_mode_u(self) -> members.FieldEnum | None:
        """The WrapModeU member."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: members.FieldEnum) -> None:
        """Set the WrapModeU member."""
        self.set_member("WrapModeU", value)

    @property
    def wrap_mode_v(self) -> members.FieldEnum | None:
        """The WrapModeV member."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: members.FieldEnum) -> None:
        """Set the WrapModeV member."""
        self.set_member("WrapModeV", value)

    @property
    def wrap_mode_w(self) -> members.FieldEnum | None:
        """The WrapModeW member."""
        member = self.get_member("WrapModeW")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_w.setter
    def wrap_mode_w(self, value: members.FieldEnum) -> None:
        """Set the WrapModeW member."""
        self.set_member("WrapModeW", value)

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
    def value_offset(self) -> primitives.Float3 | None:
        """The ValueOffset field value."""
        member = self.get_member("ValueOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_offset.setter
    def value_offset(self, value: primitives.Float3) -> None:
        """Set the ValueOffset field value."""
        member = self.get_member("ValueOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ValueOffset", fields.FieldFloat3(value=value)
            )

    @property
    def value_multiplier(self) -> primitives.Float3 | None:
        """The ValueMultiplier field value."""
        member = self.get_member("ValueMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_multiplier.setter
    def value_multiplier(self, value: primitives.Float3) -> None:
        """Set the ValueMultiplier field value."""
        member = self.get_member("ValueMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ValueMultiplier", fields.FieldFloat3(value=value)
            )

