"""Generated component: HierarchyMaterialTarget."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imaterial_target import IMaterialTarget
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HierarchyMaterialTarget(GeneratedComponent, IMaterialTarget, IWorldEventReceiver):
    """The HierarchyMaterialTarget component signals that a slot tagged with this component you are hitting with the Material Tool is an appropriate target to look for materials in.

    Category: Assets/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HierarchyMaterialTarget"

    pass

