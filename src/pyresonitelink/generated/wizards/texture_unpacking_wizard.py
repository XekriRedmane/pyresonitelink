"""Generated component: TextureUnpackingWizard."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureUnpackingWizard(GeneratedComponent, IDeveloperInterface, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextureUnpackingWizard.

    Category: Wizards
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureUnpackingWizard"

    def __init__(self, input_texture: str | IAssetProvider[ITexture2D] | None = None, channels: primitives.Bool4 | None = None, rtexture: str | IAssetProvider[ITexture2D] | None = None, gtexture: str | IAssetProvider[ITexture2D] | None = None, btexture: str | IAssetProvider[ITexture2D] | None = None, atexture: str | IAssetProvider[ITexture2D] | None = None, is_processing: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            input_texture: Initial value for InputTexture.
            channels: Initial value for Channels.
            rtexture: Initial value for RTexture.
            gtexture: Initial value for GTexture.
            btexture: Initial value for BTexture.
            atexture: Initial value for ATexture.
            is_processing: Initial value for IsProcessing.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if input_texture is not None:
            self.input_texture = input_texture
        if channels is not None:
            self.channels = channels
        if rtexture is not None:
            self.rtexture = rtexture
        if gtexture is not None:
            self.gtexture = gtexture
        if btexture is not None:
            self.btexture = btexture
        if atexture is not None:
            self.atexture = atexture
        if is_processing is not None:
            self.is_processing = is_processing

    @property
    def input_texture(self) -> str | None:
        """Target ID of the InputTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("InputTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_texture.setter
    def input_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the InputTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("InputTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InputTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def channels(self) -> primitives.Bool4 | None:
        """The Channels field value."""
        member = self.get_member("Channels")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @channels.setter
    def channels(self, value: primitives.Bool4) -> None:
        """Set the Channels field value."""
        member = self.get_member("Channels")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Channels", fields.FieldBool4(value=value)
            )

    @property
    def resolution_override(self) -> members.FieldEnum | None:
        """The ResolutionOverride member."""
        member = self.get_member("ResolutionOverride")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @resolution_override.setter
    def resolution_override(self, value: members.FieldEnum) -> None:
        """Set the ResolutionOverride member."""
        self.set_member("ResolutionOverride", value)

    @property
    def rtexture(self) -> str | None:
        """Target ID of the RTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("RTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rtexture.setter
    def rtexture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the RTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("RTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def gtexture(self) -> str | None:
        """Target ID of the GTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("GTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gtexture.setter
    def gtexture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the GTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("GTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def btexture(self) -> str | None:
        """Target ID of the BTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("BTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @btexture.setter
    def btexture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the BTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("BTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def atexture(self) -> str | None:
        """Target ID of the ATexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ATexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @atexture.setter
    def atexture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ATexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ATexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ATexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def is_processing(self) -> primitives.Bool | None:
        """The IsProcessing field value."""
        member = self.get_member("IsProcessing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_processing.setter
    def is_processing(self, value: primitives.Bool) -> None:
        """Set the IsProcessing field value."""
        member = self.get_member("IsProcessing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsProcessing", fields.FieldBool(value=value)
            )

    async def unpack_textures(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the UnpackTextures sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "UnpackTextures", {}, debug,
        )

