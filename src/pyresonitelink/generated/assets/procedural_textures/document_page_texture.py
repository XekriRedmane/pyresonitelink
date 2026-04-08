"""Generated component: DocumentPageTexture."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.document import Document
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DocumentPageTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DocumentPageTexture.

    Category: Assets/Procedural Textures
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DocumentPageTexture"

    def __init__(self, high_priority_integration: bool | None = None, anisotropic_level: np.int32 | None = None, mipmap_bias: np.float32 | None = None, size: np.int32 | None = None, mipmaps: bool | None = None, document: str | IAssetProvider[Document] | None = None, page_index: np.int32 | None = None, page_region: primitives.Rect | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            anisotropic_level: Initial value for AnisotropicLevel.
            mipmap_bias: Initial value for MipmapBias.
            size: Initial value for Size.
            mipmaps: Initial value for Mipmaps.
            document: Initial value for Document.
            page_index: Initial value for PageIndex.
            page_region: Initial value for PageRegion.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if mipmap_bias is not None:
            self.mipmap_bias = mipmap_bias
        if size is not None:
            self.size = size
        if mipmaps is not None:
            self.mipmaps = mipmaps
        if document is not None:
            self.document = document
        if page_index is not None:
            self.page_index = page_index
        if page_region is not None:
            self.page_region = page_region

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def filter_mode(self) -> members.FieldEnum | None:
        """The FilterMode member."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @filter_mode.setter
    def filter_mode(self, value: members.FieldEnum) -> None:
        """Set the FilterMode member."""
        self.set_member("FilterMode", value)

    @property
    def anisotropic_level(self) -> np.int32 | None:
        """The AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anisotropic_level.setter
    def anisotropic_level(self, value: np.int32) -> None:
        """Set the AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnisotropicLevel", fields.FieldInt(value=value)
            )

    @property
    def wrap_mode_u(self) -> members.FieldEnum | None:
        """The WrapModeU member."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: members.FieldEnum) -> None:
        """Set the WrapModeU member."""
        self.set_member("WrapModeU", value)

    @property
    def wrap_mode_v(self) -> members.FieldEnum | None:
        """The WrapModeV member."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: members.FieldEnum) -> None:
        """Set the WrapModeV member."""
        self.set_member("WrapModeV", value)

    @property
    def mipmap_bias(self) -> np.float32 | None:
        """The MipmapBias field value."""
        member = self.get_member("MipmapBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mipmap_bias.setter
    def mipmap_bias(self, value: np.float32) -> None:
        """Set the MipmapBias field value."""
        member = self.get_member("MipmapBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipmapBias", fields.FieldFloat(value=value)
            )

    @property
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def size(self) -> np.int32 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: np.int32) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldInt(value=value)
            )

    @property
    def mipmaps(self) -> bool | None:
        """The Mipmaps field value."""
        member = self.get_member("Mipmaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mipmaps.setter
    def mipmaps(self, value: bool) -> None:
        """Set the Mipmaps field value."""
        member = self.get_member("Mipmaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mipmaps", fields.FieldBool(value=value)
            )

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
    def page_region(self) -> primitives.Rect | None:
        """The PageRegion field value."""
        member = self.get_member("PageRegion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @page_region.setter
    def page_region(self, value: primitives.Rect) -> None:
        """Set the PageRegion field value."""
        member = self.get_member("PageRegion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PageRegion", fields.FieldRect(value=value)
            )

    async def bake_texture(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeTexture sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeTexture", {}, debug,
        )

