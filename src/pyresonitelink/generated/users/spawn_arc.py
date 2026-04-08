"""Generated component: SpawnArc."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iuser_spawn_area import IUserSpawnArea
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SpawnArc(GeneratedComponent, IUserSpawnArea, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SpawnArc.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SpawnArc"

    def __init__(self, weight: np.float32 | None = None, capacity: np.int32 | None = None, radius: np.float32 | None = None, arc: np.float32 | None = None, users_per_arc: np.int32 | None = None, center_arc_offset: np.float32 | None = None, grow_both_sides: bool | None = None, row_height_offset: np.float32 | None = None, orient_user: bool | None = None, parent_user: bool | None = None, tilt_users: bool | None = None, show_test: bool | None = None, test_slots: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
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
        if show_test is not None:
            self.show_test = show_test
        if test_slots is not None:
            self.test_slots = test_slots

    @property
    def weight(self) -> np.float32 | None:
        """The Weight field value."""
        member = self.get_member("Weight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @weight.setter
    def weight(self, value: np.float32) -> None:
        """Set the Weight field value."""
        member = self.get_member("Weight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Weight", fields.FieldFloat(value=value)
            )

    @property
    def capacity(self) -> np.int32 | None:
        """The Capacity field value."""
        member = self.get_member("Capacity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @capacity.setter
    def capacity(self, value: np.int32) -> None:
        """Set the Capacity field value."""
        member = self.get_member("Capacity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Capacity", fields.FieldInt(value=value)
            )

    @property
    def radius(self) -> np.float32 | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: np.float32) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def arc(self) -> np.float32 | None:
        """The Arc field value."""
        member = self.get_member("Arc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @arc.setter
    def arc(self, value: np.float32) -> None:
        """Set the Arc field value."""
        member = self.get_member("Arc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Arc", fields.FieldFloat(value=value)
            )

    @property
    def users_per_arc(self) -> np.int32 | None:
        """The UsersPerArc field value."""
        member = self.get_member("UsersPerArc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_per_arc.setter
    def users_per_arc(self, value: np.int32) -> None:
        """Set the UsersPerArc field value."""
        member = self.get_member("UsersPerArc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersPerArc", fields.FieldInt(value=value)
            )

    @property
    def center_arc_offset(self) -> np.float32 | None:
        """The CenterArcOffset field value."""
        member = self.get_member("CenterArcOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @center_arc_offset.setter
    def center_arc_offset(self, value: np.float32) -> None:
        """Set the CenterArcOffset field value."""
        member = self.get_member("CenterArcOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CenterArcOffset", fields.FieldFloat(value=value)
            )

    @property
    def grow_both_sides(self) -> bool | None:
        """The GrowBothSides field value."""
        member = self.get_member("GrowBothSides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grow_both_sides.setter
    def grow_both_sides(self, value: bool) -> None:
        """Set the GrowBothSides field value."""
        member = self.get_member("GrowBothSides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrowBothSides", fields.FieldBool(value=value)
            )

    @property
    def row_height_offset(self) -> np.float32 | None:
        """The RowHeightOffset field value."""
        member = self.get_member("RowHeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @row_height_offset.setter
    def row_height_offset(self, value: np.float32) -> None:
        """Set the RowHeightOffset field value."""
        member = self.get_member("RowHeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RowHeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def orient_user(self) -> bool | None:
        """The OrientUser field value."""
        member = self.get_member("OrientUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orient_user.setter
    def orient_user(self, value: bool) -> None:
        """Set the OrientUser field value."""
        member = self.get_member("OrientUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrientUser", fields.FieldBool(value=value)
            )

    @property
    def parent_user(self) -> bool | None:
        """The ParentUser field value."""
        member = self.get_member("ParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_user.setter
    def parent_user(self, value: bool) -> None:
        """Set the ParentUser field value."""
        member = self.get_member("ParentUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentUser", fields.FieldBool(value=value)
            )

    @property
    def tilt_users(self) -> bool | None:
        """The TiltUsers field value."""
        member = self.get_member("TiltUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tilt_users.setter
    def tilt_users(self, value: bool) -> None:
        """Set the TiltUsers field value."""
        member = self.get_member("TiltUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TiltUsers", fields.FieldBool(value=value)
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
    def show_test(self) -> bool | None:
        """The _showTest field value."""
        member = self.get_member("_showTest")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_test.setter
    def show_test(self, value: bool) -> None:
        """Set the _showTest field value."""
        member = self.get_member("_showTest")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_showTest", fields.FieldBool(value=value)
            )

    @property
    def test_slots(self) -> np.int32 | None:
        """The _testSlots field value."""
        member = self.get_member("_testSlots")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @test_slots.setter
    def test_slots(self, value: np.int32) -> None:
        """Set the _testSlots field value."""
        member = self.get_member("_testSlots")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_testSlots", fields.FieldInt(value=value)
            )

