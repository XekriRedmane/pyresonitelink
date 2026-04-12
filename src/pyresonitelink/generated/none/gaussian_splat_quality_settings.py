"""Generated component: GaussianSplatQualitySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.gaussian_splat_quality_preset import GaussianSplatQualityPreset
from pyresonitelink.generated._enums.gaussian_vector_format import GaussianVectorFormat
from pyresonitelink.generated._enums.gaussian_color_format import GaussianColorFormat
from pyresonitelink.generated._enums.gaussian_sh_format import GaussianSHFormat
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GaussianSplatQualitySettings(GeneratedComponent, ICustomInspector):
    """The Gaussian Splat Quality Settings component is used to control the quality of Gaussian Splats in a world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatQualitySettings"

    def __init__(self, quality_preset: GaussianSplatQualityPreset | str | None = None, min_local_quality: GaussianSplatQualityPreset | str | None = None, advanced_quality: primitives.Bool | None = None, position_format: GaussianVectorFormat | str | None = None, scale_format: GaussianVectorFormat | str | None = None, color_format: GaussianColorFormat | str | None = None, spherical_harmonics_format: GaussianSHFormat | str | None = None, sort_mega_operations_per_camera: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            quality_preset: Initial value for QualityPreset.
            min_local_quality: Initial value for MinLocalQuality.
            advanced_quality: Initial value for AdvancedQuality.
            position_format: Initial value for PositionFormat.
            scale_format: Initial value for ScaleFormat.
            color_format: Initial value for ColorFormat.
            spherical_harmonics_format: Initial value for SphericalHarmonicsFormat.
            sort_mega_operations_per_camera: Initial value for SortMegaOperationsPerCamera.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if quality_preset is not None:
            self.quality_preset = quality_preset
        if min_local_quality is not None:
            self.min_local_quality = min_local_quality
        if advanced_quality is not None:
            self.advanced_quality = advanced_quality
        if position_format is not None:
            self.position_format = position_format
        if scale_format is not None:
            self.scale_format = scale_format
        if color_format is not None:
            self.color_format = color_format
        if spherical_harmonics_format is not None:
            self.spherical_harmonics_format = spherical_harmonics_format
        if sort_mega_operations_per_camera is not None:
            self.sort_mega_operations_per_camera = sort_mega_operations_per_camera

    @property
    def quality_preset(self) -> GaussianSplatQualityPreset | None:
        """The preset to use for quality of Gaussian splats."""
        member = self.get_member("QualityPreset")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return GaussianSplatQualityPreset(member.value)
        return None

    @quality_preset.setter
    def quality_preset(self, value: GaussianSplatQualityPreset | str) -> None:
        """Set QualityPreset. The preset to use for quality of Gaussian splats."""
        member = self.get_member("QualityPreset")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "QualityPreset",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_local_quality(self) -> GaussianSplatQualityPreset | None:
        """The preset to use for the minimum quality of Gaussian splats."""
        member = self.get_member("MinLocalQuality")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return GaussianSplatQualityPreset(member.value)
        return None

    @min_local_quality.setter
    def min_local_quality(self, value: GaussianSplatQualityPreset | str) -> None:
        """Set MinLocalQuality. The preset to use for the minimum quality of Gaussian splats."""
        member = self.get_member("MinLocalQuality")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MinLocalQuality",
                members.FieldEnum(value=str(value)),
            )

    @property
    def advanced_quality(self) -> primitives.Bool | None:
        """The AdvancedQuality field value."""
        member = self.get_member("AdvancedQuality")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @advanced_quality.setter
    def advanced_quality(self, value: primitives.Bool) -> None:
        """Set the AdvancedQuality field value."""
        member = self.get_member("AdvancedQuality")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AdvancedQuality", fields.FieldBool(value=value)
            )

    @property
    def position_format(self) -> GaussianVectorFormat | None:
        """The PositionFormat enum value."""
        member = self.get_member("PositionFormat")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return GaussianVectorFormat(member.value)
        return None

    @position_format.setter
    def position_format(self, value: GaussianVectorFormat | str) -> None:
        """Set the PositionFormat enum value."""
        member = self.get_member("PositionFormat")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositionFormat",
                members.FieldEnum(value=str(value)),
            )

    @property
    def scale_format(self) -> GaussianVectorFormat | None:
        """The ScaleFormat enum value."""
        member = self.get_member("ScaleFormat")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return GaussianVectorFormat(member.value)
        return None

    @scale_format.setter
    def scale_format(self, value: GaussianVectorFormat | str) -> None:
        """Set the ScaleFormat enum value."""
        member = self.get_member("ScaleFormat")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ScaleFormat",
                members.FieldEnum(value=str(value)),
            )

    @property
    def color_format(self) -> GaussianColorFormat | None:
        """The ColorFormat enum value."""
        member = self.get_member("ColorFormat")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return GaussianColorFormat(member.value)
        return None

    @color_format.setter
    def color_format(self, value: GaussianColorFormat | str) -> None:
        """Set the ColorFormat enum value."""
        member = self.get_member("ColorFormat")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ColorFormat",
                members.FieldEnum(value=str(value)),
            )

    @property
    def spherical_harmonics_format(self) -> GaussianSHFormat | None:
        """The SphericalHarmonicsFormat enum value."""
        member = self.get_member("SphericalHarmonicsFormat")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return GaussianSHFormat(member.value)
        return None

    @spherical_harmonics_format.setter
    def spherical_harmonics_format(self, value: GaussianSHFormat | str) -> None:
        """Set the SphericalHarmonicsFormat enum value."""
        member = self.get_member("SphericalHarmonicsFormat")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SphericalHarmonicsFormat",
                members.FieldEnum(value=str(value)),
            )

    @property
    def sort_mega_operations_per_camera(self) -> primitives.Float | None:
        """The amount of sorting to do in different cameras rendering Gaussian splats."""
        member = self.get_member("SortMegaOperationsPerCamera")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sort_mega_operations_per_camera.setter
    def sort_mega_operations_per_camera(self, value: primitives.Float) -> None:
        """Set the SortMegaOperationsPerCamera field value."""
        member = self.get_member("SortMegaOperationsPerCamera")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SortMegaOperationsPerCamera", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

