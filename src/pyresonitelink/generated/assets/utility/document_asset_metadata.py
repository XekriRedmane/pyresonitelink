"""Generated component: DocumentAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.document import Document
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DocumentAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DocumentAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DocumentAssetMetadata"

    def __init__(self, document: str | IAssetProvider[Document] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            document: Initial value for Document.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if document is not None:
            self.document = document

    @property
    def document(self) -> str | None:
        """Target ID of the Document reference (targets IAssetProvider[Document])."""
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
    def page_count(self) -> members.EmptyElement | None:
        """The PageCount member."""
        member = self.get_member("PageCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @page_count.setter
    def page_count(self, value: members.EmptyElement) -> None:
        """Set the PageCount member."""
        self.set_member("PageCount", value)

