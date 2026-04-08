"""Generated component: TexturePackingWizard."""

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


class TexturePackingWizard(GeneratedComponent, IDeveloperInterface, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TexturePackingWizard.

    Category: Wizards
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TexturePackingWizard"

    def __init__(self, rtexture: str | IAssetProvider[ITexture2D] | None = None, rfallback_value: primitives.Float | None = None, rinvert: primitives.Bool | None = None, gtexture: str | IAssetProvider[ITexture2D] | None = None, gfallback_value: primitives.Float | None = None, ginvert: primitives.Bool | None = None, btexture: str | IAssetProvider[ITexture2D] | None = None, bfallback_value: primitives.Float | None = None, binvert: primitives.Bool | None = None, atexture: str | IAssetProvider[ITexture2D] | None = None, afallback_value: primitives.Float | None = None, ainvert: primitives.Bool | None = None, empty_fallback_resolution: primitives.Int2 | None = None, generate_mips: primitives.Bool | None = None, output_texture: str | IAssetProvider[ITexture2D] | None = None, is_processing: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rtexture: Initial value for RTexture.
            rfallback_value: Initial value for RFallbackValue.
            rinvert: Initial value for RInvert.
            gtexture: Initial value for GTexture.
            gfallback_value: Initial value for GFallbackValue.
            ginvert: Initial value for GInvert.
            btexture: Initial value for BTexture.
            bfallback_value: Initial value for BFallbackValue.
            binvert: Initial value for BInvert.
            atexture: Initial value for ATexture.
            afallback_value: Initial value for AFallbackValue.
            ainvert: Initial value for AInvert.
            empty_fallback_resolution: Initial value for EmptyFallbackResolution.
            generate_mips: Initial value for GenerateMips.
            output_texture: Initial value for OutputTexture.
            is_processing: Initial value for IsProcessing.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rtexture is not None:
            self.rtexture = rtexture
        if rfallback_value is not None:
            self.rfallback_value = rfallback_value
        if rinvert is not None:
            self.rinvert = rinvert
        if gtexture is not None:
            self.gtexture = gtexture
        if gfallback_value is not None:
            self.gfallback_value = gfallback_value
        if ginvert is not None:
            self.ginvert = ginvert
        if btexture is not None:
            self.btexture = btexture
        if bfallback_value is not None:
            self.bfallback_value = bfallback_value
        if binvert is not None:
            self.binvert = binvert
        if atexture is not None:
            self.atexture = atexture
        if afallback_value is not None:
            self.afallback_value = afallback_value
        if ainvert is not None:
            self.ainvert = ainvert
        if empty_fallback_resolution is not None:
            self.empty_fallback_resolution = empty_fallback_resolution
        if generate_mips is not None:
            self.generate_mips = generate_mips
        if output_texture is not None:
            self.output_texture = output_texture
        if is_processing is not None:
            self.is_processing = is_processing

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
    def rfallback_value(self) -> primitives.Float | None:
        """The RFallbackValue field value."""
        member = self.get_member("RFallbackValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rfallback_value.setter
    def rfallback_value(self, value: primitives.Float) -> None:
        """Set the RFallbackValue field value."""
        member = self.get_member("RFallbackValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RFallbackValue", fields.FieldFloat(value=value)
            )

    @property
    def rcolor_channel(self) -> members.FieldEnum | None:
        """The RColorChannel member."""
        member = self.get_member("RColorChannel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rcolor_channel.setter
    def rcolor_channel(self, value: members.FieldEnum) -> None:
        """Set the RColorChannel member."""
        self.set_member("RColorChannel", value)

    @property
    def rinvert(self) -> primitives.Bool | None:
        """The RInvert field value."""
        member = self.get_member("RInvert")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rinvert.setter
    def rinvert(self, value: primitives.Bool) -> None:
        """Set the RInvert field value."""
        member = self.get_member("RInvert")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RInvert", fields.FieldBool(value=value)
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
    def gfallback_value(self) -> primitives.Float | None:
        """The GFallbackValue field value."""
        member = self.get_member("GFallbackValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gfallback_value.setter
    def gfallback_value(self, value: primitives.Float) -> None:
        """Set the GFallbackValue field value."""
        member = self.get_member("GFallbackValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GFallbackValue", fields.FieldFloat(value=value)
            )

    @property
    def gcolor_channel(self) -> members.FieldEnum | None:
        """The GColorChannel member."""
        member = self.get_member("GColorChannel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @gcolor_channel.setter
    def gcolor_channel(self, value: members.FieldEnum) -> None:
        """Set the GColorChannel member."""
        self.set_member("GColorChannel", value)

    @property
    def ginvert(self) -> primitives.Bool | None:
        """The GInvert field value."""
        member = self.get_member("GInvert")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ginvert.setter
    def ginvert(self, value: primitives.Bool) -> None:
        """Set the GInvert field value."""
        member = self.get_member("GInvert")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GInvert", fields.FieldBool(value=value)
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
    def bfallback_value(self) -> primitives.Float | None:
        """The BFallbackValue field value."""
        member = self.get_member("BFallbackValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bfallback_value.setter
    def bfallback_value(self, value: primitives.Float) -> None:
        """Set the BFallbackValue field value."""
        member = self.get_member("BFallbackValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BFallbackValue", fields.FieldFloat(value=value)
            )

    @property
    def bcolor_channel(self) -> members.FieldEnum | None:
        """The BColorChannel member."""
        member = self.get_member("BColorChannel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @bcolor_channel.setter
    def bcolor_channel(self, value: members.FieldEnum) -> None:
        """Set the BColorChannel member."""
        self.set_member("BColorChannel", value)

    @property
    def binvert(self) -> primitives.Bool | None:
        """The BInvert field value."""
        member = self.get_member("BInvert")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @binvert.setter
    def binvert(self, value: primitives.Bool) -> None:
        """Set the BInvert field value."""
        member = self.get_member("BInvert")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BInvert", fields.FieldBool(value=value)
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
    def afallback_value(self) -> primitives.Float | None:
        """The AFallbackValue field value."""
        member = self.get_member("AFallbackValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @afallback_value.setter
    def afallback_value(self, value: primitives.Float) -> None:
        """Set the AFallbackValue field value."""
        member = self.get_member("AFallbackValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AFallbackValue", fields.FieldFloat(value=value)
            )

    @property
    def acolor_channel(self) -> members.FieldEnum | None:
        """The AColorChannel member."""
        member = self.get_member("AColorChannel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @acolor_channel.setter
    def acolor_channel(self, value: members.FieldEnum) -> None:
        """Set the AColorChannel member."""
        self.set_member("AColorChannel", value)

    @property
    def ainvert(self) -> primitives.Bool | None:
        """The AInvert field value."""
        member = self.get_member("AInvert")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ainvert.setter
    def ainvert(self, value: primitives.Bool) -> None:
        """Set the AInvert field value."""
        member = self.get_member("AInvert")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AInvert", fields.FieldBool(value=value)
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
    def resolution_sizing(self) -> members.FieldEnum | None:
        """The ResolutionSizing member."""
        member = self.get_member("ResolutionSizing")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @resolution_sizing.setter
    def resolution_sizing(self, value: members.FieldEnum) -> None:
        """Set the ResolutionSizing member."""
        self.set_member("ResolutionSizing", value)

    @property
    def empty_fallback_resolution(self) -> primitives.Int2 | None:
        """The EmptyFallbackResolution field value."""
        member = self.get_member("EmptyFallbackResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @empty_fallback_resolution.setter
    def empty_fallback_resolution(self, value: primitives.Int2) -> None:
        """Set the EmptyFallbackResolution field value."""
        member = self.get_member("EmptyFallbackResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmptyFallbackResolution", fields.FieldInt2(value=value)
            )

    @property
    def generate_mips(self) -> primitives.Bool | None:
        """The GenerateMips field value."""
        member = self.get_member("GenerateMips")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @generate_mips.setter
    def generate_mips(self, value: primitives.Bool) -> None:
        """Set the GenerateMips field value."""
        member = self.get_member("GenerateMips")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GenerateMips", fields.FieldBool(value=value)
            )

    @property
    def output_texture(self) -> str | None:
        """Target ID of the OutputTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OutputTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @output_texture.setter
    def output_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OutputTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OutputTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OutputTexture",
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

    async def pack_textures(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the PackTextures sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PackTextures", {}, debug,
        )

