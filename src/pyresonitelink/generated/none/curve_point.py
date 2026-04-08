"""Generated component: CurvePoint."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CurvePoint(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CurvePoint.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CurvePoint"

    def __init__(self, left_tangent_source: str | Slot | None = None, right_tangent_source: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            left_tangent_source: Initial value for LeftTangentSource.
            right_tangent_source: Initial value for RightTangentSource.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if left_tangent_source is not None:
            self.left_tangent_source = left_tangent_source
        if right_tangent_source is not None:
            self.right_tangent_source = right_tangent_source

    @property
    def left_tangent_source(self) -> str | None:
        """Target ID of the LeftTangentSource reference (targets Slot)."""
        member = self.get_member("LeftTangentSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_tangent_source.setter
    def left_tangent_source(self, target: str | Slot | None) -> None:
        """Set the LeftTangentSource reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("LeftTangentSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LeftTangentSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_tangent_source(self) -> str | None:
        """Target ID of the RightTangentSource reference (targets Slot)."""
        member = self.get_member("RightTangentSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_tangent_source.setter
    def right_tangent_source(self, target: str | Slot | None) -> None:
        """Set the RightTangentSource reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("RightTangentSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RightTangentSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

