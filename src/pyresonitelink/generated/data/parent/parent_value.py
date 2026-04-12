"""Generated component: ParentValue."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParentValue(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ParentValue&lt;T&gt; component provides a value type for the parent value system.

    Category: Data/Parent

    When this component is on a slot, all immediate children are part of its
    parent value system. Any immediate children of the slot with a
    ParentValueLink component that matches the type and ``Tag`` of this
    component will be linked to the ``Value`` provided by this component.
    This can be especially useful for Snapper/SnapTarget systems.

    Parameterize with a value type::

        ParentValue[primitives.Float]
        ParentValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ParentValue<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ParentValue<>"

    def __init__(self, tag: primitives.String | None = None, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tag: Initial value for Tag.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tag is not None:
            self.tag = tag
        if value is not None:
            self.value = value

    @property
    def tag(self) -> primitives.String | None:
        """Tag of the parent value. Compatible ParentValueLink components on the slot's immediate children must have the same tag."""
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
    def value(self) -> T | None:
        """The Value field value (type depends on type parameter)."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: T) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value", self._type_info.field_class(value=value)
            )

