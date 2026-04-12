"""Generated component: BoxGradientValueSpatialVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.spatial_variable_blend_distance_mode import SpatialVariableBlendDistanceMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxGradientValueSpatialVariable(GenericComponent[T], ISpatialVariable[T], IComponent, IWorldEventReceiver):
    """The Box Gradient Value Spatial Variable`1 component is a Spatial variables variable where the value changes from Start to End value along a Direction. This works best when the direction is aligned with one of the cube's axes. Start value starts at the edge of the shape and goes inwards towards the center.

    Category: Data/Spatial/Box Variables

    Attach to a slot and provide a size and variable name in order for this
    to function.

    Parameterize with a value type::

        BoxGradientValueSpatialVariable[primitives.Float]
        BoxGradientValueSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxGradientValueSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BoxGradientValueSpatialVariable<>"

    def __init__(self, variable_name: primitives.String | None = None, priority: primitives.Int | None = None, size: primitives.Float3 | None = None, blend_distance: primitives.Float | None = None, blend_distance_mode: SpatialVariableBlendDistanceMode | str | None = None, start_value: T | None = None, end_value: T | None = None, gradient_direction: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            size: Initial value for Size.
            blend_distance: Initial value for BlendDistance.
            blend_distance_mode: Initial value for BlendDistanceMode.
            start_value: Initial value for StartValue.
            end_value: Initial value for EndValue.
            gradient_direction: Initial value for GradientDirection.
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
        if start_value is not None:
            self.start_value = start_value
        if end_value is not None:
            self.end_value = end_value
        if gradient_direction is not None:
            self.gradient_direction = gradient_direction

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
        """The size of the cube in which this variable can be sampled from."""
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
    def start_value(self) -> T | None:
        """The StartValue field value (type depends on type parameter)."""
        member = self.get_member("StartValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_value.setter
    def start_value(self, value: T) -> None:
        """Set the StartValue field value."""
        member = self.get_member("StartValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "StartValue", self._type_info.field_class(value=value)
            )

    @property
    def end_value(self) -> T | None:
        """The EndValue field value (type depends on type parameter)."""
        member = self.get_member("EndValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_value.setter
    def end_value(self, value: T) -> None:
        """Set the EndValue field value."""
        member = self.get_member("EndValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "EndValue", self._type_info.field_class(value=value)
            )

    @property
    def gradient_direction(self) -> primitives.Float3 | None:
        """The direction the Gradient goes in local space to the Spatial variable."""
        member = self.get_member("GradientDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gradient_direction.setter
    def gradient_direction(self, value: primitives.Float3) -> None:
        """Set the GradientDirection field value."""
        member = self.get_member("GradientDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GradientDirection", fields.FieldFloat3(value=value)
            )

