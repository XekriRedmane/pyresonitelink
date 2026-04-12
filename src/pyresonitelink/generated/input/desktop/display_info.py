"""Generated component: DisplayInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.rect_orientation import RectOrientation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DisplayInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DisplayInfo component is used to get information about the local user's display.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DisplayInfo"

    def __init__(self, display_index: primitives.Int | None = None, resolution: primitives.Int2 | None = None, offset: primitives.Int2 | None = None, dpi: primitives.Float2 | None = None, refresh_rate: primitives.Double | None = None, orientation: RectOrientation | str | None = None, is_primary: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_index: Initial value for DisplayIndex.
            resolution: Initial value for Resolution.
            offset: Initial value for Offset.
            dpi: Initial value for DPI.
            refresh_rate: Initial value for RefreshRate.
            orientation: Initial value for Orientation.
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
        if orientation is not None:
            self.orientation = orientation
        if is_primary is not None:
            self.is_primary = is_primary

    @property
    def display_index(self) -> primitives.Int | None:
        """The display index to get info on."""
        member = self.get_member("DisplayIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_index.setter
    def display_index(self, value: primitives.Int) -> None:
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
        """The resolution of display ``DisplayIndex``"""
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
        """The offset of pixels of display ``DisplayIndex``"""
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
        """The Dots Per Inch of display ``DisplayIndex``"""
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
    def refresh_rate(self) -> primitives.Double | None:
        """The refresh rate in Hertz of ``DisplayIndex``"""
        member = self.get_member("RefreshRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @refresh_rate.setter
    def refresh_rate(self, value: primitives.Double) -> None:
        """Set the RefreshRate field value."""
        member = self.get_member("RefreshRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RefreshRate", fields.FieldDouble(value=value)
            )

    @property
    def orientation(self) -> RectOrientation | None:
        """The orientation of ``DisplayIndex``."""
        member = self.get_member("Orientation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RectOrientation(member.value)
        return None

    @orientation.setter
    def orientation(self, value: RectOrientation | str) -> None:
        """Set Orientation. The orientation of ``DisplayIndex``."""
        member = self.get_member("Orientation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Orientation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def is_primary(self) -> primitives.Bool | None:
        """Whether display ``DisplayIndex`` is the main monitor in the OS."""
        member = self.get_member("IsPrimary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_primary.setter
    def is_primary(self, value: primitives.Bool) -> None:
        """Set the IsPrimary field value."""
        member = self.get_member("IsPrimary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPrimary", fields.FieldBool(value=value)
            )

