"""Generated component: BooleanSwitcher."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanSwitcher(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BooleanSwitcher.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanSwitcher"

    def __init__(self, auto_add_children: bool | None = None, active_index: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            active_index: Initial value for ActiveIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if active_index is not None:
            self.active_index = active_index

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
    def targets(self) -> members.SyncList | None:
        """The Targets member."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the Targets member."""
        self.set_member("Targets", value)

    @property
    def active_index(self) -> np.int32 | None:
        """The ActiveIndex field value."""
        member = self.get_member("ActiveIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_index.setter
    def active_index(self, value: np.int32) -> None:
        """Set the ActiveIndex field value."""
        member = self.get_member("ActiveIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveIndex", fields.FieldInt(value=value)
            )

    @property
    def activation_mode(self) -> members.FieldEnum | None:
        """The ActivationMode member."""
        member = self.get_member("ActivationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @activation_mode.setter
    def activation_mode(self, value: members.FieldEnum) -> None:
        """Set the ActivationMode member."""
        self.set_member("ActivationMode", value)

