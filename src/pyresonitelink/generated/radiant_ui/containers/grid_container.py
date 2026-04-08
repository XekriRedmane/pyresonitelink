"""Generated component: GridContainer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iui_preprocess_interactable import IUIPreprocessInteractable
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GridContainer(GeneratedComponent, ICustomInspector, IUIPreprocessInteractable, IUIGrabbable, IUIGrabReceiver, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GridContainer.

    Category: Radiant UI/Containers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GridContainer"

    def __init__(self, edit_mode: bool | None = None, facets_root: str | Slot | None = None, background: str | RectTransform | None = None, content: str | RectTransform | None = None, overlay: str | RectTransform | None = None, recalculate_on_size_change: bool | None = None, cell_size: primitives.Float2 | None = None, padding: primitives.Float2 | None = None, last_calculated_centering_offset: primitives.Float2 | None = None, last_calculated_cell_size: primitives.Float2 | None = None, last_calculated_padding: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            edit_mode: Initial value for EditMode.
            facets_root: Initial value for FacetsRoot.
            background: Initial value for _background.
            content: Initial value for _content.
            overlay: Initial value for _overlay.
            recalculate_on_size_change: Initial value for RecalculateOnSizeChange.
            cell_size: Initial value for CellSize.
            padding: Initial value for Padding.
            last_calculated_centering_offset: Initial value for _lastCalculatedCenteringOffset.
            last_calculated_cell_size: Initial value for _lastCalculatedCellSize.
            last_calculated_padding: Initial value for _lastCalculatedPadding.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if edit_mode is not None:
            self.edit_mode = edit_mode
        if facets_root is not None:
            self.facets_root = facets_root
        if background is not None:
            self.background = background
        if content is not None:
            self.content = content
        if overlay is not None:
            self.overlay = overlay
        if recalculate_on_size_change is not None:
            self.recalculate_on_size_change = recalculate_on_size_change
        if cell_size is not None:
            self.cell_size = cell_size
        if padding is not None:
            self.padding = padding
        if last_calculated_centering_offset is not None:
            self.last_calculated_centering_offset = last_calculated_centering_offset
        if last_calculated_cell_size is not None:
            self.last_calculated_cell_size = last_calculated_cell_size
        if last_calculated_padding is not None:
            self.last_calculated_padding = last_calculated_padding

    @property
    def edit_mode(self) -> bool | None:
        """The EditMode field value."""
        member = self.get_member("EditMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode.setter
    def edit_mode(self, value: bool) -> None:
        """Set the EditMode field value."""
        member = self.get_member("EditMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditMode", fields.FieldBool(value=value)
            )

    @property
    def facets_root(self) -> str | None:
        """Target ID of the FacetsRoot reference (targets Slot)."""
        member = self.get_member("FacetsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @facets_root.setter
    def facets_root(self, target: str | Slot | None) -> None:
        """Set the FacetsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("FacetsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FacetsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def background(self) -> str | None:
        """Target ID of the _background reference (targets RectTransform)."""
        member = self.get_member("_background")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @background.setter
    def background(self, target: str | RectTransform | None) -> None:
        """Set the _background reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_background")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_background",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def content(self) -> str | None:
        """Target ID of the _content reference (targets RectTransform)."""
        member = self.get_member("_content")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content.setter
    def content(self, target: str | RectTransform | None) -> None:
        """Set the _content reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_content")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_content",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def overlay(self) -> str | None:
        """Target ID of the _overlay reference (targets RectTransform)."""
        member = self.get_member("_overlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overlay.setter
    def overlay(self, target: str | RectTransform | None) -> None:
        """Set the _overlay reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_overlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def recalculate_on_size_change(self) -> bool | None:
        """The RecalculateOnSizeChange field value."""
        member = self.get_member("RecalculateOnSizeChange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @recalculate_on_size_change.setter
    def recalculate_on_size_change(self, value: bool) -> None:
        """Set the RecalculateOnSizeChange field value."""
        member = self.get_member("RecalculateOnSizeChange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RecalculateOnSizeChange", fields.FieldBool(value=value)
            )

    @property
    def cell_count(self) -> members.FieldEnum | None:
        """The CellCount member."""
        member = self.get_member("CellCount")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @cell_count.setter
    def cell_count(self, value: members.FieldEnum) -> None:
        """Set the CellCount member."""
        self.set_member("CellCount", value)

    @property
    def cell_size(self) -> primitives.Float2 | None:
        """The CellSize field value."""
        member = self.get_member("CellSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cell_size.setter
    def cell_size(self, value: primitives.Float2) -> None:
        """Set the CellSize field value."""
        member = self.get_member("CellSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CellSize", fields.FieldNullableFloat2(value=value)
            )

    @property
    def padding(self) -> primitives.Float2 | None:
        """The Padding field value."""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: primitives.Float2) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldFloat2(value=value)
            )

    @property
    def last_calculated_centering_offset(self) -> primitives.Float2 | None:
        """The _lastCalculatedCenteringOffset field value."""
        member = self.get_member("_lastCalculatedCenteringOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_calculated_centering_offset.setter
    def last_calculated_centering_offset(self, value: primitives.Float2) -> None:
        """Set the _lastCalculatedCenteringOffset field value."""
        member = self.get_member("_lastCalculatedCenteringOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastCalculatedCenteringOffset", fields.FieldNullableFloat2(value=value)
            )

    @property
    def last_calculated_cell_size(self) -> primitives.Float2 | None:
        """The _lastCalculatedCellSize field value."""
        member = self.get_member("_lastCalculatedCellSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_calculated_cell_size.setter
    def last_calculated_cell_size(self, value: primitives.Float2) -> None:
        """Set the _lastCalculatedCellSize field value."""
        member = self.get_member("_lastCalculatedCellSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastCalculatedCellSize", fields.FieldNullableFloat2(value=value)
            )

    @property
    def last_calculated_padding(self) -> primitives.Float2 | None:
        """The _lastCalculatedPadding field value."""
        member = self.get_member("_lastCalculatedPadding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_calculated_padding.setter
    def last_calculated_padding(self, value: primitives.Float2) -> None:
        """Set the _lastCalculatedPadding field value."""
        member = self.get_member("_lastCalculatedPadding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastCalculatedPadding", fields.FieldNullableFloat2(value=value)
            )

