"""Generated component: DynamicVariableSpace."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicVariableSpace(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicVariableSpace.

    Category: Data/Dynamic
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
        """The SpaceName field value."""
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
        """The OnlyDirectBinding field value."""
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

