"""Generated component: ValueOptionDescriptionDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueOptionDescriptionDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ValueOptionDescriptionDriver component is used primarily to drive the parts that make up a Context Menu Item Source. This component along with ContextMenuItemSource is used in context menus for toggles where the toggle controls a value.

}}

    Category: Common UI/Drivers

    This component can be more efficient than using a bunch of Value
    Equality Drivers and generating a number based on such, or using
    ProtoFlux for a context menu.

    Parameterize with a value type::

        ValueOptionDescriptionDriver[primitives.Float]
        ValueOptionDescriptionDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueOptionDescriptionDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueOptionDescriptionDriver<>"

    def __init__(self, value: str | IField[T] | None = None, force_deselected: primitives.Bool | None = None, label: str | IField[primitives.String] | None = None, color: str | IField[primitives.ColorX] | None = None, sprite: str | SyncRef[IAssetProvider[Sprite]] | None = None, sprite_url: str | IField[str] | None = None, sprite_tint: str | IField[primitives.ColorX] | None = None, sprite_tint_base: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            force_deselected: Initial value for ForceDeselected.
            label: Initial value for Label.
            color: Initial value for Color.
            sprite: Initial value for Sprite.
            sprite_url: Initial value for SpriteURL.
            sprite_tint: Initial value for SpriteTint.
            sprite_tint_base: Initial value for SpriteTintBase.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if force_deselected is not None:
            self.force_deselected = force_deselected
        if label is not None:
            self.label = label
        if color is not None:
            self.color = color
        if sprite is not None:
            self.sprite = sprite
        if sprite_url is not None:
            self.sprite_url = sprite_url
        if sprite_tint is not None:
            self.sprite_tint = sprite_tint
        if sprite_tint_base is not None:
            self.sprite_tint_base = sprite_tint_base

    @property
    def value(self) -> str | None:
        """The value field to compare against."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | IField[T] | None) -> None:
        """Set the Value reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def force_deselected(self) -> primitives.Bool | None:
        """Forces any context menu item source to change regardless if it is deselected."""
        member = self.get_member("ForceDeselected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_deselected.setter
    def force_deselected(self, value: primitives.Bool) -> None:
        """Set the ForceDeselected field value."""
        member = self.get_member("ForceDeselected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceDeselected", fields.FieldBool(value=value)
            )

    @property
    def label(self) -> str | None:
        """The string to set to the chosen label in the list of ``Options``."""
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Label reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Label",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def color(self) -> str | None:
        """The color to set to the chosen color in the list of ``Options``"""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the Color reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def sprite(self) -> str | None:
        """The Sprite to set to the chosen Sprite in the list of ``Options``."""
        member = self.get_member("Sprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite.setter
    def sprite(self, target: str | SyncRef[IAssetProvider[Sprite]] | None) -> None:
        """Set the Sprite reference by target ID or SyncRef[IAssetProvider[Sprite]] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Sprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Sprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Sprite>>'),
            )

    @property
    def sprite_url(self) -> str | None:
        """The sprite url."""
        member = self.get_member("SpriteURL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_url.setter
    def sprite_url(self, target: str | IField[str] | None) -> None:
        """Set the SpriteURL reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpriteURL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpriteURL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def sprite_tint(self) -> str | None:
        """The sprite tint."""
        member = self.get_member("SpriteTint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_tint.setter
    def sprite_tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the SpriteTint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpriteTint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpriteTint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def default_option(self) -> members.SyncObject | None:
        """The option to set ``Label``, ``Color``, and ``Sprite`` to when ``Reference`` doesn't match any ``ReferenceTarget``s under the list of ``Options``."""
        member = self.get_member("DefaultOption")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @default_option.setter
    def default_option(self, value: members.SyncObject) -> None:
        """Set DefaultOption. The option to set ``Label``, ``Color``, and ``Sprite`` to when ``Reference`` doesn't match any ``ReferenceTarget``s under the list of ``Options``."""
        self.set_member("DefaultOption", value)

    @property
    def options(self) -> members.SyncList | None:
        """The list to search for a ``ReferenceTarget`` that matches ``Value``. once a match is found, the option's ``Label``, ``Color``, and ``Sprite`` is used to drive this section's drive targets of ``Label``, ``Color``, and ``Sprite``."""
        member = self.get_member("Options")
        if isinstance(member, members.SyncList):
            return member
        return None

    @options.setter
    def options(self, value: members.SyncList) -> None:
        """Set Options. The list to search for a ``ReferenceTarget`` that matches ``Value``. once a match is found, the option's ``Label``, ``Color``, and ``Sprite`` is used to drive this section's drive targets of ``Label``, ``Color``, and ``Sprite``."""
        self.set_member("Options", value)

    @property
    def sprite_tint_base(self) -> primitives.ColorX | None:
        """Tints the entire sprite with a ColorX."""
        member = self.get_member("SpriteTintBase")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sprite_tint_base.setter
    def sprite_tint_base(self, value: primitives.ColorX) -> None:
        """Set the SpriteTintBase field value."""
        member = self.get_member("SpriteTintBase")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpriteTintBase", fields.FieldColorX(value=value)
            )

