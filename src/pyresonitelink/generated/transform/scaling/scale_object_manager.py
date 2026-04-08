"""Generated component: ScaleObjectManager."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleObjectManager(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaleObjectManager.

    Category: Transform/Scaling
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleObjectManager"

    def __init__(self, scale_power: np.float32 | None = None, lower_bound: np.float32 | None = None, upper_bound: np.float32 | None = None, far_size_transition_range: np.float32 | None = None, far_size_transition_exp: np.float32 | None = None, near_size_transition_range: np.float32 | None = None, near_size_transition_exp: np.float32 | None = None, far_offset_transition_range: np.float32 | None = None, far_offset_transition_exp: np.float32 | None = None, far_transition_offset: primitives.Float3 | None = None, near_offset_transition_range: np.float32 | None = None, near_offset_transition_exp: np.float32 | None = None, near_transition_offset: primitives.Float3 | None = None, center_offset_radius: np.float32 | None = None, optimal_distance: np.float32 | None = None, coordinate_power_base: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scale_power: Initial value for ScalePower.
            lower_bound: Initial value for LowerBound.
            upper_bound: Initial value for UpperBound.
            far_size_transition_range: Initial value for FarSizeTransitionRange.
            far_size_transition_exp: Initial value for FarSizeTransitionExp.
            near_size_transition_range: Initial value for NearSizeTransitionRange.
            near_size_transition_exp: Initial value for NearSizeTransitionExp.
            far_offset_transition_range: Initial value for FarOffsetTransitionRange.
            far_offset_transition_exp: Initial value for FarOffsetTransitionExp.
            far_transition_offset: Initial value for FarTransitionOffset.
            near_offset_transition_range: Initial value for NearOffsetTransitionRange.
            near_offset_transition_exp: Initial value for NearOffsetTransitionExp.
            near_transition_offset: Initial value for NearTransitionOffset.
            center_offset_radius: Initial value for CenterOffsetRadius.
            optimal_distance: Initial value for OptimalDistance.
            coordinate_power_base: Initial value for CoordinatePowerBase.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scale_power is not None:
            self.scale_power = scale_power
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound
        if far_size_transition_range is not None:
            self.far_size_transition_range = far_size_transition_range
        if far_size_transition_exp is not None:
            self.far_size_transition_exp = far_size_transition_exp
        if near_size_transition_range is not None:
            self.near_size_transition_range = near_size_transition_range
        if near_size_transition_exp is not None:
            self.near_size_transition_exp = near_size_transition_exp
        if far_offset_transition_range is not None:
            self.far_offset_transition_range = far_offset_transition_range
        if far_offset_transition_exp is not None:
            self.far_offset_transition_exp = far_offset_transition_exp
        if far_transition_offset is not None:
            self.far_transition_offset = far_transition_offset
        if near_offset_transition_range is not None:
            self.near_offset_transition_range = near_offset_transition_range
        if near_offset_transition_exp is not None:
            self.near_offset_transition_exp = near_offset_transition_exp
        if near_transition_offset is not None:
            self.near_transition_offset = near_transition_offset
        if center_offset_radius is not None:
            self.center_offset_radius = center_offset_radius
        if optimal_distance is not None:
            self.optimal_distance = optimal_distance
        if coordinate_power_base is not None:
            self.coordinate_power_base = coordinate_power_base

    @property
    def scale_power(self) -> np.float32 | None:
        """The ScalePower field value."""
        member = self.get_member("ScalePower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_power.setter
    def scale_power(self, value: np.float32) -> None:
        """Set the ScalePower field value."""
        member = self.get_member("ScalePower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScalePower", fields.FieldFloat(value=value)
            )

    @property
    def lower_bound(self) -> np.float32 | None:
        """The LowerBound field value."""
        member = self.get_member("LowerBound")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lower_bound.setter
    def lower_bound(self, value: np.float32) -> None:
        """Set the LowerBound field value."""
        member = self.get_member("LowerBound")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowerBound", fields.FieldFloat(value=value)
            )

    @property
    def upper_bound(self) -> np.float32 | None:
        """The UpperBound field value."""
        member = self.get_member("UpperBound")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upper_bound.setter
    def upper_bound(self, value: np.float32) -> None:
        """Set the UpperBound field value."""
        member = self.get_member("UpperBound")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpperBound", fields.FieldFloat(value=value)
            )

    @property
    def far_size_transition_range(self) -> np.float32 | None:
        """The FarSizeTransitionRange field value."""
        member = self.get_member("FarSizeTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_size_transition_range.setter
    def far_size_transition_range(self, value: np.float32) -> None:
        """Set the FarSizeTransitionRange field value."""
        member = self.get_member("FarSizeTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarSizeTransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def far_size_transition_exp(self) -> np.float32 | None:
        """The FarSizeTransitionExp field value."""
        member = self.get_member("FarSizeTransitionExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_size_transition_exp.setter
    def far_size_transition_exp(self, value: np.float32) -> None:
        """Set the FarSizeTransitionExp field value."""
        member = self.get_member("FarSizeTransitionExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarSizeTransitionExp", fields.FieldFloat(value=value)
            )

    @property
    def near_size_transition_range(self) -> np.float32 | None:
        """The NearSizeTransitionRange field value."""
        member = self.get_member("NearSizeTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_size_transition_range.setter
    def near_size_transition_range(self, value: np.float32) -> None:
        """Set the NearSizeTransitionRange field value."""
        member = self.get_member("NearSizeTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearSizeTransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def near_size_transition_exp(self) -> np.float32 | None:
        """The NearSizeTransitionExp field value."""
        member = self.get_member("NearSizeTransitionExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_size_transition_exp.setter
    def near_size_transition_exp(self, value: np.float32) -> None:
        """Set the NearSizeTransitionExp field value."""
        member = self.get_member("NearSizeTransitionExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearSizeTransitionExp", fields.FieldFloat(value=value)
            )

    @property
    def far_offset_transition_range(self) -> np.float32 | None:
        """The FarOffsetTransitionRange field value."""
        member = self.get_member("FarOffsetTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_offset_transition_range.setter
    def far_offset_transition_range(self, value: np.float32) -> None:
        """Set the FarOffsetTransitionRange field value."""
        member = self.get_member("FarOffsetTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarOffsetTransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def far_offset_transition_exp(self) -> np.float32 | None:
        """The FarOffsetTransitionExp field value."""
        member = self.get_member("FarOffsetTransitionExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_offset_transition_exp.setter
    def far_offset_transition_exp(self, value: np.float32) -> None:
        """Set the FarOffsetTransitionExp field value."""
        member = self.get_member("FarOffsetTransitionExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarOffsetTransitionExp", fields.FieldFloat(value=value)
            )

    @property
    def far_transition_offset(self) -> primitives.Float3 | None:
        """The FarTransitionOffset field value."""
        member = self.get_member("FarTransitionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_transition_offset.setter
    def far_transition_offset(self, value: primitives.Float3) -> None:
        """Set the FarTransitionOffset field value."""
        member = self.get_member("FarTransitionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarTransitionOffset", fields.FieldFloat3(value=value)
            )

    @property
    def near_offset_transition_range(self) -> np.float32 | None:
        """The NearOffsetTransitionRange field value."""
        member = self.get_member("NearOffsetTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_offset_transition_range.setter
    def near_offset_transition_range(self, value: np.float32) -> None:
        """Set the NearOffsetTransitionRange field value."""
        member = self.get_member("NearOffsetTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearOffsetTransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def near_offset_transition_exp(self) -> np.float32 | None:
        """The NearOffsetTransitionExp field value."""
        member = self.get_member("NearOffsetTransitionExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_offset_transition_exp.setter
    def near_offset_transition_exp(self, value: np.float32) -> None:
        """Set the NearOffsetTransitionExp field value."""
        member = self.get_member("NearOffsetTransitionExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearOffsetTransitionExp", fields.FieldFloat(value=value)
            )

    @property
    def near_transition_offset(self) -> primitives.Float3 | None:
        """The NearTransitionOffset field value."""
        member = self.get_member("NearTransitionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_transition_offset.setter
    def near_transition_offset(self, value: primitives.Float3) -> None:
        """Set the NearTransitionOffset field value."""
        member = self.get_member("NearTransitionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearTransitionOffset", fields.FieldFloat3(value=value)
            )

    @property
    def center_offset_radius(self) -> np.float32 | None:
        """The CenterOffsetRadius field value."""
        member = self.get_member("CenterOffsetRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @center_offset_radius.setter
    def center_offset_radius(self, value: np.float32) -> None:
        """Set the CenterOffsetRadius field value."""
        member = self.get_member("CenterOffsetRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CenterOffsetRadius", fields.FieldFloat(value=value)
            )

    @property
    def optimal_distance(self) -> np.float32 | None:
        """The OptimalDistance field value."""
        member = self.get_member("OptimalDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @optimal_distance.setter
    def optimal_distance(self, value: np.float32) -> None:
        """Set the OptimalDistance field value."""
        member = self.get_member("OptimalDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OptimalDistance", fields.FieldFloat(value=value)
            )

    @property
    def coordinate_power_base(self) -> primitives.Float3 | None:
        """The CoordinatePowerBase field value."""
        member = self.get_member("CoordinatePowerBase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @coordinate_power_base.setter
    def coordinate_power_base(self, value: primitives.Float3) -> None:
        """Set the CoordinatePowerBase field value."""
        member = self.get_member("CoordinatePowerBase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CoordinatePowerBase", fields.FieldFloat3(value=value)
            )

