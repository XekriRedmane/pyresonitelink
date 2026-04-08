"""Generated component: MeshRendererMaterialRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.imaterial_target import IMaterialTarget
from pyresonitelink.generated._types.imaterial_source import IMaterialSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshRendererMaterialRelay(GeneratedComponent, IMaterialTarget, IMaterialSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MeshRendererMaterialRelay.

    Category: Assets/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshRendererMaterialRelay"

    def __init__(self, renderer: str | MeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            renderer: Initial value for _renderer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if renderer is not None:
            self.renderer = renderer

    @property
    def renderers(self) -> members.SyncList | None:
        """The Renderers member."""
        member = self.get_member("Renderers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @renderers.setter
    def renderers(self, value: members.SyncList) -> None:
        """Set the Renderers member."""
        self.set_member("Renderers", value)

    @property
    def renderer(self) -> str | None:
        """Target ID of the _renderer reference (targets MeshRenderer)."""
        member = self.get_member("_renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the _renderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

