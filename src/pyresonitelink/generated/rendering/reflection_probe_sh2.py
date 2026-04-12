"""Generated component: ReflectionProbeSH2."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.spherical_harmonics_l2 import SphericalHarmonicsL2
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.reflection_probe import ReflectionProbe
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReflectionProbeSH2(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The Reflection Probe SH2 component is used to turn what a ReflectionProbe sees into a spherical harmonic for use in ambient lighting like a AmbientLightSH2 component.

    Category: Rendering

    Can be used to drive a AmbientLightSH2 component via a value copy or by
    drag and dropping this component's ``AmbientLight`` into that
    component's value
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionProbeSH2"

    def __init__(self, probe: str | ReflectionProbe | None = None, ambient_light: SphericalHarmonicsL2 | str | None = None, order0_scale: primitives.Float | None = None, order1_scale: primitives.Float | None = None, order2_scale: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            probe: Initial value for Probe.
            ambient_light: Initial value for AmbientLight.
            order0_scale: Initial value for Order0Scale.
            order1_scale: Initial value for Order1Scale.
            order2_scale: Initial value for Order2Scale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if probe is not None:
            self.probe = probe
        if ambient_light is not None:
            self.ambient_light = ambient_light
        if order0_scale is not None:
            self.order0_scale = order0_scale
        if order1_scale is not None:
            self.order1_scale = order1_scale
        if order2_scale is not None:
            self.order2_scale = order2_scale

    @property
    def probe(self) -> str | None:
        """The probe to get color data from."""
        member = self.get_member("Probe")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @probe.setter
    def probe(self, target: str | ReflectionProbe | None) -> None:
        """Set the Probe reference by target ID or ReflectionProbe instance."""
        target_id: str | None = target.id if isinstance(target, ReflectionProbe) else target  # type: ignore[assignment]
        member = self.get_member("Probe")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Probe",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ReflectionProbe'),
            )

    @property
    def ambient_light(self) -> SphericalHarmonicsL2 | None:
        """``Probe``'s sampled data as SH2 color data for ambient lighting usage."""
        member = self.get_member("AmbientLight")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SphericalHarmonicsL2(member.value)
        return None

    @ambient_light.setter
    def ambient_light(self, value: SphericalHarmonicsL2 | str) -> None:
        """Set AmbientLight. ``Probe``'s sampled data as SH2 color data for ambient lighting usage."""
        member = self.get_member("AmbientLight")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AmbientLight",
                members.FieldEnum(value=str(value)),
            )

    @property
    def order0_scale(self) -> primitives.Float | None:
        """The scale factor for Order 0 for the spherical harmonics."""
        member = self.get_member("Order0Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order0_scale.setter
    def order0_scale(self, value: primitives.Float) -> None:
        """Set the Order0Scale field value."""
        member = self.get_member("Order0Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Order0Scale", fields.FieldFloat(value=value)
            )

    @property
    def order1_scale(self) -> primitives.Float | None:
        """The scale factor for Order 1 for the spherical harmonics."""
        member = self.get_member("Order1Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order1_scale.setter
    def order1_scale(self, value: primitives.Float) -> None:
        """Set the Order1Scale field value."""
        member = self.get_member("Order1Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Order1Scale", fields.FieldFloat(value=value)
            )

    @property
    def order2_scale(self) -> primitives.Float | None:
        """The scale factor for Order 2 for the spherical harmonics."""
        member = self.get_member("Order2Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order2_scale.setter
    def order2_scale(self, value: primitives.Float) -> None:
        """Set the Order2Scale field value."""
        member = self.get_member("Order2Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Order2Scale", fields.FieldFloat(value=value)
            )

