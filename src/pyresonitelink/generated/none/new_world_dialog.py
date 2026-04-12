"""Generated component: NewWorldDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.session_access_level import SessionAccessLevel
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NewWorldDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The NewWorldDialog component is used internally to control the new world prompt when making a new world in dash space.

    Used internally.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NewWorldDialog"

    def __init__(self, world_name: str | TextField | None = None, mobile_friendly: str | Checkbox | None = None, unsafe_mode: str | Checkbox | None = None, auto_port: str | Checkbox | None = None, port: str | TextField | None = None, access_level: SessionAccessLevel | str | None = None, preset_index: primitives.Int | None = None, ui_built: primitives.Bool | None = None, initialized: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_name: Initial value for _worldName.
            mobile_friendly: Initial value for _mobileFriendly.
            unsafe_mode: Initial value for _unsafeMode.
            auto_port: Initial value for _autoPort.
            port: Initial value for _port.
            access_level: Initial value for _accessLevel.
            preset_index: Initial value for _presetIndex.
            ui_built: Initial value for _uiBuilt.
            initialized: Initial value for _initialized.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_name is not None:
            self.world_name = world_name
        if mobile_friendly is not None:
            self.mobile_friendly = mobile_friendly
        if unsafe_mode is not None:
            self.unsafe_mode = unsafe_mode
        if auto_port is not None:
            self.auto_port = auto_port
        if port is not None:
            self.port = port
        if access_level is not None:
            self.access_level = access_level
        if preset_index is not None:
            self.preset_index = preset_index
        if ui_built is not None:
            self.ui_built = ui_built
        if initialized is not None:
            self.initialized = initialized

    @property
    def world_name(self) -> str | None:
        """The field to define the name of the new world."""
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
    def mobile_friendly(self) -> str | None:
        """Whether the new world should be mobile friendly."""
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
    def unsafe_mode(self) -> str | None:
        """Whether the new world is going to be unsafe mode."""
        member = self.get_member("_unsafeMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unsafe_mode.setter
    def unsafe_mode(self, target: str | Checkbox | None) -> None:
        """Set the _unsafeMode reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_unsafeMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unsafeMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def auto_port(self) -> str | None:
        """Whether the new world should boot with auto defined port."""
        member = self.get_member("_autoPort")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_port.setter
    def auto_port(self, target: str | Checkbox | None) -> None:
        """Set the _autoPort reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_autoPort")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_autoPort",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def port(self) -> str | None:
        """The port of the new world."""
        member = self.get_member("_port")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @port.setter
    def port(self, target: str | TextField | None) -> None:
        """Set the _port reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_port")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_port",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def access_level(self) -> SessionAccessLevel | None:
        """The access level of the new world."""
        member = self.get_member("_accessLevel")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SessionAccessLevel(member.value)
        return None

    @access_level.setter
    def access_level(self, value: SessionAccessLevel | str) -> None:
        """Set _accessLevel. The access level of the new world."""
        member = self.get_member("_accessLevel")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_accessLevel",
                members.FieldEnum(value=str(value)),
            )

    @property
    def preset_index(self) -> primitives.Int | None:
        """Which preset to use for the new world."""
        member = self.get_member("_presetIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preset_index.setter
    def preset_index(self, value: primitives.Int) -> None:
        """Set the _presetIndex field value."""
        member = self.get_member("_presetIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_presetIndex", fields.FieldInt(value=value)
            )

    @property
    def ui_built(self) -> primitives.Bool | None:
        """Whether the world UI is built."""
        member = self.get_member("_uiBuilt")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ui_built.setter
    def ui_built(self, value: primitives.Bool) -> None:
        """Set the _uiBuilt field value."""
        member = self.get_member("_uiBuilt")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_uiBuilt", fields.FieldBool(value=value)
            )

    @property
    def access_level_radios(self) -> members.SyncList | None:
        """A list of session access level options for the UI."""
        member = self.get_member("_accessLevelRadios")
        if isinstance(member, members.SyncList):
            return member
        return None

    @access_level_radios.setter
    def access_level_radios(self, value: members.SyncList) -> None:
        """Set _accessLevelRadios. A list of session access level options for the UI."""
        self.set_member("_accessLevelRadios", value)

    @property
    def initialized(self) -> primitives.Bool | None:
        """Whether the UI is built and ready."""
        member = self.get_member("_initialized")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initialized.setter
    def initialized(self, value: primitives.Bool) -> None:
        """Set the _initialized field value."""
        member = self.get_member("_initialized")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_initialized", fields.FieldBool(value=value)
            )

