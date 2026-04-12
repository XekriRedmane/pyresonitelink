"""Generated component: AvatarEyeTrackingInfo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ieye_data_source_component import IEyeDataSourceComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarEyeTrackingInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AvatarEyeTrackingInfo is used to override the assigning behavior from a AvatarEyeDataSourceAssigner on the avatar when it assigns a target.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarEyeTrackingInfo"

    def __init__(self, eye_data_source: str | IEyeDataSourceComponent | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            eye_data_source: Initial value for EyeDataSource.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if eye_data_source is not None:
            self.eye_data_source = eye_data_source

    @property
    def eye_data_source(self) -> str | None:
        """The data source to override the assigning behavior of a Component:AvatarEyeDataSourceAssigner on the avatar with."""
        member = self.get_member("EyeDataSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eye_data_source.setter
    def eye_data_source(self, target: str | IEyeDataSourceComponent | None) -> None:
        """Set the EyeDataSource reference by target ID or IEyeDataSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IEyeDataSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("EyeDataSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EyeDataSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IEyeDataSourceComponent'),
            )

