"""Generated component: CommonSpawnArea."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iuser_spawn_area import IUserSpawnArea
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CommonSpawnArea(GeneratedComponent, IUserSpawnArea, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonSpawnArea.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonSpawnArea"

    def __init__(self, spawn_point_generator: str | IPointGenerator | None = None, floor_point_ray: primitives.Float3 | None = None, other_user_check_radius: primitives.Float | None = None, parent_user: primitives.Bool | None = None, orient_user: primitives.Bool | None = None, scale_user: primitives.Bool | None = None, capacity: primitives.Int | None = None, base_weight: primitives.Float | None = None, parent_override: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            spawn_point_generator: Initial value for SpawnPointGenerator.
            floor_point_ray: Initial value for FloorPointRay.
            other_user_check_radius: Initial value for OtherUserCheckRadius.
            parent_user: Initial value for ParentUser.
            orient_user: Initial value for OrientUser.
            scale_user: Initial value for ScaleUser.
            capacity: Initial value for Capacity.
            base_weight: Initial value for BaseWeight.
            parent_override: Initial value for ParentOverride.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if spawn_point_generator is not None:
            self.spawn_point_generator = spawn_point_generator
        if floor_point_ray is not None:
            self.floor_point_ray = floor_point_ray
        if other_user_check_radius is not None:
            self.other_user_check_radius = other_user_check_radius
        if parent_user is not None:
            self.parent_user = parent_user
        if orient_user is not None:
            self.orient_user = orient_user
        if scale_user is not None:
            self.scale_user = scale_user
        if capacity is not None:
            self.capacity = capacity
        if base_weight is not None:
            self.base_weight = base_weight
        if parent_override is not None:
            self.parent_override = parent_override

    @property
    def spawn_point_generator(self) -> str | None:
        """Target ID of the SpawnPointGenerator reference (targets IPointGenerator)."""
        member = self.get_member("SpawnPointGenerator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawn_point_generator.setter
    def spawn_point_generator(self, target: str | IPointGenerator | None) -> None:
        """Set the SpawnPointGenerator reference by target ID or IPointGenerator instance."""
        target_id: str | None = target.id if isinstance(target, IPointGenerator) else target  # type: ignore[assignment]
        member = self.get_member("SpawnPointGenerator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawnPointGenerator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IPointGenerator'),
            )

    @property
    def floor_point_ray(self) -> primitives.Float3 | None:
        """The FloorPointRay field value."""
        member = self.get_member("FloorPointRay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @floor_point_ray.setter
    def floor_point_ray(self, value: primitives.Float3) -> None:
        """Set the FloorPointRay field value."""
        member = self.get_member("FloorPointRay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FloorPointRay", fields.FieldFloat3(value=value)
            )

    @property
    def other_user_check_radius(self) -> primitives.Float | None:
        """The OtherUserCheckRadius field value."""
        member = self.get_member("OtherUserCheckRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @other_user_check_radius.setter
    def other_user_check_radius(self, value: primitives.Float) -> None:
        """Set the OtherUserCheckRadius field value."""
        member = self.get_member("OtherUserCheckRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OtherUserCheckRadius", fields.FieldFloat(value=value)
            )

    @property
    def parent_user(self) -> primitives.Bool | None:
        """The ParentUser field value."""
        member = self.get_member("ParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_user.setter
    def parent_user(self, value: primitives.Bool) -> None:
        """Set the ParentUser field value."""
        member = self.get_member("ParentUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentUser", fields.FieldBool(value=value)
            )

    @property
    def orient_user(self) -> primitives.Bool | None:
        """The OrientUser field value."""
        member = self.get_member("OrientUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orient_user.setter
    def orient_user(self, value: primitives.Bool) -> None:
        """Set the OrientUser field value."""
        member = self.get_member("OrientUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrientUser", fields.FieldBool(value=value)
            )

    @property
    def scale_user(self) -> primitives.Bool | None:
        """The ScaleUser field value."""
        member = self.get_member("ScaleUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_user.setter
    def scale_user(self, value: primitives.Bool) -> None:
        """Set the ScaleUser field value."""
        member = self.get_member("ScaleUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleUser", fields.FieldBool(value=value)
            )

    @property
    def capacity(self) -> primitives.Int | None:
        """The Capacity field value."""
        member = self.get_member("Capacity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @capacity.setter
    def capacity(self, value: primitives.Int) -> None:
        """Set the Capacity field value."""
        member = self.get_member("Capacity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Capacity", fields.FieldInt(value=value)
            )

    @property
    def base_weight(self) -> primitives.Float | None:
        """The BaseWeight field value."""
        member = self.get_member("BaseWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_weight.setter
    def base_weight(self, value: primitives.Float) -> None:
        """Set the BaseWeight field value."""
        member = self.get_member("BaseWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseWeight", fields.FieldFloat(value=value)
            )

    @property
    def position_node(self) -> members.FieldEnum | None:
        """The PositionNode member."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @position_node.setter
    def position_node(self, value: members.FieldEnum) -> None:
        """Set the PositionNode member."""
        self.set_member("PositionNode", value)

    @property
    def rotation_node(self) -> members.FieldEnum | None:
        """The RotationNode member."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rotation_node.setter
    def rotation_node(self, value: members.FieldEnum) -> None:
        """Set the RotationNode member."""
        self.set_member("RotationNode", value)

    @property
    def parent_override(self) -> str | None:
        """Target ID of the ParentOverride reference (targets Slot)."""
        member = self.get_member("ParentOverride")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_override.setter
    def parent_override(self, target: str | Slot | None) -> None:
        """Set the ParentOverride reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentOverride")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentOverride",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

