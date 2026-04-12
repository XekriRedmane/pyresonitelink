"""Generated component: AudioZitaReverb."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.izita_filter import IZitaFilter
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioZitaReverb(GeneratedComponent, IZitaFilter, ICustomInspector, IComponent, IWorldEventReceiver):
    """The Audio Zita Reverb component can be used to create echo effects (called ZitaParameters) onto audio clips, or on listeners in an area using the Awwdio system. To see how to use it with audio listeners, see AudioListener.

    Category: Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioZitaReverb"

    def __init__(self, in_delay: primitives.Float | None = None, crossover: primitives.Float | None = None, rt60_low: primitives.Float | None = None, rt60_mid: primitives.Float | None = None, high_frequency_damping: primitives.Float | None = None, eq1_frequency: primitives.Float | None = None, eq1_level: primitives.Float | None = None, eq2_frequency: primitives.Float | None = None, eq2_level: primitives.Float | None = None, mix: primitives.Float | None = None, level: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            in_delay: Initial value for InDelay.
            crossover: Initial value for Crossover.
            rt60_low: Initial value for RT60Low.
            rt60_mid: Initial value for RT60Mid.
            high_frequency_damping: Initial value for HighFrequencyDamping.
            eq1_frequency: Initial value for EQ1Frequency.
            eq1_level: Initial value for EQ1Level.
            eq2_frequency: Initial value for EQ2Frequency.
            eq2_level: Initial value for EQ2Level.
            mix: Initial value for Mix.
            level: Initial value for Level.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if in_delay is not None:
            self.in_delay = in_delay
        if crossover is not None:
            self.crossover = crossover
        if rt60_low is not None:
            self.rt60_low = rt60_low
        if rt60_mid is not None:
            self.rt60_mid = rt60_mid
        if high_frequency_damping is not None:
            self.high_frequency_damping = high_frequency_damping
        if eq1_frequency is not None:
            self.eq1_frequency = eq1_frequency
        if eq1_level is not None:
            self.eq1_level = eq1_level
        if eq2_frequency is not None:
            self.eq2_frequency = eq2_frequency
        if eq2_level is not None:
            self.eq2_level = eq2_level
        if mix is not None:
            self.mix = mix
        if level is not None:
            self.level = level

    @property
    def in_delay(self) -> primitives.Float | None:
        """Delay in ms before reverberation begins."""
        member = self.get_member("InDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @in_delay.setter
    def in_delay(self, value: primitives.Float) -> None:
        """Set the InDelay field value."""
        member = self.get_member("InDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InDelay", fields.FieldFloat(value=value)
            )

    @property
    def crossover(self) -> primitives.Float | None:
        """Crossover frequency separating low and middle frequencies (Hz)."""
        member = self.get_member("Crossover")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crossover.setter
    def crossover(self, value: primitives.Float) -> None:
        """Set the Crossover field value."""
        member = self.get_member("Crossover")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Crossover", fields.FieldFloat(value=value)
            )

    @property
    def rt60_low(self) -> primitives.Float | None:
        """Time (in seconds) to decay 60db in low-frequency band."""
        member = self.get_member("RT60Low")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rt60_low.setter
    def rt60_low(self, value: primitives.Float) -> None:
        """Set the RT60Low field value."""
        member = self.get_member("RT60Low")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RT60Low", fields.FieldFloat(value=value)
            )

    @property
    def rt60_mid(self) -> primitives.Float | None:
        """Time (in seconds) to decay 60db in mid-frequency band."""
        member = self.get_member("RT60Mid")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rt60_mid.setter
    def rt60_mid(self, value: primitives.Float) -> None:
        """Set the RT60Mid field value."""
        member = self.get_member("RT60Mid")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RT60Mid", fields.FieldFloat(value=value)
            )

    @property
    def high_frequency_damping(self) -> primitives.Float | None:
        """Frequency (Hz) at which the high-frequency T60 is half the middle-band's T60."""
        member = self.get_member("HighFrequencyDamping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_frequency_damping.setter
    def high_frequency_damping(self, value: primitives.Float) -> None:
        """Set the HighFrequencyDamping field value."""
        member = self.get_member("HighFrequencyDamping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighFrequencyDamping", fields.FieldFloat(value=value)
            )

    @property
    def eq1_frequency(self) -> primitives.Float | None:
        """Center frequency of second-order Regalia Mitra peaking equalizer section 1."""
        member = self.get_member("EQ1Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eq1_frequency.setter
    def eq1_frequency(self, value: primitives.Float) -> None:
        """Set the EQ1Frequency field value."""
        member = self.get_member("EQ1Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EQ1Frequency", fields.FieldFloat(value=value)
            )

    @property
    def eq1_level(self) -> primitives.Float | None:
        """Peak level in dB of second-order Regalia-Mitra peaking equalizer section 1"""
        member = self.get_member("EQ1Level")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eq1_level.setter
    def eq1_level(self, value: primitives.Float) -> None:
        """Set the EQ1Level field value."""
        member = self.get_member("EQ1Level")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EQ1Level", fields.FieldFloat(value=value)
            )

    @property
    def eq2_frequency(self) -> primitives.Float | None:
        """Center frequency of second-order Regalia Mitra peaking equalizer section 2."""
        member = self.get_member("EQ2Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eq2_frequency.setter
    def eq2_frequency(self, value: primitives.Float) -> None:
        """Set the EQ2Frequency field value."""
        member = self.get_member("EQ2Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EQ2Frequency", fields.FieldFloat(value=value)
            )

    @property
    def eq2_level(self) -> primitives.Float | None:
        """Peak level in dB of second-order Regalia-Mitra peaking equalizer section 2."""
        member = self.get_member("EQ2Level")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eq2_level.setter
    def eq2_level(self, value: primitives.Float) -> None:
        """Set the EQ2Level field value."""
        member = self.get_member("EQ2Level")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EQ2Level", fields.FieldFloat(value=value)
            )

    @property
    def mix(self) -> primitives.Float | None:
        """0 is all dry, 1 is all wet."""
        member = self.get_member("Mix")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mix.setter
    def mix(self, value: primitives.Float) -> None:
        """Set the Mix field value."""
        member = self.get_member("Mix")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mix", fields.FieldFloat(value=value)
            )

    @property
    def level(self) -> primitives.Float | None:
        """Output scale factor (in dB)."""
        member = self.get_member("Level")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @level.setter
    def level(self, value: primitives.Float) -> None:
        """Set the Level field value."""
        member = self.get_member("Level")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Level", fields.FieldFloat(value=value)
            )

    async def preset_off(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to not have an effect at all

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetOff", {}, debug,
        )

    async def preset_generic(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetGeneric", {}, debug,
        )

    async def preset_padded_cell(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetPaddedCell", {}, debug,
        )

    async def preset_room(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetRoom", {}, debug,
        )

    async def preset_bathroom(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetBathroom", {}, debug,
        )

    async def preset_livingroom(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetLivingroom", {}, debug,
        )

    async def preset_stoneroom(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetStoneroom", {}, debug,
        )

    async def preset_auditorium(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetAuditorium", {}, debug,
        )

    async def preset_concerthall(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetConcerthall", {}, debug,
        )

    async def preset_cave(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetCave", {}, debug,
        )

    async def preset_arena(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetArena", {}, debug,
        )

    async def preset_hangar(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetHangar", {}, debug,
        )

    async def preset_carpeted_hallway(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetCarpetedHallway", {}, debug,
        )

    async def preset_hallway(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetHallway", {}, debug,
        )

    async def preset_stone_corridor(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetStoneCorridor", {}, debug,
        )

    async def preset_alley(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetAlley", {}, debug,
        )

    async def preset_forest(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetForest", {}, debug,
        )

    async def preset_city(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetCity", {}, debug,
        )

    async def preset_mountains(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetMountains", {}, debug,
        )

    async def preset_quarry(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetQuarry", {}, debug,
        )

    async def preset_plain(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetPlain", {}, debug,
        )

    async def preset_parking_lot(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetParkingLot", {}, debug,
        )

    async def preset_sewer_pipe(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetSewerPipe", {}, debug,
        )

    async def preset_underwater(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetUnderwater", {}, debug,
        )

    async def preset_drugged(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetDrugged", {}, debug,
        )

    async def preset_dizzy(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetDizzy", {}, debug,
        )

    async def preset_psychotic(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Sets the values to a preset that replicates this button's name

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PresetPsychotic", {}, debug,
        )

