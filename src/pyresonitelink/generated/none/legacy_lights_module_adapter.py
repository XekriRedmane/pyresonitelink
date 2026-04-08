"""Generated component: LegacyLightsModuleAdapter."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyLightsModuleAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.LegacyLightsModuleAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyLightsModuleAdapter"

    def __init__(self, legacy_light: str | Light | None = None, reference_light: str | Light | None = None, lights_module_enabled: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            legacy_light: Initial value for LegacyLight.
            reference_light: Initial value for ReferenceLight.
            lights_module_enabled: Initial value for LightsModuleEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if legacy_light is not None:
            self.legacy_light = legacy_light
        if reference_light is not None:
            self.reference_light = reference_light
        if lights_module_enabled is not None:
            self.lights_module_enabled = lights_module_enabled

    @property
    def legacy_light(self) -> str | None:
        """Target ID of the LegacyLight reference (targets Light)."""
        member = self.get_member("LegacyLight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_light.setter
    def legacy_light(self, target: str | Light | None) -> None:
        """Set the LegacyLight reference by target ID or Light instance."""
        target_id: str | None = target.id if isinstance(target, Light) else target  # type: ignore[assignment]
        member = self.get_member("LegacyLight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LegacyLight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Light'),
            )

    @property
    def reference_light(self) -> str | None:
        """Target ID of the ReferenceLight reference (targets Light)."""
        member = self.get_member("ReferenceLight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference_light.setter
    def reference_light(self, target: str | Light | None) -> None:
        """Set the ReferenceLight reference by target ID or Light instance."""
        target_id: str | None = target.id if isinstance(target, Light) else target  # type: ignore[assignment]
        member = self.get_member("ReferenceLight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReferenceLight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Light'),
            )

    @property
    def lights_module_enabled(self) -> str | None:
        """Target ID of the LightsModuleEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("LightsModuleEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lights_module_enabled.setter
    def lights_module_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the LightsModuleEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LightsModuleEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LightsModuleEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

