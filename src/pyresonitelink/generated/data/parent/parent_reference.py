"""Generated component: ParentReference."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParentReference(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ParentReference&lt;T&gt; component provides a reference type for the parent value system.

    Category: Data/Parent

    When this component is on a slot, all immediate children are part of its
    parent value system. Any immediate children of the slot with a
    ParentReferenceLink component that matches the type and ``Tag`` of this
    component will be linked to the ``Reference`` provided by this
    component. This can be especially useful for Snapper/SnapTarget systems.

    Parameterize with a value type::

        ParentReference[primitives.Float]
        ParentReference[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ParentReference<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ParentReference<>"

    def __init__(self, tag: primitives.String | None = None, reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tag: Initial value for Tag.
            reference: Initial value for Reference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tag is not None:
            self.tag = tag
        if reference is not None:
            self.reference = reference

    @property
    def tag(self) -> primitives.String | None:
        """Tag of the parent value. Compatible ParentReferenceLink components on the slot's immediate children must have the same tag."""
        member = self.get_member("Tag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tag.setter
    def tag(self, value: primitives.String) -> None:
        """Set the Tag field value."""
        member = self.get_member("Tag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tag", fields.FieldString(value=value)
            )

    @property
    def reference(self) -> str | None:
        """The value of the parent value associated with the ``Tag`` and type."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | T | None) -> None:
        """Set the Reference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='T'),
            )

