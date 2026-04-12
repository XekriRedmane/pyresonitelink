"""Generated component: MultiBoolConditionDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.condition_mode import ConditionMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiBoolConditionDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The MultiBoolConditionDriver drives ``Target`` depending on the state of the ``Conditions`` list, and the ``ConditionMode`` selected.

One popular use for this component is disabling meshes that need to be turned on or off in conjunction with other meshes.

For example, disabling fur tufts when clothing is enabled by using Active on each clothing item as a Condition, Mode set to 'None', and Target being Active on the fur tuft.

    Category: Transform/Drivers

    **Behavior**: Mode can be one of:

* All: Logical AND
* Any: Logical OR
* None: Logical NOR
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiBoolConditionDriver"

    def __init__(self, target: str | IField[primitives.Bool] | None = None, mode: ConditionMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            mode: Initial value for Mode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if mode is not None:
            self.mode = mode

    @property
    def target(self) -> str | None:
        """The field to drive to true if the bools in ``Conditions`` meet the conditions set by ``ConditionMode``"""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def mode(self) -> ConditionMode | None:
        """What state the bools in ``Conditions`` must be in, to drive ``Target`` to true."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ConditionMode(member.value)
        return None

    @mode.setter
    def mode(self, value: ConditionMode | str) -> None:
        """Set Mode. What state the bools in ``Conditions`` must be in, to drive ``Target`` to true."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def conditions(self) -> members.SyncList | None:
        """A list of bool fields to compare against the ``ConditionMode``"""
        member = self.get_member("Conditions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @conditions.setter
    def conditions(self, value: members.SyncList) -> None:
        """Set Conditions. A list of bool fields to compare against the ``ConditionMode``"""
        self.set_member("Conditions", value)

