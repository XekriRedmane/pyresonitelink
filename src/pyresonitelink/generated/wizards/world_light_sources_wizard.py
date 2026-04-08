"""Generated component: WorldLightSourcesWizard."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldLightSourcesWizard(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldLightSourcesWizard.

    Category: Wizards
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldLightSourcesWizard"

    def __init__(self, root: str | Slot | None = None, process_point_lights: bool | None = None, process_spot_lights: bool | None = None, process_directional_lights: bool | None = None, process_disabled: bool | None = None, tag: str | TextField | None = None, intensity_field: str | FloatTextEditorParser | None = None, range_field: str | FloatTextEditorParser | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            process_point_lights: Initial value for ProcessPointLights.
            process_spot_lights: Initial value for ProcessSpotLights.
            process_directional_lights: Initial value for ProcessDirectionalLights.
            process_disabled: Initial value for ProcessDisabled.
            tag: Initial value for _tag.
            intensity_field: Initial value for _intensityField.
            range_field: Initial value for _rangeField.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if process_point_lights is not None:
            self.process_point_lights = process_point_lights
        if process_spot_lights is not None:
            self.process_spot_lights = process_spot_lights
        if process_directional_lights is not None:
            self.process_directional_lights = process_directional_lights
        if process_disabled is not None:
            self.process_disabled = process_disabled
        if tag is not None:
            self.tag = tag
        if intensity_field is not None:
            self.intensity_field = intensity_field
        if range_field is not None:
            self.range_field = range_field

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets Slot)."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def process_point_lights(self) -> bool | None:
        """The ProcessPointLights field value."""
        member = self.get_member("ProcessPointLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_point_lights.setter
    def process_point_lights(self, value: bool) -> None:
        """Set the ProcessPointLights field value."""
        member = self.get_member("ProcessPointLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessPointLights", fields.FieldBool(value=value)
            )

    @property
    def process_spot_lights(self) -> bool | None:
        """The ProcessSpotLights field value."""
        member = self.get_member("ProcessSpotLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_spot_lights.setter
    def process_spot_lights(self, value: bool) -> None:
        """Set the ProcessSpotLights field value."""
        member = self.get_member("ProcessSpotLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessSpotLights", fields.FieldBool(value=value)
            )

    @property
    def process_directional_lights(self) -> bool | None:
        """The ProcessDirectionalLights field value."""
        member = self.get_member("ProcessDirectionalLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_directional_lights.setter
    def process_directional_lights(self, value: bool) -> None:
        """Set the ProcessDirectionalLights field value."""
        member = self.get_member("ProcessDirectionalLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessDirectionalLights", fields.FieldBool(value=value)
            )

    @property
    def process_disabled(self) -> bool | None:
        """The ProcessDisabled field value."""
        member = self.get_member("ProcessDisabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_disabled.setter
    def process_disabled(self, value: bool) -> None:
        """Set the ProcessDisabled field value."""
        member = self.get_member("ProcessDisabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessDisabled", fields.FieldBool(value=value)
            )

    @property
    def target_shadow_type(self) -> members.FieldEnum | None:
        """The TargetShadowType member."""
        member = self.get_member("TargetShadowType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @target_shadow_type.setter
    def target_shadow_type(self, value: members.FieldEnum) -> None:
        """Set the TargetShadowType member."""
        self.set_member("TargetShadowType", value)

    @property
    def tag(self) -> str | None:
        """Target ID of the _tag reference (targets TextField)."""
        member = self.get_member("_tag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tag.setter
    def tag(self, target: str | TextField | None) -> None:
        """Set the _tag reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_tag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def intensity_field(self) -> str | None:
        """Target ID of the _intensityField reference (targets FloatTextEditorParser)."""
        member = self.get_member("_intensityField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @intensity_field.setter
    def intensity_field(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _intensityField reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_intensityField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_intensityField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def range_field(self) -> str | None:
        """Target ID of the _rangeField reference (targets FloatTextEditorParser)."""
        member = self.get_member("_rangeField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @range_field.setter
    def range_field(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _rangeField reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_rangeField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rangeField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

