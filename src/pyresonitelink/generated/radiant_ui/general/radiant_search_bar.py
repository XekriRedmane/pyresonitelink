"""Generated component: RadiantSearchBar."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.tiled_raw_image import TiledRawImage
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadiantSearchBar(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RadiantSearchBar.

    Category: Radiant UI/General
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadiantSearchBar"

    def __init__(self, search_term: primitives.String | None = None, is_searching: primitives.Bool | None = None, search_anim_tile_speed: primitives.Float | None = None, search_anim_color: primitives.ColorX | None = None, text_field: str | TextField | None = None, search_text: str | Text | None = None, default_text: str | Text | None = None, searching_visual: str | TiledRawImage | None = None, cancel_button: str | Button | None = None, default_visible: str | IField[primitives.Bool] | None = None, searching_animation_color: str | IField[primitives.ColorX] | None = None, searching_texture_offset: str | IField[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            search_term: Initial value for SearchTerm.
            is_searching: Initial value for IsSearching.
            search_anim_tile_speed: Initial value for SearchAnimTileSpeed.
            search_anim_color: Initial value for SearchAnimColor.
            text_field: Initial value for _textField.
            search_text: Initial value for _searchText.
            default_text: Initial value for _defaultText.
            searching_visual: Initial value for _searchingVisual.
            cancel_button: Initial value for _cancelButton.
            default_visible: Initial value for _defaultVisible.
            searching_animation_color: Initial value for _searchingAnimationColor.
            searching_texture_offset: Initial value for _searchingTextureOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if search_term is not None:
            self.search_term = search_term
        if is_searching is not None:
            self.is_searching = is_searching
        if search_anim_tile_speed is not None:
            self.search_anim_tile_speed = search_anim_tile_speed
        if search_anim_color is not None:
            self.search_anim_color = search_anim_color
        if text_field is not None:
            self.text_field = text_field
        if search_text is not None:
            self.search_text = search_text
        if default_text is not None:
            self.default_text = default_text
        if searching_visual is not None:
            self.searching_visual = searching_visual
        if cancel_button is not None:
            self.cancel_button = cancel_button
        if default_visible is not None:
            self.default_visible = default_visible
        if searching_animation_color is not None:
            self.searching_animation_color = searching_animation_color
        if searching_texture_offset is not None:
            self.searching_texture_offset = searching_texture_offset

    @property
    def search_term(self) -> primitives.String | None:
        """The SearchTerm field value."""
        member = self.get_member("SearchTerm")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_term.setter
    def search_term(self, value: primitives.String) -> None:
        """Set the SearchTerm field value."""
        member = self.get_member("SearchTerm")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchTerm", fields.FieldString(value=value)
            )

    @property
    def is_searching(self) -> primitives.Bool | None:
        """The IsSearching field value."""
        member = self.get_member("IsSearching")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_searching.setter
    def is_searching(self, value: primitives.Bool) -> None:
        """Set the IsSearching field value."""
        member = self.get_member("IsSearching")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSearching", fields.FieldBool(value=value)
            )

    @property
    def search_anim_tile_speed(self) -> primitives.Float | None:
        """The SearchAnimTileSpeed field value."""
        member = self.get_member("SearchAnimTileSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_anim_tile_speed.setter
    def search_anim_tile_speed(self, value: primitives.Float) -> None:
        """Set the SearchAnimTileSpeed field value."""
        member = self.get_member("SearchAnimTileSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchAnimTileSpeed", fields.FieldFloat(value=value)
            )

    @property
    def search_anim_color(self) -> primitives.ColorX | None:
        """The SearchAnimColor field value."""
        member = self.get_member("SearchAnimColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @search_anim_color.setter
    def search_anim_color(self, value: primitives.ColorX) -> None:
        """Set the SearchAnimColor field value."""
        member = self.get_member("SearchAnimColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SearchAnimColor", fields.FieldColorX(value=value)
            )

    @property
    def text_field(self) -> str | None:
        """Target ID of the _textField reference (targets TextField)."""
        member = self.get_member("_textField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_field.setter
    def text_field(self, target: str | TextField | None) -> None:
        """Set the _textField reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_textField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def search_text(self) -> str | None:
        """Target ID of the _searchText reference (targets Text)."""
        member = self.get_member("_searchText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search_text.setter
    def search_text(self, target: str | Text | None) -> None:
        """Set the _searchText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_searchText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_searchText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def default_text(self) -> str | None:
        """Target ID of the _defaultText reference (targets Text)."""
        member = self.get_member("_defaultText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_text.setter
    def default_text(self, target: str | Text | None) -> None:
        """Set the _defaultText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_defaultText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_defaultText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def searching_visual(self) -> str | None:
        """Target ID of the _searchingVisual reference (targets TiledRawImage)."""
        member = self.get_member("_searchingVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @searching_visual.setter
    def searching_visual(self, target: str | TiledRawImage | None) -> None:
        """Set the _searchingVisual reference by target ID or TiledRawImage instance."""
        target_id: str | None = target.id if isinstance(target, TiledRawImage) else target  # type: ignore[assignment]
        member = self.get_member("_searchingVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_searchingVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TiledRawImage'),
            )

    @property
    def cancel_button(self) -> str | None:
        """Target ID of the _cancelButton reference (targets Button)."""
        member = self.get_member("_cancelButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cancel_button.setter
    def cancel_button(self, target: str | Button | None) -> None:
        """Set the _cancelButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_cancelButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cancelButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def default_visible(self) -> str | None:
        """Target ID of the _defaultVisible reference (targets IField[primitives.Bool])."""
        member = self.get_member("_defaultVisible")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_visible.setter
    def default_visible(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _defaultVisible reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_defaultVisible")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_defaultVisible",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def searching_animation_color(self) -> str | None:
        """Target ID of the _searchingAnimationColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_searchingAnimationColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @searching_animation_color.setter
    def searching_animation_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _searchingAnimationColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_searchingAnimationColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_searchingAnimationColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def searching_texture_offset(self) -> str | None:
        """Target ID of the _searchingTextureOffset reference (targets IField[primitives.Float2])."""
        member = self.get_member("_searchingTextureOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @searching_texture_offset.setter
    def searching_texture_offset(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _searchingTextureOffset reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_searchingTextureOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_searchingTextureOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

