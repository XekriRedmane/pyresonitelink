"""Generated component: TubeSpiralMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TubeSpiralMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TubeSpiralMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TubeSpiralMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, steps: np.int32 | None = None, maximum_distance_between_rings: np.float32 | None = None, radius_independent_step_scaling: bool | None = None, coil_count: np.float32 | None = None, scale_coil_count_by_length: bool | None = None, coil_phase: np.float32 | None = None, start_point: primitives.Float3 | None = None, start_tangent: primitives.Float3 | None = None, end_point: primitives.Float3 | None = None, end_tangent: primitives.Float3 | None = None, start_spiral_radius: np.float32 | None = None, end_spiral_radius: np.float32 | None = None, start_spiral_orientation: primitives.FloatQ | None = None, end_spiral_orientation: primitives.FloatQ | None = None, start_tube_radius: np.float32 | None = None, end_tube_radius: np.float32 | None = None, tube_points: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            steps: Initial value for Steps.
            maximum_distance_between_rings: Initial value for MaximumDistanceBetweenRings.
            radius_independent_step_scaling: Initial value for RadiusIndependentStepScaling.
            coil_count: Initial value for CoilCount.
            scale_coil_count_by_length: Initial value for ScaleCoilCountByLength.
            coil_phase: Initial value for CoilPhase.
            start_point: Initial value for StartPoint.
            start_tangent: Initial value for StartTangent.
            end_point: Initial value for EndPoint.
            end_tangent: Initial value for EndTangent.
            start_spiral_radius: Initial value for StartSpiralRadius.
            end_spiral_radius: Initial value for EndSpiralRadius.
            start_spiral_orientation: Initial value for StartSpiralOrientation.
            end_spiral_orientation: Initial value for EndSpiralOrientation.
            start_tube_radius: Initial value for StartTubeRadius.
            end_tube_radius: Initial value for EndTubeRadius.
            tube_points: Initial value for TubePoints.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if steps is not None:
            self.steps = steps
        if maximum_distance_between_rings is not None:
            self.maximum_distance_between_rings = maximum_distance_between_rings
        if radius_independent_step_scaling is not None:
            self.radius_independent_step_scaling = radius_independent_step_scaling
        if coil_count is not None:
            self.coil_count = coil_count
        if scale_coil_count_by_length is not None:
            self.scale_coil_count_by_length = scale_coil_count_by_length
        if coil_phase is not None:
            self.coil_phase = coil_phase
        if start_point is not None:
            self.start_point = start_point
        if start_tangent is not None:
            self.start_tangent = start_tangent
        if end_point is not None:
            self.end_point = end_point
        if end_tangent is not None:
            self.end_tangent = end_tangent
        if start_spiral_radius is not None:
            self.start_spiral_radius = start_spiral_radius
        if end_spiral_radius is not None:
            self.end_spiral_radius = end_spiral_radius
        if start_spiral_orientation is not None:
            self.start_spiral_orientation = start_spiral_orientation
        if end_spiral_orientation is not None:
            self.end_spiral_orientation = end_spiral_orientation
        if start_tube_radius is not None:
            self.start_tube_radius = start_tube_radius
        if end_tube_radius is not None:
            self.end_tube_radius = end_tube_radius
        if tube_points is not None:
            self.tube_points = tube_points

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: bool) -> None:
        """Set the OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideBoundingBox", fields.FieldBool(value=value)
            )

    @property
    def overriden_bounding_box(self) -> primitives.BoundingBox | None:
        """The OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overriden_bounding_box.setter
    def overriden_bounding_box(self, value: primitives.BoundingBox) -> None:
        """Set the OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverridenBoundingBox", fields.FieldBoundingBox(value=value)
            )

    @property
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def steps(self) -> np.int32 | None:
        """The Steps field value."""
        member = self.get_member("Steps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @steps.setter
    def steps(self, value: np.int32) -> None:
        """Set the Steps field value."""
        member = self.get_member("Steps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Steps", fields.FieldInt(value=value)
            )

    @property
    def maximum_distance_between_rings(self) -> np.float32 | None:
        """The MaximumDistanceBetweenRings field value."""
        member = self.get_member("MaximumDistanceBetweenRings")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_distance_between_rings.setter
    def maximum_distance_between_rings(self, value: np.float32) -> None:
        """Set the MaximumDistanceBetweenRings field value."""
        member = self.get_member("MaximumDistanceBetweenRings")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumDistanceBetweenRings", fields.FieldNullableFloat(value=value)
            )

    @property
    def radius_independent_step_scaling(self) -> bool | None:
        """The RadiusIndependentStepScaling field value."""
        member = self.get_member("RadiusIndependentStepScaling")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_independent_step_scaling.setter
    def radius_independent_step_scaling(self, value: bool) -> None:
        """Set the RadiusIndependentStepScaling field value."""
        member = self.get_member("RadiusIndependentStepScaling")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusIndependentStepScaling", fields.FieldBool(value=value)
            )

    @property
    def coil_count(self) -> np.float32 | None:
        """The CoilCount field value."""
        member = self.get_member("CoilCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @coil_count.setter
    def coil_count(self, value: np.float32) -> None:
        """Set the CoilCount field value."""
        member = self.get_member("CoilCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CoilCount", fields.FieldFloat(value=value)
            )

    @property
    def scale_coil_count_by_length(self) -> bool | None:
        """The ScaleCoilCountByLength field value."""
        member = self.get_member("ScaleCoilCountByLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_coil_count_by_length.setter
    def scale_coil_count_by_length(self, value: bool) -> None:
        """Set the ScaleCoilCountByLength field value."""
        member = self.get_member("ScaleCoilCountByLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleCoilCountByLength", fields.FieldBool(value=value)
            )

    @property
    def coil_phase(self) -> np.float32 | None:
        """The CoilPhase field value."""
        member = self.get_member("CoilPhase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @coil_phase.setter
    def coil_phase(self, value: np.float32) -> None:
        """Set the CoilPhase field value."""
        member = self.get_member("CoilPhase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CoilPhase", fields.FieldFloat(value=value)
            )

    @property
    def start_point(self) -> primitives.Float3 | None:
        """The StartPoint field value."""
        member = self.get_member("StartPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_point.setter
    def start_point(self, value: primitives.Float3) -> None:
        """Set the StartPoint field value."""
        member = self.get_member("StartPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartPoint", fields.FieldFloat3(value=value)
            )

    @property
    def start_tangent(self) -> primitives.Float3 | None:
        """The StartTangent field value."""
        member = self.get_member("StartTangent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_tangent.setter
    def start_tangent(self, value: primitives.Float3) -> None:
        """Set the StartTangent field value."""
        member = self.get_member("StartTangent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartTangent", fields.FieldFloat3(value=value)
            )

    @property
    def end_point(self) -> primitives.Float3 | None:
        """The EndPoint field value."""
        member = self.get_member("EndPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_point.setter
    def end_point(self, value: primitives.Float3) -> None:
        """Set the EndPoint field value."""
        member = self.get_member("EndPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndPoint", fields.FieldFloat3(value=value)
            )

    @property
    def end_tangent(self) -> primitives.Float3 | None:
        """The EndTangent field value."""
        member = self.get_member("EndTangent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_tangent.setter
    def end_tangent(self, value: primitives.Float3) -> None:
        """Set the EndTangent field value."""
        member = self.get_member("EndTangent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndTangent", fields.FieldFloat3(value=value)
            )

    @property
    def start_spiral_radius(self) -> np.float32 | None:
        """The StartSpiralRadius field value."""
        member = self.get_member("StartSpiralRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_spiral_radius.setter
    def start_spiral_radius(self, value: np.float32) -> None:
        """Set the StartSpiralRadius field value."""
        member = self.get_member("StartSpiralRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartSpiralRadius", fields.FieldFloat(value=value)
            )

    @property
    def end_spiral_radius(self) -> np.float32 | None:
        """The EndSpiralRadius field value."""
        member = self.get_member("EndSpiralRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_spiral_radius.setter
    def end_spiral_radius(self, value: np.float32) -> None:
        """Set the EndSpiralRadius field value."""
        member = self.get_member("EndSpiralRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndSpiralRadius", fields.FieldFloat(value=value)
            )

    @property
    def start_spiral_orientation(self) -> primitives.FloatQ | None:
        """The StartSpiralOrientation field value."""
        member = self.get_member("StartSpiralOrientation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_spiral_orientation.setter
    def start_spiral_orientation(self, value: primitives.FloatQ) -> None:
        """Set the StartSpiralOrientation field value."""
        member = self.get_member("StartSpiralOrientation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartSpiralOrientation", fields.FieldFloatQ(value=value)
            )

    @property
    def end_spiral_orientation(self) -> primitives.FloatQ | None:
        """The EndSpiralOrientation field value."""
        member = self.get_member("EndSpiralOrientation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_spiral_orientation.setter
    def end_spiral_orientation(self, value: primitives.FloatQ) -> None:
        """Set the EndSpiralOrientation field value."""
        member = self.get_member("EndSpiralOrientation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndSpiralOrientation", fields.FieldFloatQ(value=value)
            )

    @property
    def ends(self) -> members.FieldEnum | None:
        """The Ends member."""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ends.setter
    def ends(self, value: members.FieldEnum) -> None:
        """Set the Ends member."""
        self.set_member("Ends", value)

    @property
    def shading(self) -> members.FieldEnum | None:
        """The Shading member."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shading.setter
    def shading(self, value: members.FieldEnum) -> None:
        """Set the Shading member."""
        self.set_member("Shading", value)

    @property
    def start_tube_radius(self) -> np.float32 | None:
        """The StartTubeRadius field value."""
        member = self.get_member("StartTubeRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_tube_radius.setter
    def start_tube_radius(self, value: np.float32) -> None:
        """Set the StartTubeRadius field value."""
        member = self.get_member("StartTubeRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartTubeRadius", fields.FieldFloat(value=value)
            )

    @property
    def end_tube_radius(self) -> np.float32 | None:
        """The EndTubeRadius field value."""
        member = self.get_member("EndTubeRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_tube_radius.setter
    def end_tube_radius(self, value: np.float32) -> None:
        """Set the EndTubeRadius field value."""
        member = self.get_member("EndTubeRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndTubeRadius", fields.FieldFloat(value=value)
            )

    @property
    def tube_points(self) -> np.int32 | None:
        """The TubePoints field value."""
        member = self.get_member("TubePoints")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tube_points.setter
    def tube_points(self, value: np.int32) -> None:
        """Set the TubePoints field value."""
        member = self.get_member("TubePoints")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TubePoints", fields.FieldInt(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

