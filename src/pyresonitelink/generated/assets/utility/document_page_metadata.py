"""Generated component: DocumentPageMetadata."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.document import Document
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DocumentPageMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DocumentPageMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DocumentPageMetadata"

    def __init__(self, document: str | IAssetProvider[Document] | None = None, page_index: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            document: Initial value for Document.
            page_index: Initial value for PageIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if document is not None:
            self.document = document
        if page_index is not None:
            self.page_index = page_index

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
    def page_index(self) -> np.int32 | None:
        """The PageIndex field value."""
        member = self.get_member("PageIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @page_index.setter
    def page_index(self, value: np.int32) -> None:
        """Set the PageIndex field value."""
        member = self.get_member("PageIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PageIndex", fields.FieldInt(value=value)
            )

    @property
    def reference_size(self) -> members.EmptyElement | None:
        """The ReferenceSize member."""
        member = self.get_member("ReferenceSize")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @reference_size.setter
    def reference_size(self, value: members.EmptyElement) -> None:
        """Set the ReferenceSize member."""
        self.set_member("ReferenceSize", value)

