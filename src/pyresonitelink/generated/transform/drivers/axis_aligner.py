"""Generated component: AxisAligner."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AxisAligner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisAligner"

    def __init__(self, auto_add_children: bool | None = None, separation: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            separation: Initial value for Separation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if separation is not None:
            self.separation = separation

    @property
    def auto_add_children(self) -> bool | None:
        """The AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: bool) -> None:
        """Set the AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddChildren", fields.FieldBool(value=value)
            )

    @property
    def auto_add_ignore_tags(self) -> members.SyncList | None:
        """The AutoAddIgnoreTags member."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set the AutoAddIgnoreTags member."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def direction(self) -> members.FieldEnum | None:
        """The Direction member."""
        member = self.get_member("Direction")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @direction.setter
    def direction(self, value: members.FieldEnum) -> None:
        """Set the Direction member."""
        self.set_member("Direction", value)

    @property
    def global_axis_xalign(self) -> members.FieldEnum | None:
        """The GlobalAxisXAlign member."""
        member = self.get_member("GlobalAxisXAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @global_axis_xalign.setter
    def global_axis_xalign(self, value: members.FieldEnum) -> None:
        """Set the GlobalAxisXAlign member."""
        self.set_member("GlobalAxisXAlign", value)

    @property
    def global_axis_yalign(self) -> members.FieldEnum | None:
        """The GlobalAxisYAlign member."""
        member = self.get_member("GlobalAxisYAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @global_axis_yalign.setter
    def global_axis_yalign(self, value: members.FieldEnum) -> None:
        """Set the GlobalAxisYAlign member."""
        self.set_member("GlobalAxisYAlign", value)

    @property
    def global_axis_zalign(self) -> members.FieldEnum | None:
        """The GlobalAxisZAlign member."""
        member = self.get_member("GlobalAxisZAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @global_axis_zalign.setter
    def global_axis_zalign(self, value: members.FieldEnum) -> None:
        """Set the GlobalAxisZAlign member."""
        self.set_member("GlobalAxisZAlign", value)

    @property
    def element_axis_xalign(self) -> members.FieldEnum | None:
        """The ElementAxisXAlign member."""
        member = self.get_member("ElementAxisXAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @element_axis_xalign.setter
    def element_axis_xalign(self, value: members.FieldEnum) -> None:
        """Set the ElementAxisXAlign member."""
        self.set_member("ElementAxisXAlign", value)

    @property
    def element_axis_yalign(self) -> members.FieldEnum | None:
        """The ElementAxisYAlign member."""
        member = self.get_member("ElementAxisYAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @element_axis_yalign.setter
    def element_axis_yalign(self, value: members.FieldEnum) -> None:
        """Set the ElementAxisYAlign member."""
        self.set_member("ElementAxisYAlign", value)

    @property
    def element_axis_zalign(self) -> members.FieldEnum | None:
        """The ElementAxisZAlign member."""
        member = self.get_member("ElementAxisZAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @element_axis_zalign.setter
    def element_axis_zalign(self, value: members.FieldEnum) -> None:
        """Set the ElementAxisZAlign member."""
        self.set_member("ElementAxisZAlign", value)

    @property
    def separation(self) -> np.float32 | None:
        """The Separation field value."""
        member = self.get_member("Separation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separation.setter
    def separation(self, value: np.float32) -> None:
        """Set the Separation field value."""
        member = self.get_member("Separation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Separation", fields.FieldFloat(value=value)
            )

    @property
    def exclude_list(self) -> members.SyncList | None:
        """The ExcludeList member."""
        member = self.get_member("ExcludeList")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclude_list.setter
    def exclude_list(self, value: members.SyncList) -> None:
        """Set the ExcludeList member."""
        self.set_member("ExcludeList", value)

    @property
    def targets(self) -> members.SyncList | None:
        """The _targets member."""
        member = self.get_member("_targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the _targets member."""
        self.set_member("_targets", value)

