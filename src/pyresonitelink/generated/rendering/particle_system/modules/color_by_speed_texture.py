"""Generated component: ColorBySpeedTexture."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.wrap_mode import WrapMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorBySpeedTexture(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Color By Speed Texture component samples from the x axis of the UV depending on the min and max speeds being a 0-1 range and values beyond the range being extrapolated.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorBySpeedTexture"

    def __init__(self, min_speed: primitives.Float | None = None, max_speed: primitives.Float | None = None, u_wrap_mode: WrapMode | str | None = None, texture: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_speed: Initial value for MinSpeed.
            max_speed: Initial value for MaxSpeed.
            u_wrap_mode: Initial value for U_WrapMode.
            texture: Initial value for Texture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_speed is not None:
            self.min_speed = min_speed
        if max_speed is not None:
            self.max_speed = max_speed
        if u_wrap_mode is not None:
            self.u_wrap_mode = u_wrap_mode
        if texture is not None:
            self.texture = texture

    @property
    def min_speed(self) -> primitives.Float | None:
        """The speed the particle has to be be traveling at or under to be considered minimum speed."""
        member = self.get_member("MinSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_speed.setter
    def min_speed(self, value: primitives.Float) -> None:
        """Set the MinSpeed field value."""
        member = self.get_member("MinSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSpeed", fields.FieldFloat(value=value)
            )

    @property
    def max_speed(self) -> primitives.Float | None:
        """The speed the particle has to be be traveling at or above to be considered maximum speed."""
        member = self.get_member("MaxSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_speed.setter
    def max_speed(self, value: primitives.Float) -> None:
        """Set the MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSpeed", fields.FieldFloat(value=value)
            )

    @property
    def u_wrap_mode(self) -> WrapMode | None:
        """How to wrap around the X axis."""
        member = self.get_member("U_WrapMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WrapMode(member.value)
        return None

    @u_wrap_mode.setter
    def u_wrap_mode(self, value: WrapMode | str) -> None:
        """Set U_WrapMode. How to wrap around the X axis."""
        member = self.get_member("U_WrapMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "U_WrapMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def texture(self) -> str | None:
        """The texture to sample color from."""
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

