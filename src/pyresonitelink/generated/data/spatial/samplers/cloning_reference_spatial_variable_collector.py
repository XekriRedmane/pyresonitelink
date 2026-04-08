"""Generated component: CloningReferenceSpatialVariableCollector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.isync_ref_list import ISyncRefList


class CloningReferenceSpatialVariableCollector(GenericComponent[T]):
    """Wrapper for [FrooxEngine]FrooxEngine.CloningReferenceSpatialVariableCollector<>.

    Category: Data/Spatial/Samplers

    Parameterize with a value type::

        CloningReferenceSpatialVariableCollector[primitives.Float]
        CloningReferenceSpatialVariableCollector[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloningReferenceSpatialVariableCollector<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CloningReferenceSpatialVariableCollector<>"

    def __init__(self, clone_parent: str | Slot | None = None, make_clones_local: primitives.Bool | None = None, variable_name: primitives.String | None = None, reference_list: str | ISyncRefList[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            clone_parent: Initial value for CloneParent.
            make_clones_local: Initial value for MakeClonesLocal.
            variable_name: Initial value for VariableName.
            reference_list: Initial value for ReferenceList.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if clone_parent is not None:
            self.clone_parent = clone_parent
        if make_clones_local is not None:
            self.make_clones_local = make_clones_local
        if variable_name is not None:
            self.variable_name = variable_name
        if reference_list is not None:
            self.reference_list = reference_list

    @property
    def clone_parent(self) -> str | None:
        """Target ID of the CloneParent reference (targets Slot)."""
        member = self.get_member("CloneParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clone_parent.setter
    def clone_parent(self, target: str | Slot | None) -> None:
        """Set the CloneParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("CloneParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CloneParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def make_clones_local(self) -> primitives.Bool | None:
        """The MakeClonesLocal field value."""
        member = self.get_member("MakeClonesLocal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @make_clones_local.setter
    def make_clones_local(self, value: primitives.Bool) -> None:
        """Set the MakeClonesLocal field value."""
        member = self.get_member("MakeClonesLocal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MakeClonesLocal", fields.FieldBool(value=value)
            )

    @property
    def variable_name(self) -> primitives.String | None:
        """The VariableName field value."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: primitives.String) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

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

