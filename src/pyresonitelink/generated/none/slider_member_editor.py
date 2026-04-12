"""Generated component: SliderMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.primitive_member_editor import PrimitiveMemberEditor
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SliderMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SliderMemberEditor is commonly used in inspectors and can be used for Ref hacking.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SliderMemberEditor"

    def __init__(self, continuous: primitives.Bool | None = None, path: primitives.String | None = None, target: str | IField | None = None, slider: str | Slider[primitives.Float] | None = None, slider_value: str | IField[primitives.Float] | None = None, text_editor: str | PrimitiveMemberEditor | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            slider: Initial value for _slider.
            slider_value: Initial value for _sliderValue.
            text_editor: Initial value for _textEditor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if continuous is not None:
            self.continuous = continuous
        if path is not None:
            self.path = path
        if target is not None:
            self.target = target
        if slider is not None:
            self.slider = slider
        if slider_value is not None:
            self.slider_value = slider_value
        if text_editor is not None:
            self.text_editor = text_editor

    @property
    def continuous(self) -> primitives.Bool | None:
        """Whether slider values should be constantly changed every frame update."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: primitives.Bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

    @property
    def path(self) -> primitives.String | None:
        """The value underneath the target element to change. path elements are separated by "."."""
        member = self.get_member("_path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
        """Set the _path field value."""
        member = self.get_member("_path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_path", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """The target field to change."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField | None) -> None:
        """Set the _target reference by target ID or IField instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField'),
            )

    @property
    def slider(self) -> str | None:
        """The slider to trigger change events this component should use to influence ``_target``"""
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider.setter
    def slider(self, target: str | Slider[primitives.Float] | None) -> None:
        """Set the _slider reference by target ID or Slider[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_slider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_slider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Slider<float>'),
            )

    @property
    def slider_value(self) -> str | None:
        """The value to be used for changing ``_target``"""
        member = self.get_member("_sliderValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @slider_value.setter
    def slider_value(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _sliderValue reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_sliderValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sliderValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def text_editor(self) -> str | None:
        """The text editor to change ``_target`` as a number text field."""
        member = self.get_member("_textEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_editor.setter
    def text_editor(self, target: str | PrimitiveMemberEditor | None) -> None:
        """Set the _textEditor reference by target ID or PrimitiveMemberEditor instance."""
        target_id: str | None = target.id if isinstance(target, PrimitiveMemberEditor) else target  # type: ignore[assignment]
        member = self.get_member("_textEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PrimitiveMemberEditor'),
            )

