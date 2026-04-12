"""Generated component: FolderImportDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FolderImportDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The FolderImportDialog component is used to make and handle the importing of a folder with the specified path. Generates a UIX upon attach.

    Used to Import folders. Use the version created via the normal Import
    process instead.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FolderImportDialog"

    def __init__(self, path: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path

    @property
    def path(self) -> primitives.String | None:
        """The folder path to Import the contents of."""
        member = self.get_member("Path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
        """Set the Path field value."""
        member = self.get_member("Path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Path", fields.FieldString(value=value)
            )

