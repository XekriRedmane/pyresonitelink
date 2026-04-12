"""Generated component: ColorFromTexture3D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorFromTexture3D(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The ColorFromTexture3D component makes particles sample their color from the color in their same position within a Texture3D.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorFromTexture3D"

    def __init__(self, texture_3d: str | IAssetProvider[Texture3D] | None = None, scale: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture_3d: Initial value for Texture3D.
            scale: Initial value for Scale.
            offset: Initial value for Offset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture_3d is not None:
            self.texture_3d = texture_3d
        if scale is not None:
            self.scale = scale
        if offset is not None:
            self.offset = offset

    @property
    def texture_3d(self) -> str | None:
        """The 3D texture to sample from."""
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
    def scale(self) -> primitives.Float3 | None:
        """How much bias to choose higher axis values. The default is 1 which is no bias."""
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
        """How much to add to the chosen point in the 3D texture, which can cut off lower or higher values from ever being chosen."""
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

