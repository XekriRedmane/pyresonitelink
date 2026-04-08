"""Generated component: GaussianSplatTool+BoxInterface."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatTool+BoxInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatTool+BoxInterface.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatTool+BoxInterface"

    def __init__(self, size: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            size: Initial value for Size.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if size is not None:
            self.size = size

    @property
    def size(self) -> str | None:
        """Target ID of the Size reference (targets IField[primitives.Float3])."""
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size.setter
    def size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Size reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Size",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

