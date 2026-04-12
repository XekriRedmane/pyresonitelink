"""Generated component: BoxVertexValueSpatialVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.spatial_variable_blend_distance_mode import SpatialVariableBlendDistanceMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxVertexValueSpatialVariable(GenericComponent[T], ISpatialVariable[T], IComponent, IWorldEventReceiver):
    """The Box Vertex Value Spatial Variable`1 component makes a spatial variable that provides samplers with a different value depending on what vertex of the area a sampler is closest to. This is similar to the color properties of a box emitter.

    Category: Data/Spatial/Box Variables

    Attach to a slot and provide a size and variable name in order for this
    to function.

    Parameterize with a value type::

        BoxVertexValueSpatialVariable[primitives.Float]
        BoxVertexValueSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxVertexValueSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.BoxVertexValueSpatialVariable<>"

    def __init__(self, variable_name: primitives.String | None = None, priority: primitives.Int | None = None, size: primitives.Float3 | None = None, blend_distance: primitives.Float | None = None, blend_distance_mode: SpatialVariableBlendDistanceMode | str | None = None, value0: T | None = None, value1: T | None = None, value2: T | None = None, value3: T | None = None, value4: T | None = None, value5: T | None = None, value6: T | None = None, value7: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            size: Initial value for Size.
            blend_distance: Initial value for BlendDistance.
            blend_distance_mode: Initial value for BlendDistanceMode.
            value0: Initial value for Value0.
            value1: Initial value for Value1.
            value2: Initial value for Value2.
            value3: Initial value for Value3.
            value4: Initial value for Value4.
            value5: Initial value for Value5.
            value6: Initial value for Value6.
            value7: Initial value for Value7.
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
        if value0 is not None:
            self.value0 = value0
        if value1 is not None:
            self.value1 = value1
        if value2 is not None:
            self.value2 = value2
        if value3 is not None:
            self.value3 = value3
        if value4 is not None:
            self.value4 = value4
        if value5 is not None:
            self.value5 = value5
        if value6 is not None:
            self.value6 = value6
        if value7 is not None:
            self.value7 = value7

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
        """The size of the cube for this spatial variable's influence."""
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
    def value0(self) -> T | None:
        """The Value0 field value (type depends on type parameter)."""
        member = self.get_member("Value0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value0.setter
    def value0(self, value: T) -> None:
        """Set the Value0 field value."""
        member = self.get_member("Value0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value0", self._type_info.field_class(value=value)
            )

    @property
    def value1(self) -> T | None:
        """The Value1 field value (type depends on type parameter)."""
        member = self.get_member("Value1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value1.setter
    def value1(self, value: T) -> None:
        """Set the Value1 field value."""
        member = self.get_member("Value1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value1", self._type_info.field_class(value=value)
            )

    @property
    def value2(self) -> T | None:
        """The Value2 field value (type depends on type parameter)."""
        member = self.get_member("Value2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value2.setter
    def value2(self, value: T) -> None:
        """Set the Value2 field value."""
        member = self.get_member("Value2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value2", self._type_info.field_class(value=value)
            )

    @property
    def value3(self) -> T | None:
        """The Value3 field value (type depends on type parameter)."""
        member = self.get_member("Value3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value3.setter
    def value3(self, value: T) -> None:
        """Set the Value3 field value."""
        member = self.get_member("Value3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value3", self._type_info.field_class(value=value)
            )

    @property
    def value4(self) -> T | None:
        """The Value4 field value (type depends on type parameter)."""
        member = self.get_member("Value4")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value4.setter
    def value4(self, value: T) -> None:
        """Set the Value4 field value."""
        member = self.get_member("Value4")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value4", self._type_info.field_class(value=value)
            )

    @property
    def value5(self) -> T | None:
        """The Value5 field value (type depends on type parameter)."""
        member = self.get_member("Value5")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value5.setter
    def value5(self, value: T) -> None:
        """Set the Value5 field value."""
        member = self.get_member("Value5")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value5", self._type_info.field_class(value=value)
            )

    @property
    def value6(self) -> T | None:
        """The Value6 field value (type depends on type parameter)."""
        member = self.get_member("Value6")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value6.setter
    def value6(self, value: T) -> None:
        """Set the Value6 field value."""
        member = self.get_member("Value6")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value6", self._type_info.field_class(value=value)
            )

    @property
    def value7(self) -> T | None:
        """The Value7 field value (type depends on type parameter)."""
        member = self.get_member("Value7")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value7.setter
    def value7(self, value: T) -> None:
        """Set the Value7 field value."""
        member = self.get_member("Value7")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value7", self._type_info.field_class(value=value)
            )

