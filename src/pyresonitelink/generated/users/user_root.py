"""Generated component: UserRoot."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.irender_settings_source import IRenderSettingsSource
from pyresonitelink.generated._types.screen_controller import ScreenController
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.audio_listener import AudioListener
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserRoot(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserRoot component can be found on the top slot of a user, this component references the user's AvatarRenderSettings, ScreenController and any current AvatarUserRootOverrideAssigners.

    Category: Users

    Usually users find the slot containing this component by using the
    ProtoFlux node User Root Slot.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserRoot"

    def __init__(self, render_settings: str | IRenderSettingsSource | None = None, screen_controller: str | ScreenController | None = None, override_root: str | Slot | None = None, override_view: str | Slot | None = None, primary_listener: str | AudioListener | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            render_settings: Initial value for RenderSettings.
            screen_controller: Initial value for ScreenController.
            override_root: Initial value for OverrideRoot.
            override_view: Initial value for OverrideView.
            primary_listener: Initial value for PrimaryListener.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if render_settings is not None:
            self.render_settings = render_settings
        if screen_controller is not None:
            self.screen_controller = screen_controller
        if override_root is not None:
            self.override_root = override_root
        if override_view is not None:
            self.override_view = override_view
        if primary_listener is not None:
            self.primary_listener = primary_listener

    @property
    def render_settings(self) -> str | None:
        """The user's render settings. Usually part of an avatar."""
        member = self.get_member("RenderSettings")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_settings.setter
    def render_settings(self, target: str | IRenderSettingsSource | None) -> None:
        """Set the RenderSettings reference by target ID or IRenderSettingsSource instance."""
        target_id: str | None = target.id if isinstance(target, IRenderSettingsSource) else target  # type: ignore[assignment]
        member = self.get_member("RenderSettings")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RenderSettings",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IRenderSettingsSource'),
            )

    @property
    def screen_controller(self) -> str | None:
        """The screen controller that the user is using to control the game."""
        member = self.get_member("ScreenController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_controller.setter
    def screen_controller(self, target: str | ScreenController | None) -> None:
        """Set the ScreenController reference by target ID or ScreenController instance."""
        target_id: str | None = target.id if isinstance(target, ScreenController) else target  # type: ignore[assignment]
        member = self.get_member("ScreenController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ScreenController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScreenController'),
            )

    @property
    def override_root(self) -> str | None:
        """The slot currently overriding the user's root position locally for rendering."""
        member = self.get_member("OverrideRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_root.setter
    def override_root(self, target: str | Slot | None) -> None:
        """Set the OverrideRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def override_view(self) -> str | None:
        """The slot currently overriding the user's view position locally for rendering."""
        member = self.get_member("OverrideView")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_view.setter
    def override_view(self, target: str | Slot | None) -> None:
        """Set the OverrideView reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideView")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideView",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def primary_listener(self) -> str | None:
        """Target ID of the PrimaryListener reference (targets AudioListener)."""
        member = self.get_member("PrimaryListener")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @primary_listener.setter
    def primary_listener(self, target: str | AudioListener | None) -> None:
        """Set the PrimaryListener reference by target ID or AudioListener instance."""
        target_id: str | None = target.id if isinstance(target, AudioListener) else target  # type: ignore[assignment]
        member = self.get_member("PrimaryListener")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PrimaryListener",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioListener'),
            )

