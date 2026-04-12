"""Generated component: BagEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_bag import ISyncBag
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BagEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The BagEditor component is a internal-use component intended to be used to generate UIX for editing an ISyncBag. Some examples of Bags include the UserBag, SlotBag and WorkerBag.

    When ``_targetBag`` receives a reference to a bag, the BagEditor's
    slot's children will be populated with items in the bag. Each of these
    child slots will have the name ``Element - IDXXXXXX``, where ``IDXXXXX``
    is the Reference ID of the element. Each child slot contains a
    BagEditorItem component with a reference to items in the bag. This
    component will misbehave when changing the ``_targetBag`` after it
    already has a reference, as doing so is unintended behavior. This
    component is frequently used in conjunction with Ref Hacking, as it
    exposes reference IDs in the element slot names.
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
        """The bag to edit."""
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
        """Button to add a new item to the bag."""
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

