"""Generated component: MazeGenerator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.material_provider import MaterialProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MazeGenerator(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MazeGenerator.

    Category: Generators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MazeGenerator"

    def __init__(self, seed: np.int32 | None = None, cells: primitives.Int2 | None = None, wall_size: primitives.Float2 | None = None, point0: primitives.Int2 | None = None, point1: primitives.Int2 | None = None, material: str | MaterialProvider | None = None, bake: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            seed: Initial value for Seed.
            cells: Initial value for Cells.
            wall_size: Initial value for WallSize.
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            material: Initial value for Material.
            bake: Initial value for Bake.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if seed is not None:
            self.seed = seed
        if cells is not None:
            self.cells = cells
        if wall_size is not None:
            self.wall_size = wall_size
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if material is not None:
            self.material = material
        if bake is not None:
            self.bake = bake

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
    def cells(self) -> primitives.Int2 | None:
        """The Cells field value."""
        member = self.get_member("Cells")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cells.setter
    def cells(self, value: primitives.Int2) -> None:
        """Set the Cells field value."""
        member = self.get_member("Cells")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Cells", fields.FieldInt2(value=value)
            )

    @property
    def wall_size(self) -> primitives.Float2 | None:
        """The WallSize field value."""
        member = self.get_member("WallSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @wall_size.setter
    def wall_size(self, value: primitives.Float2) -> None:
        """Set the WallSize field value."""
        member = self.get_member("WallSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WallSize", fields.FieldFloat2(value=value)
            )

    @property
    def point0(self) -> primitives.Int2 | None:
        """The Point0 field value."""
        member = self.get_member("Point0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point0.setter
    def point0(self, value: primitives.Int2) -> None:
        """Set the Point0 field value."""
        member = self.get_member("Point0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point0", fields.FieldInt2(value=value)
            )

    @property
    def point1(self) -> primitives.Int2 | None:
        """The Point1 field value."""
        member = self.get_member("Point1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point1.setter
    def point1(self, value: primitives.Int2) -> None:
        """Set the Point1 field value."""
        member = self.get_member("Point1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point1", fields.FieldInt2(value=value)
            )

    @property
    def material(self) -> str | None:
        """Target ID of the Material reference (targets MaterialProvider)."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | MaterialProvider | None) -> None:
        """Set the Material reference by target ID or MaterialProvider instance."""
        target_id: str | None = target.id if isinstance(target, MaterialProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MaterialProvider'),
            )

    @property
    def bake(self) -> bool | None:
        """The Bake field value."""
        member = self.get_member("Bake")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bake.setter
    def bake(self, value: bool) -> None:
        """Set the Bake field value."""
        member = self.get_member("Bake")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Bake", fields.FieldBool(value=value)
            )

    async def generate(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Generate sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Generate", {}, debug,
        )

