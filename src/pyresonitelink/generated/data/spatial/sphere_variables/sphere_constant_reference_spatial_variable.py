"""Generated component: SphereConstantReferenceSpatialVariable."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SphereConstantReferenceSpatialVariable(GenericComponent[T], ISpatialVariable[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SphereConstantReferenceSpatialVariable<>.

    Category: Data/Spatial/Sphere Variables

    Parameterize with a value type::

        SphereConstantReferenceSpatialVariable[np.float32]
        SphereConstantReferenceSpatialVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SphereConstantReferenceSpatialVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.SphereConstantReferenceSpatialVariable<>"

    def __init__(self, variable_name: str | None = None, priority: np.int32 | None = None, radius: np.float32 | None = None, blend_distance: np.float32 | None = None, reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            radius: Initial value for Radius.
            blend_distance: Initial value for BlendDistance.
            reference: Initial value for Reference.
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
        if reference is not None:
            self.reference = reference

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

