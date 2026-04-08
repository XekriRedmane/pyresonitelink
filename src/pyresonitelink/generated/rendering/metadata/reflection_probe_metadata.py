"""Generated component: ReflectionProbeMetadata."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.reflection_probe import ReflectionProbe
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReflectionProbeMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReflectionProbeMetadata.

    Category: Rendering/Metadata
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionProbeMetadata"

    def __init__(self, probe: str | ReflectionProbe | None = None, on_changes_render_count: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            probe: Initial value for Probe.
            on_changes_render_count: Initial value for OnChangesRenderCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if probe is not None:
            self.probe = probe
        if on_changes_render_count is not None:
            self.on_changes_render_count = on_changes_render_count

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
    def on_changes_render_count(self) -> np.int32 | None:
        """The OnChangesRenderCount field value."""
        member = self.get_member("OnChangesRenderCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @on_changes_render_count.setter
    def on_changes_render_count(self, value: np.int32) -> None:
        """Set the OnChangesRenderCount field value."""
        member = self.get_member("OnChangesRenderCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OnChangesRenderCount", fields.FieldInt(value=value)
            )

