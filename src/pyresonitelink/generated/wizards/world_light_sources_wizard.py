"""Generated component: WorldLightSourcesWizard."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.shadow_type import ShadowType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldLightSourcesWizard(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """See World Light Sources Wizard.

    Category: Wizards

    See World Light Sources Wizard.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldLightSourcesWizard"

    def __init__(self, root: str | Slot | None = None, process_point_lights: primitives.Bool | None = None, process_spot_lights: primitives.Bool | None = None, process_directional_lights: primitives.Bool | None = None, process_disabled: primitives.Bool | None = None, target_shadow_type: ShadowType | str | None = None, tag: str | TextField | None = None, intensity_field: str | FloatTextEditorParser | None = None, range_field: str | FloatTextEditorParser | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            process_point_lights: Initial value for ProcessPointLights.
            process_spot_lights: Initial value for ProcessSpotLights.
            process_directional_lights: Initial value for ProcessDirectionalLights.
            process_disabled: Initial value for ProcessDisabled.
            target_shadow_type: Initial value for TargetShadowType.
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
        if target_shadow_type is not None:
            self.target_shadow_type = target_shadow_type
        if tag is not None:
            self.tag = tag
        if intensity_field is not None:
            self.intensity_field = intensity_field
        if range_field is not None:
            self.range_field = range_field

    @property
    def root(self) -> str | None:
        """The root directory in which all lights underneath it will be affected."""
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
    def process_point_lights(self) -> primitives.Bool | None:
        """Whether to process point lights."""
        member = self.get_member("ProcessPointLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_point_lights.setter
    def process_point_lights(self, value: primitives.Bool) -> None:
        """Set the ProcessPointLights field value."""
        member = self.get_member("ProcessPointLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessPointLights", fields.FieldBool(value=value)
            )

    @property
    def process_spot_lights(self) -> primitives.Bool | None:
        """Whether to process spot lights."""
        member = self.get_member("ProcessSpotLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_spot_lights.setter
    def process_spot_lights(self, value: primitives.Bool) -> None:
        """Set the ProcessSpotLights field value."""
        member = self.get_member("ProcessSpotLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessSpotLights", fields.FieldBool(value=value)
            )

    @property
    def process_directional_lights(self) -> primitives.Bool | None:
        """Whether to process directional lights."""
        member = self.get_member("ProcessDirectionalLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_directional_lights.setter
    def process_directional_lights(self, value: primitives.Bool) -> None:
        """Set the ProcessDirectionalLights field value."""
        member = self.get_member("ProcessDirectionalLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessDirectionalLights", fields.FieldBool(value=value)
            )

    @property
    def process_disabled(self) -> primitives.Bool | None:
        """Whether to process lights that are not part of an active hiearchy or the component itself is disabled."""
        member = self.get_member("ProcessDisabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_disabled.setter
    def process_disabled(self, value: primitives.Bool) -> None:
        """Set the ProcessDisabled field value."""
        member = self.get_member("ProcessDisabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessDisabled", fields.FieldBool(value=value)
            )

    @property
    def target_shadow_type(self) -> ShadowType | None:
        """The shadow type to set all lights to."""
        member = self.get_member("TargetShadowType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ShadowType(member.value)
        return None

    @target_shadow_type.setter
    def target_shadow_type(self, value: ShadowType | str) -> None:
        """Set TargetShadowType. The shadow type to set all lights to."""
        member = self.get_member("TargetShadowType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TargetShadowType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def tag(self) -> str | None:
        """The slot tag that lights have to have under ``Root`` to be affected."""
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
        """The intensity to set all lights under ``Root`` to."""
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
        """The distance range to set all lights under ``Root`` to."""
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

