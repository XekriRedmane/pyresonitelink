"""Generated component: DebugSettingSwitch."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent


class DebugSettingSwitch(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugSettingSwitch.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugSettingSwitch"

    def __init__(self, target_profile: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_profile: Initial value for TargetProfile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_profile is not None:
            self.target_profile = target_profile

    @property
    def target_profile(self) -> str | None:
        """The TargetProfile field value."""
        member = self.get_member("TargetProfile")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_profile.setter
    def target_profile(self, value: str) -> None:
        """Set the TargetProfile field value."""
        member = self.get_member("TargetProfile")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetProfile", fields.FieldString(value=value)
            )

