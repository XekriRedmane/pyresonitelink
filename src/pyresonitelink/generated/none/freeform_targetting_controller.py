"""Generated component: FreeformTargettingController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot


class FreeformTargettingController(GeneratedComponent):
    """The FreeformTargettingController component is used to handle the 3rd person targeting onto UIX in desktop mode.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FreeformTargettingController"

    def __init__(self, focus_target: str | Slot | None = None, focus_center_point: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            focus_target: Initial value for FocusTarget.
            focus_center_point: Initial value for FocusCenterPoint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if focus_target is not None:
            self.focus_target = focus_target
        if focus_center_point is not None:
            self.focus_center_point = focus_center_point

    @property
    def focus_target(self) -> str | None:
        """The object to focus on."""
        member = self.get_member("FocusTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @focus_target.setter
    def focus_target(self, target: str | Slot | None) -> None:
        """Set the FocusTarget reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("FocusTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FocusTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def focus_center_point(self) -> primitives.Float3 | None:
        """The center focus position. Acts as an offset."""
        member = self.get_member("FocusCenterPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @focus_center_point.setter
    def focus_center_point(self, value: primitives.Float3) -> None:
        """Set the FocusCenterPoint field value."""
        member = self.get_member("FocusCenterPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FocusCenterPoint", fields.FieldFloat3(value=value)
            )

