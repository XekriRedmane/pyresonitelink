"""Generated component: ButtonReferenceCycle."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonReferenceCycle(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonReferenceCycle component holds a list of references and takes in a ``TargetReference`` of a provided type. When an IButton is pressed while this component is on it, this will cycle through the listed references and send the data through the ``TargetReference``.

    Category: Common UI/Button Interactions

    Useful for needing a way to cycle through references of any type.

    Parameterize with a value type::

        ButtonReferenceCycle[primitives.Float]
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
        """The reference data to send outwards."""
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
        """The list of references to cycle through."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set Targets. The list of references to cycle through."""
        self.set_member("Targets", value)

