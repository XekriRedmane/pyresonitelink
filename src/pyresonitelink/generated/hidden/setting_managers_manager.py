"""Generated component: SettingManagersManager."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent

if TYPE_CHECKING:
    from pyresonitelink.generated.hidden.setting_manager import SettingManager
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SettingManagersManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Setting Managers Manager component is used to manage the changing from cloud to local setting sets.

    Category: Hidden
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
        """The manager handling locally stored settings."""
        member = self.get_member("LocalSettings")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_settings.setter
    def local_settings(self, target: str | SettingManager | None) -> None:
        """Set the LocalSettings reference by target ID or SettingManager instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """The manager handling cloud stored settings."""
        member = self.get_member("CloudSettings")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cloud_settings.setter
    def cloud_settings(self, target: str | SettingManager | None) -> None:
        """Set the CloudSettings reference by target ID or SettingManager instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("CloudSettings")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CloudSettings",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SettingManager'),
            )

