"""Generated component: RendererDecouplingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class RendererDecouplingSettings(GeneratedComponent, ICustomInspector):
    """The Renderer Decoupling Settings component controls how the render engine will decouple from FrooxEngine when FrooxEngine lags to prevent sea-sickness.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RendererDecouplingSettings"

    def __init__(self, activation_framerate: primitives.Float | None = None, deactivation_frames: primitives.Int | None = None, force_decouple: primitives.Bool | None = None, asset_processing_max_time_milliseconds: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
    def activation_framerate(self) -> primitives.Float | None:
        """How low the framerate from frooxengine needs to be to activate a decoupled frooxengine state"""
        member = self.get_member("ActivationFramerate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_framerate.setter
    def activation_framerate(self, value: primitives.Float) -> None:
        """Set the ActivationFramerate field value."""
        member = self.get_member("ActivationFramerate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationFramerate", fields.FieldFloat(value=value)
            )

    @property
    def deactivation_frames(self) -> primitives.Int | None:
        """How high the framerate from frooxengine needs to be to deactivate a decoupled frooxengine state"""
        member = self.get_member("DeactivationFrames")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deactivation_frames.setter
    def deactivation_frames(self, value: primitives.Int) -> None:
        """Set the DeactivationFrames field value."""
        member = self.get_member("DeactivationFrames")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeactivationFrames", fields.FieldInt(value=value)
            )

    @property
    def force_decouple(self) -> primitives.Bool | None:
        """Whether or not to wait for frooxengine at all, and to just runaway render frames."""
        member = self.get_member("ForceDecouple")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_decouple.setter
    def force_decouple(self, value: primitives.Bool) -> None:
        """Set the ForceDecouple field value."""
        member = self.get_member("ForceDecouple")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceDecouple", fields.FieldBool(value=value)
            )

    @property
    def asset_processing_max_time_milliseconds(self) -> primitives.Float | None:
        """How long to wait to process assets before continuing on the next frame anyways."""
        member = self.get_member("AssetProcessingMaxTimeMilliseconds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @asset_processing_max_time_milliseconds.setter
    def asset_processing_max_time_milliseconds(self, value: primitives.Float) -> None:
        """Set the AssetProcessingMaxTimeMilliseconds field value."""
        member = self.get_member("AssetProcessingMaxTimeMilliseconds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AssetProcessingMaxTimeMilliseconds", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Reset settings on this component back to their default.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

