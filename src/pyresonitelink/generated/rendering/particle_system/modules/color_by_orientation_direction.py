"""Generated component: ColorByOrientationDirection."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorByOrientationDirection(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The ColorByOrientationDirection component is used to make particles change color depending on their dot product of their orientation to a reference orientation. Dot product essentially means how close in terms of angle is one direction to another. The colors when in-between are lerped.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorByOrientationDirection"

    def __init__(self, reference_direction: primitives.Float3 | None = None, aligned_color: primitives.ColorX | None = None, orthogonal_color: primitives.ColorX | None = None, opposite_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference_direction: Initial value for ReferenceDirection.
            aligned_color: Initial value for AlignedColor.
            orthogonal_color: Initial value for OrthogonalColor.
            opposite_color: Initial value for OppositeColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference_direction is not None:
            self.reference_direction = reference_direction
        if aligned_color is not None:
            self.aligned_color = aligned_color
        if orthogonal_color is not None:
            self.orthogonal_color = orthogonal_color
        if opposite_color is not None:
            self.opposite_color = opposite_color

    @property
    def reference_direction(self) -> primitives.Float3 | None:
        """The direction in local space that is being used as a reference."""
        member = self.get_member("ReferenceDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_direction.setter
    def reference_direction(self, value: primitives.Float3) -> None:
        """Set the ReferenceDirection field value."""
        member = self.get_member("ReferenceDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReferenceDirection", fields.FieldFloat3(value=value)
            )

    @property
    def aligned_color(self) -> primitives.ColorX | None:
        """The color to use if the particle's orientation is exactly the same direction as ``ReferenceDirection``."""
        member = self.get_member("AlignedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aligned_color.setter
    def aligned_color(self, value: primitives.ColorX) -> None:
        """Set the AlignedColor field value."""
        member = self.get_member("AlignedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlignedColor", fields.FieldColorX(value=value)
            )

    @property
    def orthogonal_color(self) -> primitives.ColorX | None:
        """The color to use if the particle's orientation is exactly 90 degrees to ``ReferenceDirection``. This 90 degrees falls onto any particle direction that is along the surface of a plane facing the same direction as ``ReferenceDirection``."""
        member = self.get_member("OrthogonalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orthogonal_color.setter
    def orthogonal_color(self, value: primitives.ColorX) -> None:
        """Set the OrthogonalColor field value."""
        member = self.get_member("OrthogonalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrthogonalColor", fields.FieldColorX(value=value)
            )

    @property
    def opposite_color(self) -> primitives.ColorX | None:
        """The color if the particle's orientation is exactly opposite of ``ReferenceDirection``."""
        member = self.get_member("OppositeColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @opposite_color.setter
    def opposite_color(self, value: primitives.ColorX) -> None:
        """Set the OppositeColor field value."""
        member = self.get_member("OppositeColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OppositeColor", fields.FieldColorX(value=value)
            )

