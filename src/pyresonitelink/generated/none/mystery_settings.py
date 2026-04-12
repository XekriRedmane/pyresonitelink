"""Generated component: MysterySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.resonite_difficulty import ResoniteDifficulty
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class MysterySettings(GeneratedComponent, ICustomInspector):
    """The Mystery Settings component is a component that is enabled on April 1st, which contains multiple settings that add joke behaviour to Resonite. The component was added in the April Fools update 2025.4.1.438.

    Part of the Settings UI. It shows up during April Fools under the 'Misc'
    category. MysterySettingsDash.png
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MysterySettings"

    def __init__(self, difficulty: ResoniteDifficulty | str | None = None, loooong: primitives.Bool | None = None, the_truth: primitives.Bool | None = None, mirror_mirrors: primitives.Bool | None = None, phantom_sense: primitives.Bool | None = None, expressiveness: primitives.Float | None = None, ghosts: primitives.Bool | None = None, more_fps: primitives.Bool | None = None, precious_toggle: primitives.Bool | None = None, toggle_toggle: primitives.Bool | None = None, toggle_toggle_toggle: primitives.Bool | None = None, toggle_toggle_toggle_toggle: primitives.Bool | None = None, toggle_toggle_toggle_toggle_toggle: primitives.Bool | None = None, toggle_toggle_toggle_toggle_toggle_toggle: primitives.Bool | None = None, toggle_toggle_toggle_toggle_toggle_toggle_toggle: primitives.Bool | None = None, toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle: primitives.Bool | None = None, precious_toggle_start: str | None = None, precious_toggle_duration: str | None = None, mysterious_message: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            difficulty: Initial value for Difficulty.
            loooong: Initial value for Loooong.
            the_truth: Initial value for TheTruth.
            mirror_mirrors: Initial value for MirrorMirrors.
            phantom_sense: Initial value for PhantomSense.
            expressiveness: Initial value for Expressiveness.
            ghosts: Initial value for Ghosts.
            more_fps: Initial value for MoreFPS.
            precious_toggle: Initial value for PreciousToggle.
            toggle_toggle: Initial value for ToggleToggle.
            toggle_toggle_toggle: Initial value for ToggleToggleToggle.
            toggle_toggle_toggle_toggle: Initial value for ToggleToggleToggleToggle.
            toggle_toggle_toggle_toggle_toggle: Initial value for ToggleToggleToggleToggleToggle.
            toggle_toggle_toggle_toggle_toggle_toggle: Initial value for ToggleToggleToggleToggleToggleToggle.
            toggle_toggle_toggle_toggle_toggle_toggle_toggle: Initial value for ToggleToggleToggleToggleToggleToggleToggle.
            toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle: Initial value for ToggleToggleToggleToggleToggleToggleToggleToggle.
            precious_toggle_start: Initial value for PreciousToggleStart.
            precious_toggle_duration: Initial value for PreciousToggleDuration.
            mysterious_message: Initial value for MysteriousMessage.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if difficulty is not None:
            self.difficulty = difficulty
        if loooong is not None:
            self.loooong = loooong
        if the_truth is not None:
            self.the_truth = the_truth
        if mirror_mirrors is not None:
            self.mirror_mirrors = mirror_mirrors
        if phantom_sense is not None:
            self.phantom_sense = phantom_sense
        if expressiveness is not None:
            self.expressiveness = expressiveness
        if ghosts is not None:
            self.ghosts = ghosts
        if more_fps is not None:
            self.more_fps = more_fps
        if precious_toggle is not None:
            self.precious_toggle = precious_toggle
        if toggle_toggle is not None:
            self.toggle_toggle = toggle_toggle
        if toggle_toggle_toggle is not None:
            self.toggle_toggle_toggle = toggle_toggle_toggle
        if toggle_toggle_toggle_toggle is not None:
            self.toggle_toggle_toggle_toggle = toggle_toggle_toggle_toggle
        if toggle_toggle_toggle_toggle_toggle is not None:
            self.toggle_toggle_toggle_toggle_toggle = toggle_toggle_toggle_toggle_toggle
        if toggle_toggle_toggle_toggle_toggle_toggle is not None:
            self.toggle_toggle_toggle_toggle_toggle_toggle = toggle_toggle_toggle_toggle_toggle_toggle
        if toggle_toggle_toggle_toggle_toggle_toggle_toggle is not None:
            self.toggle_toggle_toggle_toggle_toggle_toggle_toggle = toggle_toggle_toggle_toggle_toggle_toggle_toggle
        if toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle is not None:
            self.toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle = toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle
        if precious_toggle_start is not None:
            self.precious_toggle_start = precious_toggle_start
        if precious_toggle_duration is not None:
            self.precious_toggle_duration = precious_toggle_duration
        if mysterious_message is not None:
            self.mysterious_message = mysterious_message

    @property
    def difficulty(self) -> ResoniteDifficulty | None:
        """This controls Resonite gameplay difficulty. If you want more challenge when playing Resonite, you can turn on the Hard difficulty."""
        member = self.get_member("Difficulty")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ResoniteDifficulty(member.value)
        return None

    @difficulty.setter
    def difficulty(self, value: ResoniteDifficulty | str) -> None:
        """Set Difficulty. This controls Resonite gameplay difficulty. If you want more challenge when playing Resonite, you can turn on the Hard difficulty."""
        member = self.get_member("Difficulty")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Difficulty",
                members.FieldEnum(value=str(value)),
            )

    @property
    def loooong(self) -> primitives.Bool | None:
        """The Loooong field value."""
        member = self.get_member("Loooong")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @loooong.setter
    def loooong(self, value: primitives.Bool) -> None:
        """Set the Loooong field value."""
        member = self.get_member("Loooong")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Loooong", fields.FieldBool(value=value)
            )

    @property
    def the_truth(self) -> primitives.Bool | None:
        """The TheTruth field value."""
        member = self.get_member("TheTruth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @the_truth.setter
    def the_truth(self, value: primitives.Bool) -> None:
        """Set the TheTruth field value."""
        member = self.get_member("TheTruth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TheTruth", fields.FieldBool(value=value)
            )

    @property
    def mirror_mirrors(self) -> primitives.Bool | None:
        """When enabled, mirrors are mirrored, so when mirrors mirror the mirroring cancels out and mirrors just become rorrs."""
        member = self.get_member("MirrorMirrors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mirror_mirrors.setter
    def mirror_mirrors(self, value: primitives.Bool) -> None:
        """Set the MirrorMirrors field value."""
        member = self.get_member("MirrorMirrors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MirrorMirrors", fields.FieldBool(value=value)
            )

    @property
    def phantom_sense(self) -> primitives.Bool | None:
        """The PhantomSense field value."""
        member = self.get_member("PhantomSense")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @phantom_sense.setter
    def phantom_sense(self, value: primitives.Bool) -> None:
        """Set the PhantomSense field value."""
        member = self.get_member("PhantomSense")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PhantomSense", fields.FieldBool(value=value)
            )

    @property
    def expressiveness(self) -> primitives.Float | None:
        """The Expressiveness field value."""
        member = self.get_member("Expressiveness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expressiveness.setter
    def expressiveness(self, value: primitives.Float) -> None:
        """Set the Expressiveness field value."""
        member = self.get_member("Expressiveness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Expressiveness", fields.FieldFloat(value=value)
            )

    @property
    def ghosts(self) -> primitives.Bool | None:
        """The Ghosts field value."""
        member = self.get_member("Ghosts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ghosts.setter
    def ghosts(self, value: primitives.Bool) -> None:
        """Set the Ghosts field value."""
        member = self.get_member("Ghosts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Ghosts", fields.FieldBool(value=value)
            )

    @property
    def more_fps(self) -> primitives.Bool | None:
        """The MoreFPS field value."""
        member = self.get_member("MoreFPS")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @more_fps.setter
    def more_fps(self, value: primitives.Bool) -> None:
        """Set the MoreFPS field value."""
        member = self.get_member("MoreFPS")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MoreFPS", fields.FieldBool(value=value)
            )

    @property
    def precious_toggle(self) -> primitives.Bool | None:
        """The PreciousToggle field value."""
        member = self.get_member("PreciousToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @precious_toggle.setter
    def precious_toggle(self, value: primitives.Bool) -> None:
        """Set the PreciousToggle field value."""
        member = self.get_member("PreciousToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreciousToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle(self) -> primitives.Bool | None:
        """The ToggleToggle field value."""
        member = self.get_member("ToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle.setter
    def toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggle field value."""
        member = self.get_member("ToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle(self) -> primitives.Bool | None:
        """The ToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle.setter
    def toggle_toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle(self) -> primitives.Bool | None:
        """The ToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle(self) -> primitives.Bool | None:
        """Toggled Toggle for Toggle: The toggles keep on toggling toggles ToggleToggleToggleToggleToggleToggle Bool 'Toggle Toggle Toggle Toggle Toggle': When toggles of toggles of toggles are toggled you'll be able to toggle this toggle so you can toggle more toggles. ToggleToggleToggleToggleToggleToggleToggle Bool Penultimate Toggle:"""
        member = self.get_member("ToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle_toggle(self) -> primitives.Bool | None:
        """The ToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle(self) -> primitives.Bool | None:
        """The ToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle(self) -> primitives.Bool | None:
        """The ToggleToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle(self, value: primitives.Bool) -> None:
        """Set the ToggleToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def precious_toggle_start(self) -> str | None:
        """The PreciousToggleStart field value."""
        member = self.get_member("PreciousToggleStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @precious_toggle_start.setter
    def precious_toggle_start(self, value: str) -> None:
        """Set the PreciousToggleStart field value."""
        member = self.get_member("PreciousToggleStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreciousToggleStart", fields.FieldNullableDateTime(value=value)
            )

    @property
    def precious_toggle_duration(self) -> str | None:
        """How long the previous precious little toggle was held."""
        member = self.get_member("PreciousToggleDuration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @precious_toggle_duration.setter
    def precious_toggle_duration(self, value: str) -> None:
        """Set the PreciousToggleDuration field value."""
        member = self.get_member("PreciousToggleDuration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreciousToggleDuration", fields.FieldNullableTimeSpan(value=value)
            )

    @property
    def mysterious_message(self) -> primitives.String | None:
        """Message for posterity: Something will appear here at some point."""
        member = self.get_member("MysteriousMessage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mysterious_message.setter
    def mysterious_message(self, value: primitives.String) -> None:
        """Set the MysteriousMessage field value."""
        member = self.get_member("MysteriousMessage")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MysteriousMessage", fields.FieldString(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

