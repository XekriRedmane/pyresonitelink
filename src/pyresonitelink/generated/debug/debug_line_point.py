"""Generated component: DebugLinePoint."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugLinePoint(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugLinePoint.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugLinePoint"

    def __init__(self, line_point0: primitives.Float3 | None = None, line_point1: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            line_point0: Initial value for LinePoint0.
            line_point1: Initial value for LinePoint1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if line_point0 is not None:
            self.line_point0 = line_point0
        if line_point1 is not None:
            self.line_point1 = line_point1

    @property
    def line_point0(self) -> primitives.Float3 | None:
        """The LinePoint0 field value."""
        member = self.get_member("LinePoint0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_point0.setter
    def line_point0(self, value: primitives.Float3) -> None:
        """Set the LinePoint0 field value."""
        member = self.get_member("LinePoint0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LinePoint0", fields.FieldFloat3(value=value)
            )

    @property
    def line_point1(self) -> primitives.Float3 | None:
        """The LinePoint1 field value."""
        member = self.get_member("LinePoint1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_point1.setter
    def line_point1(self, value: primitives.Float3) -> None:
        """Set the LinePoint1 field value."""
        member = self.get_member("LinePoint1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LinePoint1", fields.FieldFloat3(value=value)
            )

    @property
    def points(self) -> members.SyncList | None:
        """The Points member."""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set the Points member."""
        self.set_member("Points", value)

