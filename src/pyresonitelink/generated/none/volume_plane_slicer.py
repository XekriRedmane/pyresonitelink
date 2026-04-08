"""Generated component: VolumePlaneSlicer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.color_dialog_interface import ColorDialogInterface
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VolumePlaneSlicer(GeneratedComponent, ITouchable, IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VolumePlaneSlicer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VolumePlaneSlicer"

    def __init__(self, highlight_color: primitives.ColorX | None = None, highlight_range: np.float32 | None = None, color_dialog: str | ColorDialogInterface | None = None, grab_grid: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            highlight_color: Initial value for HighlightColor.
            highlight_range: Initial value for HighlightRange.
            color_dialog: Initial value for _colorDialog.
            grab_grid: Initial value for _grabGrid.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if highlight_color is not None:
            self.highlight_color = highlight_color
        if highlight_range is not None:
            self.highlight_range = highlight_range
        if color_dialog is not None:
            self.color_dialog = color_dialog
        if grab_grid is not None:
            self.grab_grid = grab_grid

    @property
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

    @property
    def highlight_color(self) -> primitives.ColorX | None:
        """The HighlightColor field value."""
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
    def highlight_range(self) -> np.float32 | None:
        """The HighlightRange field value."""
        member = self.get_member("HighlightRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight_range.setter
    def highlight_range(self, value: np.float32) -> None:
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
        """Target ID of the _colorDialog reference (targets ColorDialogInterface)."""
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
        """Target ID of the _grabGrid reference (targets Slot)."""
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

