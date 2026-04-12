"""Generated component: ComponentSelector."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ComponentSelector(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """The Component Selector is better understood on its page, Complex Types in Components.

    See Complex Types in Components.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ComponentSelector"

    def __init__(self, ui_root: str | Slot | None = None, root_path: primitives.String | None = None, generic_type: Type | str | None = None, custom_generic_type_label: str | IField[primitives.String] | None = None, custom_generic_type_color: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ui_root: Initial value for _uiRoot.
            root_path: Initial value for _rootPath.
            generic_type: Initial value for _genericType.
            custom_generic_type_label: Initial value for _customGenericTypeLabel.
            custom_generic_type_color: Initial value for _customGenericTypeColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ui_root is not None:
            self.ui_root = ui_root
        if root_path is not None:
            self.root_path = root_path
        if generic_type is not None:
            self.generic_type = generic_type
        if custom_generic_type_label is not None:
            self.custom_generic_type_label = custom_generic_type_label
        if custom_generic_type_color is not None:
            self.custom_generic_type_color = custom_generic_type_color

    @property
    def ui_root(self) -> str | None:
        """The root slot of the UI."""
        member = self.get_member("_uiRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ui_root.setter
    def ui_root(self, target: str | Slot | None) -> None:
        """Set the _uiRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_uiRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_uiRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def root_path(self) -> primitives.String | None:
        """The path that this is navigated to in the component attacher."""
        member = self.get_member("_rootPath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_path.setter
    def root_path(self, value: primitives.String) -> None:
        """Set the _rootPath field value."""
        member = self.get_member("_rootPath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rootPath", fields.FieldString(value=value)
            )

    @property
    def generic_type(self) -> Type | None:
        """The generic type we are trying to make a generic fill for."""
        member = self.get_member("_genericType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @generic_type.setter
    def generic_type(self, value: Type | str) -> None:
        """Set _genericType. The generic type we are trying to make a generic fill for."""
        member = self.get_member("_genericType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_genericType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def custom_generic_type_label(self) -> str | None:
        """The label for the generic type we are attaching."""
        member = self.get_member("_customGenericTypeLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_generic_type_label.setter
    def custom_generic_type_label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _customGenericTypeLabel reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_customGenericTypeLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customGenericTypeLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def custom_generic_type_color(self) -> str | None:
        """The color for the generic type we are attaching."""
        member = self.get_member("_customGenericTypeColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @custom_generic_type_color.setter
    def custom_generic_type_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _customGenericTypeColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_customGenericTypeColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_customGenericTypeColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def custom_generic_arguments(self) -> members.SyncList | None:
        """The generic arguments being used for the current Component being attached. See Complex Types in Components."""
        member = self.get_member("_customGenericArguments")
        if isinstance(member, members.SyncList):
            return member
        return None

    @custom_generic_arguments.setter
    def custom_generic_arguments(self, value: members.SyncList) -> None:
        """Set _customGenericArguments. The generic arguments being used for the current Component being attached. See Complex Types in Components."""
        self.set_member("_customGenericArguments", value)

