"""Generated component: SizeModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SizeModifier(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The SizeModifier component modifies the size of particles as an extra effect on top of existing size modifiers.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SizeModifier"

    def __init__(self, multiplier: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, size_clamp_min: primitives.Float3 | None = None, size_clamp_max: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            multiplier: Initial value for Multiplier.
            offset: Initial value for Offset.
            size_clamp_min: Initial value for SizeClampMin.
            size_clamp_max: Initial value for SizeClampMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if multiplier is not None:
            self.multiplier = multiplier
        if offset is not None:
            self.offset = offset
        if size_clamp_min is not None:
            self.size_clamp_min = size_clamp_min
        if size_clamp_max is not None:
            self.size_clamp_max = size_clamp_max

    @property
    def multiplier(self) -> primitives.Float3 | None:
        """How much to multiply the size of all particles."""
        member = self.get_member("Multiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiplier.setter
    def multiplier(self, value: primitives.Float3) -> None:
        """Set the Multiplier field value."""
        member = self.get_member("Multiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Multiplier", fields.FieldFloat3(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """How much to add to the size of all particles."""
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
    def size_clamp_min(self) -> primitives.Float3 | None:
        """The minimum size particles can be."""
        member = self.get_member("SizeClampMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size_clamp_min.setter
    def size_clamp_min(self, value: primitives.Float3) -> None:
        """Set the SizeClampMin field value."""
        member = self.get_member("SizeClampMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SizeClampMin", fields.FieldFloat3(value=value)
            )

    @property
    def size_clamp_max(self) -> primitives.Float3 | None:
        """The maximum size particles can be."""
        member = self.get_member("SizeClampMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size_clamp_max.setter
    def size_clamp_max(self, value: primitives.Float3) -> None:
        """Set the SizeClampMax field value."""
        member = self.get_member("SizeClampMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SizeClampMax", fields.FieldFloat3(value=value)
            )

