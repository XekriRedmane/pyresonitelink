"""Generated component: BallisticPathMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BallisticPathMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BallisticPathMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BallisticPathMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, initial_position: primitives.Float3 | None = None, initial_velocity: primitives.Float3 | None = None, gravity: primitives.Float3 | None = None, drag: primitives.Float | None = None, step_size: primitives.Float | None = None, total_units: primitives.Float | None = None, size: primitives.Float | None = None, points: primitives.Int | None = None, dual_sided: primitives.Bool | None = None, up: primitives.Float3 | None = None, distance_size_growth: primitives.Float | None = None, min_grown_size: primitives.Float | None = None, max_grown_size: primitives.Float | None = None, use_last_segment: primitives.Bool | None = None, last_segment_position: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            initial_position: Initial value for InitialPosition.
            initial_velocity: Initial value for InitialVelocity.
            gravity: Initial value for Gravity.
            drag: Initial value for Drag.
            step_size: Initial value for StepSize.
            total_units: Initial value for TotalUnits.
            size: Initial value for Size.
            points: Initial value for Points.
            dual_sided: Initial value for DualSided.
            up: Initial value for Up.
            distance_size_growth: Initial value for DistanceSizeGrowth.
            min_grown_size: Initial value for MinGrownSize.
            max_grown_size: Initial value for MaxGrownSize.
            use_last_segment: Initial value for UseLastSegment.
            last_segment_position: Initial value for LastSegmentPosition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if initial_position is not None:
            self.initial_position = initial_position
        if initial_velocity is not None:
            self.initial_velocity = initial_velocity
        if gravity is not None:
            self.gravity = gravity
        if drag is not None:
            self.drag = drag
        if step_size is not None:
            self.step_size = step_size
        if total_units is not None:
            self.total_units = total_units
        if size is not None:
            self.size = size
        if points is not None:
            self.points = points
        if dual_sided is not None:
            self.dual_sided = dual_sided
        if up is not None:
            self.up = up
        if distance_size_growth is not None:
            self.distance_size_growth = distance_size_growth
        if min_grown_size is not None:
            self.min_grown_size = min_grown_size
        if max_grown_size is not None:
            self.max_grown_size = max_grown_size
        if use_last_segment is not None:
            self.use_last_segment = use_last_segment
        if last_segment_position is not None:
            self.last_segment_position = last_segment_position

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> primitives.Bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: primitives.Bool) -> None:
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
    def initial_position(self) -> primitives.Float3 | None:
        """The InitialPosition field value."""
        member = self.get_member("InitialPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initial_position.setter
    def initial_position(self, value: primitives.Float3) -> None:
        """Set the InitialPosition field value."""
        member = self.get_member("InitialPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InitialPosition", fields.FieldFloat3(value=value)
            )

    @property
    def initial_velocity(self) -> primitives.Float3 | None:
        """The InitialVelocity field value."""
        member = self.get_member("InitialVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initial_velocity.setter
    def initial_velocity(self, value: primitives.Float3) -> None:
        """Set the InitialVelocity field value."""
        member = self.get_member("InitialVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InitialVelocity", fields.FieldFloat3(value=value)
            )

    @property
    def gravity(self) -> primitives.Float3 | None:
        """The Gravity field value."""
        member = self.get_member("Gravity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gravity.setter
    def gravity(self, value: primitives.Float3) -> None:
        """Set the Gravity field value."""
        member = self.get_member("Gravity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gravity", fields.FieldFloat3(value=value)
            )

    @property
    def drag(self) -> primitives.Float | None:
        """The Drag field value."""
        member = self.get_member("Drag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drag.setter
    def drag(self, value: primitives.Float) -> None:
        """Set the Drag field value."""
        member = self.get_member("Drag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Drag", fields.FieldFloat(value=value)
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
    def step_size(self) -> primitives.Float | None:
        """The StepSize field value."""
        member = self.get_member("StepSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @step_size.setter
    def step_size(self, value: primitives.Float) -> None:
        """Set the StepSize field value."""
        member = self.get_member("StepSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StepSize", fields.FieldFloat(value=value)
            )

    @property
    def total_units(self) -> primitives.Float | None:
        """The TotalUnits field value."""
        member = self.get_member("TotalUnits")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_units.setter
    def total_units(self, value: primitives.Float) -> None:
        """Set the TotalUnits field value."""
        member = self.get_member("TotalUnits")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalUnits", fields.FieldFloat(value=value)
            )

    @property
    def shape(self) -> members.FieldEnum | None:
        """The Shape member."""
        member = self.get_member("Shape")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shape.setter
    def shape(self, value: members.FieldEnum) -> None:
        """Set the Shape member."""
        self.set_member("Shape", value)

    @property
    def size(self) -> primitives.Float | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat(value=value)
            )

    @property
    def points(self) -> primitives.Int | None:
        """The Points field value."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @points.setter
    def points(self, value: primitives.Int) -> None:
        """Set the Points field value."""
        member = self.get_member("Points")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.FieldInt(value=value)
            )

    @property
    def dual_sided(self) -> primitives.Bool | None:
        """The DualSided field value."""
        member = self.get_member("DualSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dual_sided.setter
    def dual_sided(self, value: primitives.Bool) -> None:
        """Set the DualSided field value."""
        member = self.get_member("DualSided")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DualSided", fields.FieldBool(value=value)
            )

    @property
    def up(self) -> primitives.Float3 | None:
        """The Up field value."""
        member = self.get_member("Up")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @up.setter
    def up(self, value: primitives.Float3) -> None:
        """Set the Up field value."""
        member = self.get_member("Up")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Up", fields.FieldFloat3(value=value)
            )

    @property
    def distance_size_growth(self) -> primitives.Float | None:
        """The DistanceSizeGrowth field value."""
        member = self.get_member("DistanceSizeGrowth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_size_growth.setter
    def distance_size_growth(self, value: primitives.Float) -> None:
        """Set the DistanceSizeGrowth field value."""
        member = self.get_member("DistanceSizeGrowth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistanceSizeGrowth", fields.FieldFloat(value=value)
            )

    @property
    def min_grown_size(self) -> primitives.Float | None:
        """The MinGrownSize field value."""
        member = self.get_member("MinGrownSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_grown_size.setter
    def min_grown_size(self, value: primitives.Float) -> None:
        """Set the MinGrownSize field value."""
        member = self.get_member("MinGrownSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinGrownSize", fields.FieldFloat(value=value)
            )

    @property
    def max_grown_size(self) -> primitives.Float | None:
        """The MaxGrownSize field value."""
        member = self.get_member("MaxGrownSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_grown_size.setter
    def max_grown_size(self, value: primitives.Float) -> None:
        """Set the MaxGrownSize field value."""
        member = self.get_member("MaxGrownSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxGrownSize", fields.FieldFloat(value=value)
            )

    @property
    def use_last_segment(self) -> primitives.Bool | None:
        """The UseLastSegment field value."""
        member = self.get_member("UseLastSegment")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_last_segment.setter
    def use_last_segment(self, value: primitives.Bool) -> None:
        """Set the UseLastSegment field value."""
        member = self.get_member("UseLastSegment")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLastSegment", fields.FieldBool(value=value)
            )

    @property
    def last_segment_position(self) -> primitives.Float3 | None:
        """The LastSegmentPosition field value."""
        member = self.get_member("LastSegmentPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_segment_position.setter
    def last_segment_position(self, value: primitives.Float3) -> None:
        """Set the LastSegmentPosition field value."""
        member = self.get_member("LastSegmentPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastSegmentPosition", fields.FieldFloat3(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

