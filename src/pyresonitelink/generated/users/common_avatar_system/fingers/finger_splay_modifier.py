"""Generated component: FingerSplayModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerSplayModifier(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """The FingerSplayModifier takes data from a ``Source``, adding splay data to a copy of that data. The resulting data becomes the pose source data of this component. This component in itself is a IFingerPoseSourceComponent.

For more information on finger pose sources, please see Finger Posing System.

    Category: Users/Common Avatar System/Fingers

    Used as a way of modifying Finger pose data to splay the fingers, and
    itself be used as new finger pose data.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerSplayModifier"

    def __init__(self, source: str | IFingerPoseSourceComponent | None = None, left_splay_magnitude: primitives.Float | None = None, right_splay_magnitude: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            left_splay_magnitude: Initial value for LeftSplayMagnitude.
            right_splay_magnitude: Initial value for RightSplayMagnitude.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if left_splay_magnitude is not None:
            self.left_splay_magnitude = left_splay_magnitude
        if right_splay_magnitude is not None:
            self.right_splay_magnitude = right_splay_magnitude

    @property
    def source(self) -> str | None:
        """The source data to copy to this component's Finger pose source data."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IFingerPoseSourceComponent | None) -> None:
        """Set the Source reference by target ID or IFingerPoseSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IFingerPoseSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFingerPoseSourceComponent'),
            )

    @property
    def left_splay_magnitude(self) -> primitives.Float | None:
        """How much splay data to the left hand to add to the data copied data from ``Source`` during copying."""
        member = self.get_member("LeftSplayMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_splay_magnitude.setter
    def left_splay_magnitude(self, value: primitives.Float) -> None:
        """Set the LeftSplayMagnitude field value."""
        member = self.get_member("LeftSplayMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftSplayMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def right_splay_magnitude(self) -> primitives.Float | None:
        """How much splay data on the right hand to add to the data copied data from ``Source`` during copying."""
        member = self.get_member("RightSplayMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_splay_magnitude.setter
    def right_splay_magnitude(self, value: primitives.Float) -> None:
        """Set the RightSplayMagnitude field value."""
        member = self.get_member("RightSplayMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightSplayMagnitude", fields.FieldFloat(value=value)
            )

