"""Generated component: LightningMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.topology import Topology
from pyresonitelink.generated._enums.shading import Shading
from pyresonitelink.generated._enums.ends import Ends
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LightningMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The LightingMesh component generates geometry of a procedural lighting bolt for use with a MeshRenderer.

    Category: Assets/Procedural Meshes

    Attach to a slot and insert into a MeshRenderer to view the geometry it
    generates. Don't forget to use a Material.

    **StrikeProperties**: Generates a group of lines that shoot out at random bent angles with multiple segments. The start and end of these forks in the lighting mesh can be controlled via its settings.

The shape of the bolt is effected by both Offset and Segments, low values of either make for a straighter bolt.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LightningMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, seed: primitives.Int | None = None, points: primitives.Int | None = None, topology: Topology | str | None = None, shading: Shading | str | None = None, ends: Ends | str | None = None, dual_sided: primitives.Bool | None = None, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            seed: Initial value for Seed.
            points: Initial value for Points.
            topology: Initial value for Topology.
            shading: Initial value for Shading.
            ends: Initial value for Ends.
            dual_sided: Initial value for DualSided.
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if profile is not None:
            self.profile = profile
        if seed is not None:
            self.seed = seed
        if points is not None:
            self.points = points
        if topology is not None:
            self.topology = topology
        if shading is not None:
            self.shading = shading
        if ends is not None:
            self.ends = ends
        if dual_sided is not None:
            self.dual_sided = dual_sided
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1

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
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def seed(self) -> primitives.Int | None:
        """Used to generate a pseudo-random variant of a lighting bolt mesh"""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: primitives.Int) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldInt(value=value)
            )

    @property
    def points(self) -> primitives.Int | None:
        """how much detail the lighting bolt's profile should have. (This has minimal effect on 'line' profile, but makes 'circle' more round.) Topology Topology The Topology setting for the lighting bolt profile. Line(a flat mesh) or Circle. Shading Shading The shading for the lighting bolt geometry. Like smooth or flat for example."""
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
    def topology(self) -> Topology | None:
        """The Topology enum value."""
        member = self.get_member("Topology")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Topology(member.value)
        return None

    @topology.setter
    def topology(self, value: Topology | str) -> None:
        """Set the Topology enum value."""
        member = self.get_member("Topology")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Topology",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shading(self) -> Shading | None:
        """The Shading enum value."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Shading(member.value)
        return None

    @shading.setter
    def shading(self, value: Shading | str) -> None:
        """Set the Shading enum value."""
        member = self.get_member("Shading")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Shading",
                members.FieldEnum(value=str(value)),
            )

    @property
    def ends(self) -> Ends | None:
        """how to handle the geometry at the beginning and end of lines in the lighting bolt"""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Ends(member.value)
        return None

    @ends.setter
    def ends(self, value: Ends | str) -> None:
        """Set Ends. how to handle the geometry at the beginning and end of lines in the lighting bolt"""
        member = self.get_member("Ends")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Ends",
                members.FieldEnum(value=str(value)),
            )

    @property
    def dual_sided(self) -> primitives.Bool | None:
        """whether the lighting bolt is visible from the inside."""
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
    def point0(self) -> primitives.Float3 | None:
        """the start point of the lightning bolt"""
        member = self.get_member("Point0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point0.setter
    def point0(self, value: primitives.Float3) -> None:
        """Set the Point0 field value."""
        member = self.get_member("Point0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point0", fields.FieldFloat3(value=value)
            )

    @property
    def point1(self) -> primitives.Float3 | None:
        """the end point of the lightning bolt"""
        member = self.get_member("Point1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point1.setter
    def point1(self, value: primitives.Float3) -> None:
        """Set the Point1 field value."""
        member = self.get_member("Point1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point1", fields.FieldFloat3(value=value)
            )

    @property
    def strike_levels(self) -> members.SyncList | None:
        """A list of different branch variants and bends in the lighting bolt."""
        member = self.get_member("StrikeLevels")
        if isinstance(member, members.SyncList):
            return member
        return None

    @strike_levels.setter
    def strike_levels(self, value: members.SyncList) -> None:
        """Set StrikeLevels. A list of different branch variants and bends in the lighting bolt."""
        self.set_member("StrikeLevels", value)

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

