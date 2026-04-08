"""Generated component: Texture3D_Force."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Texture3D_Force(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.Texture3D_Force.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.Texture3D_Force"

    def __init__(self, texture_3d: str | IAssetProvider[Texture3D] | None = None, strength: primitives.Float | None = None, scale: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, color_bias: primitives.Float | None = None, color_scale: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture_3d: Initial value for Texture3D.
            strength: Initial value for Strength.
            scale: Initial value for Scale.
            offset: Initial value for Offset.
            color_bias: Initial value for ColorBias.
            color_scale: Initial value for ColorScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture_3d is not None:
            self.texture_3d = texture_3d
        if strength is not None:
            self.strength = strength
        if scale is not None:
            self.scale = scale
        if offset is not None:
            self.offset = offset
        if color_bias is not None:
            self.color_bias = color_bias
        if color_scale is not None:
            self.color_scale = color_scale

    @property
    def texture_3d(self) -> str | None:
        """Target ID of the Texture3D reference (targets IAssetProvider[Texture3D])."""
        member = self.get_member("Texture3D")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture_3d.setter
    def texture_3d(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the Texture3D reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture3D")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture3D",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

    @property
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

    @property
    def strength(self) -> primitives.Float | None:
        """The Strength field value."""
        member = self.get_member("Strength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strength.setter
    def strength(self, value: primitives.Float) -> None:
        """Set the Strength field value."""
        member = self.get_member("Strength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Strength", fields.FieldFloat(value=value)
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def color_bias(self) -> primitives.Float | None:
        """The ColorBias field value."""
        member = self.get_member("ColorBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_bias.setter
    def color_bias(self, value: primitives.Float) -> None:
        """Set the ColorBias field value."""
        member = self.get_member("ColorBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorBias", fields.FieldFloat(value=value)
            )

    @property
    def color_scale(self) -> primitives.Float | None:
        """The ColorScale field value."""
        member = self.get_member("ColorScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_scale.setter
    def color_scale(self, value: primitives.Float) -> None:
        """Set the ColorScale field value."""
        member = self.get_member("ColorScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorScale", fields.FieldFloat(value=value)
            )

