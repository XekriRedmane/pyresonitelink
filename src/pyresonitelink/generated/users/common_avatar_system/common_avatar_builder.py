"""Generated component: CommonAvatarBuilder."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ilocomotion_module import ILocomotionModule
from pyresonitelink.generated._types.iempty_avatar_slot_handler import IEmptyAvatarSlotHandler
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CommonAvatarBuilder(GeneratedComponent, IEmptyAvatarSlotHandler, ICustomInspector, IWorldEventReceiver):
    """Common Avatar Builder is a component that is part of every world that defines the spawning behavior and routines to do for all users when they spawn into a world. This can be used to add world settings menus, change what parts of a user get automatically set up, and so on.

    Category: Users/Common Avatar System

    **Behavior**: This component gets read and executed every time a user respawns or joins into a world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatarBuilder"

    def __init__(self, load_cloud_avatars: primitives.Bool | None = None, auto_inject: str | Slot | None = None, setup_name_badges: primitives.Bool | None = None, setup_icon_badges: primitives.Bool | None = None, setup_server_voice: primitives.Bool | None = None, setup_client_voice: primitives.Bool | None = None, setup_server_tools: primitives.Bool | None = None, setup_client_tools: primitives.Bool | None = None, setup_locomotion: primitives.Bool | None = None, allow_locomotion: primitives.Bool | None = None, default_host_silenced: primitives.Bool | None = None, default_client_silenced: primitives.Bool | None = None, locomotion_modules: str | Slot | None = None, force_default_locomotion_module: str | ILocomotionModule | None = None, find_user_preferred_module: primitives.Bool | None = None, setup_item_shelves: primitives.Bool | None = None, parent_clients_to_server: primitives.Bool | None = None, align_tracking: primitives.Bool | None = None, empty_avatar_slot_handler: str | IEmptyAvatarSlotHandler | None = None, fill_empty_slots: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            load_cloud_avatars: Initial value for LoadCloudAvatars.
            auto_inject: Initial value for AutoInject.
            setup_name_badges: Initial value for SetupNameBadges.
            setup_icon_badges: Initial value for SetupIconBadges.
            setup_server_voice: Initial value for SetupServerVoice.
            setup_client_voice: Initial value for SetupClientVoice.
            setup_server_tools: Initial value for SetupServerTools.
            setup_client_tools: Initial value for SetupClientTools.
            setup_locomotion: Initial value for SetupLocomotion.
            allow_locomotion: Initial value for AllowLocomotion.
            default_host_silenced: Initial value for DefaultHostSilenced.
            default_client_silenced: Initial value for DefaultClientSilenced.
            locomotion_modules: Initial value for LocomotionModules.
            force_default_locomotion_module: Initial value for ForceDefaultLocomotionModule.
            find_user_preferred_module: Initial value for FindUserPreferredModule.
            setup_item_shelves: Initial value for SetupItemShelves.
            parent_clients_to_server: Initial value for ParentClientsToServer.
            align_tracking: Initial value for AlignTracking.
            empty_avatar_slot_handler: Initial value for EmptyAvatarSlotHandler.
            fill_empty_slots: Initial value for FillEmptySlots.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if load_cloud_avatars is not None:
            self.load_cloud_avatars = load_cloud_avatars
        if auto_inject is not None:
            self.auto_inject = auto_inject
        if setup_name_badges is not None:
            self.setup_name_badges = setup_name_badges
        if setup_icon_badges is not None:
            self.setup_icon_badges = setup_icon_badges
        if setup_server_voice is not None:
            self.setup_server_voice = setup_server_voice
        if setup_client_voice is not None:
            self.setup_client_voice = setup_client_voice
        if setup_server_tools is not None:
            self.setup_server_tools = setup_server_tools
        if setup_client_tools is not None:
            self.setup_client_tools = setup_client_tools
        if setup_locomotion is not None:
            self.setup_locomotion = setup_locomotion
        if allow_locomotion is not None:
            self.allow_locomotion = allow_locomotion
        if default_host_silenced is not None:
            self.default_host_silenced = default_host_silenced
        if default_client_silenced is not None:
            self.default_client_silenced = default_client_silenced
        if locomotion_modules is not None:
            self.locomotion_modules = locomotion_modules
        if force_default_locomotion_module is not None:
            self.force_default_locomotion_module = force_default_locomotion_module
        if find_user_preferred_module is not None:
            self.find_user_preferred_module = find_user_preferred_module
        if setup_item_shelves is not None:
            self.setup_item_shelves = setup_item_shelves
        if parent_clients_to_server is not None:
            self.parent_clients_to_server = parent_clients_to_server
        if align_tracking is not None:
            self.align_tracking = align_tracking
        if empty_avatar_slot_handler is not None:
            self.empty_avatar_slot_handler = empty_avatar_slot_handler
        if fill_empty_slots is not None:
            self.fill_empty_slots = fill_empty_slots

    @property
    def load_cloud_avatars(self) -> primitives.Bool | None:
        """Whether to load the User's set avatar, or load the default avatar instead."""
        member = self.get_member("LoadCloudAvatars")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @load_cloud_avatars.setter
    def load_cloud_avatars(self, value: primitives.Bool) -> None:
        """Set the LoadCloudAvatars field value."""
        member = self.get_member("LoadCloudAvatars")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoadCloudAvatars", fields.FieldBool(value=value)
            )

    @property
    def custom_avatar_templates(self) -> members.SyncList | None:
        """Avatars that user's will spawn into if they don't have a cloud avatar, or optionally force them into one of these templates."""
        member = self.get_member("CustomAvatarTemplates")
        if isinstance(member, members.SyncList):
            return member
        return None

    @custom_avatar_templates.setter
    def custom_avatar_templates(self, value: members.SyncList) -> None:
        """Set CustomAvatarTemplates. Avatars that user's will spawn into if they don't have a cloud avatar, or optionally force them into one of these templates."""
        self.set_member("CustomAvatarTemplates", value)

    @property
    def auto_inject(self) -> str | None:
        """A slot that will automatically be duplicated and added as a child of a user when they join the world. Certain components will use this to override user behavior when part of this slot's hierarchy, like Avatar Audio Configuration to name one."""
        member = self.get_member("AutoInject")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_inject.setter
    def auto_inject(self, target: str | Slot | None) -> None:
        """Set the AutoInject reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("AutoInject")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AutoInject",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def setup_name_badges(self) -> primitives.Bool | None:
        """Whether to set up the user's default name badge when they spawn"""
        member = self.get_member("SetupNameBadges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_name_badges.setter
    def setup_name_badges(self, value: primitives.Bool) -> None:
        """Set the SetupNameBadges field value."""
        member = self.get_member("SetupNameBadges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupNameBadges", fields.FieldBool(value=value)
            )

    @property
    def setup_icon_badges(self) -> primitives.Bool | None:
        """Whether to set up the user's default badges when they spawn."""
        member = self.get_member("SetupIconBadges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_icon_badges.setter
    def setup_icon_badges(self, value: primitives.Bool) -> None:
        """Set the SetupIconBadges field value."""
        member = self.get_member("SetupIconBadges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupIconBadges", fields.FieldBool(value=value)
            )

    @property
    def setup_server_voice(self) -> primitives.Bool | None:
        """Only used in kiosk mode."""
        member = self.get_member("SetupServerVoice")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_server_voice.setter
    def setup_server_voice(self, value: primitives.Bool) -> None:
        """Set the SetupServerVoice field value."""
        member = self.get_member("SetupServerVoice")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupServerVoice", fields.FieldBool(value=value)
            )

    @property
    def setup_client_voice(self) -> primitives.Bool | None:
        """Only used in kiosk mode."""
        member = self.get_member("SetupClientVoice")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_client_voice.setter
    def setup_client_voice(self, value: primitives.Bool) -> None:
        """Set the SetupClientVoice field value."""
        member = self.get_member("SetupClientVoice")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupClientVoice", fields.FieldBool(value=value)
            )

    @property
    def setup_server_tools(self) -> primitives.Bool | None:
        """Only used in kiosk mode."""
        member = self.get_member("SetupServerTools")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_server_tools.setter
    def setup_server_tools(self, value: primitives.Bool) -> None:
        """Set the SetupServerTools field value."""
        member = self.get_member("SetupServerTools")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupServerTools", fields.FieldBool(value=value)
            )

    @property
    def setup_client_tools(self) -> primitives.Bool | None:
        """Only used in kiosk mode."""
        member = self.get_member("SetupClientTools")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_client_tools.setter
    def setup_client_tools(self, value: primitives.Bool) -> None:
        """Set the SetupClientTools field value."""
        member = self.get_member("SetupClientTools")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupClientTools", fields.FieldBool(value=value)
            )

    @property
    def setup_locomotion(self) -> primitives.Bool | None:
        """Whether to give the user the default locomotion modules when they spawn."""
        member = self.get_member("SetupLocomotion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_locomotion.setter
    def setup_locomotion(self, value: primitives.Bool) -> None:
        """Set the SetupLocomotion field value."""
        member = self.get_member("SetupLocomotion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupLocomotion", fields.FieldBool(value=value)
            )

    @property
    def allow_locomotion(self) -> primitives.Bool | None:
        """Whether to allow the user to move using locomotion when they spawn."""
        member = self.get_member("AllowLocomotion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_locomotion.setter
    def allow_locomotion(self, value: primitives.Bool) -> None:
        """Set the AllowLocomotion field value."""
        member = self.get_member("AllowLocomotion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowLocomotion", fields.FieldBool(value=value)
            )

    @property
    def default_host_silenced(self) -> primitives.Bool | None:
        """Whether the user should be default muted to the host when they spawn."""
        member = self.get_member("DefaultHostSilenced")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_host_silenced.setter
    def default_host_silenced(self, value: primitives.Bool) -> None:
        """Set the DefaultHostSilenced field value."""
        member = self.get_member("DefaultHostSilenced")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultHostSilenced", fields.FieldBool(value=value)
            )

    @property
    def default_client_silenced(self) -> primitives.Bool | None:
        """Whether the user should be default muted on their end when they spawn."""
        member = self.get_member("DefaultClientSilenced")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_client_silenced.setter
    def default_client_silenced(self, value: primitives.Bool) -> None:
        """Set the DefaultClientSilenced field value."""
        member = self.get_member("DefaultClientSilenced")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultClientSilenced", fields.FieldBool(value=value)
            )

    @property
    def locomotion_modules(self) -> str | None:
        """The slot full of locomotion modules that the user will have by default after they spawn."""
        member = self.get_member("LocomotionModules")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locomotion_modules.setter
    def locomotion_modules(self, target: str | Slot | None) -> None:
        """Set the LocomotionModules reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("LocomotionModules")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocomotionModules",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def force_default_locomotion_module(self) -> str | None:
        """The locomotion to enable for the user by default when spawning rather than the one in that user's locomotion settings set in their dash."""
        member = self.get_member("ForceDefaultLocomotionModule")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @force_default_locomotion_module.setter
    def force_default_locomotion_module(self, target: str | ILocomotionModule | None) -> None:
        """Set the ForceDefaultLocomotionModule reference by target ID or ILocomotionModule instance."""
        target_id: str | None = target.id if isinstance(target, ILocomotionModule) else target  # type: ignore[assignment]
        member = self.get_member("ForceDefaultLocomotionModule")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ForceDefaultLocomotionModule",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ILocomotionModule'),
            )

    @property
    def find_user_preferred_module(self) -> primitives.Bool | None:
        """Whether to try to spawn the user into their preferred locomotion module they set in settings."""
        member = self.get_member("FindUserPreferredModule")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @find_user_preferred_module.setter
    def find_user_preferred_module(self, value: primitives.Bool) -> None:
        """Set the FindUserPreferredModule field value."""
        member = self.get_member("FindUserPreferredModule")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FindUserPreferredModule", fields.FieldBool(value=value)
            )

    @property
    def setup_item_shelves(self) -> primitives.Bool | None:
        """Whether to add item shelves to the user when they spawn."""
        member = self.get_member("SetupItemShelves")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_item_shelves.setter
    def setup_item_shelves(self, value: primitives.Bool) -> None:
        """Set the SetupItemShelves field value."""
        member = self.get_member("SetupItemShelves")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupItemShelves", fields.FieldBool(value=value)
            )

    @property
    def parent_clients_to_server(self) -> primitives.Bool | None:
        """Parents users that join under the host user's slot (yes this is what it does)"""
        member = self.get_member("ParentClientsToServer")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_clients_to_server.setter
    def parent_clients_to_server(self, value: primitives.Bool) -> None:
        """Set the ParentClientsToServer field value."""
        member = self.get_member("ParentClientsToServer")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentClientsToServer", fields.FieldBool(value=value)
            )

    @property
    def align_tracking(self) -> primitives.Bool | None:
        """used in Kiosk mode in dash space to show Debug tracking visuals"""
        member = self.get_member("AlignTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @align_tracking.setter
    def align_tracking(self, value: primitives.Bool) -> None:
        """Set the AlignTracking field value."""
        member = self.get_member("AlignTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlignTracking", fields.FieldBool(value=value)
            )

    @property
    def empty_avatar_slot_handler(self) -> str | None:
        """Uses this component to handle empty slots like head and hands on a spawning avatar."""
        member = self.get_member("EmptyAvatarSlotHandler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @empty_avatar_slot_handler.setter
    def empty_avatar_slot_handler(self, target: str | IEmptyAvatarSlotHandler | None) -> None:
        """Set the EmptyAvatarSlotHandler reference by target ID or IEmptyAvatarSlotHandler instance."""
        target_id: str | None = target.id if isinstance(target, IEmptyAvatarSlotHandler) else target  # type: ignore[assignment]
        member = self.get_member("EmptyAvatarSlotHandler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmptyAvatarSlotHandler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.IEmptyAvatarSlotHandler'),
            )

    @property
    def fill_empty_slots(self) -> primitives.Bool | None:
        """Whether to fill empty AvatarObjectSlots with default head and hand objects if they are missing on their loaded avatar."""
        member = self.get_member("FillEmptySlots")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_empty_slots.setter
    def fill_empty_slots(self, value: primitives.Bool) -> None:
        """Set the FillEmptySlots field value."""
        member = self.get_member("FillEmptySlots")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillEmptySlots", fields.FieldBool(value=value)
            )

