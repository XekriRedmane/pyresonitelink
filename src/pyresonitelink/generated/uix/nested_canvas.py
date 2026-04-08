"""Generated component: NestedCanvas."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NestedCanvas(GeneratedComponent, IUIInteractable, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.NestedCanvas.

    Category: UIX
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NestedCanvas"

    def __init__(self, target_canvas: str | Canvas | None = None, render_offset: str | IField[np.int32] | None = None, mask_depth: str | IField[np.int32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_canvas: Initial value for TargetCanvas.
            render_offset: Initial value for _renderOffset.
            mask_depth: Initial value for _maskDepth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_canvas is not None:
            self.target_canvas = target_canvas
        if render_offset is not None:
            self.render_offset = render_offset
        if mask_depth is not None:
            self.mask_depth = mask_depth

    @property
    def target_canvas(self) -> str | None:
        """Target ID of the TargetCanvas reference (targets Canvas)."""
        member = self.get_member("TargetCanvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_canvas.setter
    def target_canvas(self, target: str | Canvas | None) -> None:
        """Set the TargetCanvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("TargetCanvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetCanvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def render_offset(self) -> str | None:
        """Target ID of the _renderOffset reference (targets IField[np.int32])."""
        member = self.get_member("_renderOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_offset.setter
    def render_offset(self, target: str | IField[np.int32] | None) -> None:
        """Set the _renderOffset reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_renderOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def mask_depth(self) -> str | None:
        """Target ID of the _maskDepth reference (targets IField[np.int32])."""
        member = self.get_member("_maskDepth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mask_depth.setter
    def mask_depth(self, target: str | IField[np.int32] | None) -> None:
        """Set the _maskDepth reference by target ID or IField[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_maskDepth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maskDepth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

