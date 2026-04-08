"""Generated component: ButtonReferenceCycle."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonReferenceCycle(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonReferenceCycle<>.

    Category: Common UI/Button Interactions

    Parameterize with a value type::

        ButtonReferenceCycle[np.float32]
        ButtonReferenceCycle[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonReferenceCycle<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonReferenceCycle<>"

    def __init__(self, target_reference: str | SyncRef[T] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the TargetReference reference (targets SyncRef[T])."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[T] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def targets(self) -> members.SyncList | None:
        """The Targets member."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the Targets member."""
        self.set_member("Targets", value)

