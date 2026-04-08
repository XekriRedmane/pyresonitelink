"""Generated component: LegHapticPointMapper."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegHapticPointMapper.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegHapticPointMapper"

    def __init__(self, priority: np.int32 | None = None, show_debug_visuals: bool | None = None, normalized_start: np.float32 | None = None, normalized_end: np.float32 | None = None, up_axis: primitives.Float3 | None = None, forward_axis: primitives.Float3 | None = None, upper_leg_radius: np.float32 | None = None, knee_radius: np.float32 | None = None, ankle_radius: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            normalized_start: Initial value for NormalizedStart.
            normalized_end: Initial value for NormalizedEnd.
            up_axis: Initial value for UpAxis.
            forward_axis: Initial value for ForwardAxis.
            upper_leg_radius: Initial value for UpperLegRadius.
            knee_radius: Initial value for KneeRadius.
            ankle_radius: Initial value for AnkleRadius.
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
        if up_axis is not None:
            self.up_axis = up_axis
        if forward_axis is not None:
            self.forward_axis = forward_axis
        if upper_leg_radius is not None:
            self.upper_leg_radius = upper_leg_radius
        if knee_radius is not None:
            self.knee_radius = knee_radius
        if ankle_radius is not None:
            self.ankle_radius = ankle_radius

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
    def side(self) -> members.FieldEnum | None:
        """The Side member."""
        member = self.get_member("Side")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @side.setter
    def side(self, value: members.FieldEnum) -> None:
        """Set the Side member."""
        self.set_member("Side", value)

    @property
    def up_axis(self) -> primitives.Float3 | None:
        """The UpAxis field value."""
        member = self.get_member("UpAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @up_axis.setter
    def up_axis(self, value: primitives.Float3) -> None:
        """Set the UpAxis field value."""
        member = self.get_member("UpAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpAxis", fields.FieldFloat3(value=value)
            )

    @property
    def forward_axis(self) -> primitives.Float3 | None:
        """The ForwardAxis field value."""
        member = self.get_member("ForwardAxis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @forward_axis.setter
    def forward_axis(self, value: primitives.Float3) -> None:
        """Set the ForwardAxis field value."""
        member = self.get_member("ForwardAxis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForwardAxis", fields.FieldFloat3(value=value)
            )

    @property
    def upper_leg_radius(self) -> np.float32 | None:
        """The UpperLegRadius field value."""
        member = self.get_member("UpperLegRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upper_leg_radius.setter
    def upper_leg_radius(self, value: np.float32) -> None:
        """Set the UpperLegRadius field value."""
        member = self.get_member("UpperLegRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpperLegRadius", fields.FieldFloat(value=value)
            )

    @property
    def knee_radius(self) -> np.float32 | None:
        """The KneeRadius field value."""
        member = self.get_member("KneeRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @knee_radius.setter
    def knee_radius(self, value: np.float32) -> None:
        """Set the KneeRadius field value."""
        member = self.get_member("KneeRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KneeRadius", fields.FieldFloat(value=value)
            )

    @property
    def ankle_radius(self) -> np.float32 | None:
        """The AnkleRadius field value."""
        member = self.get_member("AnkleRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ankle_radius.setter
    def ankle_radius(self, value: np.float32) -> None:
        """Set the AnkleRadius field value."""
        member = self.get_member("AnkleRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnkleRadius", fields.FieldFloat(value=value)
            )

