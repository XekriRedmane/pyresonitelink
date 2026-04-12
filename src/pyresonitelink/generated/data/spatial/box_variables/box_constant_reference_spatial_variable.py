"""Generated component: BoxConstantReferenceSpatialVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.spatial_variable_blend_distance_mode import SpatialVariableBlendDistanceMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxConstantReferenceSpatialVariable(GenericComponent[T], ISpatialVariable[T], IComponent, IWorldEventReceiver):
    """The Box Constant Reference Spatial Variable`1 component provides a constant value regardless of position inside of it as a contribution to a Spatial variables system.

    Category: Data/Spatial/Box Variables

    Attach to a slot and provide a size and variable name in order for this
    to function.

    Parameterize with a value type::

        BoxConstantReferenceSpatialVariable[primitives.Float]
        BoxConstantReferenceSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxConstantReferenceSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BoxConstantReferenceSpatialVariable<>"

    def __init__(self, variable_name: primitives.String | None = None, priority: primitives.Int | None = None, size: primitives.Float3 | None = None, blend_distance: primitives.Float | None = None, blend_distance_mode: SpatialVariableBlendDistanceMode | str | None = None, reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            size: Initial value for Size.
            blend_distance: Initial value for BlendDistance.
            blend_distance_mode: Initial value for BlendDistanceMode.
            reference: Initial value for Reference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if priority is not None:
            self.priority = priority
        if size is not None:
            self.size = size
        if blend_distance is not None:
            self.blend_distance = blend_distance
        if blend_distance_mode is not None:
            self.blend_distance_mode = blend_distance_mode
        if reference is not None:
            self.reference = reference

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
    def priority(self) -> primitives.Int | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def size(self) -> primitives.Float3 | None:
        """How big the box is for the area of influence."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float3) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat3(value=value)
            )

    @property
    def blend_distance(self) -> primitives.Float | None:
        """The BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blend_distance.setter
    def blend_distance(self, value: primitives.Float) -> None:
        """Set the BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendDistance", fields.FieldFloat(value=value)
            )

    @property
    def blend_distance_mode(self) -> SpatialVariableBlendDistanceMode | None:
        """The BlendDistanceMode enum value."""
        member = self.get_member("BlendDistanceMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SpatialVariableBlendDistanceMode(member.value)
        return None

    @blend_distance_mode.setter
    def blend_distance_mode(self, value: SpatialVariableBlendDistanceMode | str) -> None:
        """Set the BlendDistanceMode enum value."""
        member = self.get_member("BlendDistanceMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BlendDistanceMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets T)."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | T | None) -> None:
        """Set the Reference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='T'),
            )

