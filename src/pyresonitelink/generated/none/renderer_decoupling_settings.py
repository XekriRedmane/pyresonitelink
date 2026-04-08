"""Generated component: RendererDecouplingSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class RendererDecouplingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.RendererDecouplingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RendererDecouplingSettings"

    def __init__(self, activation_framerate: np.float32 | None = None, deactivation_frames: np.int32 | None = None, force_decouple: bool | None = None, asset_processing_max_time_milliseconds: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            activation_framerate: Initial value for ActivationFramerate.
            deactivation_frames: Initial value for DeactivationFrames.
            force_decouple: Initial value for ForceDecouple.
            asset_processing_max_time_milliseconds: Initial value for AssetProcessingMaxTimeMilliseconds.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if activation_framerate is not None:
            self.activation_framerate = activation_framerate
        if deactivation_frames is not None:
            self.deactivation_frames = deactivation_frames
        if force_decouple is not None:
            self.force_decouple = force_decouple
        if asset_processing_max_time_milliseconds is not None:
            self.asset_processing_max_time_milliseconds = asset_processing_max_time_milliseconds

    @property
    def activation_framerate(self) -> np.float32 | None:
        """The ActivationFramerate field value."""
        member = self.get_member("ActivationFramerate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_framerate.setter
    def activation_framerate(self, value: np.float32) -> None:
        """Set the ActivationFramerate field value."""
        member = self.get_member("ActivationFramerate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationFramerate", fields.FieldFloat(value=value)
            )

    @property
    def deactivation_frames(self) -> np.int32 | None:
        """The DeactivationFrames field value."""
        member = self.get_member("DeactivationFrames")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deactivation_frames.setter
    def deactivation_frames(self, value: np.int32) -> None:
        """Set the DeactivationFrames field value."""
        member = self.get_member("DeactivationFrames")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeactivationFrames", fields.FieldInt(value=value)
            )

    @property
    def force_decouple(self) -> bool | None:
        """The ForceDecouple field value."""
        member = self.get_member("ForceDecouple")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_decouple.setter
    def force_decouple(self, value: bool) -> None:
        """Set the ForceDecouple field value."""
        member = self.get_member("ForceDecouple")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceDecouple", fields.FieldBool(value=value)
            )

    @property
    def asset_processing_max_time_milliseconds(self) -> np.float32 | None:
        """The AssetProcessingMaxTimeMilliseconds field value."""
        member = self.get_member("AssetProcessingMaxTimeMilliseconds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @asset_processing_max_time_milliseconds.setter
    def asset_processing_max_time_milliseconds(self, value: np.float32) -> None:
        """Set the AssetProcessingMaxTimeMilliseconds field value."""
        member = self.get_member("AssetProcessingMaxTimeMilliseconds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AssetProcessingMaxTimeMilliseconds", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

