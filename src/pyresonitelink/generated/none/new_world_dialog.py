"""Generated component: NewWorldDialog."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NewWorldDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.NewWorldDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NewWorldDialog"

    def __init__(self, world_name: str | TextField | None = None, mobile_friendly: str | Checkbox | None = None, unsafe_mode: str | Checkbox | None = None, auto_port: str | Checkbox | None = None, port: str | TextField | None = None, preset_index: np.int32 | None = None, ui_built: bool | None = None, initialized: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_name: Initial value for _worldName.
            mobile_friendly: Initial value for _mobileFriendly.
            unsafe_mode: Initial value for _unsafeMode.
            auto_port: Initial value for _autoPort.
            port: Initial value for _port.
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
        if preset_index is not None:
            self.preset_index = preset_index
        if ui_built is not None:
            self.ui_built = ui_built
        if initialized is not None:
            self.initialized = initialized

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
    def unsafe_mode(self) -> str | None:
        """Target ID of the _unsafeMode reference (targets Checkbox)."""
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
        """Target ID of the _autoPort reference (targets Checkbox)."""
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
        """Target ID of the _port reference (targets TextField)."""
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
    def access_level(self) -> members.FieldEnum | None:
        """The _accessLevel member."""
        member = self.get_member("_accessLevel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @access_level.setter
    def access_level(self, value: members.FieldEnum) -> None:
        """Set the _accessLevel member."""
        self.set_member("_accessLevel", value)

    @property
    def preset_index(self) -> np.int32 | None:
        """The _presetIndex field value."""
        member = self.get_member("_presetIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preset_index.setter
    def preset_index(self, value: np.int32) -> None:
        """Set the _presetIndex field value."""
        member = self.get_member("_presetIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_presetIndex", fields.FieldInt(value=value)
            )

    @property
    def ui_built(self) -> bool | None:
        """The _uiBuilt field value."""
        member = self.get_member("_uiBuilt")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ui_built.setter
    def ui_built(self, value: bool) -> None:
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
    def initialized(self) -> bool | None:
        """The _initialized field value."""
        member = self.get_member("_initialized")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initialized.setter
    def initialized(self, value: bool) -> None:
        """Set the _initialized field value."""
        member = self.get_member("_initialized")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_initialized", fields.FieldBool(value=value)
            )

