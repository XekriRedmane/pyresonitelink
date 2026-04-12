"""Generated component: ConstantCharacterControllerModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.character_controller_parameter import CharacterControllerParameter
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConstantCharacterControllerModifier(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ConstantCharacterController component modifies the properties of a CharacterController that makes contact with a character collider on the same Slot as this component.

    Category: Locomotion/Modifiers

    Attach to a slot with a collider that is a character collider. Then
    specify the settings this component should change and how. Then this
    component will be ready to use.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConstantCharacterControllerModifier"

    def __init__(self, parameter: CharacterControllerParameter | str | None = None, modification_mode: Mode | str | None = None, value: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parameter: Initial value for Parameter.
            modification_mode: Initial value for ModificationMode.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parameter is not None:
            self.parameter = parameter
        if modification_mode is not None:
            self.modification_mode = modification_mode
        if value is not None:
            self.value = value

    @property
    def parameter(self) -> CharacterControllerParameter | None:
        """The parameter to modify"""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CharacterControllerParameter(member.value)
        return None

    @parameter.setter
    def parameter(self, value: CharacterControllerParameter | str) -> None:
        """Set Parameter. The parameter to modify"""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Parameter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def modification_mode(self) -> Mode | None:
        """How to modify the parameter."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @modification_mode.setter
    def modification_mode(self, value: Mode | str) -> None:
        """Set ModificationMode. How to modify the parameter."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ModificationMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def value(self) -> primitives.Float | None:
        """the value to use in the modification."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: primitives.Float) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Value", fields.FieldFloat(value=value)
            )

