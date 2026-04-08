"""Generated component: ConstrainedDelaunayMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConstrainedDelaunayMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ConstrainedDelaunayMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConstrainedDelaunayMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, auto_triangulation_plane: bool | None = None, triangulation_center: primitives.Float3 | None = None, triangulation_plane_normal: primitives.Float3 | None = None, auto_normals: bool | None = None, auto_tangents: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            auto_triangulation_plane: Initial value for AutoTriangulationPlane.
            triangulation_center: Initial value for TriangulationCenter.
            triangulation_plane_normal: Initial value for TriangulationPlaneNormal.
            auto_normals: Initial value for AutoNormals.
            auto_tangents: Initial value for AutoTangents.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if auto_triangulation_plane is not None:
            self.auto_triangulation_plane = auto_triangulation_plane
        if triangulation_center is not None:
            self.triangulation_center = triangulation_center
        if triangulation_plane_normal is not None:
            self.triangulation_plane_normal = triangulation_plane_normal
        if auto_normals is not None:
            self.auto_normals = auto_normals
        if auto_tangents is not None:
            self.auto_tangents = auto_tangents

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
    def vertices(self) -> members.SyncList | None:
        """The Vertices member."""
        member = self.get_member("Vertices")
        if isinstance(member, members.SyncList):
            return member
        return None

    @vertices.setter
    def vertices(self, value: members.SyncList) -> None:
        """Set the Vertices member."""
        self.set_member("Vertices", value)

    @property
    def holes(self) -> members.SyncList | None:
        """The Holes member."""
        member = self.get_member("Holes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @holes.setter
    def holes(self, value: members.SyncList) -> None:
        """Set the Holes member."""
        self.set_member("Holes", value)

    @property
    def auto_triangulation_plane(self) -> bool | None:
        """The AutoTriangulationPlane field value."""
        member = self.get_member("AutoTriangulationPlane")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_triangulation_plane.setter
    def auto_triangulation_plane(self, value: bool) -> None:
        """Set the AutoTriangulationPlane field value."""
        member = self.get_member("AutoTriangulationPlane")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoTriangulationPlane", fields.FieldBool(value=value)
            )

    @property
    def triangulation_center(self) -> primitives.Float3 | None:
        """The TriangulationCenter field value."""
        member = self.get_member("TriangulationCenter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triangulation_center.setter
    def triangulation_center(self, value: primitives.Float3) -> None:
        """Set the TriangulationCenter field value."""
        member = self.get_member("TriangulationCenter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriangulationCenter", fields.FieldFloat3(value=value)
            )

    @property
    def triangulation_plane_normal(self) -> primitives.Float3 | None:
        """The TriangulationPlaneNormal field value."""
        member = self.get_member("TriangulationPlaneNormal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triangulation_plane_normal.setter
    def triangulation_plane_normal(self, value: primitives.Float3) -> None:
        """Set the TriangulationPlaneNormal field value."""
        member = self.get_member("TriangulationPlaneNormal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriangulationPlaneNormal", fields.FieldFloat3(value=value)
            )

    @property
    def auto_normals(self) -> bool | None:
        """The AutoNormals field value."""
        member = self.get_member("AutoNormals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_normals.setter
    def auto_normals(self, value: bool) -> None:
        """Set the AutoNormals field value."""
        member = self.get_member("AutoNormals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoNormals", fields.FieldBool(value=value)
            )

    @property
    def auto_tangents(self) -> bool | None:
        """The AutoTangents field value."""
        member = self.get_member("AutoTangents")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_tangents.setter
    def auto_tangents(self, value: bool) -> None:
        """Set the AutoTangents field value."""
        member = self.get_member("AutoTangents")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoTangents", fields.FieldBool(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

