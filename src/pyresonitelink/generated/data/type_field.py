"""Generated component: TypeField."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TypeField(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TypeField component is used to store a Type which is usually a reference to a C# class.

    Category: Data

    This can be used with ProtoFlux to get the color of a Type or its full
    name.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TypeField"

    def __init__(self, type_: Type | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            type_: Initial value for Type.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if type_ is not None:
            self.type_ = type_

    @property
    def type_(self) -> Type | None:
        """The Type this component is storing."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @type_.setter
    def type_(self, value: Type | str) -> None:
        """Set Type. The Type this component is storing."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Type",
                members.FieldEnum(value=str(value)),
            )

