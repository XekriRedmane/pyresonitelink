"""Generated component: SlotInspector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.expander import Expander
from pyresonitelink.generated._types.text_expand_indicator import TextExpandIndicator
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlotInspector(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SlotInspector.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SlotInspector"

    def __init__(self, selection_reference: str | SyncRef[Slot] | None = None, root_slot: str | Slot | None = None, child_container: str | Slot | None = None, depth: primitives.Int | None = None, expander: str | Expander | None = None, expander_indicator: str | TextExpandIndicator | None = None, slot_name_text: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selection_reference: Initial value for _selectionReference.
            root_slot: Initial value for _rootSlot.
            child_container: Initial value for _childContainer.
            depth: Initial value for _depth.
            expander: Initial value for _expander.
            expander_indicator: Initial value for _expanderIndicator.
            slot_name_text: Initial value for _slotNameText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selection_reference is not None:
            self.selection_reference = selection_reference
        if root_slot is not None:
            self.root_slot = root_slot
        if child_container is not None:
            self.child_container = child_container
        if depth is not None:
            self.depth = depth
        if expander is not None:
            self.expander = expander
        if expander_indicator is not None:
            self.expander_indicator = expander_indicator
        if slot_name_text is not None:
            self.slot_name_text = slot_name_text

    @property
    def selection_reference(self) -> str | None:
        """Target ID of the _selectionReference reference (targets SyncRef[Slot])."""
        member = self.get_member("_selectionReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selection_reference.setter
    def selection_reference(self, target: str | SyncRef[Slot] | None) -> None:
        """Set the _selectionReference reference by target ID or SyncRef[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("_selectionReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selectionReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def root_slot(self) -> str | None:
        """Target ID of the _rootSlot reference (targets Slot)."""
        member = self.get_member("_rootSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_slot.setter
    def root_slot(self, target: str | Slot | None) -> None:
        """Set the _rootSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rootSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rootSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def child_container(self) -> str | None:
        """Target ID of the _childContainer reference (targets Slot)."""
        member = self.get_member("_childContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @child_container.setter
    def child_container(self, target: str | Slot | None) -> None:
        """Set the _childContainer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_childContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_childContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def depth(self) -> primitives.Int | None:
        """The _depth field value."""
        member = self.get_member("_depth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth.setter
    def depth(self, value: primitives.Int) -> None:
        """Set the _depth field value."""
        member = self.get_member("_depth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_depth", fields.FieldInt(value=value)
            )

    @property
    def expander(self) -> str | None:
        """Target ID of the _expander reference (targets Expander)."""
        member = self.get_member("_expander")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expander.setter
    def expander(self, target: str | Expander | None) -> None:
        """Set the _expander reference by target ID or Expander instance."""
        target_id: str | None = target.id if isinstance(target, Expander) else target  # type: ignore[assignment]
        member = self.get_member("_expander")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expander",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Expander'),
            )

    @property
    def expander_indicator(self) -> str | None:
        """Target ID of the _expanderIndicator reference (targets TextExpandIndicator)."""
        member = self.get_member("_expanderIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @expander_indicator.setter
    def expander_indicator(self, target: str | TextExpandIndicator | None) -> None:
        """Set the _expanderIndicator reference by target ID or TextExpandIndicator instance."""
        target_id: str | None = target.id if isinstance(target, TextExpandIndicator) else target  # type: ignore[assignment]
        member = self.get_member("_expanderIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_expanderIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextExpandIndicator'),
            )

    @property
    def slot_name_text(self) -> str | None:
        """Target ID of the _slotNameText reference (targets Text)."""
        member = self.get_member("_slotNameText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slot_name_text.setter
    def slot_name_text(self, target: str | Text | None) -> None:
        """Set the _slotNameText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_slotNameText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slotNameText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

