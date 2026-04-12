"""Generated component: TorsoHapticPointMapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TorsoHapticPointMapper(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TorsoHapticPointMapper component is used to tell the game the size of an Avatar's torso and its bones in order for the game to know where to place haptic point samplers so they better match the size and positions of the body.

The area makes up a 3d trapezoid with thickness, with a parallel front and back, and top and bottom, but a non parallel left and right.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TorsoHapticPointMapper"

    def __init__(self, priority: primitives.Int | None = None, show_debug_visuals: primitives.Bool | None = None, normalized_start: primitives.Float | None = None, normalized_end: primitives.Float | None = None, lower_width: primitives.Float | None = None, upper_width: primitives.Float | None = None, front_offset: primitives.Float | None = None, back_offset: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
    def priority(self) -> primitives.Int | None:
        """The priority of this Mapper over other mappers."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def show_debug_visuals(self) -> primitives.Bool | None:
        """Whether to show the area and haptic point Debug visuals."""
        member = self.get_member("ShowDebugVisuals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visuals.setter
    def show_debug_visuals(self, value: primitives.Bool) -> None:
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
        """A list of bones that make up the center spine of the avatar. (Hips, Spine(s), Chest, upper chest)"""
        member = self.get_member("BoneChain")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bone_chain.setter
    def bone_chain(self, value: members.SyncList) -> None:
        """Set BoneChain. A list of bones that make up the center spine of the avatar. (Hips, Spine(s), Chest, upper chest)"""
        self.set_member("BoneChain", value)

    @property
    def normalized_start(self) -> primitives.Float | None:
        """Where in the chain does the haptics mapping start?"""
        member = self.get_member("NormalizedStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_start.setter
    def normalized_start(self, value: primitives.Float) -> None:
        """Set the NormalizedStart field value."""
        member = self.get_member("NormalizedStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedStart", fields.FieldFloat(value=value)
            )

    @property
    def normalized_end(self) -> primitives.Float | None:
        """Where in the chain does the haptics mapping end?"""
        member = self.get_member("NormalizedEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_end.setter
    def normalized_end(self, value: primitives.Float) -> None:
        """Set the NormalizedEnd field value."""
        member = self.get_member("NormalizedEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedEnd", fields.FieldFloat(value=value)
            )

    @property
    def lower_width(self) -> primitives.Float | None:
        """The width of the lower spine."""
        member = self.get_member("LowerWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lower_width.setter
    def lower_width(self, value: primitives.Float) -> None:
        """Set the LowerWidth field value."""
        member = self.get_member("LowerWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowerWidth", fields.FieldFloat(value=value)
            )

    @property
    def upper_width(self) -> primitives.Float | None:
        """The width of the upper spine."""
        member = self.get_member("UpperWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upper_width.setter
    def upper_width(self, value: primitives.Float) -> None:
        """Set the UpperWidth field value."""
        member = self.get_member("UpperWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpperWidth", fields.FieldFloat(value=value)
            )

    @property
    def front_offset(self) -> primitives.Float | None:
        """How far the front side is from the spine bones."""
        member = self.get_member("FrontOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_offset.setter
    def front_offset(self, value: primitives.Float) -> None:
        """Set the FrontOffset field value."""
        member = self.get_member("FrontOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontOffset", fields.FieldFloat(value=value)
            )

    @property
    def back_offset(self) -> primitives.Float | None:
        """How far the back side is from the spine bones."""
        member = self.get_member("BackOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @back_offset.setter
    def back_offset(self, value: primitives.Float) -> None:
        """Set the BackOffset field value."""
        member = self.get_member("BackOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackOffset", fields.FieldFloat(value=value)
            )

