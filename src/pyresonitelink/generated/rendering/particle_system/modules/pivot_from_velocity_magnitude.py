"""Generated component: PivotFromVelocityMagnitude."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PivotFromVelocityMagnitude(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Pivot From Velocity Magnitude component is used in Photon Dust to make particles rotate based on their velocity direction on a pivot.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.PivotFromVelocityMagnitude"

    def __init__(self, pivot_base_offset: primitives.Float3 | None = None, pivot_clamp_min: primitives.Float3 | None = None, pivot_clamp_max: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pivot_base_offset: Initial value for PivotBaseOffset.
            pivot_clamp_min: Initial value for PivotClampMin.
            pivot_clamp_max: Initial value for PivotClampMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pivot_base_offset is not None:
            self.pivot_base_offset = pivot_base_offset
        if pivot_clamp_min is not None:
            self.pivot_clamp_min = pivot_clamp_min
        if pivot_clamp_max is not None:
            self.pivot_clamp_max = pivot_clamp_max

    @property
    def pivot_base_offset(self) -> primitives.Float3 | None:
        """The PivotBaseOffset field value."""
        member = self.get_member("PivotBaseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pivot_base_offset.setter
    def pivot_base_offset(self, value: primitives.Float3) -> None:
        """Set the PivotBaseOffset field value."""
        member = self.get_member("PivotBaseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PivotBaseOffset", fields.FieldFloat3(value=value)
            )

    @property
    def pivot_clamp_min(self) -> primitives.Float3 | None:
        """The PivotClampMin field value."""
        member = self.get_member("PivotClampMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pivot_clamp_min.setter
    def pivot_clamp_min(self, value: primitives.Float3) -> None:
        """Set the PivotClampMin field value."""
        member = self.get_member("PivotClampMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PivotClampMin", fields.FieldFloat3(value=value)
            )

    @property
    def pivot_clamp_max(self) -> primitives.Float3 | None:
        """The PivotClampMax field value."""
        member = self.get_member("PivotClampMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pivot_clamp_max.setter
    def pivot_clamp_max(self, value: primitives.Float3) -> None:
        """Set the PivotClampMax field value."""
        member = self.get_member("PivotClampMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PivotClampMax", fields.FieldFloat3(value=value)
            )

