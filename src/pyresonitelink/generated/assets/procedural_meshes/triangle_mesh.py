"""Generated component: TriangleMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TriangleMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TriangleMesh.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TriangleMesh"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, auto_normals: bool | None = None, auto_tangents: bool | None = None, dual_sided: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            auto_normals: Initial value for AutoNormals.
            auto_tangents: Initial value for AutoTangents.
            dual_sided: Initial value for DualSided.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if auto_normals is not None:
            self.auto_normals = auto_normals
        if auto_tangents is not None:
            self.auto_tangents = auto_tangents
        if dual_sided is not None:
            self.dual_sided = dual_sided

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
    def vertex0(self) -> members.SyncObject | None:
        """The Vertex0 member."""
        member = self.get_member("Vertex0")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @vertex0.setter
    def vertex0(self, value: members.SyncObject) -> None:
        """Set the Vertex0 member."""
        self.set_member("Vertex0", value)

    @property
    def vertex1(self) -> members.SyncObject | None:
        """The Vertex1 member."""
        member = self.get_member("Vertex1")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @vertex1.setter
    def vertex1(self, value: members.SyncObject) -> None:
        """Set the Vertex1 member."""
        self.set_member("Vertex1", value)

    @property
    def vertex2(self) -> members.SyncObject | None:
        """The Vertex2 member."""
        member = self.get_member("Vertex2")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @vertex2.setter
    def vertex2(self, value: members.SyncObject) -> None:
        """Set the Vertex2 member."""
        self.set_member("Vertex2", value)

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

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

