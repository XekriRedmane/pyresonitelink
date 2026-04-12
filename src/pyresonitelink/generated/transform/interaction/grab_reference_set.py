"""Generated component: GrabReferenceSet."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabReferenceSet(GenericComponent[T], IGrabEventReceiver, IWorldEventReceiver):
    """The GrabReferenceSet can be used to write a reference to a field on grab and release.

    Category: Transform/Interaction

    While on the same slot as a Grabbable the component can be configured to
    set a reference on grabbed and on released.

    Parameterize with a value type::

        GrabReferenceSet[primitives.Float]
        GrabReferenceSet[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabReferenceSet<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.GrabReferenceSet<>"

    def __init__(self, target: str | SyncRef[T] | None = None, grabbed_target: str | T | None = None, released_target: str | T | None = None, set_on_grabbed: primitives.Bool | None = None, set_on_released: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            grabbed_target: Initial value for GrabbedTarget.
            released_target: Initial value for ReleasedTarget.
            set_on_grabbed: Initial value for SetOnGrabbed.
            set_on_released: Initial value for SetOnReleased.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if grabbed_target is not None:
            self.grabbed_target = grabbed_target
        if released_target is not None:
            self.released_target = released_target
        if set_on_grabbed is not None:
            self.set_on_grabbed = set_on_grabbed
        if set_on_released is not None:
            self.set_on_released = set_on_released

    @property
    def target(self) -> str | None:
        """The field in which to change on grab and release."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncRef[T] | None) -> None:
        """Set the Target reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def grabbed_target(self) -> str | None:
        """The value to set the contained data of the SyncRef referenced in ``Target`` when the item is grabbed."""
        member = self.get_member("GrabbedTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabbed_target.setter
    def grabbed_target(self, target: str | T | None) -> None:
        """Set the GrabbedTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("GrabbedTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GrabbedTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def released_target(self) -> str | None:
        """The value to set the contained data of the SyncRef referenced in ``Target`` when the item is released."""
        member = self.get_member("ReleasedTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @released_target.setter
    def released_target(self, target: str | T | None) -> None:
        """Set the ReleasedTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("ReleasedTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReleasedTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def set_on_grabbed(self) -> primitives.Bool | None:
        """Whether to set the contained data of the SyncRef referenced in ``Target`` when the item is grabbed."""
        member = self.get_member("SetOnGrabbed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_grabbed.setter
    def set_on_grabbed(self, value: primitives.Bool) -> None:
        """Set the SetOnGrabbed field value."""
        member = self.get_member("SetOnGrabbed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnGrabbed", fields.FieldBool(value=value)
            )

    @property
    def set_on_released(self) -> primitives.Bool | None:
        """Whether to set the contained data of the SyncRef referenced in ``Target`` when the item is released."""
        member = self.get_member("SetOnReleased")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_released.setter
    def set_on_released(self, value: primitives.Bool) -> None:
        """Set the SetOnReleased field value."""
        member = self.get_member("SetOnReleased")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnReleased", fields.FieldBool(value=value)
            )

