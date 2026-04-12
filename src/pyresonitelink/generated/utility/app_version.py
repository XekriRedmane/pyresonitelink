"""Generated component: AppVersion."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AppVersion(GeneratedComponent, IComponent, IWorldEventReceiver):
    """App version is a component that updates it's fields with the live information of Resonite's version.

    Category: Utility

    **Behavior**: The fields are "Pseudo Driven" or constantly being written to. Attempting to change a field makes it instantly change back and not send an update event.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AppVersion"

    def __init__(self, version_number: primitives.String | None = None, version_name: primitives.String | None = None, full_version_string: primitives.String | None = None, build_year: primitives.Int | None = None, build_month: primitives.Int | None = None, build_day: primitives.Int | None = None, build_time_of_day: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
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
    def version_number(self) -> primitives.String | None:
        """The version number of Resonite. usually formatted year.month.day.minute. The minute part of the version is the minute from midnight UTC the version was compiled."""
        member = self.get_member("VersionNumber")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @version_number.setter
    def version_number(self, value: primitives.String) -> None:
        """Set the VersionNumber field value."""
        member = self.get_member("VersionNumber")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VersionNumber", fields.FieldString(value=value)
            )

    @property
    def version_name(self) -> primitives.String | None:
        """The name of the version of Resonite. Usually this is "Beta", "Alpha" or "Release" followed by ``VersionNumber``"""
        member = self.get_member("VersionName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @version_name.setter
    def version_name(self, value: primitives.String) -> None:
        """Set the VersionName field value."""
        member = self.get_member("VersionName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VersionName", fields.FieldString(value=value)
            )

    @property
    def full_version_string(self) -> primitives.String | None:
        """Usually the same as ``VersionNumber``"""
        member = self.get_member("FullVersionString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @full_version_string.setter
    def full_version_string(self, value: primitives.String) -> None:
        """Set the FullVersionString field value."""
        member = self.get_member("FullVersionString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullVersionString", fields.FieldString(value=value)
            )

    @property
    def build_year(self) -> primitives.Int | None:
        """The year Resonite was compiled."""
        member = self.get_member("BuildYear")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_year.setter
    def build_year(self, value: primitives.Int) -> None:
        """Set the BuildYear field value."""
        member = self.get_member("BuildYear")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildYear", fields.FieldInt(value=value)
            )

    @property
    def build_month(self) -> primitives.Int | None:
        """The month Resonite was compiled."""
        member = self.get_member("BuildMonth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_month.setter
    def build_month(self, value: primitives.Int) -> None:
        """Set the BuildMonth field value."""
        member = self.get_member("BuildMonth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildMonth", fields.FieldInt(value=value)
            )

    @property
    def build_day(self) -> primitives.Int | None:
        """The day Resonite was compiled."""
        member = self.get_member("BuildDay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_day.setter
    def build_day(self, value: primitives.Int) -> None:
        """Set the BuildDay field value."""
        member = self.get_member("BuildDay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildDay", fields.FieldInt(value=value)
            )

    @property
    def build_time_of_day(self) -> primitives.Int | None:
        """The amount of minutes since midnight UTC."""
        member = self.get_member("BuildTimeOfDay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @build_time_of_day.setter
    def build_time_of_day(self, value: primitives.Int) -> None:
        """Set the BuildTimeOfDay field value."""
        member = self.get_member("BuildTimeOfDay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BuildTimeOfDay", fields.FieldInt(value=value)
            )

