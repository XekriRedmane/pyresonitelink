"""Generated component: HapticPointSampler."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.overlay_fresnel_material import OverlayFresnelMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HapticPointSampler(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HapticPointSampler.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HapticPointSampler"

    def __init__(self, radius: primitives.Float | None = None, show_debug_visual: primitives.Bool | None = None, debug_visual: str | OverlayFresnelMaterial | None = None, haptic_point_index: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            show_debug_visual: Initial value for ShowDebugVisual.
            debug_visual: Initial value for _debugVisual.
            haptic_point_index: Initial value for HapticPointIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if show_debug_visual is not None:
            self.show_debug_visual = show_debug_visual
        if debug_visual is not None:
            self.debug_visual = debug_visual
        if haptic_point_index is not None:
            self.haptic_point_index = haptic_point_index

    @property
    def radius(self) -> primitives.Float | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def show_debug_visual(self) -> primitives.Bool | None:
        """The ShowDebugVisual field value."""
        member = self.get_member("ShowDebugVisual")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visual.setter
    def show_debug_visual(self, value: primitives.Bool) -> None:
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
    def sampling_user(self) -> members.SyncObject | None:
        """The SamplingUser member."""
        member = self.get_member("SamplingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @sampling_user.setter
    def sampling_user(self, value: members.SyncObject) -> None:
        """Set the SamplingUser member."""
        self.set_member("SamplingUser", value)

    @property
    def haptic_point_index(self) -> primitives.Int | None:
        """The HapticPointIndex field value."""
        member = self.get_member("HapticPointIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @haptic_point_index.setter
    def haptic_point_index(self, value: primitives.Int) -> None:
        """Set the HapticPointIndex field value."""
        member = self.get_member("HapticPointIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HapticPointIndex", fields.FieldInt(value=value)
            )

