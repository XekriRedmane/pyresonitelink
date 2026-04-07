"""Generated component: FileMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FileMetadata(GeneratedComponent, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FileMetadata.

    Category: Data
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FileMetadata"

    def __init__(self, filename: str | None = None, mime: str | None = None, is_processing: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            filename: Initial value for Filename.
            mime: Initial value for MIME.
            is_processing: Initial value for IsProcessing.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if filename is not None:
            self.filename = filename
        if mime is not None:
            self.mime = mime
        if is_processing is not None:
            self.is_processing = is_processing

    @property
    def filename(self) -> str | None:
        """The Filename field value."""
        member = self.get_member("Filename")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @filename.setter
    def filename(self, value: str) -> None:
        """Set the Filename field value."""
        member = self.get_member("Filename")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Filename", fields.FieldString(value=value)
            )

    @property
    def mime(self) -> str | None:
        """The MIME field value."""
        member = self.get_member("MIME")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mime.setter
    def mime(self, value: str) -> None:
        """Set the MIME field value."""
        member = self.get_member("MIME")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MIME", fields.FieldString(value=value)
            )

    @property
    def is_processing(self) -> bool | None:
        """The IsProcessing field value."""
        member = self.get_member("IsProcessing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_processing.setter
    def is_processing(self, value: bool) -> None:
        """Set the IsProcessing field value."""
        member = self.get_member("IsProcessing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsProcessing", fields.FieldBool(value=value)
            )

