"""Generated component: LegacyCloudStorageSpaceIndicator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.storage_usage_status import StorageUsageStatus
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.legacy_progress_bar import LegacyProgressBar
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyCloudStorageSpaceIndicator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyCloudStorageSpaceIndicator.

    Category: Cloud
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyCloudStorageSpaceIndicator"

    def __init__(self, source: str | StorageUsageStatus | None = None, container_color: primitives.ColorX | None = None, used_color: primitives.ColorX | None = None, low_space_color: primitives.ColorX | None = None, critical_space_color: primitives.ColorX | None = None, low_space_threshold: primitives.Float | None = None, critical_space_threshold: primitives.Float | None = None, owner_label: str | TextRenderer | None = None, usage_label: str | TextRenderer | None = None, percent_label: str | TextRenderer | None = None, progress_bar: str | LegacyProgressBar | None = None, legacy_owner_id: primitives.String | None = None, legacy_member_quota: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            container_color: Initial value for ContainerColor.
            used_color: Initial value for UsedColor.
            low_space_color: Initial value for LowSpaceColor.
            critical_space_color: Initial value for CriticalSpaceColor.
            low_space_threshold: Initial value for LowSpaceThreshold.
            critical_space_threshold: Initial value for CriticalSpaceThreshold.
            owner_label: Initial value for _ownerLabel.
            usage_label: Initial value for _usageLabel.
            percent_label: Initial value for _percentLabel.
            progress_bar: Initial value for _progressBar.
            legacy_owner_id: Initial value for __legacyOwnerId.
            legacy_member_quota: Initial value for __legacyMemberQuota.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if container_color is not None:
            self.container_color = container_color
        if used_color is not None:
            self.used_color = used_color
        if low_space_color is not None:
            self.low_space_color = low_space_color
        if critical_space_color is not None:
            self.critical_space_color = critical_space_color
        if low_space_threshold is not None:
            self.low_space_threshold = low_space_threshold
        if critical_space_threshold is not None:
            self.critical_space_threshold = critical_space_threshold
        if owner_label is not None:
            self.owner_label = owner_label
        if usage_label is not None:
            self.usage_label = usage_label
        if percent_label is not None:
            self.percent_label = percent_label
        if progress_bar is not None:
            self.progress_bar = progress_bar
        if legacy_owner_id is not None:
            self.legacy_owner_id = legacy_owner_id
        if legacy_member_quota is not None:
            self.legacy_member_quota = legacy_member_quota

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets StorageUsageStatus)."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | StorageUsageStatus | None) -> None:
        """Set the Source reference by target ID or StorageUsageStatus instance."""
        target_id: str | None = target.id if isinstance(target, StorageUsageStatus) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StorageUsageStatus'),
            )

    @property
    def container_color(self) -> primitives.ColorX | None:
        """The ContainerColor field value."""
        member = self.get_member("ContainerColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @container_color.setter
    def container_color(self, value: primitives.ColorX) -> None:
        """Set the ContainerColor field value."""
        member = self.get_member("ContainerColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ContainerColor", fields.FieldColorX(value=value)
            )

    @property
    def used_color(self) -> primitives.ColorX | None:
        """The UsedColor field value."""
        member = self.get_member("UsedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @used_color.setter
    def used_color(self, value: primitives.ColorX) -> None:
        """Set the UsedColor field value."""
        member = self.get_member("UsedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsedColor", fields.FieldColorX(value=value)
            )

    @property
    def low_space_color(self) -> primitives.ColorX | None:
        """The LowSpaceColor field value."""
        member = self.get_member("LowSpaceColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @low_space_color.setter
    def low_space_color(self, value: primitives.ColorX) -> None:
        """Set the LowSpaceColor field value."""
        member = self.get_member("LowSpaceColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowSpaceColor", fields.FieldColorX(value=value)
            )

    @property
    def critical_space_color(self) -> primitives.ColorX | None:
        """The CriticalSpaceColor field value."""
        member = self.get_member("CriticalSpaceColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @critical_space_color.setter
    def critical_space_color(self, value: primitives.ColorX) -> None:
        """Set the CriticalSpaceColor field value."""
        member = self.get_member("CriticalSpaceColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CriticalSpaceColor", fields.FieldColorX(value=value)
            )

    @property
    def low_space_threshold(self) -> primitives.Float | None:
        """The LowSpaceThreshold field value."""
        member = self.get_member("LowSpaceThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @low_space_threshold.setter
    def low_space_threshold(self, value: primitives.Float) -> None:
        """Set the LowSpaceThreshold field value."""
        member = self.get_member("LowSpaceThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LowSpaceThreshold", fields.FieldFloat(value=value)
            )

    @property
    def critical_space_threshold(self) -> primitives.Float | None:
        """The CriticalSpaceThreshold field value."""
        member = self.get_member("CriticalSpaceThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @critical_space_threshold.setter
    def critical_space_threshold(self, value: primitives.Float) -> None:
        """Set the CriticalSpaceThreshold field value."""
        member = self.get_member("CriticalSpaceThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CriticalSpaceThreshold", fields.FieldFloat(value=value)
            )

    @property
    def owner_label(self) -> str | None:
        """Target ID of the _ownerLabel reference (targets TextRenderer)."""
        member = self.get_member("_ownerLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @owner_label.setter
    def owner_label(self, target: str | TextRenderer | None) -> None:
        """Set the _ownerLabel reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_ownerLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_ownerLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def usage_label(self) -> str | None:
        """Target ID of the _usageLabel reference (targets TextRenderer)."""
        member = self.get_member("_usageLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @usage_label.setter
    def usage_label(self, target: str | TextRenderer | None) -> None:
        """Set the _usageLabel reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_usageLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_usageLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def percent_label(self) -> str | None:
        """Target ID of the _percentLabel reference (targets TextRenderer)."""
        member = self.get_member("_percentLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @percent_label.setter
    def percent_label(self, target: str | TextRenderer | None) -> None:
        """Set the _percentLabel reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_percentLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_percentLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def progress_bar(self) -> str | None:
        """Target ID of the _progressBar reference (targets LegacyProgressBar)."""
        member = self.get_member("_progressBar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress_bar.setter
    def progress_bar(self, target: str | LegacyProgressBar | None) -> None:
        """Set the _progressBar reference by target ID or LegacyProgressBar instance."""
        target_id: str | None = target.id if isinstance(target, LegacyProgressBar) else target  # type: ignore[assignment]
        member = self.get_member("_progressBar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_progressBar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyProgressBar'),
            )

    @property
    def legacy_owner_id(self) -> primitives.String | None:
        """The __legacyOwnerId field value."""
        member = self.get_member("__legacyOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_owner_id.setter
    def legacy_owner_id(self, value: primitives.String) -> None:
        """Set the __legacyOwnerId field value."""
        member = self.get_member("__legacyOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyOwnerId", fields.FieldString(value=value)
            )

    @property
    def legacy_member_quota(self) -> primitives.Bool | None:
        """The __legacyMemberQuota field value."""
        member = self.get_member("__legacyMemberQuota")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_member_quota.setter
    def legacy_member_quota(self, value: primitives.Bool) -> None:
        """Set the __legacyMemberQuota field value."""
        member = self.get_member("__legacyMemberQuota")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyMemberQuota", fields.FieldBool(value=value)
            )

