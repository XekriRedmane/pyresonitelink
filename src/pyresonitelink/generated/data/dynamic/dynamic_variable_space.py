"""Generated component: DynamicVariableSpace."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicVariableSpace(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DynamicVariableSpace component is used to separate dynamic variables into namespaces. Since dynamic variables are, by default, created on the slot of the nearest parent DynamicVariableSpace, this component provides control over where the root of that space is, as well as part of the path name to be referenced when using a consumer of dynamic variables, such as DynamicValueVariableDriver`1. For more info see Dynamic Variables.

    Category: Data/Dynamic

    **Introduction**: The DynamicVariableSpace component is used to separate dynamic variables into namespaces.
Since dynamic variables are, by default, created on the slot of the nearest parent DynamicVariableSpace, this component provides control over where the root of that space is, as well as part of the path name to be referenced when using a consumer of dynamic variables, such as DynamicValueVariableDriver`1. For more info see Dynamic Variables.

    **Behavior**: == Examples ==
By default worlds have a DynamicVariableSpace named "World" and users have a DynamicVariableSpace named "User\"
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicVariableSpace"

    def __init__(self, space_name: primitives.String | None = None, only_direct_binding: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            space_name: Initial value for SpaceName.
            only_direct_binding: Initial value for OnlyDirectBinding.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if space_name is not None:
            self.space_name = space_name
        if only_direct_binding is not None:
            self.only_direct_binding = only_direct_binding

    @property
    def space_name(self) -> primitives.String | None:
        """The name of the space."""
        member = self.get_member("SpaceName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @space_name.setter
    def space_name(self, value: primitives.String) -> None:
        """Set the SpaceName field value."""
        member = self.get_member("SpaceName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpaceName", fields.FieldString(value=value)
            )

    @property
    def only_direct_binding(self) -> primitives.Bool | None:
        """When enabled, variables won't be bound to this space unless they specify it by name: /."""
        member = self.get_member("OnlyDirectBinding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @only_direct_binding.setter
    def only_direct_binding(self, value: primitives.Bool) -> None:
        """Set the OnlyDirectBinding field value."""
        member = self.get_member("OnlyDirectBinding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OnlyDirectBinding", fields.FieldBool(value=value)
            )

