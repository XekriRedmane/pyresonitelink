"""Generated component: GaussianSplatQualitySettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GaussianSplatQualitySettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatQualitySettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatQualitySettings"

    def __init__(self, advanced_quality: bool | None = None, sort_mega_operations_per_camera: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            advanced_quality: Initial value for AdvancedQuality.
            sort_mega_operations_per_camera: Initial value for SortMegaOperationsPerCamera.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if advanced_quality is not None:
            self.advanced_quality = advanced_quality
        if sort_mega_operations_per_camera is not None:
            self.sort_mega_operations_per_camera = sort_mega_operations_per_camera

    @property
    def quality_preset(self) -> members.FieldEnum | None:
        """The QualityPreset member."""
        member = self.get_member("QualityPreset")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @quality_preset.setter
    def quality_preset(self, value: members.FieldEnum) -> None:
        """Set the QualityPreset member."""
        self.set_member("QualityPreset", value)

    @property
    def min_local_quality(self) -> members.FieldEnum | None:
        """The MinLocalQuality member."""
        member = self.get_member("MinLocalQuality")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @min_local_quality.setter
    def min_local_quality(self, value: members.FieldEnum) -> None:
        """Set the MinLocalQuality member."""
        self.set_member("MinLocalQuality", value)

    @property
    def advanced_quality(self) -> bool | None:
        """The AdvancedQuality field value."""
        member = self.get_member("AdvancedQuality")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @advanced_quality.setter
    def advanced_quality(self, value: bool) -> None:
        """Set the AdvancedQuality field value."""
        member = self.get_member("AdvancedQuality")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AdvancedQuality", fields.FieldBool(value=value)
            )

    @property
    def position_format(self) -> members.FieldEnum | None:
        """The PositionFormat member."""
        member = self.get_member("PositionFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @position_format.setter
    def position_format(self, value: members.FieldEnum) -> None:
        """Set the PositionFormat member."""
        self.set_member("PositionFormat", value)

    @property
    def scale_format(self) -> members.FieldEnum | None:
        """The ScaleFormat member."""
        member = self.get_member("ScaleFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @scale_format.setter
    def scale_format(self, value: members.FieldEnum) -> None:
        """Set the ScaleFormat member."""
        self.set_member("ScaleFormat", value)

    @property
    def color_format(self) -> members.FieldEnum | None:
        """The ColorFormat member."""
        member = self.get_member("ColorFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @color_format.setter
    def color_format(self, value: members.FieldEnum) -> None:
        """Set the ColorFormat member."""
        self.set_member("ColorFormat", value)

    @property
    def spherical_harmonics_format(self) -> members.FieldEnum | None:
        """The SphericalHarmonicsFormat member."""
        member = self.get_member("SphericalHarmonicsFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @spherical_harmonics_format.setter
    def spherical_harmonics_format(self, value: members.FieldEnum) -> None:
        """Set the SphericalHarmonicsFormat member."""
        self.set_member("SphericalHarmonicsFormat", value)

    @property
    def sort_mega_operations_per_camera(self) -> np.float32 | None:
        """The SortMegaOperationsPerCamera field value."""
        member = self.get_member("SortMegaOperationsPerCamera")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sort_mega_operations_per_camera.setter
    def sort_mega_operations_per_camera(self, value: np.float32) -> None:
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

