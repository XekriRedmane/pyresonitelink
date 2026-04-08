"""Generated component: AudioDeviceIndexFinder."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioDeviceIndexFinder(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioDeviceIndexFinder.

    Category: Audio/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioDeviceIndexFinder"

    def __init__(self, device_index: primitives.Int | None = None, device_name: primitives.String | None = None, case_sensitive: primitives.Bool | None = None, allow_partial_match: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            device_index: Initial value for DeviceIndex.
            device_name: Initial value for DeviceName.
            case_sensitive: Initial value for CaseSensitive.
            allow_partial_match: Initial value for AllowPartialMatch.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if device_index is not None:
            self.device_index = device_index
        if device_name is not None:
            self.device_name = device_name
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if allow_partial_match is not None:
            self.allow_partial_match = allow_partial_match

    @property
    def device_index(self) -> primitives.Int | None:
        """The DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_index.setter
    def device_index(self, value: primitives.Int) -> None:
        """Set the DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def device_name(self) -> primitives.String | None:
        """The DeviceName field value."""
        member = self.get_member("DeviceName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_name.setter
    def device_name(self, value: primitives.String) -> None:
        """Set the DeviceName field value."""
        member = self.get_member("DeviceName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceName", fields.FieldString(value=value)
            )

    @property
    def case_sensitive(self) -> primitives.Bool | None:
        """The CaseSensitive field value."""
        member = self.get_member("CaseSensitive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @case_sensitive.setter
    def case_sensitive(self, value: primitives.Bool) -> None:
        """Set the CaseSensitive field value."""
        member = self.get_member("CaseSensitive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CaseSensitive", fields.FieldBool(value=value)
            )

    @property
    def allow_partial_match(self) -> primitives.Bool | None:
        """The AllowPartialMatch field value."""
        member = self.get_member("AllowPartialMatch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_partial_match.setter
    def allow_partial_match(self, value: primitives.Bool) -> None:
        """Set the AllowPartialMatch field value."""
        member = self.get_member("AllowPartialMatch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowPartialMatch", fields.FieldBool(value=value)
            )

