"""Generated component: MysterySettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class MysterySettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.MysterySettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MysterySettings"

    def __init__(self, loooong: bool | None = None, the_truth: bool | None = None, mirror_mirrors: bool | None = None, phantom_sense: bool | None = None, expressiveness: np.float32 | None = None, ghosts: bool | None = None, more_fps: bool | None = None, precious_toggle: bool | None = None, toggle_toggle: bool | None = None, toggle_toggle_toggle: bool | None = None, toggle_toggle_toggle_toggle: bool | None = None, toggle_toggle_toggle_toggle_toggle: bool | None = None, toggle_toggle_toggle_toggle_toggle_toggle: bool | None = None, toggle_toggle_toggle_toggle_toggle_toggle_toggle: bool | None = None, toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle: bool | None = None, precious_toggle_start: str | None = None, precious_toggle_duration: str | None = None, mysterious_message: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
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
    def difficulty(self) -> members.FieldEnum | None:
        """The Difficulty member."""
        member = self.get_member("Difficulty")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @difficulty.setter
    def difficulty(self, value: members.FieldEnum) -> None:
        """Set the Difficulty member."""
        self.set_member("Difficulty", value)

    @property
    def loooong(self) -> bool | None:
        """The Loooong field value."""
        member = self.get_member("Loooong")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @loooong.setter
    def loooong(self, value: bool) -> None:
        """Set the Loooong field value."""
        member = self.get_member("Loooong")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Loooong", fields.FieldBool(value=value)
            )

    @property
    def the_truth(self) -> bool | None:
        """The TheTruth field value."""
        member = self.get_member("TheTruth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @the_truth.setter
    def the_truth(self, value: bool) -> None:
        """Set the TheTruth field value."""
        member = self.get_member("TheTruth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TheTruth", fields.FieldBool(value=value)
            )

    @property
    def mirror_mirrors(self) -> bool | None:
        """The MirrorMirrors field value."""
        member = self.get_member("MirrorMirrors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mirror_mirrors.setter
    def mirror_mirrors(self, value: bool) -> None:
        """Set the MirrorMirrors field value."""
        member = self.get_member("MirrorMirrors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MirrorMirrors", fields.FieldBool(value=value)
            )

    @property
    def phantom_sense(self) -> bool | None:
        """The PhantomSense field value."""
        member = self.get_member("PhantomSense")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @phantom_sense.setter
    def phantom_sense(self, value: bool) -> None:
        """Set the PhantomSense field value."""
        member = self.get_member("PhantomSense")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PhantomSense", fields.FieldBool(value=value)
            )

    @property
    def expressiveness(self) -> np.float32 | None:
        """The Expressiveness field value."""
        member = self.get_member("Expressiveness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expressiveness.setter
    def expressiveness(self, value: np.float32) -> None:
        """Set the Expressiveness field value."""
        member = self.get_member("Expressiveness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Expressiveness", fields.FieldFloat(value=value)
            )

    @property
    def ghosts(self) -> bool | None:
        """The Ghosts field value."""
        member = self.get_member("Ghosts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ghosts.setter
    def ghosts(self, value: bool) -> None:
        """Set the Ghosts field value."""
        member = self.get_member("Ghosts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Ghosts", fields.FieldBool(value=value)
            )

    @property
    def more_fps(self) -> bool | None:
        """The MoreFPS field value."""
        member = self.get_member("MoreFPS")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @more_fps.setter
    def more_fps(self, value: bool) -> None:
        """Set the MoreFPS field value."""
        member = self.get_member("MoreFPS")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MoreFPS", fields.FieldBool(value=value)
            )

    @property
    def precious_toggle(self) -> bool | None:
        """The PreciousToggle field value."""
        member = self.get_member("PreciousToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @precious_toggle.setter
    def precious_toggle(self, value: bool) -> None:
        """Set the PreciousToggle field value."""
        member = self.get_member("PreciousToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreciousToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle(self) -> bool | None:
        """The ToggleToggle field value."""
        member = self.get_member("ToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle.setter
    def toggle_toggle(self, value: bool) -> None:
        """Set the ToggleToggle field value."""
        member = self.get_member("ToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle(self) -> bool | None:
        """The ToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle.setter
    def toggle_toggle_toggle(self, value: bool) -> None:
        """Set the ToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle(self) -> bool | None:
        """The ToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle(self, value: bool) -> None:
        """Set the ToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle(self) -> bool | None:
        """The ToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle(self, value: bool) -> None:
        """Set the ToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle_toggle(self) -> bool | None:
        """The ToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle_toggle(self, value: bool) -> None:
        """Set the ToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle(self) -> bool | None:
        """The ToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle(self, value: bool) -> None:
        """Set the ToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ToggleToggleToggleToggleToggleToggleToggle", fields.FieldBool(value=value)
            )

    @property
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle(self) -> bool | None:
        """The ToggleToggleToggleToggleToggleToggleToggleToggle field value."""
        member = self.get_member("ToggleToggleToggleToggleToggleToggleToggleToggle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle.setter
    def toggle_toggle_toggle_toggle_toggle_toggle_toggle_toggle(self, value: bool) -> None:
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
        """The PreciousToggleDuration field value."""
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
    def mysterious_message(self) -> str | None:
        """The MysteriousMessage field value."""
        member = self.get_member("MysteriousMessage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mysterious_message.setter
    def mysterious_message(self, value: str) -> None:
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

