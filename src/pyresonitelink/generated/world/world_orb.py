"""Generated component: WorldOrb."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.ring_mesh import RingMesh
from pyresonitelink.generated._types.unlit_material import UnlitMaterial
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.projection360_material import Projection360Material
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.new_world_dialog import NewWorldDialog
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_link import IWorldLink
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldOrb(GeneratedComponent, ITouchable, IWorldLink, IMaterialApplyPolicy, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldOrb.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldOrb"

    def __init__(self, session_starting_user: str | User | None = None, url: str | None = None, active_users: np.int32 | None = None, record_state_updated: bool | None = None, is_public: bool | None = None, can_modify: bool | None = None, long_press_indicator_color: primitives.ColorX | None = None, long_press_time: np.float32 | None = None, long_press_indicator: str | RingMesh | None = None, long_press_indicator_material: str | UnlitMaterial | None = None, last_fetched_url: str | None = None, is_read_only: bool | None = None, orb_root: str | Slot | None = None, info_root: str | Slot | None = None, thumb_tex: str | StaticTexture2D | None = None, thumb_material: str | Projection360Material | None = None, shell_material: str | PBS_RimMetallic | None = None, name_text: str | TextRenderer | None = None, creator_text: str | TextRenderer | None = None, visits_text: str | TextRenderer | None = None, users_text: str | TextRenderer | None = None, name_position: str | IField[primitives.Float3] | None = None, creator_position: str | IField[primitives.Float3] | None = None, visits_position: str | IField[primitives.Float3] | None = None, users_position: str | IField[primitives.Float3] | None = None, user_count_text: str | IField[str] | None = None, size_drive: str | IField[primitives.Float3] | None = None, icon_slot: str | Slot | None = None, icon_texture: str | StaticTexture2D | None = None, icon_material: str | UnlitMaterial | None = None, icon_position: str | IField[primitives.Float3] | None = None, session_start_dialog: str | NewWorldDialog | None = None, last_touch: np.float64 | None = None, last_flash: np.float64 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            session_starting_user: Initial value for SessionStartingUser.
            url: Initial value for URL.
            active_users: Initial value for ActiveUsers.
            record_state_updated: Initial value for RecordStateUpdated.
            is_public: Initial value for IsPublic.
            can_modify: Initial value for CanModify.
            long_press_indicator_color: Initial value for LongPressIndicatorColor.
            long_press_time: Initial value for LongPressTime.
            long_press_indicator: Initial value for _longPressIndicator.
            long_press_indicator_material: Initial value for _longPressIndicatorMaterial.
            last_fetched_url: Initial value for _lastFetchedUrl.
            is_read_only: Initial value for _isReadOnly.
            orb_root: Initial value for _orbRoot.
            info_root: Initial value for _infoRoot.
            thumb_tex: Initial value for _thumbTex.
            thumb_material: Initial value for _thumbMaterial.
            shell_material: Initial value for _shellMaterial.
            name_text: Initial value for _nameText.
            creator_text: Initial value for _creatorText.
            visits_text: Initial value for _visitsText.
            users_text: Initial value for _usersText.
            name_position: Initial value for _namePosition.
            creator_position: Initial value for _creatorPosition.
            visits_position: Initial value for _visitsPosition.
            users_position: Initial value for _usersPosition.
            user_count_text: Initial value for _userCountText.
            size_drive: Initial value for _sizeDrive.
            icon_slot: Initial value for _iconSlot.
            icon_texture: Initial value for _iconTexture.
            icon_material: Initial value for _iconMaterial.
            icon_position: Initial value for _iconPosition.
            session_start_dialog: Initial value for _sessionStartDialog.
            last_touch: Initial value for _lastTouch.
            last_flash: Initial value for _lastFlash.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if session_starting_user is not None:
            self.session_starting_user = session_starting_user
        if url is not None:
            self.url = url
        if active_users is not None:
            self.active_users = active_users
        if record_state_updated is not None:
            self.record_state_updated = record_state_updated
        if is_public is not None:
            self.is_public = is_public
        if can_modify is not None:
            self.can_modify = can_modify
        if long_press_indicator_color is not None:
            self.long_press_indicator_color = long_press_indicator_color
        if long_press_time is not None:
            self.long_press_time = long_press_time
        if long_press_indicator is not None:
            self.long_press_indicator = long_press_indicator
        if long_press_indicator_material is not None:
            self.long_press_indicator_material = long_press_indicator_material
        if last_fetched_url is not None:
            self.last_fetched_url = last_fetched_url
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if orb_root is not None:
            self.orb_root = orb_root
        if info_root is not None:
            self.info_root = info_root
        if thumb_tex is not None:
            self.thumb_tex = thumb_tex
        if thumb_material is not None:
            self.thumb_material = thumb_material
        if shell_material is not None:
            self.shell_material = shell_material
        if name_text is not None:
            self.name_text = name_text
        if creator_text is not None:
            self.creator_text = creator_text
        if visits_text is not None:
            self.visits_text = visits_text
        if users_text is not None:
            self.users_text = users_text
        if name_position is not None:
            self.name_position = name_position
        if creator_position is not None:
            self.creator_position = creator_position
        if visits_position is not None:
            self.visits_position = visits_position
        if users_position is not None:
            self.users_position = users_position
        if user_count_text is not None:
            self.user_count_text = user_count_text
        if size_drive is not None:
            self.size_drive = size_drive
        if icon_slot is not None:
            self.icon_slot = icon_slot
        if icon_texture is not None:
            self.icon_texture = icon_texture
        if icon_material is not None:
            self.icon_material = icon_material
        if icon_position is not None:
            self.icon_position = icon_position
        if session_start_dialog is not None:
            self.session_start_dialog = session_start_dialog
        if last_touch is not None:
            self.last_touch = last_touch
        if last_flash is not None:
            self.last_flash = last_flash

    @property
    def session_starting_user(self) -> str | None:
        """Target ID of the SessionStartingUser reference (targets User)."""
        member = self.get_member("SessionStartingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @session_starting_user.setter
    def session_starting_user(self, target: str | User | None) -> None:
        """Set the SessionStartingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("SessionStartingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SessionStartingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def url(self) -> str | None:
        """The URL field value."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def active_session_urls(self) -> members.SyncList | None:
        """The ActiveSessionURLs member."""
        member = self.get_member("ActiveSessionURLs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @active_session_urls.setter
    def active_session_urls(self, value: members.SyncList) -> None:
        """Set the ActiveSessionURLs member."""
        self.set_member("ActiveSessionURLs", value)

    @property
    def visit(self) -> members.FieldEnum | None:
        """The Visit member."""
        member = self.get_member("Visit")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @visit.setter
    def visit(self, value: members.FieldEnum) -> None:
        """Set the Visit member."""
        self.set_member("Visit", value)

    @property
    def active_users(self) -> np.int32 | None:
        """The ActiveUsers field value."""
        member = self.get_member("ActiveUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_users.setter
    def active_users(self, value: np.int32) -> None:
        """Set the ActiveUsers field value."""
        member = self.get_member("ActiveUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUsers", fields.FieldInt(value=value)
            )

    @property
    def record_state_updated(self) -> bool | None:
        """The RecordStateUpdated field value."""
        member = self.get_member("RecordStateUpdated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @record_state_updated.setter
    def record_state_updated(self, value: bool) -> None:
        """Set the RecordStateUpdated field value."""
        member = self.get_member("RecordStateUpdated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RecordStateUpdated", fields.FieldBool(value=value)
            )

    @property
    def is_public(self) -> bool | None:
        """The IsPublic field value."""
        member = self.get_member("IsPublic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_public.setter
    def is_public(self, value: bool) -> None:
        """Set the IsPublic field value."""
        member = self.get_member("IsPublic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPublic", fields.FieldBool(value=value)
            )

    @property
    def can_modify(self) -> bool | None:
        """The CanModify field value."""
        member = self.get_member("CanModify")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_modify.setter
    def can_modify(self, value: bool) -> None:
        """Set the CanModify field value."""
        member = self.get_member("CanModify")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CanModify", fields.FieldBool(value=value)
            )

    @property
    def long_press_indicator_color(self) -> primitives.ColorX | None:
        """The LongPressIndicatorColor field value."""
        member = self.get_member("LongPressIndicatorColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @long_press_indicator_color.setter
    def long_press_indicator_color(self, value: primitives.ColorX) -> None:
        """Set the LongPressIndicatorColor field value."""
        member = self.get_member("LongPressIndicatorColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LongPressIndicatorColor", fields.FieldColorX(value=value)
            )

    @property
    def long_press_time(self) -> np.float32 | None:
        """The LongPressTime field value."""
        member = self.get_member("LongPressTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @long_press_time.setter
    def long_press_time(self, value: np.float32) -> None:
        """Set the LongPressTime field value."""
        member = self.get_member("LongPressTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LongPressTime", fields.FieldFloat(value=value)
            )

    @property
    def long_press_indicator(self) -> str | None:
        """Target ID of the _longPressIndicator reference (targets RingMesh)."""
        member = self.get_member("_longPressIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @long_press_indicator.setter
    def long_press_indicator(self, target: str | RingMesh | None) -> None:
        """Set the _longPressIndicator reference by target ID or RingMesh instance."""
        target_id: str | None = target.id if isinstance(target, RingMesh) else target  # type: ignore[assignment]
        member = self.get_member("_longPressIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_longPressIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RingMesh'),
            )

    @property
    def long_press_indicator_material(self) -> str | None:
        """Target ID of the _longPressIndicatorMaterial reference (targets UnlitMaterial)."""
        member = self.get_member("_longPressIndicatorMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @long_press_indicator_material.setter
    def long_press_indicator_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _longPressIndicatorMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_longPressIndicatorMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_longPressIndicatorMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def last_fetched_url(self) -> str | None:
        """The _lastFetchedUrl field value."""
        member = self.get_member("_lastFetchedUrl")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_fetched_url.setter
    def last_fetched_url(self, value: str) -> None:
        """Set the _lastFetchedUrl field value."""
        member = self.get_member("_lastFetchedUrl")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastFetchedUrl", fields.FieldUri(value=value)
            )

    @property
    def is_read_only(self) -> bool | None:
        """The _isReadOnly field value."""
        member = self.get_member("_isReadOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_read_only.setter
    def is_read_only(self, value: bool) -> None:
        """Set the _isReadOnly field value."""
        member = self.get_member("_isReadOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_isReadOnly", fields.FieldBool(value=value)
            )

    @property
    def orb_root(self) -> str | None:
        """Target ID of the _orbRoot reference (targets Slot)."""
        member = self.get_member("_orbRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @orb_root.setter
    def orb_root(self, target: str | Slot | None) -> None:
        """Set the _orbRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_orbRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_orbRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def info_root(self) -> str | None:
        """Target ID of the _infoRoot reference (targets Slot)."""
        member = self.get_member("_infoRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @info_root.setter
    def info_root(self, target: str | Slot | None) -> None:
        """Set the _infoRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_infoRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_infoRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def thumb_tex(self) -> str | None:
        """Target ID of the _thumbTex reference (targets StaticTexture2D)."""
        member = self.get_member("_thumbTex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thumb_tex.setter
    def thumb_tex(self, target: str | StaticTexture2D | None) -> None:
        """Set the _thumbTex reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_thumbTex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thumbTex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

    @property
    def thumb_material(self) -> str | None:
        """Target ID of the _thumbMaterial reference (targets Projection360Material)."""
        member = self.get_member("_thumbMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thumb_material.setter
    def thumb_material(self, target: str | Projection360Material | None) -> None:
        """Set the _thumbMaterial reference by target ID or Projection360Material instance."""
        target_id: str | None = target.id if isinstance(target, Projection360Material) else target  # type: ignore[assignment]
        member = self.get_member("_thumbMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thumbMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Projection360Material'),
            )

    @property
    def shell_material(self) -> str | None:
        """Target ID of the _shellMaterial reference (targets PBS_RimMetallic)."""
        member = self.get_member("_shellMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shell_material.setter
    def shell_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _shellMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_shellMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shellMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def name_text(self) -> str | None:
        """Target ID of the _nameText reference (targets TextRenderer)."""
        member = self.get_member("_nameText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_text.setter
    def name_text(self, target: str | TextRenderer | None) -> None:
        """Set the _nameText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_nameText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nameText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def creator_text(self) -> str | None:
        """Target ID of the _creatorText reference (targets TextRenderer)."""
        member = self.get_member("_creatorText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @creator_text.setter
    def creator_text(self, target: str | TextRenderer | None) -> None:
        """Set the _creatorText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_creatorText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_creatorText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def visits_text(self) -> str | None:
        """Target ID of the _visitsText reference (targets TextRenderer)."""
        member = self.get_member("_visitsText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visits_text.setter
    def visits_text(self, target: str | TextRenderer | None) -> None:
        """Set the _visitsText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_visitsText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visitsText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def users_text(self) -> str | None:
        """Target ID of the _usersText reference (targets TextRenderer)."""
        member = self.get_member("_usersText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @users_text.setter
    def users_text(self, target: str | TextRenderer | None) -> None:
        """Set the _usersText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_usersText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_usersText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def name_position(self) -> str | None:
        """Target ID of the _namePosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_namePosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_position.setter
    def name_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _namePosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_namePosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_namePosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def creator_position(self) -> str | None:
        """Target ID of the _creatorPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_creatorPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @creator_position.setter
    def creator_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _creatorPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_creatorPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_creatorPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def visits_position(self) -> str | None:
        """Target ID of the _visitsPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_visitsPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visits_position.setter
    def visits_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _visitsPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visitsPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visitsPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def users_position(self) -> str | None:
        """Target ID of the _usersPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_usersPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @users_position.setter
    def users_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _usersPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_usersPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_usersPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def user_count_text(self) -> str | None:
        """Target ID of the _userCountText reference (targets IField[str])."""
        member = self.get_member("_userCountText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_count_text.setter
    def user_count_text(self, target: str | IField[str] | None) -> None:
        """Set the _userCountText reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_userCountText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userCountText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def size_drive(self) -> str | None:
        """Target ID of the _sizeDrive reference (targets IField[primitives.Float3])."""
        member = self.get_member("_sizeDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_drive.setter
    def size_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _sizeDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sizeDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sizeDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def icon_slot(self) -> str | None:
        """Target ID of the _iconSlot reference (targets Slot)."""
        member = self.get_member("_iconSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_slot.setter
    def icon_slot(self, target: str | Slot | None) -> None:
        """Set the _iconSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_iconSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def icon_texture(self) -> str | None:
        """Target ID of the _iconTexture reference (targets StaticTexture2D)."""
        member = self.get_member("_iconTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_texture.setter
    def icon_texture(self, target: str | StaticTexture2D | None) -> None:
        """Set the _iconTexture reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_iconTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

    @property
    def icon_material(self) -> str | None:
        """Target ID of the _iconMaterial reference (targets UnlitMaterial)."""
        member = self.get_member("_iconMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_material.setter
    def icon_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _iconMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_iconMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def icon_position(self) -> str | None:
        """Target ID of the _iconPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_iconPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_position.setter
    def icon_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _iconPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_iconPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def session_start_dialog(self) -> str | None:
        """Target ID of the _sessionStartDialog reference (targets NewWorldDialog)."""
        member = self.get_member("_sessionStartDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @session_start_dialog.setter
    def session_start_dialog(self, target: str | NewWorldDialog | None) -> None:
        """Set the _sessionStartDialog reference by target ID or NewWorldDialog instance."""
        target_id: str | None = target.id if isinstance(target, NewWorldDialog) else target  # type: ignore[assignment]
        member = self.get_member("_sessionStartDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sessionStartDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.NewWorldDialog'),
            )

    @property
    def last_touch(self) -> np.float64 | None:
        """The _lastTouch field value."""
        member = self.get_member("_lastTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_touch.setter
    def last_touch(self, value: np.float64) -> None:
        """Set the _lastTouch field value."""
        member = self.get_member("_lastTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastTouch", fields.FieldDouble(value=value)
            )

    @property
    def last_flash(self) -> np.float64 | None:
        """The _lastFlash field value."""
        member = self.get_member("_lastFlash")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_flash.setter
    def last_flash(self, value: np.float64) -> None:
        """Set the _lastFlash field value."""
        member = self.get_member("_lastFlash")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastFlash", fields.FieldDouble(value=value)
            )

