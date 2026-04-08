"""Generated component: MigrationDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MigrationDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MigrationDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MigrationDialog"

    def __init__(self, username_field: str | TextField | None = None, password_field: str | TextField | None = None, migrate_favorites: bool | None = None, overwrite_favorites: bool | None = None, preserve_old_home: bool | None = None, migrate_contacts: bool | None = None, migrate_message_history: bool | None = None, migrate_records: bool | None = None, migrate_cloud_variables: bool | None = None, migrated_cloud_variable_definitions: bool | None = None, migrate_groups: bool | None = None, groups_root: str | Slot | None = None, groups_message: str | Text | None = None, load_groups_button: str | Button | None = None, swap_region: str | SlideSwapRegion | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            username_field: Initial value for _usernameField.
            password_field: Initial value for _passwordField.
            migrate_favorites: Initial value for _migrateFavorites.
            overwrite_favorites: Initial value for _overwriteFavorites.
            preserve_old_home: Initial value for _preserveOldHome.
            migrate_contacts: Initial value for _migrateContacts.
            migrate_message_history: Initial value for _migrateMessageHistory.
            migrate_records: Initial value for _migrateRecords.
            migrate_cloud_variables: Initial value for _migrateCloudVariables.
            migrated_cloud_variable_definitions: Initial value for _migratedCloudVariableDefinitions.
            migrate_groups: Initial value for _migrateGroups.
            groups_root: Initial value for _groupsRoot.
            groups_message: Initial value for _groupsMessage.
            load_groups_button: Initial value for _loadGroupsButton.
            swap_region: Initial value for _swapRegion.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if username_field is not None:
            self.username_field = username_field
        if password_field is not None:
            self.password_field = password_field
        if migrate_favorites is not None:
            self.migrate_favorites = migrate_favorites
        if overwrite_favorites is not None:
            self.overwrite_favorites = overwrite_favorites
        if preserve_old_home is not None:
            self.preserve_old_home = preserve_old_home
        if migrate_contacts is not None:
            self.migrate_contacts = migrate_contacts
        if migrate_message_history is not None:
            self.migrate_message_history = migrate_message_history
        if migrate_records is not None:
            self.migrate_records = migrate_records
        if migrate_cloud_variables is not None:
            self.migrate_cloud_variables = migrate_cloud_variables
        if migrated_cloud_variable_definitions is not None:
            self.migrated_cloud_variable_definitions = migrated_cloud_variable_definitions
        if migrate_groups is not None:
            self.migrate_groups = migrate_groups
        if groups_root is not None:
            self.groups_root = groups_root
        if groups_message is not None:
            self.groups_message = groups_message
        if load_groups_button is not None:
            self.load_groups_button = load_groups_button
        if swap_region is not None:
            self.swap_region = swap_region

    @property
    def username_field(self) -> str | None:
        """Target ID of the _usernameField reference (targets TextField)."""
        member = self.get_member("_usernameField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username_field.setter
    def username_field(self, target: str | TextField | None) -> None:
        """Set the _usernameField reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_usernameField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_usernameField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def password_field(self) -> str | None:
        """Target ID of the _passwordField reference (targets TextField)."""
        member = self.get_member("_passwordField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @password_field.setter
    def password_field(self, target: str | TextField | None) -> None:
        """Set the _passwordField reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_passwordField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_passwordField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def migrate_favorites(self) -> bool | None:
        """The _migrateFavorites field value."""
        member = self.get_member("_migrateFavorites")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrate_favorites.setter
    def migrate_favorites(self, value: bool) -> None:
        """Set the _migrateFavorites field value."""
        member = self.get_member("_migrateFavorites")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migrateFavorites", fields.FieldBool(value=value)
            )

    @property
    def overwrite_favorites(self) -> bool | None:
        """The _overwriteFavorites field value."""
        member = self.get_member("_overwriteFavorites")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overwrite_favorites.setter
    def overwrite_favorites(self, value: bool) -> None:
        """Set the _overwriteFavorites field value."""
        member = self.get_member("_overwriteFavorites")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_overwriteFavorites", fields.FieldBool(value=value)
            )

    @property
    def preserve_old_home(self) -> bool | None:
        """The _preserveOldHome field value."""
        member = self.get_member("_preserveOldHome")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_old_home.setter
    def preserve_old_home(self, value: bool) -> None:
        """Set the _preserveOldHome field value."""
        member = self.get_member("_preserveOldHome")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_preserveOldHome", fields.FieldBool(value=value)
            )

    @property
    def migrate_contacts(self) -> bool | None:
        """The _migrateContacts field value."""
        member = self.get_member("_migrateContacts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrate_contacts.setter
    def migrate_contacts(self, value: bool) -> None:
        """Set the _migrateContacts field value."""
        member = self.get_member("_migrateContacts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migrateContacts", fields.FieldBool(value=value)
            )

    @property
    def migrate_message_history(self) -> bool | None:
        """The _migrateMessageHistory field value."""
        member = self.get_member("_migrateMessageHistory")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrate_message_history.setter
    def migrate_message_history(self, value: bool) -> None:
        """Set the _migrateMessageHistory field value."""
        member = self.get_member("_migrateMessageHistory")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migrateMessageHistory", fields.FieldBool(value=value)
            )

    @property
    def migrate_records(self) -> bool | None:
        """The _migrateRecords field value."""
        member = self.get_member("_migrateRecords")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrate_records.setter
    def migrate_records(self, value: bool) -> None:
        """Set the _migrateRecords field value."""
        member = self.get_member("_migrateRecords")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migrateRecords", fields.FieldBool(value=value)
            )

    @property
    def migrate_cloud_variables(self) -> bool | None:
        """The _migrateCloudVariables field value."""
        member = self.get_member("_migrateCloudVariables")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrate_cloud_variables.setter
    def migrate_cloud_variables(self, value: bool) -> None:
        """Set the _migrateCloudVariables field value."""
        member = self.get_member("_migrateCloudVariables")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migrateCloudVariables", fields.FieldBool(value=value)
            )

    @property
    def migrated_cloud_variable_definitions(self) -> bool | None:
        """The _migratedCloudVariableDefinitions field value."""
        member = self.get_member("_migratedCloudVariableDefinitions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrated_cloud_variable_definitions.setter
    def migrated_cloud_variable_definitions(self, value: bool) -> None:
        """Set the _migratedCloudVariableDefinitions field value."""
        member = self.get_member("_migratedCloudVariableDefinitions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migratedCloudVariableDefinitions", fields.FieldBool(value=value)
            )

    @property
    def migrate_groups(self) -> bool | None:
        """The _migrateGroups field value."""
        member = self.get_member("_migrateGroups")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrate_groups.setter
    def migrate_groups(self, value: bool) -> None:
        """Set the _migrateGroups field value."""
        member = self.get_member("_migrateGroups")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_migrateGroups", fields.FieldBool(value=value)
            )

    @property
    def groups_root(self) -> str | None:
        """Target ID of the _groupsRoot reference (targets Slot)."""
        member = self.get_member("_groupsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @groups_root.setter
    def groups_root(self, target: str | Slot | None) -> None:
        """Set the _groupsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_groupsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_groupsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def groups_message(self) -> str | None:
        """Target ID of the _groupsMessage reference (targets Text)."""
        member = self.get_member("_groupsMessage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @groups_message.setter
    def groups_message(self, target: str | Text | None) -> None:
        """Set the _groupsMessage reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_groupsMessage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_groupsMessage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def load_groups_button(self) -> str | None:
        """Target ID of the _loadGroupsButton reference (targets Button)."""
        member = self.get_member("_loadGroupsButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @load_groups_button.setter
    def load_groups_button(self, target: str | Button | None) -> None:
        """Set the _loadGroupsButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_loadGroupsButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loadGroupsButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def current_state(self) -> members.FieldEnum | None:
        """The CurrentState member."""
        member = self.get_member("CurrentState")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @current_state.setter
    def current_state(self, value: members.FieldEnum) -> None:
        """Set the CurrentState member."""
        self.set_member("CurrentState", value)

    @property
    def swap_region(self) -> str | None:
        """Target ID of the _swapRegion reference (targets SlideSwapRegion)."""
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @swap_region.setter
    def swap_region(self, target: str | SlideSwapRegion | None) -> None:
        """Set the _swapRegion reference by target ID or SlideSwapRegion instance."""
        target_id: str | None = target.id if isinstance(target, SlideSwapRegion) else target  # type: ignore[assignment]
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_swapRegion",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion'),
            )

    async def set_overwrite(self, resolink: protocols.ResoniteLinkClient, button: str, data: str, overwrite: bool, debug: bool = False) -> dict:
        """Call the SetOverwrite sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            data: The data parameter.
            overwrite: The overwrite parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetOverwrite", {"button": button, "data": data, "overwrite": overwrite}, debug,
        )

    async def set_preserve_home(self, resolink: protocols.ResoniteLinkClient, button: str, data: str, overwrite: bool, debug: bool = False) -> dict:
        """Call the SetPreserveHome sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            data: The data parameter.
            overwrite: The overwrite parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetPreserveHome", {"button": button, "data": data, "overwrite": overwrite}, debug,
        )

    async def choose_all_data(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the ChooseAllData sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ChooseAllData", {"button": button, "eventData": event_data}, debug,
        )

    async def change_step(self, resolink: protocols.ResoniteLinkClient, butoon: str, event_data: str, target_state: str, debug: bool = False) -> dict:
        """Call the ChangeStep sync method.

        Args:
            resolink: Connected ResoniteLink client.
            butoon: The butoon parameter.
            event_data: The eventData parameter.
            target_state: The targetState parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ChangeStep", {"butoon": butoon, "eventData": event_data, "targetState": target_state}, debug,
        )

    async def save_group_selection_and_change(self, resolink: protocols.ResoniteLinkClient, butoon: str, event_data: str, target_state: str, debug: bool = False) -> dict:
        """Call the SaveGroupSelectionAndChange sync method.

        Args:
            resolink: Connected ResoniteLink client.
            butoon: The butoon parameter.
            event_data: The eventData parameter.
            target_state: The targetState parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SaveGroupSelectionAndChange", {"butoon": butoon, "eventData": event_data, "targetState": target_state}, debug,
        )

    async def check_login_and_next(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, next: str, debug: bool = False) -> dict:
        """Call the CheckLoginAndNext sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            next: The next parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "CheckLoginAndNext", {"button": button, "eventData": event_data, "next": next}, debug,
        )

