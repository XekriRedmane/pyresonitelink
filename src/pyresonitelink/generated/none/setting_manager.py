"""Generated component: SettingManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.setting_manager import SettingManager
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SettingManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Setting Manager component is internally used by the settings system to handle settings changes.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SettingManager"

    def __init__(self, owner_id: primitives.String | None = None, supressed_by: str | SettingManager | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            owner_id: Initial value for OwnerId.
            supressed_by: Initial value for SupressedBy.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if owner_id is not None:
            self.owner_id = owner_id
        if supressed_by is not None:
            self.supressed_by = supressed_by

    @property
    def owner_id(self) -> primitives.String | None:
        """The owner of the settings that this manages."""
        member = self.get_member("OwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @owner_id.setter
    def owner_id(self, value: primitives.String) -> None:
        """Set the OwnerId field value."""
        member = self.get_member("OwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OwnerId", fields.FieldString(value=value)
            )

    @property
    def supressed_by(self) -> str | None:
        """Whether changes in this are suppressed by another setting manager."""
        member = self.get_member("SupressedBy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @supressed_by.setter
    def supressed_by(self, target: str | SettingManager | None) -> None:
        """Set the SupressedBy reference by target ID or SettingManager instance."""
        target_id: str | None = target.id if isinstance(target, SettingManager) else target  # type: ignore[assignment]
        member = self.get_member("SupressedBy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SupressedBy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SettingManager'),
            )

