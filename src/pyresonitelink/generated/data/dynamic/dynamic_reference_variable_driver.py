"""Generated component: DynamicReferenceVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.idynamic_variable import IDynamicVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicReferenceVariableDriver(GenericComponent[T], IDynamicVariable[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicReferenceVariableDriver<>.

    Category: Data/Dynamic

    Parameterize with a value type::

        DynamicReferenceVariableDriver[np.float32]
        DynamicReferenceVariableDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicReferenceVariableDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DynamicReferenceVariableDriver<>"

    def __init__(self, variable_name: str | None = None, target: str | SyncRef[T] | None = None, default_target: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            target: Initial value for Target.
            default_target: Initial value for DefaultTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if target is not None:
            self.target = target
        if default_target is not None:
            self.default_target = default_target

    @property
    def variable_name(self) -> str | None:
        """The VariableName field value."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: str) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncRef[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncRef[T] | None) -> None:
        """Set the Target reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def default_target(self) -> str | None:
        """Target ID of the DefaultTarget reference (targets T)."""
        member = self.get_member("DefaultTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_target.setter
    def default_target(self, target: str | T | None) -> None:
        """Set the DefaultTarget reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("DefaultTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultTarget",
                members.Reference(targetId=target_id, targetType='T'),
            )

