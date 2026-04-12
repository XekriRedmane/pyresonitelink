"""Generated component: FingerPoseModifier."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPoseModifier(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """The FingerPoseModifier component takes a ``Source`` and makes a copy of the finger pose data from it. It then modifies the copied data before making it the finger pose data of this component. This component in itself is a IFingerPoseSourceComponent.

For more information on finger pose sources, please see Finger Posing System.

    Category: Users/Common Avatar System/Fingers

    Provide the component with data from another IFingerPoseSourceComponent
    to add extra offsets onto. This component can be used as a
    IFingerPoseSourceComponent for other components.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPoseModifier"

    def __init__(self, source: str | IFingerPoseSourceComponent | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> str | None:
        """The component to take finger pose data from and make a copy to modify and make this component's finger pose data."""
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
    def left_offsets(self) -> members.SyncObject | None:
        """How to modify the left finger pose data before making it this component's finger pose data."""
        member = self.get_member("LeftOffsets")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @left_offsets.setter
    def left_offsets(self, value: members.SyncObject) -> None:
        """Set LeftOffsets. How to modify the left finger pose data before making it this component's finger pose data."""
        self.set_member("LeftOffsets", value)

    @property
    def right_offsets(self) -> members.SyncObject | None:
        """How to modify the right finger pose data before making it this component's finger pose data."""
        member = self.get_member("RightOffsets")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @right_offsets.setter
    def right_offsets(self, value: members.SyncObject) -> None:
        """Set RightOffsets. How to modify the right finger pose data before making it this component's finger pose data."""
        self.set_member("RightOffsets", value)

