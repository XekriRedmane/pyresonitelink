"""Generated component: DynamicBlendShapeDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.skinned_mesh_renderer import SkinnedMeshRenderer
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBlendShapeDriver(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """This component is used to map values to Blendshapes by name. 
}}

    Category: Transform/Drivers

    To efficiently use this component, first add some blendshape items to
    the ``blendshapes`` list and give the blendshapes names of the
    blendshapes on your target mesh. Next, add the skinned mesh renderer to
    ``Renderer`` you want to automatically find the blendshapes for. The
    component in the next update will automatically add the value sliders of
    the blendshapes it can find on the target ``Renderer`` to the ``Field``
    on each ``BlendShape``. To drive the blendshapes, just simply drive the
    ``Value`` on each ``BlendShape`` for each blendshape you want. Driving
    ``Value`` is not required, and this can be used in cases where you want
    to toggle, cycle, or modify a blendshape's value without driving it.
    This can be useful if you don't want to accidentally bake blendshapes
    you are still using despite them not being driven.
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
        """The renderer to use to search for shapekeys with"""
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
        """A list of BlendShape that are searched for in order on the Renderer."""
        member = self.get_member("BlendShapes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @blend_shapes.setter
    def blend_shapes(self, value: members.SyncList) -> None:
        """Set BlendShapes. A list of BlendShape that are searched for in order on the Renderer."""
        self.set_member("BlendShapes", value)

    @property
    def last_renderer(self) -> str | None:
        """The last renderer that was searched. This value is automatically filled and is read only."""
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

