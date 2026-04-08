"""Generated component: DebugTangentSpace."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugTangentSpace(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugTangentSpace.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugTangentSpace"

    def __init__(self, mesh: str | MeshRenderer | None = None, triangle: primitives.Int | None = None, bary_coord: primitives.Float3 | None = None, radius_ratio: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mesh: Initial value for Mesh.
            triangle: Initial value for Triangle.
            bary_coord: Initial value for BaryCoord.
            radius_ratio: Initial value for RadiusRatio.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mesh is not None:
            self.mesh = mesh
        if triangle is not None:
            self.triangle = triangle
        if bary_coord is not None:
            self.bary_coord = bary_coord
        if radius_ratio is not None:
            self.radius_ratio = radius_ratio

    @property
    def mesh(self) -> str | None:
        """Target ID of the Mesh reference (targets MeshRenderer)."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | MeshRenderer | None) -> None:
        """Set the Mesh reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def triangle(self) -> primitives.Int | None:
        """The Triangle field value."""
        member = self.get_member("Triangle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triangle.setter
    def triangle(self, value: primitives.Int) -> None:
        """Set the Triangle field value."""
        member = self.get_member("Triangle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Triangle", fields.FieldInt(value=value)
            )

    @property
    def bary_coord(self) -> primitives.Float3 | None:
        """The BaryCoord field value."""
        member = self.get_member("BaryCoord")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bary_coord.setter
    def bary_coord(self, value: primitives.Float3) -> None:
        """Set the BaryCoord field value."""
        member = self.get_member("BaryCoord")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaryCoord", fields.FieldFloat3(value=value)
            )

    @property
    def radius_ratio(self) -> primitives.Float | None:
        """The RadiusRatio field value."""
        member = self.get_member("RadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_ratio.setter
    def radius_ratio(self, value: primitives.Float) -> None:
        """Set the RadiusRatio field value."""
        member = self.get_member("RadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusRatio", fields.FieldFloat(value=value)
            )

