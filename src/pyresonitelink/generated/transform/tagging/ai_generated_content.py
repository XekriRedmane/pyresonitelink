"""Generated component: AI_GeneratedContent."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AI_GeneratedContent(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AI_GeneratedContent.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AI_GeneratedContent"

    def __init__(self, source: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source

    @property
    def source(self) -> primitives.String | None:
        """The Source field value."""
        member = self.get_member("Source")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @source.setter
    def source(self, value: primitives.String) -> None:
        """Set the Source field value."""
        member = self.get_member("Source")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Source", fields.FieldString(value=value)
            )

