"""Generated component: RelativePositioner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RelativePositioner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RelativePositioner component puts the slot its attached to in a position based on the Bounding box and position of ``Reference``. Optionally deleting the component on an update when the slot is positioned successfully.

    Category: Transform/Drivers

    Attach to a slot and provide a ``Reference`` in order for this component
    to do a valid position and optionally delete itself within that update.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RelativePositioner"

    def __init__(self, reference: str | Slot | None = None, reference_anchor: primitives.Float3 | None = None, reference_offset: primitives.Float3 | None = None, destroy_after_done: primitives.Bool | None = None, target: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            reference_anchor: Initial value for ReferenceAnchor.
            reference_offset: Initial value for ReferenceOffset.
            destroy_after_done: Initial value for DestroyAfterDone.
            target: Initial value for _target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference
        if reference_anchor is not None:
            self.reference_anchor = reference_anchor
        if reference_offset is not None:
            self.reference_offset = reference_offset
        if destroy_after_done is not None:
            self.destroy_after_done = destroy_after_done
        if target is not None:
            self.target = target

    @property
    def reference(self) -> str | None:
        """The slot to Relative position to."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | Slot | None) -> None:
        """Set the Reference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def reference_bounds_space(self) -> members.SyncObject | None:
        """The space to calculate the Bounding box of ``Reference`` in."""
        member = self.get_member("ReferenceBoundsSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @reference_bounds_space.setter
    def reference_bounds_space(self, value: members.SyncObject) -> None:
        """Set ReferenceBoundsSpace. The space to calculate the Bounding box of ``Reference`` in."""
        self.set_member("ReferenceBoundsSpace", value)

    @property
    def reference_anchor(self) -> primitives.Float3 | None:
        """How far away from the center of the ``Reference``'s Bounding box based on size. (1,1,1) puts this slot at the positive corner in global space of ``Reference``'s Bounding box and (0,0,0) put it at ``Reference``'s center Bounding box point."""
        member = self.get_member("ReferenceAnchor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_anchor.setter
    def reference_anchor(self, value: primitives.Float3) -> None:
        """Set the ReferenceAnchor field value."""
        member = self.get_member("ReferenceAnchor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReferenceAnchor", fields.FieldFloat3(value=value)
            )

    @property
    def reference_offset(self) -> primitives.Float3 | None:
        """How much to add to the slot position after Bounding box positioning."""
        member = self.get_member("ReferenceOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_offset.setter
    def reference_offset(self, value: primitives.Float3) -> None:
        """Set the ReferenceOffset field value."""
        member = self.get_member("ReferenceOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReferenceOffset", fields.FieldFloat3(value=value)
            )

    @property
    def destroy_after_done(self) -> primitives.Bool | None:
        """Whether to destroy this component after update and positioning was successfully done due to needed fields not being null."""
        member = self.get_member("DestroyAfterDone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @destroy_after_done.setter
    def destroy_after_done(self, value: primitives.Bool) -> None:
        """Set the DestroyAfterDone field value."""
        member = self.get_member("DestroyAfterDone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DestroyAfterDone", fields.FieldBool(value=value)
            )

    @property
    def target(self) -> str | None:
        """The position field of this slot to drive."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _target reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

