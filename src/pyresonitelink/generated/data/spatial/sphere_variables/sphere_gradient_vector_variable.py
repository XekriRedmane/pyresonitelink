"""Generated component: SphereGradientVectorVariable."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SphereGradientVectorVariable(GeneratedComponent, ISpatialVariable, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SphereGradientVectorVariable.

    Category: Data/Spatial/Sphere Variables
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SphereGradientVectorVariable"

    def __init__(self, variable_name: str | None = None, priority: np.int32 | None = None, radius: np.float32 | None = None, blend_distance: np.float32 | None = None, edge_magnitude: np.float32 | None = None, center_magnitude: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            radius: Initial value for Radius.
            blend_distance: Initial value for BlendDistance.
            edge_magnitude: Initial value for EdgeMagnitude.
            center_magnitude: Initial value for CenterMagnitude.
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
        if edge_magnitude is not None:
            self.edge_magnitude = edge_magnitude
        if center_magnitude is not None:
            self.center_magnitude = center_magnitude

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
    def edge_magnitude(self) -> np.float32 | None:
        """The EdgeMagnitude field value."""
        member = self.get_member("EdgeMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_magnitude.setter
    def edge_magnitude(self, value: np.float32) -> None:
        """Set the EdgeMagnitude field value."""
        member = self.get_member("EdgeMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def center_magnitude(self) -> np.float32 | None:
        """The CenterMagnitude field value."""
        member = self.get_member("CenterMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @center_magnitude.setter
    def center_magnitude(self, value: np.float32) -> None:
        """Set the CenterMagnitude field value."""
        member = self.get_member("CenterMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CenterMagnitude", fields.FieldFloat(value=value)
            )

