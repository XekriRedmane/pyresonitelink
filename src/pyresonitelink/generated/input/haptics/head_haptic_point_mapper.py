"""Generated component: HeadHapticPointMapper."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HeadHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HeadHapticPointMapper.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HeadHapticPointMapper"

    def __init__(self, priority: np.int32 | None = None, show_debug_visuals: bool | None = None, head_size: primitives.Float3 | None = None, head_center: primitives.Float3 | None = None, debug_visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            head_size: Initial value for HeadSize.
            head_center: Initial value for HeadCenter.
            debug_visual: Initial value for _debugVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if priority is not None:
            self.priority = priority
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals
        if head_size is not None:
            self.head_size = head_size
        if head_center is not None:
            self.head_center = head_center
        if debug_visual is not None:
            self.debug_visual = debug_visual

    @property
    def priority(self) -> np.int32 | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: np.int32) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def show_debug_visuals(self) -> bool | None:
        """The ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visuals.setter
    def show_debug_visuals(self, value: bool) -> None:
        """Set the ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowDebugVisuals", fields.FieldBool(value=value)
            )

    @property
    def head_size(self) -> primitives.Float3 | None:
        """The HeadSize field value."""
        member = self.get_member("HeadSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_size.setter
    def head_size(self, value: primitives.Float3) -> None:
        """Set the HeadSize field value."""
        member = self.get_member("HeadSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadSize", fields.FieldFloat3(value=value)
            )

    @property
    def head_center(self) -> primitives.Float3 | None:
        """The HeadCenter field value."""
        member = self.get_member("HeadCenter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_center.setter
    def head_center(self, value: primitives.Float3) -> None:
        """Set the HeadCenter field value."""
        member = self.get_member("HeadCenter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadCenter", fields.FieldFloat3(value=value)
            )

    @property
    def debug_visual(self) -> str | None:
        """Target ID of the _debugVisual reference (targets Slot)."""
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_visual.setter
    def debug_visual(self, target: str | Slot | None) -> None:
        """Set the _debugVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_debugVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

