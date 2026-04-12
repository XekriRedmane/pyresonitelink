"""Generated component: AvatarMouthDataSourceAssigner."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarMouthDataSourceAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Avatar Mouth Data Source Assigner is a component that is able to assign a mouth tracking source to a field that accepts it.

    Category: Users/Common Avatar System/Face

    **Behavior**: This component is triggered when a user equips an avatar that has this component as part of the hierarchy. The user that equipped the avatar needs to have an active mouth data source on their client, such as a Vive facial tracker, or using a mod that creates a source for mouth tracking (like VRCFTReceiver)
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarMouthDataSourceAssigner"

    def __init__(self, target_reference: str | SyncRef[IMouthTrackingSourceComponent] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_reference: Initial value for TargetReference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_reference is not None:
            self.target_reference = target_reference

    @property
    def target_reference(self) -> str | None:
        """A field that accepts a mouth tracking source (like ``DataSource`` on the Avatar Expression Driver Component) to assign a tracking source to."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[IMouthTrackingSourceComponent] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[IMouthTrackingSourceComponent] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IMouthTrackingSourceComponent>'),
            )

