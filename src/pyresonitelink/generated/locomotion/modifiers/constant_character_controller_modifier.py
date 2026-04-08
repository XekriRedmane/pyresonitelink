"""Generated component: ConstantCharacterControllerModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConstantCharacterControllerModifier(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ConstantCharacterControllerModifier.

    Category: Locomotion/Modifiers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConstantCharacterControllerModifier"

    def __init__(self, value: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value

    @property
    def parameter(self) -> members.FieldEnum | None:
        """The Parameter member."""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @parameter.setter
    def parameter(self, value: members.FieldEnum) -> None:
        """Set the Parameter member."""
        self.set_member("Parameter", value)

    @property
    def modification_mode(self) -> members.FieldEnum | None:
        """The ModificationMode member."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @modification_mode.setter
    def modification_mode(self, value: members.FieldEnum) -> None:
        """Set the ModificationMode member."""
        self.set_member("ModificationMode", value)

    @property
    def value(self) -> primitives.Float | None:
        """The Value field value."""
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

