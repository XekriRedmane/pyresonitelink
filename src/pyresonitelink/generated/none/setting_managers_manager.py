"""Generated component: SettingManagersManager."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.setting_manager import SettingManager
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SettingManagersManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SettingManagersManager.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SettingManagersManager"

    def __init__(self, local_settings: str | SettingManager | None = None, cloud_settings: str | SettingManager | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            local_settings: Initial value for LocalSettings.
            cloud_settings: Initial value for CloudSettings.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if local_settings is not None:
            self.local_settings = local_settings
        if cloud_settings is not None:
            self.cloud_settings = cloud_settings

    @property
    def local_settings(self) -> str | None:
        """Target ID of the LocalSettings reference (targets SettingManager)."""
        member = self.get_member("LocalSettings")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_settings.setter
    def local_settings(self, target: str | SettingManager | None) -> None:
        """Set the LocalSettings reference by target ID or SettingManager instance."""
        target_id: str | None = target.id if isinstance(target, SettingManager) else target  # type: ignore[assignment]
        member = self.get_member("LocalSettings")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalSettings",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SettingManager'),
            )

    @property
    def cloud_settings(self) -> str | None:
        """Target ID of the CloudSettings reference (targets SettingManager)."""
        member = self.get_member("CloudSettings")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cloud_settings.setter
    def cloud_settings(self, target: str | SettingManager | None) -> None:
        """Set the CloudSettings reference by target ID or SettingManager instance."""
        target_id: str | None = target.id if isinstance(target, SettingManager) else target  # type: ignore[assignment]
        member = self.get_member("CloudSettings")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CloudSettings",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SettingManager'),
            )

