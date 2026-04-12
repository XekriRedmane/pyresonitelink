"""Generated component: AmbientLightSH2."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.spherical_harmonics_l2 import SphericalHarmonicsL2
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AmbientLightSH2(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The Ambient Light SH2 component creates ambient lighting data that creates global colored light using sampling from a Level 2 Spherical Harmonic type ColorX.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AmbientLightSH2"

    def __init__(self, ambient_light: SphericalHarmonicsL2 | str | None = None, is_active: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ambient_light: Initial value for AmbientLight.
            is_active: Initial value for IsActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ambient_light is not None:
            self.ambient_light = ambient_light
        if is_active is not None:
            self.is_active = is_active

    @property
    def ambient_light(self) -> SphericalHarmonicsL2 | None:
        """The spherical harmonic to sample for ambient lighting."""
        member = self.get_member("AmbientLight")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SphericalHarmonicsL2(member.value)
        return None

    @ambient_light.setter
    def ambient_light(self, value: SphericalHarmonicsL2 | str) -> None:
        """Set AmbientLight. The spherical harmonic to sample for ambient lighting."""
        member = self.get_member("AmbientLight")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AmbientLight",
                members.FieldEnum(value=str(value)),
            )

    @property
    def is_active(self) -> primitives.Bool | None:
        """The IsActive field value."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: primitives.Bool) -> None:
        """Set the IsActive field value."""
        member = self.get_member("IsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsActive", fields.FieldBool(value=value)
            )

    async def set_active(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Make this ambient lighting component the current world ambient light.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetActive", {}, debug,
        )

