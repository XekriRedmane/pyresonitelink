"""Generated component: MeshRendererMaterialRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.imaterial_target import IMaterialTarget
from pyresonitelink.generated._types.imaterial_source import IMaterialSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshRendererMaterialRelay(GeneratedComponent, IMaterialTarget, IMaterialSource, IWorldEventReceiver):
    """Attach to a slot and provide the mesh renderers that should have materials applied to them with the material Tool in Renderers.

    Category: Assets/Tagging

    Attach to a slot and provide the mesh renderers that should have
    materials applied to them with the material Tool in ``Renderers``.
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
        """The list of renderers to relay to the material tool."""
        member = self.get_member("Renderers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @renderers.setter
    def renderers(self, value: members.SyncList) -> None:
        """Set Renderers. The list of renderers to relay to the material tool."""
        self.set_member("Renderers", value)

    @property
    def renderer(self) -> str | None:
        """An extra renderer that's legacy."""
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

