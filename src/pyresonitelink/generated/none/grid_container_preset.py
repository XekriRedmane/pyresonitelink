"""Generated component: GridContainerPreset."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imodified_event_receiver import IModifiedEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GridContainerPreset(GeneratedComponent, IModifiedEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GridContainerPreset.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GridContainerPreset"

    def __init__(self, initialized_version: np.int32 | None = None, is_modified: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            initialized_version: Initial value for _initializedVersion.
            is_modified: Initial value for _isModified.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if initialized_version is not None:
            self.initialized_version = initialized_version
        if is_modified is not None:
            self.is_modified = is_modified

    @property
    def initializer(self) -> members.FieldEnum | None:
        """The _initializer member."""
        member = self.get_member("_initializer")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @initializer.setter
    def initializer(self, value: members.FieldEnum) -> None:
        """Set the _initializer member."""
        self.set_member("_initializer", value)

    @property
    def initialized_version(self) -> np.int32 | None:
        """The _initializedVersion field value."""
        member = self.get_member("_initializedVersion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initialized_version.setter
    def initialized_version(self, value: np.int32) -> None:
        """Set the _initializedVersion field value."""
        member = self.get_member("_initializedVersion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_initializedVersion", fields.FieldInt(value=value)
            )

    @property
    def is_modified(self) -> bool | None:
        """The _isModified field value."""
        member = self.get_member("_isModified")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_modified.setter
    def is_modified(self, value: bool) -> None:
        """Set the _isModified field value."""
        member = self.get_member("_isModified")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isModified", fields.FieldBool(value=value)
            )

