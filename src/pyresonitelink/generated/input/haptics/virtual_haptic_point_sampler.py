"""Generated component: VirtualHapticPointSampler."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualHapticPointSampler(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualHapticPointSampler.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualHapticPointSampler"

    def __init__(self, radius: np.float32 | None = None, show_debug_visual: bool | None = None, debug_visual: str | OverlayFresnelMaterial | None = None, force: np.float32 | None = None, pain: np.float32 | None = None, temperature: np.float32 | None = None, vibration: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            show_debug_visual: Initial value for ShowDebugVisual.
            debug_visual: Initial value for _debugVisual.
            force: Initial value for Force.
            pain: Initial value for Pain.
            temperature: Initial value for Temperature.
            vibration: Initial value for Vibration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if show_debug_visual is not None:
            self.show_debug_visual = show_debug_visual
        if debug_visual is not None:
            self.debug_visual = debug_visual
        if force is not None:
            self.force = force
        if pain is not None:
            self.pain = pain
        if temperature is not None:
            self.temperature = temperature
        if vibration is not None:
            self.vibration = vibration

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def show_debug_visual(self) -> bool | None:
        """The ShowDebugVisual field value."""
        member = self.get_member("ShowDebugVisual")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visual.setter
    def show_debug_visual(self, value: bool) -> None:
        """Set the ShowDebugVisual field value."""
        member = self.get_member("ShowDebugVisual")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowDebugVisual", fields.FieldBool(value=value)
            )

    @property
    def debug_visual(self) -> str | None:
        """Target ID of the _debugVisual reference (targets OverlayFresnelMaterial)."""
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_visual.setter
    def debug_visual(self, target: str | OverlayFresnelMaterial | None) -> None:
        """Set the _debugVisual reference by target ID or OverlayFresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, OverlayFresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_debugVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.OverlayFresnelMaterial'),
            )

    @property
    def force(self) -> np.float32 | None:
        """The Force field value."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: np.float32) -> None:
        """Set the Force field value."""
        member = self.get_member("Force")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Force", fields.FieldFloat(value=value)
            )

    @property
    def pain(self) -> np.float32 | None:
        """The Pain field value."""
        member = self.get_member("Pain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pain.setter
    def pain(self, value: np.float32) -> None:
        """Set the Pain field value."""
        member = self.get_member("Pain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pain", fields.FieldFloat(value=value)
            )

    @property
    def temperature(self) -> np.float32 | None:
        """The Temperature field value."""
        member = self.get_member("Temperature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @temperature.setter
    def temperature(self, value: np.float32) -> None:
        """Set the Temperature field value."""
        member = self.get_member("Temperature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Temperature", fields.FieldFloat(value=value)
            )

    @property
    def vibration(self) -> np.float32 | None:
        """The Vibration field value."""
        member = self.get_member("Vibration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration.setter
    def vibration(self, value: np.float32) -> None:
        """Set the Vibration field value."""
        member = self.get_member("Vibration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vibration", fields.FieldFloat(value=value)
            )

