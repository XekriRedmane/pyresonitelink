"""Generated component: ReflectionProbeSH2."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.reflection_probe import ReflectionProbe
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReflectionProbeSH2(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReflectionProbeSH2.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionProbeSH2"

    def __init__(self, probe: str | ReflectionProbe | None = None, order0_scale: np.float32 | None = None, order1_scale: np.float32 | None = None, order2_scale: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            probe: Initial value for Probe.
            order0_scale: Initial value for Order0Scale.
            order1_scale: Initial value for Order1Scale.
            order2_scale: Initial value for Order2Scale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if probe is not None:
            self.probe = probe
        if order0_scale is not None:
            self.order0_scale = order0_scale
        if order1_scale is not None:
            self.order1_scale = order1_scale
        if order2_scale is not None:
            self.order2_scale = order2_scale

    @property
    def probe(self) -> str | None:
        """Target ID of the Probe reference (targets ReflectionProbe)."""
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
    def ambient_light(self) -> members.FieldEnum | None:
        """The AmbientLight member."""
        member = self.get_member("AmbientLight")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ambient_light.setter
    def ambient_light(self, value: members.FieldEnum) -> None:
        """Set the AmbientLight member."""
        self.set_member("AmbientLight", value)

    @property
    def order0_scale(self) -> np.float32 | None:
        """The Order0Scale field value."""
        member = self.get_member("Order0Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order0_scale.setter
    def order0_scale(self, value: np.float32) -> None:
        """Set the Order0Scale field value."""
        member = self.get_member("Order0Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Order0Scale", fields.FieldFloat(value=value)
            )

    @property
    def order1_scale(self) -> np.float32 | None:
        """The Order1Scale field value."""
        member = self.get_member("Order1Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order1_scale.setter
    def order1_scale(self, value: np.float32) -> None:
        """Set the Order1Scale field value."""
        member = self.get_member("Order1Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Order1Scale", fields.FieldFloat(value=value)
            )

    @property
    def order2_scale(self) -> np.float32 | None:
        """The Order2Scale field value."""
        member = self.get_member("Order2Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @order2_scale.setter
    def order2_scale(self, value: np.float32) -> None:
        """Set the Order2Scale field value."""
        member = self.get_member("Order2Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Order2Scale", fields.FieldFloat(value=value)
            )

