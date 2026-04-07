"""Generated component: SphereStartEndValueSpatialVariable."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SphereStartEndValueSpatialVariable(GenericComponent[T], ISpatialVariable[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SphereStartEndValueSpatialVariable<>.

    Category: Data/Spatial/Sphere Variables

    Parameterize with a value type::

        SphereStartEndValueSpatialVariable[np.float32]
        SphereStartEndValueSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SphereStartEndValueSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.SphereStartEndValueSpatialVariable<>"

    def __init__(self, variable_name: str | None = None, priority: np.int32 | None = None, radius: np.float32 | None = None, blend_distance: np.float32 | None = None, start_value: T | None = None, end_value: T | None = None, start_distance: np.float32 | None = None, end_distance: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            radius: Initial value for Radius.
            blend_distance: Initial value for BlendDistance.
            start_value: Initial value for StartValue.
            end_value: Initial value for EndValue.
            start_distance: Initial value for StartDistance.
            end_distance: Initial value for EndDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if priority is not None:
            self.priority = priority
        if radius is not None:
            self.radius = radius
        if blend_distance is not None:
            self.blend_distance = blend_distance
        if start_value is not None:
            self.start_value = start_value
        if end_value is not None:
            self.end_value = end_value
        if start_distance is not None:
            self.start_distance = start_distance
        if end_distance is not None:
            self.end_distance = end_distance

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
    def priority(self) -> np.int32 | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: np.int32) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def blend_distance(self) -> np.float32 | None:
        """The BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blend_distance.setter
    def blend_distance(self, value: np.float32) -> None:
        """Set the BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendDistance", fields.FieldFloat(value=value)
            )

    @property
    def blend_distance_mode(self) -> members.FieldEnum | None:
        """The BlendDistanceMode member."""
        member = self.get_member("BlendDistanceMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @blend_distance_mode.setter
    def blend_distance_mode(self, value: members.FieldEnum) -> None:
        """Set the BlendDistanceMode member."""
        self.set_member("BlendDistanceMode", value)

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
        elif self._type_info is not None:
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
        elif self._type_info is not None:
            self.set_member(
                "EndValue", self._type_info.field_class(value=value)
            )

    @property
    def start_distance(self) -> np.float32 | None:
        """The StartDistance field value."""
        member = self.get_member("StartDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_distance.setter
    def start_distance(self, value: np.float32) -> None:
        """Set the StartDistance field value."""
        member = self.get_member("StartDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartDistance", fields.FieldFloat(value=value)
            )

    @property
    def end_distance(self) -> np.float32 | None:
        """The EndDistance field value."""
        member = self.get_member("EndDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_distance.setter
    def end_distance(self, value: np.float32) -> None:
        """Set the EndDistance field value."""
        member = self.get_member("EndDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndDistance", fields.FieldFloat(value=value)
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

