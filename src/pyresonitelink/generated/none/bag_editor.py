"""Generated component: BagEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_bag import ISyncBag
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BagEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BagEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BagEditor"

    def __init__(self, target_bag: str | ISyncBag | None = None, add_new_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_bag: Initial value for _targetBag.
            add_new_button: Initial value for _addNewButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_bag is not None:
            self.target_bag = target_bag
        if add_new_button is not None:
            self.add_new_button = add_new_button

    @property
    def target_bag(self) -> str | None:
        """Target ID of the _targetBag reference (targets ISyncBag)."""
        member = self.get_member("_targetBag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_bag.setter
    def target_bag(self, target: str | ISyncBag | None) -> None:
        """Set the _targetBag reference by target ID or ISyncBag instance."""
        target_id: str | None = target.id if isinstance(target, ISyncBag) else target  # type: ignore[assignment]
        member = self.get_member("_targetBag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetBag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncBag'),
            )

    @property
    def add_new_button(self) -> str | None:
        """Target ID of the _addNewButton reference (targets Button)."""
        member = self.get_member("_addNewButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @add_new_button.setter
    def add_new_button(self, target: str | Button | None) -> None:
        """Set the _addNewButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_addNewButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_addNewButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

