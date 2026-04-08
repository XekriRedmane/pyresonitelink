"""Generated component: RenderMaterialOverride."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RenderMaterialOverride(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RenderMaterialOverride.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderMaterialOverride"

    def __init__(self, renderer: str | MeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            renderer: Initial value for Renderer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if renderer is not None:
            self.renderer = renderer

    @property
    def context(self) -> members.FieldEnum | None:
        """The Context member."""
        member = self.get_member("Context")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @context.setter
    def context(self, value: members.FieldEnum) -> None:
        """Set the Context member."""
        self.set_member("Context", value)

    @property
    def renderer(self) -> str | None:
        """Target ID of the Renderer reference (targets MeshRenderer)."""
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the Renderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def overrides(self) -> members.SyncList | None:
        """The Overrides member."""
        member = self.get_member("Overrides")
        if isinstance(member, members.SyncList):
            return member
        return None

    @overrides.setter
    def overrides(self, value: members.SyncList) -> None:
        """Set the Overrides member."""
        self.set_member("Overrides", value)

