"""Generated component: DynamicBlendShapeDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.skinned_mesh_renderer import SkinnedMeshRenderer
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBlendShapeDriver(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicBlendShapeDriver.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBlendShapeDriver"

    def __init__(self, renderer: str | SkinnedMeshRenderer | None = None, last_renderer: str | SkinnedMeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            renderer: Initial value for Renderer.
            last_renderer: Initial value for _lastRenderer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if renderer is not None:
            self.renderer = renderer
        if last_renderer is not None:
            self.last_renderer = last_renderer

    @property
    def renderer(self) -> str | None:
        """Target ID of the Renderer reference (targets SkinnedMeshRenderer)."""
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | SkinnedMeshRenderer | None) -> None:
        """Set the Renderer reference by target ID or SkinnedMeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, SkinnedMeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SkinnedMeshRenderer'),
            )

    @property
    def blend_shapes(self) -> members.SyncList | None:
        """The BlendShapes member."""
        member = self.get_member("BlendShapes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @blend_shapes.setter
    def blend_shapes(self, value: members.SyncList) -> None:
        """Set the BlendShapes member."""
        self.set_member("BlendShapes", value)

    @property
    def last_renderer(self) -> str | None:
        """Target ID of the _lastRenderer reference (targets SkinnedMeshRenderer)."""
        member = self.get_member("_lastRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_renderer.setter
    def last_renderer(self, target: str | SkinnedMeshRenderer | None) -> None:
        """Set the _lastRenderer reference by target ID or SkinnedMeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, SkinnedMeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_lastRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SkinnedMeshRenderer'),
            )

