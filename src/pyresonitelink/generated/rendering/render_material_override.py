"""Generated component: RenderMaterialOverride."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.rendering_context import RenderingContext
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RenderMaterialOverride(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The RenderMaterialOverride Component allows for overriding materials on a renderer when it is rendered in certain contexts.

Note: This only overrides materials properly if all ``Context``s are used, with a component for each one. This may be a bug.

    Category: Rendering

    Used to hide materials or change them in a mirror. like showing an evil
    version of yourself in a mirror, or to hide your head material from your
    own viewpoint
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderMaterialOverride"

    def __init__(self, context: RenderingContext | str | None = None, renderer: str | MeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            context: Initial value for Context.
            renderer: Initial value for Renderer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if context is not None:
            self.context = context
        if renderer is not None:
            self.renderer = renderer

    @property
    def context(self) -> RenderingContext | None:
        """The context in which to override the materials of ``Renderer`` with the list of ``Overrides``."""
        member = self.get_member("Context")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RenderingContext(member.value)
        return None

    @context.setter
    def context(self, value: RenderingContext | str) -> None:
        """Set Context. The context in which to override the materials of ``Renderer`` with the list of ``Overrides``."""
        member = self.get_member("Context")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Context",
                members.FieldEnum(value=str(value)),
            )

    @property
    def renderer(self) -> str | None:
        """The renderer to override materials for."""
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
        """A list of materials to override during rendering in a ``Context`` context."""
        member = self.get_member("Overrides")
        if isinstance(member, members.SyncList):
            return member
        return None

    @overrides.setter
    def overrides(self, value: members.SyncList) -> None:
        """Set Overrides. A list of materials to override during rendering in a ``Context`` context."""
        self.set_member("Overrides", value)

