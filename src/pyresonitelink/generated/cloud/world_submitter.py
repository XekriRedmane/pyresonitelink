"""Generated component: WorldSubmitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldSubmitter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldSubmitter.

    Category: Cloud
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldSubmitter"

    def __init__(self, group_id: primitives.String | None = None, radius: primitives.Float | None = None, height: primitives.Float | None = None, visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            group_id: Initial value for GroupId.
            radius: Initial value for Radius.
            height: Initial value for Height.
            visual: Initial value for _visual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if group_id is not None:
            self.group_id = group_id
        if radius is not None:
            self.radius = radius
        if height is not None:
            self.height = height
        if visual is not None:
            self.visual = visual

    @property
    def group_id(self) -> primitives.String | None:
        """The GroupId field value."""
        member = self.get_member("GroupId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_id.setter
    def group_id(self, value: primitives.String) -> None:
        """Set the GroupId field value."""
        member = self.get_member("GroupId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupId", fields.FieldString(value=value)
            )

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
    def height(self) -> primitives.Float | None:
        """The Height field value."""
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
    def visual(self) -> str | None:
        """Target ID of the _visual reference (targets Slot)."""
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual.setter
    def visual(self, target: str | Slot | None) -> None:
        """Set the _visual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

