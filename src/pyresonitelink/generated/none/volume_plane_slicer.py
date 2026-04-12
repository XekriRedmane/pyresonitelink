"""Generated component: VolumePlaneSlicer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.volume_plane_mode import VolumePlaneMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.color_dialog_interface import ColorDialogInterface
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VolumePlaneSlicer(GeneratedComponent, ITouchable, IGrabEventReceiver, IWorldEventReceiver):
    """See Volume Unlit Material Examples section for better information on how slicers work.

    See Volume Unlit Material Examples section.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VolumePlaneSlicer"

    def __init__(self, mode: VolumePlaneMode | str | None = None, highlight_color: primitives.ColorX | None = None, highlight_range: primitives.Float | None = None, color_dialog: str | ColorDialogInterface | None = None, grab_grid: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mode: Initial value for Mode.
            highlight_color: Initial value for HighlightColor.
            highlight_range: Initial value for HighlightRange.
            color_dialog: Initial value for _colorDialog.
            grab_grid: Initial value for _grabGrid.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mode is not None:
            self.mode = mode
        if highlight_color is not None:
            self.highlight_color = highlight_color
        if highlight_range is not None:
            self.highlight_range = highlight_range
        if color_dialog is not None:
            self.color_dialog = color_dialog
        if grab_grid is not None:
            self.grab_grid = grab_grid

    @property
    def mode(self) -> VolumePlaneMode | None:
        """The kind of slicer mode this slicer is doing."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VolumePlaneMode(member.value)
        return None

    @mode.setter
    def mode(self, value: VolumePlaneMode | str) -> None:
        """Set Mode. The kind of slicer mode this slicer is doing."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def highlight_color(self) -> primitives.ColorX | None:
        """The color highlight to highlight the slicer with. please see Volume Unlit Material Examples section for better info."""
        member = self.get_member("HighlightColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight_color.setter
    def highlight_color(self, value: primitives.ColorX) -> None:
        """Set the HighlightColor field value."""
        member = self.get_member("HighlightColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighlightColor", fields.FieldColorX(value=value)
            )

    @property
    def highlight_range(self) -> primitives.Float | None:
        """The color highlight range to use. please see Volume Unlit Material Examples section for better info."""
        member = self.get_member("HighlightRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight_range.setter
    def highlight_range(self, value: primitives.Float) -> None:
        """Set the HighlightRange field value."""
        member = self.get_member("HighlightRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighlightRange", fields.FieldFloat(value=value)
            )

    @property
    def color_dialog(self) -> str | None:
        """The dialog ui currently being used to choose a color to display for the color highlight."""
        member = self.get_member("_colorDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_dialog.setter
    def color_dialog(self, target: str | ColorDialogInterface | None) -> None:
        """Set the _colorDialog reference by target ID or ColorDialogInterface instance."""
        target_id: str | None = target.id if isinstance(target, ColorDialogInterface) else target  # type: ignore[assignment]
        member = self.get_member("_colorDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colorDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ColorDialogInterface'),
            )

    @property
    def grab_grid(self) -> str | None:
        """The slot to enable when grabbing the slicer to show the grid visual."""
        member = self.get_member("_grabGrid")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grab_grid.setter
    def grab_grid(self, target: str | Slot | None) -> None:
        """Set the _grabGrid reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_grabGrid")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabGrid",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

