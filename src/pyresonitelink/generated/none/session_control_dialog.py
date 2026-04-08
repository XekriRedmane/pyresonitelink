"""Generated component: SessionControlDialog."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.int_text_editor_parser import IntTextEditorParser
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.world_value_sync import WorldValueSync
from pyresonitelink.generated._types.session_access_level import SessionAccessLevel
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SessionControlDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SessionControlDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SessionControlDialog"

    def __init__(self, content_root: str | Slot | None = None, world_name: str | TextField | None = None, max_users: str | IntTextEditorParser | None = None, away_kick_enabled: str | Checkbox | None = None, away_kick_minutes: str | FloatTextEditorParser | None = None, autosave_enabled: str | Checkbox | None = None, autosave_minutes: str | FloatTextEditorParser | None = None, autoclean_enabled: str | Checkbox | None = None, autoclean_minutes: str | FloatTextEditorParser | None = None, mobile_friendly: str | Checkbox | None = None, hide_from_listing: str | Checkbox | None = None, description: str | TextField | None = None, world_name_button: str | Button | None = None, description_button: str | Button | None = None, max_users_button: str | Button | None = None, away_kick_enabled_button: str | Button | None = None, away_kick_minutes_button: str | Button | None = None, autosave_enabled_button: str | Button | None = None, autosave_minutes_button: str | Button | None = None, autoclean_enabled_button: str | Button | None = None, autoclean_minutes_button: str | Button | None = None, mobile_friendly_button: str | Button | None = None, hide_from_listing_button: str | Button | None = None, permission_overrides_indicator: str | Text | None = None, permission_overrides_button: str | Button | None = None, get_session_orb: str | Button | None = None, get_world_orb: str | Button | None = None, edit_mode: str | Button | None = None, copy_session_url: str | Button | None = None, copy_world_url: str | Button | None = None, copy_record_url: str | Button | None = None, world_name_sync: str | WorldValueSync[primitives.String] | None = None, description_sync: str | WorldValueSync[primitives.String] | None = None, max_users_sync: str | WorldValueSync[primitives.Int] | None = None, away_kick_enabled_sync: str | WorldValueSync[primitives.Bool] | None = None, away_kick_minutes_sync: str | WorldValueSync[primitives.Float] | None = None, autosave_enabled_sync: str | WorldValueSync[primitives.Bool] | None = None, autosave_minutes_sync: str | WorldValueSync[primitives.Float] | None = None, autoclean_enabled_sync: str | WorldValueSync[primitives.Bool] | None = None, autoclean_seconds_sync: str | WorldValueSync[primitives.Float] | None = None, mobile_friendly_sync: str | WorldValueSync[primitives.Bool] | None = None, hide_from_listing_sync: str | WorldValueSync[primitives.Bool] | None = None, edit_mode_sync: str | WorldValueSync[primitives.Bool] | None = None, access_level_sync: str | WorldValueSync[SessionAccessLevel] | None = None, custom_verifier_label: str | Text | None = None, custom_verifier_checkbox: str | Checkbox | None = None, custom_verifier_button: str | Button | None = None, custom_verifier_sync: str | WorldValueSync[primitives.Bool] | None = None, ui_content_root: str | Slot | None = None, slide_swap: str | SlideSwapRegion | None = None, save_world: str | Button | None = None, save_world_as: str | Button | None = None, save_world_copy: str | Button | None = None, enable_resonite_link: str | Button | None = None, resonite_link_port: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            content_root: Initial value for _contentRoot.
            world_name: Initial value for _worldName.
            max_users: Initial value for _maxUsers.
            away_kick_enabled: Initial value for _awayKickEnabled.
            away_kick_minutes: Initial value for _awayKickMinutes.
            autosave_enabled: Initial value for _autosaveEnabled.
            autosave_minutes: Initial value for _autosaveMinutes.
            autoclean_enabled: Initial value for _autocleanEnabled.
            autoclean_minutes: Initial value for _autocleanMinutes.
            mobile_friendly: Initial value for _mobileFriendly.
            hide_from_listing: Initial value for _hideFromListing.
            description: Initial value for _description.
            world_name_button: Initial value for _worldNameButton.
            description_button: Initial value for _descriptionButton.
            max_users_button: Initial value for _maxUsersButton.
            away_kick_enabled_button: Initial value for _awayKickEnabledButton.
            away_kick_minutes_button: Initial value for _awayKickMinutesButton.
            autosave_enabled_button: Initial value for _autosaveEnabledButton.
            autosave_minutes_button: Initial value for _autosaveMinutesButton.
            autoclean_enabled_button: Initial value for _autocleanEnabledButton.
            autoclean_minutes_button: Initial value for _autocleanMinutesButton.
            mobile_friendly_button: Initial value for _mobileFriendlyButton.
            hide_from_listing_button: Initial value for _hideFromListingButton.
            permission_overrides_indicator: Initial value for _permissionOverridesIndicator.
            permission_overrides_button: Initial value for _permissionOverridesButton.
            get_session_orb: Initial value for _getSessionOrb.
            get_world_orb: Initial value for _getWorldOrb.
            edit_mode: Initial value for _editMode.
            copy_session_url: Initial value for _copySessionURL.
            copy_world_url: Initial value for _copyWorldURL.
            copy_record_url: Initial value for _copyRecordURL.
            world_name_sync: Initial value for _worldNameSync.
            description_sync: Initial value for _descriptionSync.
            max_users_sync: Initial value for _maxUsersSync.
            away_kick_enabled_sync: Initial value for _awayKickEnabledSync.
            away_kick_minutes_sync: Initial value for _awayKickMinutesSync.
            autosave_enabled_sync: Initial value for _autosaveEnabledSync.
            autosave_minutes_sync: Initial value for _autosaveMinutesSync.
            autoclean_enabled_sync: Initial value for _autocleanEnabledSync.
            autoclean_seconds_sync: Initial value for _autocleanSecondsSync.
            mobile_friendly_sync: Initial value for _mobileFriendlySync.
            hide_from_listing_sync: Initial value for _hideFromListingSync.
            edit_mode_sync: Initial value for _editModeSync.
            access_level_sync: Initial value for _accessLevelSync.
            custom_verifier_label: Initial value for _customVerifierLabel.
            custom_verifier_checkbox: Initial value for _customVerifierCheckbox.
            custom_verifier_button: Initial value for _customVerifierButton.
            custom_verifier_sync: Initial value for _customVerifierSync.
            ui_content_root: Initial value for _uiContentRoot.
            slide_swap: Initial value for _slideSwap.
            save_world: Initial value for _saveWorld.
            save_world_as: Initial value for _saveWorldAs.
            save_world_copy: Initial value for _saveWorldCopy.
            enable_resonite_link: Initial value for _enableResoniteLink.
            resonite_link_port: Initial value for _resoniteLinkPort.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if content_root is not None:
            self.content_root = content_root
        if world_name is not None:
            self.world_name = world_name
        if max_users is not None:
            self.max_users = max_users
        if away_kick_enabled is not None:
            self.away_kick_enabled = away_kick_enabled
        if away_kick_minutes is not None:
            self.away_kick_minutes = away_kick_minutes
        if autosave_enabled is not None:
            self.autosave_enabled = autosave_enabled
        if autosave_minutes is not None:
            self.autosave_minutes = autosave_minutes
        if autoclean_enabled is not None:
            self.autoclean_enabled = autoclean_enabled
        if autoclean_minutes is not None:
            self.autoclean_minutes = autoclean_minutes
        if mobile_friendly is not None:
            self.mobile_friendly = mobile_friendly
        if hide_from_listing is not None:
            self.hide_from_listing = hide_from_listing
        if description is not None:
            self.description = description
        if world_name_button is not None:
            self.world_name_button = world_name_button
        if description_button is not None:
            self.description_button = description_button
        if max_users_button is not None:
            self.max_users_button = max_users_button
        if away_kick_enabled_button is not None:
            self.away_kick_enabled_button = away_kick_enabled_button
        if away_kick_minutes_button is not None:
            self.away_kick_minutes_button = away_kick_minutes_button
        if autosave_enabled_button is not None:
            self.autosave_enabled_button = autosave_enabled_button
        if autosave_minutes_button is not None:
            self.autosave_minutes_button = autosave_minutes_button
        if autoclean_enabled_button is not None:
            self.autoclean_enabled_button = autoclean_enabled_button
        if autoclean_minutes_button is not None:
            self.autoclean_minutes_button = autoclean_minutes_button
        if mobile_friendly_button is not None:
            self.mobile_friendly_button = mobile_friendly_button
        if hide_from_listing_button is not None:
            self.hide_from_listing_button = hide_from_listing_button
        if permission_overrides_indicator is not None:
            self.permission_overrides_indicator = permission_overrides_indicator
        if permission_overrides_button is not None:
            self.permission_overrides_button = permission_overrides_button
        if get_session_orb is not None:
            self.get_session_orb = get_session_orb
        if get_world_orb is not None:
            self.get_world_orb = get_world_orb
        if edit_mode is not None:
            self.edit_mode = edit_mode
        if copy_session_url is not None:
            self.copy_session_url = copy_session_url
        if copy_world_url is not None:
            self.copy_world_url = copy_world_url
        if copy_record_url is not None:
            self.copy_record_url = copy_record_url
        if world_name_sync is not None:
            self.world_name_sync = world_name_sync
        if description_sync is not None:
            self.description_sync = description_sync
        if max_users_sync is not None:
            self.max_users_sync = max_users_sync
        if away_kick_enabled_sync is not None:
            self.away_kick_enabled_sync = away_kick_enabled_sync
        if away_kick_minutes_sync is not None:
            self.away_kick_minutes_sync = away_kick_minutes_sync
        if autosave_enabled_sync is not None:
            self.autosave_enabled_sync = autosave_enabled_sync
        if autosave_minutes_sync is not None:
            self.autosave_minutes_sync = autosave_minutes_sync
        if autoclean_enabled_sync is not None:
            self.autoclean_enabled_sync = autoclean_enabled_sync
        if autoclean_seconds_sync is not None:
            self.autoclean_seconds_sync = autoclean_seconds_sync
        if mobile_friendly_sync is not None:
            self.mobile_friendly_sync = mobile_friendly_sync
        if hide_from_listing_sync is not None:
            self.hide_from_listing_sync = hide_from_listing_sync
        if edit_mode_sync is not None:
            self.edit_mode_sync = edit_mode_sync
        if access_level_sync is not None:
            self.access_level_sync = access_level_sync
        if custom_verifier_label is not None:
            self.custom_verifier_label = custom_verifier_label
        if custom_verifier_checkbox is not None:
            self.custom_verifier_checkbox = custom_verifier_checkbox
        if custom_verifier_button is not None:
            self.custom_verifier_button = custom_verifier_button
        if custom_verifier_sync is not None:
            self.custom_verifier_sync = custom_verifier_sync
        if ui_content_root is not None:
            self.ui_content_root = ui_content_root
        if slide_swap is not None:
            self.slide_swap = slide_swap
        if save_world is not None:
            self.save_world = save_world
        if save_world_as is not None:
            self.save_world_as = save_world_as
        if save_world_copy is not None:
            self.save_world_copy = save_world_copy
        if enable_resonite_link is not None:
            self.enable_resonite_link = enable_resonite_link
        if resonite_link_port is not None:
            self.resonite_link_port = resonite_link_port

    @property
    def active_tab(self) -> members.FieldEnum | None:
        """The ActiveTab member."""
        member = self.get_member("ActiveTab")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @active_tab.setter
    def active_tab(self, value: members.FieldEnum) -> None:
        """Set the ActiveTab member."""
        self.set_member("ActiveTab", value)

    @property
    def content_root(self) -> str | None:
        """Target ID of the _contentRoot reference (targets Slot)."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def world_name(self) -> str | None:
        """Target ID of the _worldName reference (targets TextField)."""
        member = self.get_member("_worldName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_name.setter
    def world_name(self, target: str | TextField | None) -> None:
        """Set the _worldName reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_worldName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worldName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def max_users(self) -> str | None:
        """Target ID of the _maxUsers reference (targets IntTextEditorParser)."""
        member = self.get_member("_maxUsers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_users.setter
    def max_users(self, target: str | IntTextEditorParser | None) -> None:
        """Set the _maxUsers reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_maxUsers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maxUsers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def away_kick_enabled(self) -> str | None:
        """Target ID of the _awayKickEnabled reference (targets Checkbox)."""
        member = self.get_member("_awayKickEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_enabled.setter
    def away_kick_enabled(self, target: str | Checkbox | None) -> None:
        """Set the _awayKickEnabled reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_awayKickEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_awayKickEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def away_kick_minutes(self) -> str | None:
        """Target ID of the _awayKickMinutes reference (targets FloatTextEditorParser)."""
        member = self.get_member("_awayKickMinutes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_minutes.setter
    def away_kick_minutes(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _awayKickMinutes reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_awayKickMinutes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_awayKickMinutes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def autosave_enabled(self) -> str | None:
        """Target ID of the _autosaveEnabled reference (targets Checkbox)."""
        member = self.get_member("_autosaveEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autosave_enabled.setter
    def autosave_enabled(self, target: str | Checkbox | None) -> None:
        """Set the _autosaveEnabled reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_autosaveEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autosaveEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def autosave_minutes(self) -> str | None:
        """Target ID of the _autosaveMinutes reference (targets FloatTextEditorParser)."""
        member = self.get_member("_autosaveMinutes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autosave_minutes.setter
    def autosave_minutes(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _autosaveMinutes reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_autosaveMinutes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autosaveMinutes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def autoclean_enabled(self) -> str | None:
        """Target ID of the _autocleanEnabled reference (targets Checkbox)."""
        member = self.get_member("_autocleanEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autoclean_enabled.setter
    def autoclean_enabled(self, target: str | Checkbox | None) -> None:
        """Set the _autocleanEnabled reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_autocleanEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autocleanEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def autoclean_minutes(self) -> str | None:
        """Target ID of the _autocleanMinutes reference (targets FloatTextEditorParser)."""
        member = self.get_member("_autocleanMinutes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autoclean_minutes.setter
    def autoclean_minutes(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _autocleanMinutes reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_autocleanMinutes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autocleanMinutes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def mobile_friendly(self) -> str | None:
        """Target ID of the _mobileFriendly reference (targets Checkbox)."""
        member = self.get_member("_mobileFriendly")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mobile_friendly.setter
    def mobile_friendly(self, target: str | Checkbox | None) -> None:
        """Set the _mobileFriendly reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_mobileFriendly")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mobileFriendly",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def hide_from_listing(self) -> str | None:
        """Target ID of the _hideFromListing reference (targets Checkbox)."""
        member = self.get_member("_hideFromListing")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hide_from_listing.setter
    def hide_from_listing(self, target: str | Checkbox | None) -> None:
        """Set the _hideFromListing reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_hideFromListing")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hideFromListing",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def description(self) -> str | None:
        """Target ID of the _description reference (targets TextField)."""
        member = self.get_member("_description")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description.setter
    def description(self, target: str | TextField | None) -> None:
        """Set the _description reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_description")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_description",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def world_name_button(self) -> str | None:
        """Target ID of the _worldNameButton reference (targets Button)."""
        member = self.get_member("_worldNameButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_name_button.setter
    def world_name_button(self, target: str | Button | None) -> None:
        """Set the _worldNameButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_worldNameButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worldNameButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def description_button(self) -> str | None:
        """Target ID of the _descriptionButton reference (targets Button)."""
        member = self.get_member("_descriptionButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description_button.setter
    def description_button(self, target: str | Button | None) -> None:
        """Set the _descriptionButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_descriptionButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_descriptionButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def max_users_button(self) -> str | None:
        """Target ID of the _maxUsersButton reference (targets Button)."""
        member = self.get_member("_maxUsersButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_users_button.setter
    def max_users_button(self, target: str | Button | None) -> None:
        """Set the _maxUsersButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_maxUsersButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maxUsersButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def away_kick_enabled_button(self) -> str | None:
        """Target ID of the _awayKickEnabledButton reference (targets Button)."""
        member = self.get_member("_awayKickEnabledButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_enabled_button.setter
    def away_kick_enabled_button(self, target: str | Button | None) -> None:
        """Set the _awayKickEnabledButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_awayKickEnabledButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_awayKickEnabledButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def away_kick_minutes_button(self) -> str | None:
        """Target ID of the _awayKickMinutesButton reference (targets Button)."""
        member = self.get_member("_awayKickMinutesButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_minutes_button.setter
    def away_kick_minutes_button(self, target: str | Button | None) -> None:
        """Set the _awayKickMinutesButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_awayKickMinutesButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_awayKickMinutesButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def autosave_enabled_button(self) -> str | None:
        """Target ID of the _autosaveEnabledButton reference (targets Button)."""
        member = self.get_member("_autosaveEnabledButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autosave_enabled_button.setter
    def autosave_enabled_button(self, target: str | Button | None) -> None:
        """Set the _autosaveEnabledButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_autosaveEnabledButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autosaveEnabledButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def autosave_minutes_button(self) -> str | None:
        """Target ID of the _autosaveMinutesButton reference (targets Button)."""
        member = self.get_member("_autosaveMinutesButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autosave_minutes_button.setter
    def autosave_minutes_button(self, target: str | Button | None) -> None:
        """Set the _autosaveMinutesButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_autosaveMinutesButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autosaveMinutesButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def autoclean_enabled_button(self) -> str | None:
        """Target ID of the _autocleanEnabledButton reference (targets Button)."""
        member = self.get_member("_autocleanEnabledButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autoclean_enabled_button.setter
    def autoclean_enabled_button(self, target: str | Button | None) -> None:
        """Set the _autocleanEnabledButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_autocleanEnabledButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autocleanEnabledButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def autoclean_minutes_button(self) -> str | None:
        """Target ID of the _autocleanMinutesButton reference (targets Button)."""
        member = self.get_member("_autocleanMinutesButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autoclean_minutes_button.setter
    def autoclean_minutes_button(self, target: str | Button | None) -> None:
        """Set the _autocleanMinutesButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_autocleanMinutesButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autocleanMinutesButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def mobile_friendly_button(self) -> str | None:
        """Target ID of the _mobileFriendlyButton reference (targets Button)."""
        member = self.get_member("_mobileFriendlyButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mobile_friendly_button.setter
    def mobile_friendly_button(self, target: str | Button | None) -> None:
        """Set the _mobileFriendlyButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_mobileFriendlyButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mobileFriendlyButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def hide_from_listing_button(self) -> str | None:
        """Target ID of the _hideFromListingButton reference (targets Button)."""
        member = self.get_member("_hideFromListingButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hide_from_listing_button.setter
    def hide_from_listing_button(self, target: str | Button | None) -> None:
        """Set the _hideFromListingButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_hideFromListingButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hideFromListingButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def permission_overrides_indicator(self) -> str | None:
        """Target ID of the _permissionOverridesIndicator reference (targets Text)."""
        member = self.get_member("_permissionOverridesIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @permission_overrides_indicator.setter
    def permission_overrides_indicator(self, target: str | Text | None) -> None:
        """Set the _permissionOverridesIndicator reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_permissionOverridesIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_permissionOverridesIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def permission_overrides_button(self) -> str | None:
        """Target ID of the _permissionOverridesButton reference (targets Button)."""
        member = self.get_member("_permissionOverridesButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @permission_overrides_button.setter
    def permission_overrides_button(self, target: str | Button | None) -> None:
        """Set the _permissionOverridesButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_permissionOverridesButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_permissionOverridesButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def get_session_orb(self) -> str | None:
        """Target ID of the _getSessionOrb reference (targets Button)."""
        member = self.get_member("_getSessionOrb")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @get_session_orb.setter
    def get_session_orb(self, target: str | Button | None) -> None:
        """Set the _getSessionOrb reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_getSessionOrb")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_getSessionOrb",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def get_world_orb(self) -> str | None:
        """Target ID of the _getWorldOrb reference (targets Button)."""
        member = self.get_member("_getWorldOrb")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @get_world_orb.setter
    def get_world_orb(self, target: str | Button | None) -> None:
        """Set the _getWorldOrb reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_getWorldOrb")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_getWorldOrb",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def edit_mode(self) -> str | None:
        """Target ID of the _editMode reference (targets Button)."""
        member = self.get_member("_editMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @edit_mode.setter
    def edit_mode(self, target: str | Button | None) -> None:
        """Set the _editMode reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_editMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_editMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def copy_session_url(self) -> str | None:
        """Target ID of the _copySessionURL reference (targets Button)."""
        member = self.get_member("_copySessionURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @copy_session_url.setter
    def copy_session_url(self, target: str | Button | None) -> None:
        """Set the _copySessionURL reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_copySessionURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_copySessionURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def copy_world_url(self) -> str | None:
        """Target ID of the _copyWorldURL reference (targets Button)."""
        member = self.get_member("_copyWorldURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @copy_world_url.setter
    def copy_world_url(self, target: str | Button | None) -> None:
        """Set the _copyWorldURL reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_copyWorldURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_copyWorldURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def copy_record_url(self) -> str | None:
        """Target ID of the _copyRecordURL reference (targets Button)."""
        member = self.get_member("_copyRecordURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @copy_record_url.setter
    def copy_record_url(self, target: str | Button | None) -> None:
        """Set the _copyRecordURL reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_copyRecordURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_copyRecordURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def access_level_radios(self) -> members.SyncList | None:
        """The _accessLevelRadios member."""
        member = self.get_member("_accessLevelRadios")
        if isinstance(member, members.SyncList):
            return member
        return None

    @access_level_radios.setter
    def access_level_radios(self, value: members.SyncList) -> None:
        """Set the _accessLevelRadios member."""
        self.set_member("_accessLevelRadios", value)

    @property
    def access_level_radios_buttons(self) -> members.SyncList | None:
        """The _accessLevelRadiosButtons member."""
        member = self.get_member("_accessLevelRadiosButtons")
        if isinstance(member, members.SyncList):
            return member
        return None

    @access_level_radios_buttons.setter
    def access_level_radios_buttons(self, value: members.SyncList) -> None:
        """Set the _accessLevelRadiosButtons member."""
        self.set_member("_accessLevelRadiosButtons", value)

    @property
    def world_name_sync(self) -> str | None:
        """Target ID of the _worldNameSync reference (targets WorldValueSync[primitives.String])."""
        member = self.get_member("_worldNameSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_name_sync.setter
    def world_name_sync(self, target: str | WorldValueSync[primitives.String] | None) -> None:
        """Set the _worldNameSync reference by target ID or WorldValueSync[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_worldNameSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worldNameSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<string>'),
            )

    @property
    def description_sync(self) -> str | None:
        """Target ID of the _descriptionSync reference (targets WorldValueSync[primitives.String])."""
        member = self.get_member("_descriptionSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description_sync.setter
    def description_sync(self, target: str | WorldValueSync[primitives.String] | None) -> None:
        """Set the _descriptionSync reference by target ID or WorldValueSync[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_descriptionSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_descriptionSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<string>'),
            )

    @property
    def max_users_sync(self) -> str | None:
        """Target ID of the _maxUsersSync reference (targets WorldValueSync[primitives.Int])."""
        member = self.get_member("_maxUsersSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_users_sync.setter
    def max_users_sync(self, target: str | WorldValueSync[primitives.Int] | None) -> None:
        """Set the _maxUsersSync reference by target ID or WorldValueSync[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_maxUsersSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maxUsersSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<int>'),
            )

    @property
    def away_kick_enabled_sync(self) -> str | None:
        """Target ID of the _awayKickEnabledSync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_awayKickEnabledSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_enabled_sync.setter
    def away_kick_enabled_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _awayKickEnabledSync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_awayKickEnabledSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_awayKickEnabledSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def away_kick_minutes_sync(self) -> str | None:
        """Target ID of the _awayKickMinutesSync reference (targets WorldValueSync[primitives.Float])."""
        member = self.get_member("_awayKickMinutesSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_kick_minutes_sync.setter
    def away_kick_minutes_sync(self, target: str | WorldValueSync[primitives.Float] | None) -> None:
        """Set the _awayKickMinutesSync reference by target ID or WorldValueSync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_awayKickMinutesSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_awayKickMinutesSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<float>'),
            )

    @property
    def autosave_enabled_sync(self) -> str | None:
        """Target ID of the _autosaveEnabledSync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_autosaveEnabledSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autosave_enabled_sync.setter
    def autosave_enabled_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _autosaveEnabledSync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_autosaveEnabledSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autosaveEnabledSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def autosave_minutes_sync(self) -> str | None:
        """Target ID of the _autosaveMinutesSync reference (targets WorldValueSync[primitives.Float])."""
        member = self.get_member("_autosaveMinutesSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autosave_minutes_sync.setter
    def autosave_minutes_sync(self, target: str | WorldValueSync[primitives.Float] | None) -> None:
        """Set the _autosaveMinutesSync reference by target ID or WorldValueSync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_autosaveMinutesSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autosaveMinutesSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<float>'),
            )

    @property
    def autoclean_enabled_sync(self) -> str | None:
        """Target ID of the _autocleanEnabledSync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_autocleanEnabledSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autoclean_enabled_sync.setter
    def autoclean_enabled_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _autocleanEnabledSync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_autocleanEnabledSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autocleanEnabledSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def autoclean_seconds_sync(self) -> str | None:
        """Target ID of the _autocleanSecondsSync reference (targets WorldValueSync[primitives.Float])."""
        member = self.get_member("_autocleanSecondsSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @autoclean_seconds_sync.setter
    def autoclean_seconds_sync(self, target: str | WorldValueSync[primitives.Float] | None) -> None:
        """Set the _autocleanSecondsSync reference by target ID or WorldValueSync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_autocleanSecondsSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autocleanSecondsSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<float>'),
            )

    @property
    def mobile_friendly_sync(self) -> str | None:
        """Target ID of the _mobileFriendlySync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_mobileFriendlySync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mobile_friendly_sync.setter
    def mobile_friendly_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _mobileFriendlySync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_mobileFriendlySync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mobileFriendlySync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def hide_from_listing_sync(self) -> str | None:
        """Target ID of the _hideFromListingSync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_hideFromListingSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hide_from_listing_sync.setter
    def hide_from_listing_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _hideFromListingSync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_hideFromListingSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hideFromListingSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def edit_mode_sync(self) -> str | None:
        """Target ID of the _editModeSync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_editModeSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @edit_mode_sync.setter
    def edit_mode_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _editModeSync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_editModeSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_editModeSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def access_level_sync(self) -> str | None:
        """Target ID of the _accessLevelSync reference (targets WorldValueSync[SessionAccessLevel])."""
        member = self.get_member("_accessLevelSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @access_level_sync.setter
    def access_level_sync(self, target: str | WorldValueSync[SessionAccessLevel] | None) -> None:
        """Set the _accessLevelSync reference by target ID or WorldValueSync[SessionAccessLevel] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_accessLevelSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_accessLevelSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>'),
            )

    @property
    def custom_verifier_label(self) -> str | None:
        """Target ID of the _customVerifierLabel reference (targets Text)."""
        member = self.get_member("_customVerifierLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_verifier_label.setter
    def custom_verifier_label(self, target: str | Text | None) -> None:
        """Set the _customVerifierLabel reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_customVerifierLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customVerifierLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def custom_verifier_checkbox(self) -> str | None:
        """Target ID of the _customVerifierCheckbox reference (targets Checkbox)."""
        member = self.get_member("_customVerifierCheckbox")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_verifier_checkbox.setter
    def custom_verifier_checkbox(self, target: str | Checkbox | None) -> None:
        """Set the _customVerifierCheckbox reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_customVerifierCheckbox")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customVerifierCheckbox",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def custom_verifier_button(self) -> str | None:
        """Target ID of the _customVerifierButton reference (targets Button)."""
        member = self.get_member("_customVerifierButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_verifier_button.setter
    def custom_verifier_button(self, target: str | Button | None) -> None:
        """Set the _customVerifierButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_customVerifierButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customVerifierButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def custom_verifier_sync(self) -> str | None:
        """Target ID of the _customVerifierSync reference (targets WorldValueSync[primitives.Bool])."""
        member = self.get_member("_customVerifierSync")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_verifier_sync.setter
    def custom_verifier_sync(self, target: str | WorldValueSync[primitives.Bool] | None) -> None:
        """Set the _customVerifierSync reference by target ID or WorldValueSync[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, WorldValueSync) else target  # type: ignore[assignment]
        member = self.get_member("_customVerifierSync")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customVerifierSync",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldValueSync<bool>'),
            )

    @property
    def ui_content_root(self) -> str | None:
        """Target ID of the _uiContentRoot reference (targets Slot)."""
        member = self.get_member("_uiContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ui_content_root.setter
    def ui_content_root(self, target: str | Slot | None) -> None:
        """Set the _uiContentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_uiContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_uiContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def slide_swap(self) -> str | None:
        """Target ID of the _slideSwap reference (targets SlideSwapRegion)."""
        member = self.get_member("_slideSwap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slide_swap.setter
    def slide_swap(self, target: str | SlideSwapRegion | None) -> None:
        """Set the _slideSwap reference by target ID or SlideSwapRegion instance."""
        target_id: str | None = target.id if isinstance(target, SlideSwapRegion) else target  # type: ignore[assignment]
        member = self.get_member("_slideSwap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slideSwap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion'),
            )

    @property
    def save_world(self) -> str | None:
        """Target ID of the _saveWorld reference (targets Button)."""
        member = self.get_member("_saveWorld")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_world.setter
    def save_world(self, target: str | Button | None) -> None:
        """Set the _saveWorld reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_saveWorld")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveWorld",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def save_world_as(self) -> str | None:
        """Target ID of the _saveWorldAs reference (targets Button)."""
        member = self.get_member("_saveWorldAs")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_world_as.setter
    def save_world_as(self, target: str | Button | None) -> None:
        """Set the _saveWorldAs reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_saveWorldAs")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveWorldAs",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def save_world_copy(self) -> str | None:
        """Target ID of the _saveWorldCopy reference (targets Button)."""
        member = self.get_member("_saveWorldCopy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_world_copy.setter
    def save_world_copy(self, target: str | Button | None) -> None:
        """Set the _saveWorldCopy reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_saveWorldCopy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_saveWorldCopy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def enable_resonite_link(self) -> str | None:
        """Target ID of the _enableResoniteLink reference (targets Button)."""
        member = self.get_member("_enableResoniteLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enable_resonite_link.setter
    def enable_resonite_link(self, target: str | Button | None) -> None:
        """Set the _enableResoniteLink reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_enableResoniteLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_enableResoniteLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def resonite_link_port(self) -> str | None:
        """Target ID of the _resoniteLinkPort reference (targets Text)."""
        member = self.get_member("_resoniteLinkPort")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @resonite_link_port.setter
    def resonite_link_port(self, target: str | Text | None) -> None:
        """Set the _resoniteLinkPort reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_resoniteLinkPort")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_resoniteLinkPort",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def tab_buttons(self) -> members.SyncList | None:
        """The _tabButtons member."""
        member = self.get_member("_tabButtons")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tab_buttons.setter
    def tab_buttons(self, value: members.SyncList) -> None:
        """Set the _tabButtons member."""
        self.set_member("_tabButtons", value)

