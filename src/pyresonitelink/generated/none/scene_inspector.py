"""Generated component: SceneInspector."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.ino_destroy_undo import INoDestroyUndo
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SceneInspector(GeneratedComponent, INoDestroyUndo, IObjectRoot, IDeveloperInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SceneInspector.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SceneInspector"

    def __init__(self, root: str | Slot | None = None, component_view: str | Slot | None = None, root_text: str | Sync[str] | None = None, component_text: str | Sync[str] | None = None, hierarchy_content_root: str | Slot | None = None, components_content_root: str | Slot | None = None, current_component: str | Slot | None = None, current_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            component_view: Initial value for ComponentView.
            root_text: Initial value for _rootText.
            component_text: Initial value for _componentText.
            hierarchy_content_root: Initial value for _hierarchyContentRoot.
            components_content_root: Initial value for _componentsContentRoot.
            current_component: Initial value for _currentComponent.
            current_root: Initial value for _currentRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if component_view is not None:
            self.component_view = component_view
        if root_text is not None:
            self.root_text = root_text
        if component_text is not None:
            self.component_text = component_text
        if hierarchy_content_root is not None:
            self.hierarchy_content_root = hierarchy_content_root
        if components_content_root is not None:
            self.components_content_root = components_content_root
        if current_component is not None:
            self.current_component = current_component
        if current_root is not None:
            self.current_root = current_root

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets Slot)."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def component_view(self) -> str | None:
        """Target ID of the ComponentView reference (targets Slot)."""
        member = self.get_member("ComponentView")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @component_view.setter
    def component_view(self, target: str | Slot | None) -> None:
        """Set the ComponentView reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ComponentView")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ComponentView",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def root_text(self) -> str | None:
        """Target ID of the _rootText reference (targets Sync[str])."""
        member = self.get_member("_rootText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_text.setter
    def root_text(self, target: str | Sync[str] | None) -> None:
        """Set the _rootText reference by target ID or Sync[str] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("_rootText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rootText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<string>'),
            )

    @property
    def component_text(self) -> str | None:
        """Target ID of the _componentText reference (targets Sync[str])."""
        member = self.get_member("_componentText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @component_text.setter
    def component_text(self, target: str | Sync[str] | None) -> None:
        """Set the _componentText reference by target ID or Sync[str] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("_componentText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_componentText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<string>'),
            )

    @property
    def hierarchy_content_root(self) -> str | None:
        """Target ID of the _hierarchyContentRoot reference (targets Slot)."""
        member = self.get_member("_hierarchyContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hierarchy_content_root.setter
    def hierarchy_content_root(self, target: str | Slot | None) -> None:
        """Set the _hierarchyContentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_hierarchyContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hierarchyContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def components_content_root(self) -> str | None:
        """Target ID of the _componentsContentRoot reference (targets Slot)."""
        member = self.get_member("_componentsContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @components_content_root.setter
    def components_content_root(self, target: str | Slot | None) -> None:
        """Set the _componentsContentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_componentsContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_componentsContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def current_component(self) -> str | None:
        """Target ID of the _currentComponent reference (targets Slot)."""
        member = self.get_member("_currentComponent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_component.setter
    def current_component(self, target: str | Slot | None) -> None:
        """Set the _currentComponent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_currentComponent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentComponent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def current_root(self) -> str | None:
        """Target ID of the _currentRoot reference (targets Slot)."""
        member = self.get_member("_currentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_root.setter
    def current_root(self, target: str | Slot | None) -> None:
        """Set the _currentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_currentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

