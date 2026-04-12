"""Generated component: DebugConeDistance."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugConeDistance(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugConeDistance component creates a Debug cone visual that draws lines from the list of ``Points`` to the surface of the cone. If the point is inside the cone, the point visual will be Cyan, if it is outside it will be red. The lines from the point to the cone are Yellow. When attached, the component will add 32 random points to ``Points`` that are 4 units away.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugConeDistance"

    def __init__(self, height: primitives.Float | None = None, radius: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            height: Initial value for Height.
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if height is not None:
            self.height = height
        if radius is not None:
            self.radius = radius

    @property
    def height(self) -> primitives.Float | None:
        """The height of the cone."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> primitives.Float | None:
        """The radius of the cone base."""
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
    def points(self) -> members.SyncList | None:
        """Points that the Debug visual will draw lines to from the cone surface to the point."""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set Points. Points that the Debug visual will draw lines to from the cone surface to the point."""
        self.set_member("Points", value)

