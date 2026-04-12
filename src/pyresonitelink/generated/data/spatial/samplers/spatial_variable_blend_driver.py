"""Generated component: SpatialVariableBlendDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SpatialVariableBlendDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Spatial Variable Blend Driver component combines with the CloningReferenceSpatialVariableCollector component. If this is on a field on a spatial variable component which is driven by this component, the cloned version will be driven with the current blend weight for that clone. This is used for the BlendWeight for the new reverb zones. For more info on making reverb zones, see AudioListener

    Category: Data/Spatial/Samplers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SpatialVariableBlendDriver"

    def __init__(self, blend_weight: str | IField[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            blend_weight: Initial value for BlendWeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if blend_weight is not None:
            self.blend_weight = blend_weight

    @property
    def blend_weight(self) -> str | None:
        """used for proportional blending and priority computation"""
        member = self.get_member("BlendWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @blend_weight.setter
    def blend_weight(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the BlendWeight reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("BlendWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BlendWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

