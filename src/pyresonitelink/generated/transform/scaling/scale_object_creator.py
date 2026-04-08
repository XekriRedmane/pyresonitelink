"""Generated component: ScaleObjectCreator."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.scale_object_manager import ScaleObjectManager
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.quantity_text_editor_parser import QuantityTextEditorParser
from pyresonitelink.generated._types.distance import Distance
from pyresonitelink.generated._types.fresnel_material import FresnelMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleObjectCreator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaleObjectCreator.

    Category: Transform/Scaling
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleObjectCreator"

    def __init__(self, manager: str | ScaleObjectManager | None = None, template: str | Slot | None = None, template_name_field: str | IField[str] | None = None, template_size_field: str | IField[np.float64] | None = None, size_parser: str | QuantityTextEditorParser[Distance] | None = None, material: str | FresnelMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            manager: Initial value for Manager.
            template: Initial value for Template.
            template_name_field: Initial value for TemplateNameField.
            template_size_field: Initial value for TemplateSizeField.
            size_parser: Initial value for _sizeParser.
            material: Initial value for _material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if manager is not None:
            self.manager = manager
        if template is not None:
            self.template = template
        if template_name_field is not None:
            self.template_name_field = template_name_field
        if template_size_field is not None:
            self.template_size_field = template_size_field
        if size_parser is not None:
            self.size_parser = size_parser
        if material is not None:
            self.material = material

    @property
    def manager(self) -> str | None:
        """Target ID of the Manager reference (targets ScaleObjectManager)."""
        member = self.get_member("Manager")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @manager.setter
    def manager(self, target: str | ScaleObjectManager | None) -> None:
        """Set the Manager reference by target ID or ScaleObjectManager instance."""
        target_id: str | None = target.id if isinstance(target, ScaleObjectManager) else target  # type: ignore[assignment]
        member = self.get_member("Manager")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Manager",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScaleObjectManager'),
            )

    @property
    def template(self) -> str | None:
        """Target ID of the Template reference (targets Slot)."""
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template.setter
    def template(self, target: str | Slot | None) -> None:
        """Set the Template reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Template",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def template_name_field(self) -> str | None:
        """Target ID of the TemplateNameField reference (targets IField[str])."""
        member = self.get_member("TemplateNameField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template_name_field.setter
    def template_name_field(self, target: str | IField[str] | None) -> None:
        """Set the TemplateNameField reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TemplateNameField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TemplateNameField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def template_size_field(self) -> str | None:
        """Target ID of the TemplateSizeField reference (targets IField[np.float64])."""
        member = self.get_member("TemplateSizeField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template_size_field.setter
    def template_size_field(self, target: str | IField[np.float64] | None) -> None:
        """Set the TemplateSizeField reference by target ID or IField[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TemplateSizeField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TemplateSizeField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<double>'),
            )

    @property
    def size_parser(self) -> str | None:
        """Target ID of the _sizeParser reference (targets QuantityTextEditorParser[Distance])."""
        member = self.get_member("_sizeParser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_parser.setter
    def size_parser(self, target: str | QuantityTextEditorParser[Distance] | None) -> None:
        """Set the _sizeParser reference by target ID or QuantityTextEditorParser[Distance] instance."""
        target_id: str | None = target.id if isinstance(target, QuantityTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_sizeParser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_sizeParser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.QuantityTextEditorParser<Distance>'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets FresnelMaterial)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | FresnelMaterial | None) -> None:
        """Set the _material reference by target ID or FresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, FresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FresnelMaterial'),
            )

