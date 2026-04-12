"""Generated component: DocumentAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.document import Document
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DocumentAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DocumentAssetMetadata component gets data about a provided document asset.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DocumentAssetMetadata"

    def __init__(self, document: str | IAssetProvider[Document] | None = None, page_count: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            document: Initial value for Document.
            page_count: Initial value for PageCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if document is not None:
            self.document = document
        if page_count is not None:
            self.page_count = page_count

    @property
    def document(self) -> str | None:
        """The document (usually PDF) that info is being acquired from."""
        member = self.get_member("Document")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @document.setter
    def document(self, target: str | IAssetProvider[Document] | None) -> None:
        """Set the Document reference by target ID or IAssetProvider[Document] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Document")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Document",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Document>'),
            )

    @property
    def page_count(self) -> primitives.Int | None:
        """The page count of the document."""
        member = self.get_member("PageCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @page_count.setter
    def page_count(self, value: primitives.Int) -> None:
        """Set the PageCount field value."""
        member = self.get_member("PageCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PageCount", fields.FieldInt(value=value)
            )

