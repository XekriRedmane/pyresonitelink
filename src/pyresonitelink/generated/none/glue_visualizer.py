"""Generated component: GlueVisualizer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.fresnel_material import FresnelMaterial
from pyresonitelink.generated._types.glue import Glue
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlueVisualizer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The GlueVisualizer component is used by the Glue Tool to visualize glue objects that are to potentially gluing objects together.

    See Glue Tool.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GlueVisualizer"

    def __init__(self, material: str | FresnelMaterial | None = None, glue: str | Glue | None = None, scale: str | IField[primitives.Float3] | None = None, base_scale: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            glue: Initial value for Glue.
            scale: Initial value for Scale.
            base_scale: Initial value for BaseScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if glue is not None:
            self.glue = glue
        if scale is not None:
            self.scale = scale
        if base_scale is not None:
            self.base_scale = base_scale

    @property
    def material(self) -> str | None:
        """The material being used to visualize the area of effect of ``Glue``."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | FresnelMaterial | None) -> None:
        """Set the Material reference by target ID or FresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, FresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FresnelMaterial'),
            )

    @property
    def glue(self) -> str | None:
        """The Glue component to visualize."""
        member = self.get_member("Glue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @glue.setter
    def glue(self, target: str | Glue | None) -> None:
        """Set the Glue reference by target ID or Glue instance."""
        target_id: str | None = target.id if isinstance(target, Glue) else target  # type: ignore[assignment]
        member = self.get_member("Glue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Glue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Glue'),
            )

    @property
    def scale(self) -> str | None:
        """The scale field of the visual so it wobbles."""
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def base_scale(self) -> primitives.Float3 | None:
        """The default or base scale of the visual."""
        member = self.get_member("BaseScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_scale.setter
    def base_scale(self, value: primitives.Float3) -> None:
        """Set the BaseScale field value."""
        member = self.get_member("BaseScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseScale", fields.FieldFloat3(value=value)
            )

