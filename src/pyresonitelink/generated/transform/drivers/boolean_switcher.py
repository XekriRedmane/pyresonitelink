"""Generated component: BooleanSwitcher."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanSwitcher(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The BooleanSwitcher component can be used to enable and disable a list of Slots depending on an index in the list.
It does so by driving the Active field of the slots.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanSwitcher"

    def __init__(self, auto_add_children: primitives.Bool | None = None, active_index: primitives.Int | None = None, activation_mode: Mode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            active_index: Initial value for ActiveIndex.
            activation_mode: Initial value for ActivationMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if active_index is not None:
            self.active_index = active_index
        if activation_mode is not None:
            self.activation_mode = activation_mode

    @property
    def auto_add_children(self) -> primitives.Bool | None:
        """If true, the Targets list will be automatically populated with the child slots of the slot that this component is on."""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: primitives.Bool) -> None:
        """Set the AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddChildren", fields.FieldBool(value=value)
            )

    @property
    def auto_add_ignore_tags(self) -> members.SyncList | None:
        """Don't auto add a child slot to the list if it has a tag that is in this list."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set AutoAddIgnoreTags. Don't auto add a child slot to the list if it has a tag that is in this list."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def targets(self) -> members.SyncList | None:
        """The list of slots of which one will be enabled."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set Targets. The list of slots of which one will be enabled."""
        self.set_member("Targets", value)

    @property
    def active_index(self) -> primitives.Int | None:
        """The index of the currently active slot."""
        member = self.get_member("ActiveIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_index.setter
    def active_index(self, value: primitives.Int) -> None:
        """Set the ActiveIndex field value."""
        member = self.get_member("ActiveIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveIndex", fields.FieldInt(value=value)
            )

    @property
    def activation_mode(self) -> Mode | None:
        """Allows for enabling items in ``Target`` based on ``ActiveIndex`` number."""
        member = self.get_member("ActivationMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @activation_mode.setter
    def activation_mode(self, value: Mode | str) -> None:
        """Set ActivationMode. Allows for enabling items in ``Target`` based on ``ActiveIndex`` number."""
        member = self.get_member("ActivationMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ActivationMode",
                members.FieldEnum(value=str(value)),
            )

