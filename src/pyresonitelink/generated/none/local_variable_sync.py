"""Generated component: LocalVariableSync."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalVariableSync(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocalVariableSync<>.

    Parameterize with a value type::

        LocalVariableSync[np.float32]
        LocalVariableSync[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalVariableSync<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.LocalVariableSync<>"

    def __init__(self, value: str | IField[T] | None = None, variable: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            variable: Initial value for Variable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if variable is not None:
            self.variable = variable

    @property
    def owner_user(self) -> members.SyncObject | None:
        """The OwnerUser member."""
        member = self.get_member("OwnerUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @owner_user.setter
    def owner_user(self, value: members.SyncObject) -> None:
        """Set the OwnerUser member."""
        self.set_member("OwnerUser", value)

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets IField[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | IField[T] | None) -> None:
        """Set the Value reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def variable(self) -> str | None:
        """The Variable field value."""
        member = self.get_member("Variable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable.setter
    def variable(self, value: str) -> None:
        """Set the Variable field value."""
        member = self.get_member("Variable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Variable", fields.FieldString(value=value)
            )

