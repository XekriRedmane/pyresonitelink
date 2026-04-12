"""Generated component: CloningReferenceSpatialVariableCollector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.clone_mode import CloneMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.isync_ref_list import ISyncRefList


class CloningReferenceSpatialVariableCollector(GenericComponent[T]):
    """The Cloning Reference Spatial Variable Collector`1 component is part of the Spatial variables system. It works similarly to ReferenceSpatialVariableCollector, but specifically for components. For each component it finds at the point, it will create & maintain a duplicate. It can duplicate either just the component itself or the whole Slot it's on. The duplicates can be made Local only (it's your responsibility to make sure that the target list can reference local elements). It will never clone spatial variables present on the slot.

    Category: Data/Spatial/Samplers

    Attach to a slot and bring near a set of Spatial variables to get a list
    of references. don't forget to add a variable name and reference list.

    Parameterize with a value type::

        CloningReferenceSpatialVariableCollector[primitives.Float]
        CloningReferenceSpatialVariableCollector[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloningReferenceSpatialVariableCollector<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CloningReferenceSpatialVariableCollector<>"

    def __init__(self, clone_parent: str | Slot | None = None, make_clones_local: primitives.Bool | None = None, variable_name: primitives.String | None = None, mode: CloneMode | str | None = None, reference_list: str | ISyncRefList[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            clone_parent: Initial value for CloneParent.
            make_clones_local: Initial value for MakeClonesLocal.
            variable_name: Initial value for VariableName.
            mode: Initial value for Mode.
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
        if mode is not None:
            self.mode = mode
        if reference_list is not None:
            self.reference_list = reference_list

    @property
    def clone_parent(self) -> str | None:
        """The slot to parent cloned elements to."""
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
        """Whether cloned items should be on the local machine rather than networked."""
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
        """The name of the variable being sampled."""
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
    def mode(self) -> CloneMode | None:
        """How to clone elements this samples."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CloneMode(member.value)
        return None

    @mode.setter
    def mode(self, value: CloneMode | str) -> None:
        """Set Mode. How to clone elements this samples."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def reference_list(self) -> str | None:
        """The list of references this component has sampled at the point of the slot it is on."""
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

