"""Generated component: LegacyFeatureSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class LegacyFeatureSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyFeatureSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyFeatureSettings"

    def __init__(self, use_legacy_grip_equip: primitives.Bool | None = None, use_legacy_world_switcher: primitives.Bool | None = None, use_legacy_inventory_session_shortcuts: primitives.Bool | None = None, suppress_feet_simulation: primitives.Bool | None = None, preserve_legacy_reverb_zone_handling: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_legacy_grip_equip: Initial value for UseLegacyGripEquip.
            use_legacy_world_switcher: Initial value for UseLegacyWorldSwitcher.
            use_legacy_inventory_session_shortcuts: Initial value for UseLegacyInventorySessionShortcuts.
            suppress_feet_simulation: Initial value for SuppressFeetSimulation.
            preserve_legacy_reverb_zone_handling: Initial value for PreserveLegacyReverbZoneHandling.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_legacy_grip_equip is not None:
            self.use_legacy_grip_equip = use_legacy_grip_equip
        if use_legacy_world_switcher is not None:
            self.use_legacy_world_switcher = use_legacy_world_switcher
        if use_legacy_inventory_session_shortcuts is not None:
            self.use_legacy_inventory_session_shortcuts = use_legacy_inventory_session_shortcuts
        if suppress_feet_simulation is not None:
            self.suppress_feet_simulation = suppress_feet_simulation
        if preserve_legacy_reverb_zone_handling is not None:
            self.preserve_legacy_reverb_zone_handling = preserve_legacy_reverb_zone_handling

    @property
    def use_legacy_grip_equip(self) -> primitives.Bool | None:
        """The UseLegacyGripEquip field value."""
        member = self.get_member("UseLegacyGripEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_legacy_grip_equip.setter
    def use_legacy_grip_equip(self, value: primitives.Bool) -> None:
        """Set the UseLegacyGripEquip field value."""
        member = self.get_member("UseLegacyGripEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLegacyGripEquip", fields.FieldBool(value=value)
            )

    @property
    def use_legacy_world_switcher(self) -> primitives.Bool | None:
        """The UseLegacyWorldSwitcher field value."""
        member = self.get_member("UseLegacyWorldSwitcher")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_legacy_world_switcher.setter
    def use_legacy_world_switcher(self, value: primitives.Bool) -> None:
        """Set the UseLegacyWorldSwitcher field value."""
        member = self.get_member("UseLegacyWorldSwitcher")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLegacyWorldSwitcher", fields.FieldBool(value=value)
            )

    @property
    def use_legacy_inventory_session_shortcuts(self) -> primitives.Bool | None:
        """The UseLegacyInventorySessionShortcuts field value."""
        member = self.get_member("UseLegacyInventorySessionShortcuts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_legacy_inventory_session_shortcuts.setter
    def use_legacy_inventory_session_shortcuts(self, value: primitives.Bool) -> None:
        """Set the UseLegacyInventorySessionShortcuts field value."""
        member = self.get_member("UseLegacyInventorySessionShortcuts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLegacyInventorySessionShortcuts", fields.FieldBool(value=value)
            )

    @property
    def suppress_feet_simulation(self) -> primitives.Bool | None:
        """The SuppressFeetSimulation field value."""
        member = self.get_member("SuppressFeetSimulation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @suppress_feet_simulation.setter
    def suppress_feet_simulation(self, value: primitives.Bool) -> None:
        """Set the SuppressFeetSimulation field value."""
        member = self.get_member("SuppressFeetSimulation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SuppressFeetSimulation", fields.FieldBool(value=value)
            )

    @property
    def preserve_legacy_reverb_zone_handling(self) -> primitives.Bool | None:
        """The PreserveLegacyReverbZoneHandling field value."""
        member = self.get_member("PreserveLegacyReverbZoneHandling")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_legacy_reverb_zone_handling.setter
    def preserve_legacy_reverb_zone_handling(self, value: primitives.Bool) -> None:
        """Set the PreserveLegacyReverbZoneHandling field value."""
        member = self.get_member("PreserveLegacyReverbZoneHandling")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveLegacyReverbZoneHandling", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

