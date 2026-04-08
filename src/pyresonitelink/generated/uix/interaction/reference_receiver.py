"""Generated component: ReferenceReceiver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_ref import ISyncRef
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceReceiver(GeneratedComponent, IUIGrabReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ReferenceReceiver.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ReferenceReceiver"

    def __init__(self, target_reference: str | ISyncRef | None = None, undoable: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_reference: Initial value for TargetReference.
            undoable: Initial value for Undoable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_reference is not None:
            self.target_reference = target_reference
        if undoable is not None:
            self.undoable = undoable

    @property
    def target_reference(self) -> str | None:
        """Target ID of the TargetReference reference (targets ISyncRef)."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | ISyncRef | None) -> None:
        """Set the TargetReference reference by target ID or ISyncRef instance."""
        target_id: str | None = target.id if isinstance(target, ISyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncRef'),
            )

    @property
    def undoable(self) -> primitives.Bool | None:
        """The Undoable field value."""
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

