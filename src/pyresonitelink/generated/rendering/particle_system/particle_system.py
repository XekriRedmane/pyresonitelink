"""Generated component: ParticleSystem."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_style import ParticleStyle
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleSystem(GeneratedComponent, ICustomInspector, IRenderable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleSystem.

    Category: Rendering/Particle System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleSystem"

    def __init__(self, max_particle_count: np.int32 | None = None, style: str | ParticleStyle | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_particle_count: Initial value for MaxParticleCount.
            style: Initial value for Style.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_particle_count is not None:
            self.max_particle_count = max_particle_count
        if style is not None:
            self.style = style

    @property
    def max_particle_count(self) -> np.int32 | None:
        """The MaxParticleCount field value."""
        member = self.get_member("MaxParticleCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_particle_count.setter
    def max_particle_count(self, value: np.int32) -> None:
        """Set the MaxParticleCount field value."""
        member = self.get_member("MaxParticleCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxParticleCount", fields.FieldInt(value=value)
            )

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets ParticleStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | ParticleStyle | None) -> None:
        """Set the Style reference by target ID or ParticleStyle instance."""
        target_id: str | None = target.id if isinstance(target, ParticleStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleStyle'),
            )

    @property
    def simulation_space(self) -> members.SyncObject | None:
        """The SimulationSpace member."""
        member = self.get_member("SimulationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @simulation_space.setter
    def simulation_space(self, value: members.SyncObject) -> None:
        """Set the SimulationSpace member."""
        self.set_member("SimulationSpace", value)

