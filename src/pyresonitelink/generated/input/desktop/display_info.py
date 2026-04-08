"""Generated component: DisplayInfo."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DisplayInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DisplayInfo.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DisplayInfo"

    def __init__(self, display_index: np.int32 | None = None, resolution: primitives.Int2 | None = None, offset: primitives.Int2 | None = None, dpi: primitives.Float2 | None = None, refresh_rate: np.float64 | None = None, is_primary: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_index: Initial value for DisplayIndex.
            resolution: Initial value for Resolution.
            offset: Initial value for Offset.
            dpi: Initial value for DPI.
            refresh_rate: Initial value for RefreshRate.
            is_primary: Initial value for IsPrimary.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_index is not None:
            self.display_index = display_index
        if resolution is not None:
            self.resolution = resolution
        if offset is not None:
            self.offset = offset
        if dpi is not None:
            self.dpi = dpi
        if refresh_rate is not None:
            self.refresh_rate = refresh_rate
        if is_primary is not None:
            self.is_primary = is_primary

    @property
    def display_index(self) -> np.int32 | None:
        """The DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_index.setter
    def display_index(self, value: np.int32) -> None:
        """Set the DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayIndex", fields.FieldInt(value=value)
            )

    @property
    def resolution(self) -> primitives.Int2 | None:
        """The Resolution field value."""
        member = self.get_member("Resolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @resolution.setter
    def resolution(self, value: primitives.Int2) -> None:
        """Set the Resolution field value."""
        member = self.get_member("Resolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Resolution", fields.FieldInt2(value=value)
            )

    @property
    def offset(self) -> primitives.Int2 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Int2) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldInt2(value=value)
            )

    @property
    def dpi(self) -> primitives.Float2 | None:
        """The DPI field value."""
        member = self.get_member("DPI")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dpi.setter
    def dpi(self, value: primitives.Float2) -> None:
        """Set the DPI field value."""
        member = self.get_member("DPI")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DPI", fields.FieldFloat2(value=value)
            )

    @property
    def refresh_rate(self) -> np.float64 | None:
        """The RefreshRate field value."""
        member = self.get_member("RefreshRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @refresh_rate.setter
    def refresh_rate(self, value: np.float64) -> None:
        """Set the RefreshRate field value."""
        member = self.get_member("RefreshRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RefreshRate", fields.FieldDouble(value=value)
            )

    @property
    def orientation(self) -> members.FieldEnum | None:
        """The Orientation member."""
        member = self.get_member("Orientation")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @orientation.setter
    def orientation(self, value: members.FieldEnum) -> None:
        """Set the Orientation member."""
        self.set_member("Orientation", value)

    @property
    def is_primary(self) -> bool | None:
        """The IsPrimary field value."""
        member = self.get_member("IsPrimary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_primary.setter
    def is_primary(self, value: bool) -> None:
        """Set the IsPrimary field value."""
        member = self.get_member("IsPrimary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPrimary", fields.FieldBool(value=value)
            )

