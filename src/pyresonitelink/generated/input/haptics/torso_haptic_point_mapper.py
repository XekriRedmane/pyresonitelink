"""Generated component: TorsoHapticPointMapper."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TorsoHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TorsoHapticPointMapper.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TorsoHapticPointMapper"

    def __init__(self, priority: np.int32 | None = None, show_debug_visuals: bool | None = None, normalized_start: np.float32 | None = None, normalized_end: np.float32 | None = None, lower_width: np.float32 | None = None, upper_width: np.float32 | None = None, front_offset: np.float32 | None = None, back_offset: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            normalized_start: Initial value for NormalizedStart.
            normalized_end: Initial value for NormalizedEnd.
            lower_width: Initial value for LowerWidth.
            upper_width: Initial value for UpperWidth.
            front_offset: Initial value for FrontOffset.
            back_offset: Initial value for BackOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if priority is not None:
            self.priority = priority
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals
        if normalized_start is not None:
            self.normalized_start = normalized_start
        if normalized_end is not None:
            self.normalized_end = normalized_end
        if lower_width is not None:
            self.lower_width = lower_width
        if upper_width is not None:
            self.upper_width = upper_width
        if front_offset is not None:
            self.front_offset = front_offset
        if back_offset is not None:
            self.back_offset = back_offset

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
    def bone_chain(self) -> members.SyncList | None:
        """The BoneChain member."""
        member = self.get_member("BoneChain")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bone_chain.setter
    def bone_chain(self, value: members.SyncList) -> None:
        """Set the BoneChain member."""
        self.set_member("BoneChain", value)

    @property
    def normalized_start(self) -> np.float32 | None:
        """The NormalizedStart field value."""
        member = self.get_member("NormalizedStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_start.setter
    def normalized_start(self, value: np.float32) -> None:
        """Set the NormalizedStart field value."""
        member = self.get_member("NormalizedStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedStart", fields.FieldFloat(value=value)
            )

    @property
    def normalized_end(self) -> np.float32 | None:
        """The NormalizedEnd field value."""
        member = self.get_member("NormalizedEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_end.setter
    def normalized_end(self, value: np.float32) -> None:
        """Set the NormalizedEnd field value."""
        member = self.get_member("NormalizedEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedEnd", fields.FieldFloat(value=value)
            )

    @property
    def lower_width(self) -> np.float32 | None:
        """The LowerWidth field value."""
        member = self.get_member("LowerWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lower_width.setter
    def lower_width(self, value: np.float32) -> None:
        """Set the LowerWidth field value."""
        member = self.get_member("LowerWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowerWidth", fields.FieldFloat(value=value)
            )

    @property
    def upper_width(self) -> np.float32 | None:
        """The UpperWidth field value."""
        member = self.get_member("UpperWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upper_width.setter
    def upper_width(self, value: np.float32) -> None:
        """Set the UpperWidth field value."""
        member = self.get_member("UpperWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpperWidth", fields.FieldFloat(value=value)
            )

    @property
    def front_offset(self) -> np.float32 | None:
        """The FrontOffset field value."""
        member = self.get_member("FrontOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_offset.setter
    def front_offset(self, value: np.float32) -> None:
        """Set the FrontOffset field value."""
        member = self.get_member("FrontOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontOffset", fields.FieldFloat(value=value)
            )

    @property
    def back_offset(self) -> np.float32 | None:
        """The BackOffset field value."""
        member = self.get_member("BackOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @back_offset.setter
    def back_offset(self, value: np.float32) -> None:
        """Set the BackOffset field value."""
        member = self.get_member("BackOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackOffset", fields.FieldFloat(value=value)
            )

