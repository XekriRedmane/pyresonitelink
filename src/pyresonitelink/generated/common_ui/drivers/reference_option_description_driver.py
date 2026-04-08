"""Generated component: ReferenceOptionDescriptionDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceOptionDescriptionDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceOptionDescriptionDriver<>.

    Category: Common UI/Drivers

    Parameterize with a value type::

        ReferenceOptionDescriptionDriver[np.float32]
        ReferenceOptionDescriptionDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceOptionDescriptionDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceOptionDescriptionDriver<>"

    def __init__(self, reference: str | SyncRef[T] | None = None, force_deselected: bool | None = None, label: str | IField[str] | None = None, color: str | IField[primitives.ColorX] | None = None, sprite: str | SyncRef[IAssetProvider[Sprite]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            force_deselected: Initial value for ForceDeselected.
            label: Initial value for Label.
            color: Initial value for Color.
            sprite: Initial value for Sprite.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference
        if force_deselected is not None:
            self.force_deselected = force_deselected
        if label is not None:
            self.label = label
        if color is not None:
            self.color = color
        if sprite is not None:
            self.sprite = sprite

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets SyncRef[T])."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | SyncRef[T] | None) -> None:
        """Set the Reference reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def force_deselected(self) -> bool | None:
        """The ForceDeselected field value."""
        member = self.get_member("ForceDeselected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_deselected.setter
    def force_deselected(self, value: bool) -> None:
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
        """Target ID of the Label reference (targets IField[str])."""
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | IField[str] | None) -> None:
        """Set the Label reference by target ID or IField[str] instance."""
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
        """Target ID of the Color reference (targets IField[primitives.ColorX])."""
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
        """Target ID of the Sprite reference (targets SyncRef[IAssetProvider[Sprite]])."""
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
    def default_option(self) -> members.SyncObject | None:
        """The DefaultOption member."""
        member = self.get_member("DefaultOption")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @default_option.setter
    def default_option(self, value: members.SyncObject) -> None:
        """Set the DefaultOption member."""
        self.set_member("DefaultOption", value)

    @property
    def options(self) -> members.SyncList | None:
        """The Options member."""
        member = self.get_member("Options")
        if isinstance(member, members.SyncList):
            return member
        return None

    @options.setter
    def options(self, value: members.SyncList) -> None:
        """Set the Options member."""
        self.set_member("Options", value)

