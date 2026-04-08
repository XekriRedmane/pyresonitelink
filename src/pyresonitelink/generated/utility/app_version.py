"""Generated component: AppVersion."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AppVersion(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AppVersion.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AppVersion"

    def __init__(self, version_number: str | None = None, version_name: str | None = None, full_version_string: str | None = None, build_year: np.int32 | None = None, build_month: np.int32 | None = None, build_day: np.int32 | None = None, build_time_of_day: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            version_number: Initial value for VersionNumber.
            version_name: Initial value for VersionName.
            full_version_string: Initial value for FullVersionString.
            build_year: Initial value for BuildYear.
            build_month: Initial value for BuildMonth.
            build_day: Initial value for BuildDay.
            build_time_of_day: Initial value for BuildTimeOfDay.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if version_number is not None:
            self.version_number = version_number
        if version_name is not None:
            self.version_name = version_name
        if full_version_string is not None:
            self.full_version_string = full_version_string
        if build_year is not None:
            self.build_year = build_year
        if build_month is not None:
            self.build_month = build_month
        if build_day is not None:
            self.build_day = build_day
        if build_time_of_day is not None:
            self.build_time_of_day = build_time_of_day

    @property
    def version_number(self) -> str | None:
        """The VersionNumber field value."""
        member = self.get_member("VersionNumber")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @version_number.setter
    def version_number(self, value: str) -> None:
        """Set the VersionNumber field value."""
        member = self.get_member("VersionNumber")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VersionNumber", fields.FieldString(value=value)
            )

    @property
    def version_name(self) -> str | None:
        """The VersionName field value."""
        member = self.get_member("VersionName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @version_name.setter
    def version_name(self, value: str) -> None:
        """Set the VersionName field value."""
        member = self.get_member("VersionName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VersionName", fields.FieldString(value=value)
            )

    @property
    def full_version_string(self) -> str | None:
        """The FullVersionString field value."""
        member = self.get_member("FullVersionString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @full_version_string.setter
    def full_version_string(self, value: str) -> None:
        """Set the FullVersionString field value."""
        member = self.get_member("FullVersionString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullVersionString", fields.FieldString(value=value)
            )

    @property
    def build_year(self) -> np.int32 | None:
        """The BuildYear field value."""
        member = self.get_member("BuildYear")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_year.setter
    def build_year(self, value: np.int32) -> None:
        """Set the BuildYear field value."""
        member = self.get_member("BuildYear")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildYear", fields.FieldInt(value=value)
            )

    @property
    def build_month(self) -> np.int32 | None:
        """The BuildMonth field value."""
        member = self.get_member("BuildMonth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_month.setter
    def build_month(self, value: np.int32) -> None:
        """Set the BuildMonth field value."""
        member = self.get_member("BuildMonth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildMonth", fields.FieldInt(value=value)
            )

    @property
    def build_day(self) -> np.int32 | None:
        """The BuildDay field value."""
        member = self.get_member("BuildDay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_day.setter
    def build_day(self, value: np.int32) -> None:
        """Set the BuildDay field value."""
        member = self.get_member("BuildDay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildDay", fields.FieldInt(value=value)
            )

    @property
    def build_time_of_day(self) -> np.int32 | None:
        """The BuildTimeOfDay field value."""
        member = self.get_member("BuildTimeOfDay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_time_of_day.setter
    def build_time_of_day(self, value: np.int32) -> None:
        """Set the BuildTimeOfDay field value."""
        member = self.get_member("BuildTimeOfDay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildTimeOfDay", fields.FieldInt(value=value)
            )

