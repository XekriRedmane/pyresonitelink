"""Generated component: FingerPoseLerp."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPoseLerp(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FingerPoseLerp.

    Category: Users/Common Avatar System/Fingers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPoseLerp"

    def __init__(self, a: str | IFingerPoseSourceComponent | None = None, b: str | IFingerPoseSourceComponent | None = None, lerp: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            b: Initial value for B.
            lerp: Initial value for Lerp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if lerp is not None:
            self.lerp = lerp

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets IFingerPoseSourceComponent)."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | IFingerPoseSourceComponent | None) -> None:
        """Set the A reference by target ID or IFingerPoseSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IFingerPoseSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent'),
            )

    @property
    def b(self) -> str | None:
        """Target ID of the B reference (targets IFingerPoseSourceComponent)."""
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b.setter
    def b(self, target: str | IFingerPoseSourceComponent | None) -> None:
        """Set the B reference by target ID or IFingerPoseSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IFingerPoseSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent'),
            )

    @property
    def lerp(self) -> primitives.Float | None:
        """The Lerp field value."""
        member = self.get_member("Lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: primitives.Float) -> None:
        """Set the Lerp field value."""
        member = self.get_member("Lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Lerp", fields.FieldFloat(value=value)
            )

