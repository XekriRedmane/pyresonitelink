"""Generated component: ButtonReferenceSet."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonReferenceSet(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonReferenceSet component takes in a Reference Type and a ``TargetReference``. When an IButton is pressed while this component is on the same slot, this will send the reference to the provided ``TargetReference``.

    Category: Common UI/Button Interactions

    This is similar to the Write ProtoFlux node but as a component instead.

    Parameterize with a value type::

        ButtonReferenceSet[primitives.Float]
        ButtonReferenceSet[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonReferenceSet<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ButtonReferenceSet<>"

    def __init__(self, target_reference: str | SyncRef[T] | None = None, set_reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_reference: Initial value for TargetReference.
            set_reference: Initial value for SetReference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_reference is not None:
            self.target_reference = target_reference
        if set_reference is not None:
            self.set_reference = set_reference

    @property
    def target_reference(self) -> str | None:
        """The target to send the reference outwards."""
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
    def set_reference(self) -> str | None:
        """The reference to set when the button is pressed."""
        member = self.get_member("SetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @set_reference.setter
    def set_reference(self, target: str | T | None) -> None:
        """Set the SetReference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("SetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SetReference",
                members.Reference(targetId=target_id, targetType='T'),
            )

