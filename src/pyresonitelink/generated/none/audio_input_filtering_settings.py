"""Generated component: AudioInputFilteringSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioInputFilteringSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioInputFilteringSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioInputFilteringSettings"

    def __init__(self, use_voice_normalization: primitives.Bool | None = None, normalization_threshold: primitives.Float | None = None, use_noise_suppression: primitives.Bool | None = None, noise_gate_threshold: primitives.Float | None = None, noise_gate_attack: primitives.Float | None = None, noise_gate_hold: primitives.Float | None = None, noise_gate_release: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_voice_normalization: Initial value for UseVoiceNormalization.
            normalization_threshold: Initial value for NormalizationThreshold.
            use_noise_suppression: Initial value for UseNoiseSuppression.
            noise_gate_threshold: Initial value for NoiseGateThreshold.
            noise_gate_attack: Initial value for NoiseGateAttack.
            noise_gate_hold: Initial value for NoiseGateHold.
            noise_gate_release: Initial value for NoiseGateRelease.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_voice_normalization is not None:
            self.use_voice_normalization = use_voice_normalization
        if normalization_threshold is not None:
            self.normalization_threshold = normalization_threshold
        if use_noise_suppression is not None:
            self.use_noise_suppression = use_noise_suppression
        if noise_gate_threshold is not None:
            self.noise_gate_threshold = noise_gate_threshold
        if noise_gate_attack is not None:
            self.noise_gate_attack = noise_gate_attack
        if noise_gate_hold is not None:
            self.noise_gate_hold = noise_gate_hold
        if noise_gate_release is not None:
            self.noise_gate_release = noise_gate_release

    @property
    def use_voice_normalization(self) -> primitives.Bool | None:
        """The UseVoiceNormalization field value."""
        member = self.get_member("UseVoiceNormalization")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_voice_normalization.setter
    def use_voice_normalization(self, value: primitives.Bool) -> None:
        """Set the UseVoiceNormalization field value."""
        member = self.get_member("UseVoiceNormalization")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVoiceNormalization", fields.FieldBool(value=value)
            )

    @property
    def normalization_threshold(self) -> primitives.Float | None:
        """The NormalizationThreshold field value."""
        member = self.get_member("NormalizationThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalization_threshold.setter
    def normalization_threshold(self, value: primitives.Float) -> None:
        """Set the NormalizationThreshold field value."""
        member = self.get_member("NormalizationThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizationThreshold", fields.FieldFloat(value=value)
            )

    @property
    def use_noise_suppression(self) -> primitives.Bool | None:
        """The UseNoiseSuppression field value."""
        member = self.get_member("UseNoiseSuppression")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_noise_suppression.setter
    def use_noise_suppression(self, value: primitives.Bool) -> None:
        """Set the UseNoiseSuppression field value."""
        member = self.get_member("UseNoiseSuppression")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseNoiseSuppression", fields.FieldBool(value=value)
            )

    @property
    def noise_gate_threshold(self) -> primitives.Float | None:
        """The NoiseGateThreshold field value."""
        member = self.get_member("NoiseGateThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_threshold.setter
    def noise_gate_threshold(self, value: primitives.Float) -> None:
        """Set the NoiseGateThreshold field value."""
        member = self.get_member("NoiseGateThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateThreshold", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_attack(self) -> primitives.Float | None:
        """The NoiseGateAttack field value."""
        member = self.get_member("NoiseGateAttack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_attack.setter
    def noise_gate_attack(self, value: primitives.Float) -> None:
        """Set the NoiseGateAttack field value."""
        member = self.get_member("NoiseGateAttack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateAttack", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_hold(self) -> primitives.Float | None:
        """The NoiseGateHold field value."""
        member = self.get_member("NoiseGateHold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_hold.setter
    def noise_gate_hold(self, value: primitives.Float) -> None:
        """Set the NoiseGateHold field value."""
        member = self.get_member("NoiseGateHold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateHold", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_release(self) -> primitives.Float | None:
        """The NoiseGateRelease field value."""
        member = self.get_member("NoiseGateRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_release.setter
    def noise_gate_release(self, value: primitives.Float) -> None:
        """Set the NoiseGateRelease field value."""
        member = self.get_member("NoiseGateRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateRelease", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

