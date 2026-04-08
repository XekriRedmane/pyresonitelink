"""Generated component: ObjectGridAligner."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectGridAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ObjectGridAligner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectGridAligner"

    def __init__(self, auto_add_children: bool | None = None, items_per_row: np.int32 | None = None, cell_size: primitives.Float2 | None = None, lerp_speed: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            items_per_row: Initial value for ItemsPerRow.
            cell_size: Initial value for CellSize.
            lerp_speed: Initial value for LerpSpeed.
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

    @property
    def auto_add_children(self) -> bool | None:
        """The AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: bool) -> None:
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
        """The AutoAddIgnoreTags member."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set the AutoAddIgnoreTags member."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def items_per_row(self) -> np.int32 | None:
        """The ItemsPerRow field value."""
        member = self.get_member("ItemsPerRow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @items_per_row.setter
    def items_per_row(self, value: np.int32) -> None:
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
                "CellSize", fields.FieldFloat2(value=value)
            )

    @property
    def lerp_speed(self) -> np.float32 | None:
        """The LerpSpeed field value."""
        member = self.get_member("LerpSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_speed.setter
    def lerp_speed(self, value: np.float32) -> None:
        """Set the LerpSpeed field value."""
        member = self.get_member("LerpSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpSpeed", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_alignment(self) -> members.FieldEnum | None:
        """The HorizontalAlignment member."""
        member = self.get_member("HorizontalAlignment")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: members.FieldEnum) -> None:
        """Set the HorizontalAlignment member."""
        self.set_member("HorizontalAlignment", value)

    @property
    def vertical_alignment(self) -> members.FieldEnum | None:
        """The VerticalAlignment member."""
        member = self.get_member("VerticalAlignment")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertical_alignment.setter
    def vertical_alignment(self, value: members.FieldEnum) -> None:
        """Set the VerticalAlignment member."""
        self.set_member("VerticalAlignment", value)

    @property
    def row_axis(self) -> members.FieldEnum | None:
        """The RowAxis member."""
        member = self.get_member("RowAxis")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @row_axis.setter
    def row_axis(self, value: members.FieldEnum) -> None:
        """Set the RowAxis member."""
        self.set_member("RowAxis", value)

    @property
    def column_axis(self) -> members.FieldEnum | None:
        """The ColumnAxis member."""
        member = self.get_member("ColumnAxis")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @column_axis.setter
    def column_axis(self, value: members.FieldEnum) -> None:
        """Set the ColumnAxis member."""
        self.set_member("ColumnAxis", value)

    @property
    def items(self) -> members.SyncList | None:
        """The Items member."""
        member = self.get_member("Items")
        if isinstance(member, members.SyncList):
            return member
        return None

    @items.setter
    def items(self, value: members.SyncList) -> None:
        """Set the Items member."""
        self.set_member("Items", value)

