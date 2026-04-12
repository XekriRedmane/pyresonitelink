"""Generated component: AvatarEyeDataSourceAssigner."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ieye_data_source_component import IEyeDataSourceComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarEyeDataSourceAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarEyeDataSourceAssigner component manages assigning eye tracking sources to fields

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarEyeDataSourceAssigner"

    def __init__(self, target_reference: str | SyncRef[IEyeDataSourceComponent] | None = None, *, component: workers.Component | None = None) -> None:
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
        """The field to assign an eye tracking source to, unless it finds a Component:AvatarEyeTrackingInfo first, it assigns from that instead of the user's one."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[IEyeDataSourceComponent] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[IEyeDataSourceComponent] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IEyeDataSourceComponent>'),
            )

