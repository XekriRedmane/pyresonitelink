"""Generated component: SpawnArc."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.user_node import UserNode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iuser_spawn_area import IUserSpawnArea
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SpawnArc(GeneratedComponent, IUserSpawnArea, IWorldEventReceiver):
    """The SpawnArc component spawns in users along the arc of a circle, with an optional weight to select this spawner.

}}

    Category: Users

    Used to help shape how you want users to spawn in a world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SpawnArc"

    def __init__(self, weight: primitives.Float | None = None, capacity: primitives.Int | None = None, radius: primitives.Float | None = None, arc: primitives.Float | None = None, users_per_arc: primitives.Int | None = None, center_arc_offset: primitives.Float | None = None, grow_both_sides: primitives.Bool | None = None, row_height_offset: primitives.Float | None = None, orient_user: primitives.Bool | None = None, parent_user: primitives.Bool | None = None, tilt_users: primitives.Bool | None = None, position_node: UserNode | str | None = None, rotation_node: UserNode | str | None = None, show_test: primitives.Bool | None = None, test_slots: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            weight: Initial value for Weight.
            capacity: Initial value for Capacity.
            radius: Initial value for Radius.
            arc: Initial value for Arc.
            users_per_arc: Initial value for UsersPerArc.
            center_arc_offset: Initial value for CenterArcOffset.
            grow_both_sides: Initial value for GrowBothSides.
            row_height_offset: Initial value for RowHeightOffset.
            orient_user: Initial value for OrientUser.
            parent_user: Initial value for ParentUser.
            tilt_users: Initial value for TiltUsers.
            position_node: Initial value for PositionNode.
            rotation_node: Initial value for RotationNode.
            show_test: Initial value for _showTest.
            test_slots: Initial value for _testSlots.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if weight is not None:
            self.weight = weight
        if capacity is not None:
            self.capacity = capacity
        if radius is not None:
            self.radius = radius
        if arc is not None:
            self.arc = arc
        if users_per_arc is not None:
            self.users_per_arc = users_per_arc
        if center_arc_offset is not None:
            self.center_arc_offset = center_arc_offset
        if grow_both_sides is not None:
            self.grow_both_sides = grow_both_sides
        if row_height_offset is not None:
            self.row_height_offset = row_height_offset
        if orient_user is not None:
            self.orient_user = orient_user
        if parent_user is not None:
            self.parent_user = parent_user
        if tilt_users is not None:
            self.tilt_users = tilt_users
        if position_node is not None:
            self.position_node = position_node
        if rotation_node is not None:
            self.rotation_node = rotation_node
        if show_test is not None:
            self.show_test = show_test
        if test_slots is not None:
            self.test_slots = test_slots

    @property
    def weight(self) -> primitives.Float | None:
        """The likelihood of this spawner being chosen for a spawning user."""
        member = self.get_member("Weight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @weight.setter
    def weight(self, value: primitives.Float) -> None:
        """Set the Weight field value."""
        member = self.get_member("Weight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Weight", fields.FieldFloat(value=value)
            )

    @property
    def capacity(self) -> primitives.Int | None:
        """How many users this spawner can have spawned at a time."""
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
    def radius(self) -> primitives.Float | None:
        """The range of how far this spawner can spawn this user."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def arc(self) -> primitives.Float | None:
        """The shape of how the spawner will place the user."""
        member = self.get_member("Arc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc.setter
    def arc(self, value: primitives.Float) -> None:
        """Set the Arc field value."""
        member = self.get_member("Arc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Arc", fields.FieldFloat(value=value)
            )

    @property
    def users_per_arc(self) -> primitives.Int | None:
        """The segment area for the users to spawn at in this arc."""
        member = self.get_member("UsersPerArc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_per_arc.setter
    def users_per_arc(self, value: primitives.Int) -> None:
        """Set the UsersPerArc field value."""
        member = self.get_member("UsersPerArc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersPerArc", fields.FieldInt(value=value)
            )

    @property
    def center_arc_offset(self) -> primitives.Float | None:
        """The offset rotation of the center of the arc circle for this spawner."""
        member = self.get_member("CenterArcOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @center_arc_offset.setter
    def center_arc_offset(self, value: primitives.Float) -> None:
        """Set the CenterArcOffset field value."""
        member = self.get_member("CenterArcOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CenterArcOffset", fields.FieldFloat(value=value)
            )

    @property
    def grow_both_sides(self) -> primitives.Bool | None:
        """The option to extend both sides for the spawn arc, fanning out from a center point."""
        member = self.get_member("GrowBothSides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grow_both_sides.setter
    def grow_both_sides(self, value: primitives.Bool) -> None:
        """Set the GrowBothSides field value."""
        member = self.get_member("GrowBothSides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrowBothSides", fields.FieldBool(value=value)
            )

    @property
    def row_height_offset(self) -> primitives.Float | None:
        """The hieght where the users will spawn along the circle."""
        member = self.get_member("RowHeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @row_height_offset.setter
    def row_height_offset(self, value: primitives.Float) -> None:
        """Set the RowHeightOffset field value."""
        member = self.get_member("RowHeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RowHeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def orient_user(self) -> primitives.Bool | None:
        """Positions and rotates the user towards the center."""
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
    def parent_user(self) -> primitives.Bool | None:
        """Keeps the user parented onto this specific spawner slot."""
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
    def tilt_users(self) -> primitives.Bool | None:
        """Tilts the user when spawning in."""
        member = self.get_member("TiltUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tilt_users.setter
    def tilt_users(self, value: primitives.Bool) -> None:
        """Set the TiltUsers field value."""
        member = self.get_member("TiltUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TiltUsers", fields.FieldBool(value=value)
            )

    @property
    def position_node(self) -> UserNode | None:
        """Takes the position of the user's body node for spawning."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @position_node.setter
    def position_node(self, value: UserNode | str) -> None:
        """Set PositionNode. Takes the position of the user's body node for spawning."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositionNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def rotation_node(self) -> UserNode | None:
        """Takes the rotation of the user's body node for spawning."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @rotation_node.setter
    def rotation_node(self, value: UserNode | str) -> None:
        """Set RotationNode. Takes the rotation of the user's body node for spawning."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RotationNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def show_test(self) -> primitives.Bool | None:
        """Internal: Mostly for debugging."""
        member = self.get_member("_showTest")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_test.setter
    def show_test(self, value: primitives.Bool) -> None:
        """Set the _showTest field value."""
        member = self.get_member("_showTest")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_showTest", fields.FieldBool(value=value)
            )

    @property
    def test_slots(self) -> primitives.Int | None:
        """Internal: Shows the number of test slots on this spawning arc."""
        member = self.get_member("_testSlots")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @test_slots.setter
    def test_slots(self, value: primitives.Int) -> None:
        """Set the _testSlots field value."""
        member = self.get_member("_testSlots")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_testSlots", fields.FieldInt(value=value)
            )

