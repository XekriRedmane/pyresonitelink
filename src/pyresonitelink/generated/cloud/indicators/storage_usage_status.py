"""Generated component: StorageUsageStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StorageUsageStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Storage Usage Status is a component that is used to read how much storage a user has used, total, shared, and that has left to share.

    Category: Cloud/Indicators

    Can only be used in user space and your active cloud home.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StorageUsageStatus"

    def __init__(self, owner_id: primitives.String | None = None, group_member_quota: primitives.Bool | None = None, has_valid_data: primitives.Bool | None = None, storage_bytes: primitives.Long | None = None, full_storage_bytes: primitives.Long | None = None, shareable_storage_bytes: primitives.Long | None = None, shared_storage_bytes: primitives.Long | None = None, usage_bytes: primitives.Long | None = None, usage_ratio: primitives.Float | None = None, storage_string: primitives.String | None = None, full_storage_string: primitives.String | None = None, shareable_storage_string: primitives.String | None = None, shared_storage_string: primitives.String | None = None, usage_string: primitives.String | None = None, ratio_string: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            owner_id: Initial value for OwnerId.
            group_member_quota: Initial value for GroupMemberQuota.
            has_valid_data: Initial value for HasValidData.
            storage_bytes: Initial value for StorageBytes.
            full_storage_bytes: Initial value for FullStorageBytes.
            shareable_storage_bytes: Initial value for ShareableStorageBytes.
            shared_storage_bytes: Initial value for SharedStorageBytes.
            usage_bytes: Initial value for UsageBytes.
            usage_ratio: Initial value for UsageRatio.
            storage_string: Initial value for StorageString.
            full_storage_string: Initial value for FullStorageString.
            shareable_storage_string: Initial value for ShareableStorageString.
            shared_storage_string: Initial value for SharedStorageString.
            usage_string: Initial value for UsageString.
            ratio_string: Initial value for RatioString.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if owner_id is not None:
            self.owner_id = owner_id
        if group_member_quota is not None:
            self.group_member_quota = group_member_quota
        if has_valid_data is not None:
            self.has_valid_data = has_valid_data
        if storage_bytes is not None:
            self.storage_bytes = storage_bytes
        if full_storage_bytes is not None:
            self.full_storage_bytes = full_storage_bytes
        if shareable_storage_bytes is not None:
            self.shareable_storage_bytes = shareable_storage_bytes
        if shared_storage_bytes is not None:
            self.shared_storage_bytes = shared_storage_bytes
        if usage_bytes is not None:
            self.usage_bytes = usage_bytes
        if usage_ratio is not None:
            self.usage_ratio = usage_ratio
        if storage_string is not None:
            self.storage_string = storage_string
        if full_storage_string is not None:
            self.full_storage_string = full_storage_string
        if shareable_storage_string is not None:
            self.shareable_storage_string = shareable_storage_string
        if shared_storage_string is not None:
            self.shared_storage_string = shared_storage_string
        if usage_string is not None:
            self.usage_string = usage_string
        if ratio_string is not None:
            self.ratio_string = ratio_string

    @property
    def owner_id(self) -> primitives.String | None:
        """The id of the user this is reading data from"""
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
    def group_member_quota(self) -> primitives.Bool | None:
        """Whether to read group storage limits."""
        member = self.get_member("GroupMemberQuota")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_member_quota.setter
    def group_member_quota(self, value: primitives.Bool) -> None:
        """Set the GroupMemberQuota field value."""
        member = self.get_member("GroupMemberQuota")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupMemberQuota", fields.FieldBool(value=value)
            )

    @property
    def has_valid_data(self) -> primitives.Bool | None:
        """Whether this component has successfully grabbed the data."""
        member = self.get_member("HasValidData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_valid_data.setter
    def has_valid_data(self, value: primitives.Bool) -> None:
        """Set the HasValidData field value."""
        member = self.get_member("HasValidData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasValidData", fields.FieldBool(value=value)
            )

    @property
    def storage_bytes(self) -> primitives.Long | None:
        """how many bytes of storage ``OwnerId`` has total"""
        member = self.get_member("StorageBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @storage_bytes.setter
    def storage_bytes(self, value: primitives.Long) -> None:
        """Set the StorageBytes field value."""
        member = self.get_member("StorageBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StorageBytes", fields.FieldLong(value=value)
            )

    @property
    def full_storage_bytes(self) -> primitives.Long | None:
        """how many bytes of storage ``OwnerId`` has used currently."""
        member = self.get_member("FullStorageBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @full_storage_bytes.setter
    def full_storage_bytes(self, value: primitives.Long) -> None:
        """Set the FullStorageBytes field value."""
        member = self.get_member("FullStorageBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullStorageBytes", fields.FieldLong(value=value)
            )

    @property
    def shareable_storage_bytes(self) -> primitives.Long | None:
        """How many bytes of storage ``OwnerId`` currently has ready to share."""
        member = self.get_member("ShareableStorageBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shareable_storage_bytes.setter
    def shareable_storage_bytes(self, value: primitives.Long) -> None:
        """Set the ShareableStorageBytes field value."""
        member = self.get_member("ShareableStorageBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShareableStorageBytes", fields.FieldLong(value=value)
            )

    @property
    def shared_storage_bytes(self) -> primitives.Long | None:
        """How many bytes of storage ``OwnerId`` has shared with others currently."""
        member = self.get_member("SharedStorageBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shared_storage_bytes.setter
    def shared_storage_bytes(self, value: primitives.Long) -> None:
        """Set the SharedStorageBytes field value."""
        member = self.get_member("SharedStorageBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SharedStorageBytes", fields.FieldLong(value=value)
            )

    @property
    def usage_bytes(self) -> primitives.Long | None:
        """The total amount of bytes being used by ``OwnerId``."""
        member = self.get_member("UsageBytes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @usage_bytes.setter
    def usage_bytes(self, value: primitives.Long) -> None:
        """Set the UsageBytes field value."""
        member = self.get_member("UsageBytes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsageBytes", fields.FieldLong(value=value)
            )

    @property
    def usage_ratio(self) -> primitives.Float | None:
        """the percentage of how full ``OwnerId``'s storage is from 0->1"""
        member = self.get_member("UsageRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @usage_ratio.setter
    def usage_ratio(self, value: primitives.Float) -> None:
        """Set the UsageRatio field value."""
        member = self.get_member("UsageRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsageRatio", fields.FieldFloat(value=value)
            )

    @property
    def storage_string(self) -> primitives.String | None:
        """String version with nice formatting applied of how much storage ``OwnerId`` has."""
        member = self.get_member("StorageString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @storage_string.setter
    def storage_string(self, value: primitives.String) -> None:
        """Set the StorageString field value."""
        member = self.get_member("StorageString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StorageString", fields.FieldString(value=value)
            )

    @property
    def full_storage_string(self) -> primitives.String | None:
        """String version with nice formatting applied of"""
        member = self.get_member("FullStorageString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @full_storage_string.setter
    def full_storage_string(self, value: primitives.String) -> None:
        """Set the FullStorageString field value."""
        member = self.get_member("FullStorageString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullStorageString", fields.FieldString(value=value)
            )

    @property
    def shareable_storage_string(self) -> primitives.String | None:
        """String version with nice formatting applied of how much storage ``OwnerId`` has ready to share."""
        member = self.get_member("ShareableStorageString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shareable_storage_string.setter
    def shareable_storage_string(self, value: primitives.String) -> None:
        """Set the ShareableStorageString field value."""
        member = self.get_member("ShareableStorageString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShareableStorageString", fields.FieldString(value=value)
            )

    @property
    def shared_storage_string(self) -> primitives.String | None:
        """String version with nice formatting applied of how much storage ``OwnerId`` has shared with others."""
        member = self.get_member("SharedStorageString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shared_storage_string.setter
    def shared_storage_string(self, value: primitives.String) -> None:
        """Set the SharedStorageString field value."""
        member = self.get_member("SharedStorageString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SharedStorageString", fields.FieldString(value=value)
            )

    @property
    def usage_string(self) -> primitives.String | None:
        """String version with nice formatting applied of how much storage ``OwnerId`` has used."""
        member = self.get_member("UsageString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @usage_string.setter
    def usage_string(self, value: primitives.String) -> None:
        """Set the UsageString field value."""
        member = self.get_member("UsageString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsageString", fields.FieldString(value=value)
            )

    @property
    def ratio_string(self) -> primitives.String | None:
        """String version with nice formatting applied of how full ``OwnerId``'s storage is."""
        member = self.get_member("RatioString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ratio_string.setter
    def ratio_string(self, value: primitives.String) -> None:
        """Set the RatioString field value."""
        member = self.get_member("RatioString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RatioString", fields.FieldString(value=value)
            )

