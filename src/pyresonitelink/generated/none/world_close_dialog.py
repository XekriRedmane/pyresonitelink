"""Generated component: WorldCloseDialog."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.world_close_action import WorldCloseAction
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldCloseDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldCloseDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldCloseDialog"

    def __init__(self, world_name: str | Text | None = None, save_button: str | Button | None = None, save_as_button: str | Button | None = None, discard_button: str | Button | None = None, save_action: str | WorldCloseAction | None = None, save_as_action: str | WorldCloseAction | None = None, discard_action: str | WorldCloseAction | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_name: Initial value for _worldName.
            save_button: Initial value for _saveButton.
            save_as_button: Initial value for _saveAsButton.
            discard_button: Initial value for _discardButton.
            save_action: Initial value for _saveAction.
            save_as_action: Initial value for _saveAsAction.
            discard_action: Initial value for _discardAction.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_name is not None:
            self.world_name = world_name
        if save_button is not None:
            self.save_button = save_button
        if save_as_button is not None:
            self.save_as_button = save_as_button
        if discard_button is not None:
            self.discard_button = discard_button
        if save_action is not None:
            self.save_action = save_action
        if save_as_action is not None:
            self.save_as_action = save_as_action
        if discard_action is not None:
            self.discard_action = discard_action

    @property
    def world_name(self) -> str | None:
        """Target ID of the _worldName reference (targets Text)."""
        member = self.get_member("_worldName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_name.setter
    def world_name(self, target: str | Text | None) -> None:
        """Set the _worldName reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_worldName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worldName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def save_button(self) -> str | None:
        """Target ID of the _saveButton reference (targets Button)."""
        member = self.get_member("_saveButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_button.setter
    def save_button(self, target: str | Button | None) -> None:
        """Set the _saveButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_saveButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def save_as_button(self) -> str | None:
        """Target ID of the _saveAsButton reference (targets Button)."""
        member = self.get_member("_saveAsButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_as_button.setter
    def save_as_button(self, target: str | Button | None) -> None:
        """Set the _saveAsButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_saveAsButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveAsButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def discard_button(self) -> str | None:
        """Target ID of the _discardButton reference (targets Button)."""
        member = self.get_member("_discardButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @discard_button.setter
    def discard_button(self, target: str | Button | None) -> None:
        """Set the _discardButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_discardButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_discardButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def save_action(self) -> str | None:
        """Target ID of the _saveAction reference (targets WorldCloseAction)."""
        member = self.get_member("_saveAction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_action.setter
    def save_action(self, target: str | WorldCloseAction | None) -> None:
        """Set the _saveAction reference by target ID or WorldCloseAction instance."""
        target_id: str | None = target.id if isinstance(target, WorldCloseAction) else target  # type: ignore[assignment]
        member = self.get_member("_saveAction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveAction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldCloseAction'),
            )

    @property
    def save_as_action(self) -> str | None:
        """Target ID of the _saveAsAction reference (targets WorldCloseAction)."""
        member = self.get_member("_saveAsAction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_as_action.setter
    def save_as_action(self, target: str | WorldCloseAction | None) -> None:
        """Set the _saveAsAction reference by target ID or WorldCloseAction instance."""
        target_id: str | None = target.id if isinstance(target, WorldCloseAction) else target  # type: ignore[assignment]
        member = self.get_member("_saveAsAction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveAsAction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldCloseAction'),
            )

    @property
    def discard_action(self) -> str | None:
        """Target ID of the _discardAction reference (targets WorldCloseAction)."""
        member = self.get_member("_discardAction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @discard_action.setter
    def discard_action(self, target: str | WorldCloseAction | None) -> None:
        """Set the _discardAction reference by target ID or WorldCloseAction instance."""
        target_id: str | None = target.id if isinstance(target, WorldCloseAction) else target  # type: ignore[assignment]
        member = self.get_member("_discardAction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_discardAction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldCloseAction'),
            )

