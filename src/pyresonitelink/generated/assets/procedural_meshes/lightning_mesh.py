"""Generated component: LightningMesh."""

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


class LightningMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LightningMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LightningMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, seed: np.int32 | None = None, points: np.int32 | None = None, dual_sided: bool | None = None, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            seed: Initial value for Seed.
            points: Initial value for Points.
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
        if seed is not None:
            self.seed = seed
        if points is not None:
            self.points = points
        if dual_sided is not None:
            self.dual_sided = dual_sided
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1

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
    def seed(self) -> np.int32 | None:
        """The Seed field value."""
        member = self.get_member("Seed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @seed.setter
    def seed(self, value: np.int32) -> None:
        """Set the Seed field value."""
        member = self.get_member("Seed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Seed", fields.FieldInt(value=value)
            )

    @property
    def points(self) -> np.int32 | None:
        """The Points field value."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @points.setter
    def points(self, value: np.int32) -> None:
        """Set the Points field value."""
        member = self.get_member("Points")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.FieldInt(value=value)
            )

    @property
    def topology(self) -> members.FieldEnum | None:
        """The Topology member."""
        member = self.get_member("Topology")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @topology.setter
    def topology(self, value: members.FieldEnum) -> None:
        """Set the Topology member."""
        self.set_member("Topology", value)

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
    def dual_sided(self) -> bool | None:
        """The DualSided field value."""
        member = self.get_member("DualSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dual_sided.setter
    def dual_sided(self, value: bool) -> None:
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
        """The Point0 field value."""
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
        """The Point1 field value."""
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
        """The StrikeLevels member."""
        member = self.get_member("StrikeLevels")
        if isinstance(member, members.SyncList):
            return member
        return None

    @strike_levels.setter
    def strike_levels(self, value: members.SyncList) -> None:
        """Set the StrikeLevels member."""
        self.set_member("StrikeLevels", value)

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

