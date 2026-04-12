"""Generated component: AvatarMouthTrackingInfo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarMouthTrackingInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AvatarMouthTrackingInfo is used to override the assigning behavior from a AvatarMouthDataSourceAssigner on the avatar when it assigns a target. or when a AvatarExpressionDriver on the avatar assigns it's own mouth data source.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarMouthTrackingInfo"

    def __init__(self, mouth_data_source: str | IMouthTrackingSourceComponent | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mouth_data_source: Initial value for MouthDataSource.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mouth_data_source is not None:
            self.mouth_data_source = mouth_data_source

    @property
    def mouth_data_source(self) -> str | None:
        """The data source to override the assigning behavior of a Component:AvatarMouthDataSourceAssigner on the avatar with. or to override what a Component:AvatarExpressionDriver on the avatar assigns it's own mouth data source with."""
        member = self.get_member("MouthDataSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_data_source.setter
    def mouth_data_source(self, target: str | IMouthTrackingSourceComponent | None) -> None:
        """Set the MouthDataSource reference by target ID or IMouthTrackingSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IMouthTrackingSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("MouthDataSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthDataSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IMouthTrackingSourceComponent'),
            )

