"""Generated component: GridContainerPreset."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imodified_event_receiver import IModifiedEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GridContainerPreset(GeneratedComponent, IModifiedEventReceiver, IWorldEventReceiver):
    """The GridContainerPreset component generates a GridContainerScreen tab and set it up when not initialized before.

    Used to make automatically updating custom screens.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GridContainerPreset"

    def __init__(self, initializer: Type | str | None = None, initialized_version: primitives.Int | None = None, is_modified: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            initializer: Initial value for _initializer.
            initialized_version: Initial value for _initializedVersion.
            is_modified: Initial value for _isModified.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if initializer is not None:
            self.initializer = initializer
        if initialized_version is not None:
            self.initialized_version = initialized_version
        if is_modified is not None:
            self.is_modified = is_modified

    @property
    def initializer(self) -> Type | None:
        """The C# Type of the object that initialized this preset."""
        member = self.get_member("_initializer")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @initializer.setter
    def initializer(self, value: Type | str) -> None:
        """Set _initializer. The C# Type of the object that initialized this preset."""
        member = self.get_member("_initializer")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_initializer",
                members.FieldEnum(value=str(value)),
            )

    @property
    def initialized_version(self) -> primitives.Int | None:
        """The version that this preset initialized. Used to reinitialize the Grid Container Screen if it has new updates."""
        member = self.get_member("_initializedVersion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initialized_version.setter
    def initialized_version(self, value: primitives.Int) -> None:
        """Set the _initializedVersion field value."""
        member = self.get_member("_initializedVersion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_initializedVersion", fields.FieldInt(value=value)
            )

    @property
    def is_modified(self) -> primitives.Bool | None:
        """Whether the Grid Container Screen has new content like facets."""
        member = self.get_member("_isModified")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_modified.setter
    def is_modified(self, value: primitives.Bool) -> None:
        """Set the _isModified field value."""
        member = self.get_member("_isModified")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isModified", fields.FieldBool(value=value)
            )

