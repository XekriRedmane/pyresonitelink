"""Generated component: QuadArrayMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class QuadArrayMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.QuadArrayMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.QuadArrayMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box

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
    def points(self) -> list[primitives.Float3] | None:
        """The Points array values."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @points.setter
    def points(self, value: list[primitives.Float3]) -> None:
        """Set the Points array values."""
        member = self.get_member("Points")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.ArrayFloat3(values=value)
            )

    @property
    def sizes(self) -> list[primitives.Float2] | None:
        """The Sizes array values."""
        member = self.get_member("Sizes")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @sizes.setter
    def sizes(self, value: list[primitives.Float2]) -> None:
        """Set the Sizes array values."""
        member = self.get_member("Sizes")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Sizes", fields.ArrayFloat2(values=value)
            )

    @property
    def rotations(self) -> list[primitives.FloatQ] | None:
        """The Rotations array values."""
        member = self.get_member("Rotations")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @rotations.setter
    def rotations(self, value: list[primitives.FloatQ]) -> None:
        """Set the Rotations array values."""
        member = self.get_member("Rotations")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rotations", fields.ArrayFloatQ(values=value)
            )

    @property
    def colors(self) -> list[primitives.Color] | None:
        """The Colors array values."""
        member = self.get_member("Colors")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @colors.setter
    def colors(self, value: list[primitives.Color]) -> None:
        """Set the Colors array values."""
        member = self.get_member("Colors")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Colors", fields.ArrayColor(values=value)
            )

    @property
    def colors_profile(self) -> members.FieldEnum | None:
        """The ColorsProfile member."""
        member = self.get_member("ColorsProfile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @colors_profile.setter
    def colors_profile(self, value: members.FieldEnum) -> None:
        """Set the ColorsProfile member."""
        self.set_member("ColorsProfile", value)

    @property
    def uvs(self) -> list[primitives.Float4] | None:
        """The UVs array values."""
        member = self.get_member("UVs")
        if member is None:
            return None
        return getattr(member, 'values', None)

    @uvs.setter
    def uvs(self, value: list[primitives.Float4]) -> None:
        """Set the UVs array values."""
        member = self.get_member("UVs")
        if member is not None:
            member.values = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVs", fields.ArrayFloat4(values=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

