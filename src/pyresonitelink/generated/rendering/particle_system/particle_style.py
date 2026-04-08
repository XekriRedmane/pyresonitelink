"""Generated component: ParticleStyle."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleStyle(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleStyle.

    Category: Rendering/Particle System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleStyle"

    def __init__(self, renderer: str | IParticleRenderer | None = None, use_system_local_scale: primitives.Bool | None = None, use_system_local_rotation: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            renderer: Initial value for Renderer.
            use_system_local_scale: Initial value for UseSystemLocalScale.
            use_system_local_rotation: Initial value for UseSystemLocalRotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if renderer is not None:
            self.renderer = renderer
        if use_system_local_scale is not None:
            self.use_system_local_scale = use_system_local_scale
        if use_system_local_rotation is not None:
            self.use_system_local_rotation = use_system_local_rotation

    @property
    def renderer(self) -> str | None:
        """Target ID of the Renderer reference (targets IParticleRenderer)."""
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | IParticleRenderer | None) -> None:
        """Set the Renderer reference by target ID or IParticleRenderer instance."""
        target_id: str | None = target.id if isinstance(target, IParticleRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.IParticleRenderer'),
            )

    @property
    def modules(self) -> members.SyncList | None:
        """The Modules member."""
        member = self.get_member("Modules")
        if isinstance(member, members.SyncList):
            return member
        return None

    @modules.setter
    def modules(self, value: members.SyncList) -> None:
        """Set the Modules member."""
        self.set_member("Modules", value)

    @property
    def use_system_local_scale(self) -> primitives.Bool | None:
        """The UseSystemLocalScale field value."""
        member = self.get_member("UseSystemLocalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_system_local_scale.setter
    def use_system_local_scale(self, value: primitives.Bool) -> None:
        """Set the UseSystemLocalScale field value."""
        member = self.get_member("UseSystemLocalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSystemLocalScale", fields.FieldBool(value=value)
            )

    @property
    def particle_scale_mode(self) -> members.FieldEnum | None:
        """The ParticleScaleMode member."""
        member = self.get_member("ParticleScaleMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @particle_scale_mode.setter
    def particle_scale_mode(self, value: members.FieldEnum) -> None:
        """Set the ParticleScaleMode member."""
        self.set_member("ParticleScaleMode", value)

    @property
    def use_system_local_rotation(self) -> primitives.Bool | None:
        """The UseSystemLocalRotation field value."""
        member = self.get_member("UseSystemLocalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_system_local_rotation.setter
    def use_system_local_rotation(self, value: primitives.Bool) -> None:
        """Set the UseSystemLocalRotation field value."""
        member = self.get_member("UseSystemLocalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSystemLocalRotation", fields.FieldBool(value=value)
            )

