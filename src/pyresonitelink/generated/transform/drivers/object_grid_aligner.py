"""Generated component: ObjectGridAligner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.align import Align
from pyresonitelink.generated._enums.axis_dir import AxisDir
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectGridAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ObjectGridAligner component aligns objects into a grid of items with x number of items per row.

    Category: Transform/Drivers

    Can be used for aligning tiles, shelves, boxes, or anything that needs
    consistent alignment.

    **Align**: Controls how the items should align themselves along the axis specified by the component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectGridAligner"

    def __init__(self, auto_add_children: primitives.Bool | None = None, items_per_row: primitives.Int | None = None, cell_size: primitives.Float2 | None = None, lerp_speed: primitives.Float | None = None, horizontal_alignment: Align | str | None = None, vertical_alignment: Align | str | None = None, row_axis: AxisDir | str | None = None, column_axis: AxisDir | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            items_per_row: Initial value for ItemsPerRow.
            cell_size: Initial value for CellSize.
            lerp_speed: Initial value for LerpSpeed.
            horizontal_alignment: Initial value for HorizontalAlignment.
            vertical_alignment: Initial value for VerticalAlignment.
            row_axis: Initial value for RowAxis.
            column_axis: Initial value for ColumnAxis.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if items_per_row is not None:
            self.items_per_row = items_per_row
        if cell_size is not None:
            self.cell_size = cell_size
        if lerp_speed is not None:
            self.lerp_speed = lerp_speed
        if horizontal_alignment is not None:
            self.horizontal_alignment = horizontal_alignment
        if vertical_alignment is not None:
            self.vertical_alignment = vertical_alignment
        if row_axis is not None:
            self.row_axis = row_axis
        if column_axis is not None:
            self.column_axis = column_axis

    @property
    def auto_add_children(self) -> primitives.Bool | None:
        """Controls whether slots below this component's slot in the hierarchy are automatically added to ``_targets``."""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: primitives.Bool) -> None:
        """Set the AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddChildren", fields.FieldBool(value=value)
            )

    @property
    def auto_add_ignore_tags(self) -> members.SyncList | None:
        """Slots that have these tags are automatically ignored by this component when adding children slots."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set AutoAddIgnoreTags. Slots that have these tags are automatically ignored by this component when adding children slots."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def items_per_row(self) -> primitives.Int | None:
        """How many items per row."""
        member = self.get_member("ItemsPerRow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @items_per_row.setter
    def items_per_row(self, value: primitives.Int) -> None:
        """Set the ItemsPerRow field value."""
        member = self.get_member("ItemsPerRow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ItemsPerRow", fields.FieldInt(value=value)
            )

    @property
    def cell_size(self) -> primitives.Float2 | None:
        """The space between each item."""
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
                "CellSize", fields.FieldFloat2(value=value)
            )

    @property
    def lerp_speed(self) -> primitives.Float | None:
        """How fast the items should move to align themselves in the specified grid arrangement."""
        member = self.get_member("LerpSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_speed.setter
    def lerp_speed(self, value: primitives.Float) -> None:
        """Set the LerpSpeed field value."""
        member = self.get_member("LerpSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpSpeed", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_alignment(self) -> Align | None:
        """How to align the items horizontally."""
        member = self.get_member("HorizontalAlignment")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: Align | str) -> None:
        """Set HorizontalAlignment. How to align the items horizontally."""
        member = self.get_member("HorizontalAlignment")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HorizontalAlignment",
                members.FieldEnum(value=str(value)),
            )

    @property
    def vertical_alignment(self) -> Align | None:
        """How to align the items vertically."""
        member = self.get_member("VerticalAlignment")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @vertical_alignment.setter
    def vertical_alignment(self, value: Align | str) -> None:
        """Set VerticalAlignment. How to align the items vertically."""
        member = self.get_member("VerticalAlignment")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VerticalAlignment",
                members.FieldEnum(value=str(value)),
            )

    @property
    def row_axis(self) -> AxisDir | None:
        """The axis that items should be aligned on for the horizontal axis of the grid."""
        member = self.get_member("RowAxis")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AxisDir(member.value)
        return None

    @row_axis.setter
    def row_axis(self, value: AxisDir | str) -> None:
        """Set RowAxis. The axis that items should be aligned on for the horizontal axis of the grid."""
        member = self.get_member("RowAxis")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RowAxis",
                members.FieldEnum(value=str(value)),
            )

    @property
    def column_axis(self) -> AxisDir | None:
        """The axis that items should be aligned on for the vertical axis of the grid."""
        member = self.get_member("ColumnAxis")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AxisDir(member.value)
        return None

    @column_axis.setter
    def column_axis(self, value: AxisDir | str) -> None:
        """Set ColumnAxis. The axis that items should be aligned on for the vertical axis of the grid."""
        member = self.get_member("ColumnAxis")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ColumnAxis",
                members.FieldEnum(value=str(value)),
            )

    @property
    def items(self) -> members.SyncList | None:
        """A list of items who's positions should be driven to place them into a grid alignment using this component's calculations."""
        member = self.get_member("Items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set Items. A list of items who's positions should be driven to place them into a grid alignment using this component's calculations."""
        self.set_member("Items", value)

