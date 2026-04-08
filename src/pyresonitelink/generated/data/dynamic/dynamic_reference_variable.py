"""Generated component: DynamicReferenceVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.idynamic_variable import IDynamicVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicReferenceVariable(GenericComponent[T], IDynamicVariable[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicReferenceVariable<>.

    Category: Data/Dynamic

    Parameterize with a value type::

        DynamicReferenceVariable[primitives.Float]
        DynamicReferenceVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicReferenceVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DynamicReferenceVariable<>"

    def __init__(self, variable_name: primitives.String | None = None, reference: str | T | None = None, override_on_link: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            reference: Initial value for Reference.
            override_on_link: Initial value for OverrideOnLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if reference is not None:
            self.reference = reference
        if override_on_link is not None:
            self.override_on_link = override_on_link

    @property
    def variable_name(self) -> primitives.String | None:
        """The VariableName field value."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: primitives.String) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets T)."""
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

    @property
    def override_on_link(self) -> primitives.Bool | None:
        """The OverrideOnLink field value."""
        member = self.get_member("OverrideOnLink")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_on_link.setter
    def override_on_link(self, value: primitives.Bool) -> None:
        """Set the OverrideOnLink field value."""
        member = self.get_member("OverrideOnLink")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideOnLink", fields.FieldBool(value=value)
            )

