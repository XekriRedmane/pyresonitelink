"""Generated component: TriangleDiagnosticMesh."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TriangleDiagnosticMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TriangleDiagnosticMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TriangleDiagnosticMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, triangle_index: np.int32 | None = None, vertex0_color: primitives.Color | None = None, vertex1_color: primitives.Color | None = None, vertex2_color: primitives.Color | None = None, displace: np.float32 | None = None, mesh: str | IAssetProvider[Mesh] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            triangle_index: Initial value for TriangleIndex.
            vertex0_color: Initial value for Vertex0Color.
            vertex1_color: Initial value for Vertex1Color.
            vertex2_color: Initial value for Vertex2Color.
            displace: Initial value for Displace.
            mesh: Initial value for Mesh.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if triangle_index is not None:
            self.triangle_index = triangle_index
        if vertex0_color is not None:
            self.vertex0_color = vertex0_color
        if vertex1_color is not None:
            self.vertex1_color = vertex1_color
        if vertex2_color is not None:
            self.vertex2_color = vertex2_color
        if displace is not None:
            self.displace = displace
        if mesh is not None:
            self.mesh = mesh

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
    def triangle_index(self) -> np.int32 | None:
        """The TriangleIndex field value."""
        member = self.get_member("TriangleIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triangle_index.setter
    def triangle_index(self, value: np.int32) -> None:
        """Set the TriangleIndex field value."""
        member = self.get_member("TriangleIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriangleIndex", fields.FieldInt(value=value)
            )

    @property
    def vertex0_color(self) -> primitives.Color | None:
        """The Vertex0Color field value."""
        member = self.get_member("Vertex0Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex0_color.setter
    def vertex0_color(self, value: primitives.Color) -> None:
        """Set the Vertex0Color field value."""
        member = self.get_member("Vertex0Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertex0Color", fields.FieldColor(value=value)
            )

    @property
    def vertex1_color(self) -> primitives.Color | None:
        """The Vertex1Color field value."""
        member = self.get_member("Vertex1Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex1_color.setter
    def vertex1_color(self, value: primitives.Color) -> None:
        """Set the Vertex1Color field value."""
        member = self.get_member("Vertex1Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertex1Color", fields.FieldColor(value=value)
            )

    @property
    def vertex2_color(self) -> primitives.Color | None:
        """The Vertex2Color field value."""
        member = self.get_member("Vertex2Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex2_color.setter
    def vertex2_color(self, value: primitives.Color) -> None:
        """Set the Vertex2Color field value."""
        member = self.get_member("Vertex2Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertex2Color", fields.FieldColor(value=value)
            )

    @property
    def vertex_color_profile(self) -> members.FieldEnum | None:
        """The VertexColorProfile member."""
        member = self.get_member("VertexColorProfile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertex_color_profile.setter
    def vertex_color_profile(self, value: members.FieldEnum) -> None:
        """Set the VertexColorProfile member."""
        self.set_member("VertexColorProfile", value)

    @property
    def displace(self) -> np.float32 | None:
        """The Displace field value."""
        member = self.get_member("Displace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @displace.setter
    def displace(self, value: np.float32) -> None:
        """Set the Displace field value."""
        member = self.get_member("Displace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Displace", fields.FieldFloat(value=value)
            )

    @property
    def mesh(self) -> str | None:
        """Target ID of the Mesh reference (targets IAssetProvider[Mesh])."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | IAssetProvider[Mesh] | None) -> None:
        """Set the Mesh reference by target ID or IAssetProvider[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

