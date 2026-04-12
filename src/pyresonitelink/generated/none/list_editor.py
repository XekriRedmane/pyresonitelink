"""Generated component: ListEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_list import ISyncList
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ListEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ListEditor component is a internal-use component intended to be used to generate UIX for editing an ISyncList.

    When ``_targetList`` receives a reference to a list, the ListEditor's
    slot's children will be populated with items in the list. Each of these
    child slots will have the name ``Element``. Each slot contains a
    HorizontalLayout component and RectTransform component. This component
    will misbehave when changing the ``_targetList`` after it already has a
    reference, as doing so is unintended behavior. This component is much
    less useful than its cousin, BagEditor, as it does not expose any method
    to reference the list members from in-game. FrooxEngine uses internal
    code to add references on child slots of the elements when building the
    Scene Inspector UI.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ListEditor"

    def __init__(self, target_list: str | ISyncList | None = None, add_new_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_list: Initial value for _targetList.
            add_new_button: Initial value for _addNewButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_list is not None:
            self.target_list = target_list
        if add_new_button is not None:
            self.add_new_button = add_new_button

    @property
    def target_list(self) -> str | None:
        """The list to edit."""
        member = self.get_member("_targetList")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_list.setter
    def target_list(self, target: str | ISyncList | None) -> None:
        """Set the _targetList reference by target ID or ISyncList instance."""
        target_id: str | None = target.id if isinstance(target, ISyncList) else target  # type: ignore[assignment]
        member = self.get_member("_targetList")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetList",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncList'),
            )

    @property
    def add_new_button(self) -> str | None:
        """Button to add a new item to the list."""
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

