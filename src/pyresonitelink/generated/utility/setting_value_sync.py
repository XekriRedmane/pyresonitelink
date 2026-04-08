"""Generated component: SettingValueSync."""

from typing import Any

T = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SettingValueSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SettingValueSync<,>.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SettingValueSync<,>"

    def __init__(self, setting_name: str | None = None, target_field: str | IField[T] | None = None, subsetting_getter: str | None = None, subsetting_key: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            setting_name: Initial value for SettingName.
            target_field: Initial value for TargetField.
            subsetting_getter: Initial value for SubsettingGetter.
            subsetting_key: Initial value for SubsettingKey.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if setting_name is not None:
            self.setting_name = setting_name
        if target_field is not None:
            self.target_field = target_field
        if subsetting_getter is not None:
            self.subsetting_getter = subsetting_getter
        if subsetting_key is not None:
            self.subsetting_key = subsetting_key

    @property
    def syncing_user(self) -> members.SyncObject | None:
        """The SyncingUser member."""
        member = self.get_member("SyncingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @syncing_user.setter
    def syncing_user(self, value: members.SyncObject) -> None:
        """Set the SyncingUser member."""
        self.set_member("SyncingUser", value)

    @property
    def setting_name(self) -> str | None:
        """The SettingName field value."""
        member = self.get_member("SettingName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setting_name.setter
    def setting_name(self, value: str) -> None:
        """Set the SettingName field value."""
        member = self.get_member("SettingName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SettingName", fields.FieldString(value=value)
            )

    @property
    def target_field(self) -> str | None:
        """Target ID of the TargetField reference (targets IField[T])."""
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField[T] | None) -> None:
        """Set the TargetField reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def subsetting_getter(self) -> str | None:
        """The SubsettingGetter field value."""
        member = self.get_member("SubsettingGetter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsetting_getter.setter
    def subsetting_getter(self, value: str) -> None:
        """Set the SubsettingGetter field value."""
        member = self.get_member("SubsettingGetter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsettingGetter", fields.FieldString(value=value)
            )

    @property
    def subsetting_key(self) -> str | None:
        """The SubsettingKey field value."""
        member = self.get_member("SubsettingKey")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsetting_key.setter
    def subsetting_key(self, value: str) -> None:
        """Set the SubsettingKey field value."""
        member = self.get_member("SubsettingKey")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsettingKey", fields.FieldString(value=value)
            )

