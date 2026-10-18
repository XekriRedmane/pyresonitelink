"""Generated component: ReferenceReceiverOf."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceReceiverOf(GenericComponent[T], IUIGrabReceiver, IWorldEventReceiver):
    """The ReferenceReceiver component can receive a reference dropped onto a UIX element Button by a user. The reference dropped is then stored into the field specified by ``TargetReference`` (an example would be to use the ReferenceField). 

}}

    Category: UIX/Interaction

    * Letting go when the reference you want to send into the
    ``TargetReference`` field, is currently the way on how it can trigger. *
    Combining this with the ReferenceProxySource component is a powerful way
    of moving references around without the need to open a Scene Inspector.
    Having a ReferenceField of IWorldElement as the ``TargetReference`` is
    the most recommended way of successfully transferring a reference this
    way.

    Parameterize with a value type::

        ReferenceReceiverOf[primitives.Float]
        ReferenceReceiverOf[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ReferenceReceiver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ReferenceReceiver<>"

    def __init__(self, reference: str | SyncRef[T] | None = None, undoable: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            undoable: Initial value for Undoable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference
        if undoable is not None:
            self.undoable = undoable

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets SyncRef[T])."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | SyncRef[T] | None) -> None:
        """Set the Reference reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def undoable(self) -> primitives.Bool | None:
        """Whether dropping elements onto this UIX interactable is undoable."""
        member = self.get_member("Undoable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undoable.setter
    def undoable(self, value: primitives.Bool) -> None:
        """Set the Undoable field value."""
        member = self.get_member("Undoable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Undoable", fields.FieldBool(value=value)
            )

