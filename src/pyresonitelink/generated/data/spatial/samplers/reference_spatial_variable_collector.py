"""Generated component: ReferenceSpatialVariableCollector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.isync_ref_list import ISyncRefList
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceSpatialVariableCollector(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceSpatialVariableCollector<>.

    Category: Data/Spatial/Samplers

    Parameterize with a value type::

        ReferenceSpatialVariableCollector[np.float32]
        ReferenceSpatialVariableCollector[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceSpatialVariableCollector<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceSpatialVariableCollector<>"

    def __init__(self, reference_list: str | ISyncRefList[T] | None = None, variable_name: str | None = None, default_target: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference_list: Initial value for ReferenceList.
            variable_name: Initial value for VariableName.
            default_target: Initial value for DefaultTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference_list is not None:
            self.reference_list = reference_list
        if variable_name is not None:
            self.variable_name = variable_name
        if default_target is not None:
            self.default_target = default_target

    @property
    def reference_list(self) -> str | None:
        """Target ID of the ReferenceList reference (targets ISyncRefList[T])."""
        member = self.get_member("ReferenceList")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_list.setter
    def reference_list(self, target: str | ISyncRefList[T] | None) -> None:
        """Set the ReferenceList reference by target ID or ISyncRefList[T] instance."""
        target_id: str | None = target.id if isinstance(target, ISyncRefList) else target  # type: ignore[assignment]
        member = self.get_member("ReferenceList")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReferenceList",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncRefList<T>'),
            )

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

