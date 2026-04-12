"""Generated component: DynamicReferenceVariableReset."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicReferenceVariableReset(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Dynamic Reference Variable Reset is a component that will reset the value for a Dynamic Variable to a specified Reference. This is useful for when you are messing with an item, but you want the values for it to clear themselves with it is saved, loaded, or duplicated. The variable space is determined by the searching algorithm explained on Dynamic Variables page from the slot this is on.
}}

    Category: Data/Dynamic

    Parameterize with a value type::

        DynamicReferenceVariableReset[primitives.Float]
        DynamicReferenceVariableReset[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicReferenceVariableReset<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DynamicReferenceVariableReset<>"

    def __init__(self, variable_name: primitives.String | None = None, reset_on_load: primitives.Bool | None = None, reset_on_duplicate: primitives.Bool | None = None, reset_on_paste: primitives.Bool | None = None, reset_target: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            reset_on_load: Initial value for ResetOnLoad.
            reset_on_duplicate: Initial value for ResetOnDuplicate.
            reset_on_paste: Initial value for ResetOnPaste.
            reset_target: Initial value for ResetTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if reset_on_load is not None:
            self.reset_on_load = reset_on_load
        if reset_on_duplicate is not None:
            self.reset_on_duplicate = reset_on_duplicate
        if reset_on_paste is not None:
            self.reset_on_paste = reset_on_paste
        if reset_target is not None:
            self.reset_target = reset_target

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
    def reset_on_load(self) -> primitives.Bool | None:
        """Reset when this component is loaded with a world."""
        member = self.get_member("ResetOnLoad")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_on_load.setter
    def reset_on_load(self, value: primitives.Bool) -> None:
        """Set the ResetOnLoad field value."""
        member = self.get_member("ResetOnLoad")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetOnLoad", fields.FieldBool(value=value)
            )

    @property
    def reset_on_duplicate(self) -> primitives.Bool | None:
        """Reset when the object this is under is duplicated."""
        member = self.get_member("ResetOnDuplicate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_on_duplicate.setter
    def reset_on_duplicate(self, value: primitives.Bool) -> None:
        """Set the ResetOnDuplicate field value."""
        member = self.get_member("ResetOnDuplicate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetOnDuplicate", fields.FieldBool(value=value)
            )

    @property
    def reset_on_paste(self) -> primitives.Bool | None:
        """Reset when the object this is under is pasted from clipboard."""
        member = self.get_member("ResetOnPaste")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_on_paste.setter
    def reset_on_paste(self, value: primitives.Bool) -> None:
        """Set the ResetOnPaste field value."""
        member = self.get_member("ResetOnPaste")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetOnPaste", fields.FieldBool(value=value)
            )

    @property
    def reset_target(self) -> str | None:
        """The reference value to reset to when any of the enabled reset events occur."""
        member = self.get_member("ResetTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reset_target.setter
    def reset_target(self, target: str | T | None) -> None:
        """Set the ResetTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("ResetTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ResetTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

