"""Generated component: BreadcrumbManager."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_field_list import SyncFieldList
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.breadcrumb_interface import BreadcrumbInterface
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BreadcrumbManager(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The BreadcrumbManager component is used to instantiate BreadcrumbInterfaces and remove them based on the list of path elements on a Data Feed View Type.

    Category: Radiant UI/Navigation
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BreadcrumbManager"

    def __init__(self, path: str | SyncFieldList[primitives.String] | None = None, ui_root: str | Slot | None = None, breadcrumb_template: str | BreadcrumbInterface | None = None, separator_template: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            ui_root: Initial value for UI_Root.
            breadcrumb_template: Initial value for BreadcrumbTemplate.
            separator_template: Initial value for SeparatorTemplate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path
        if ui_root is not None:
            self.ui_root = ui_root
        if breadcrumb_template is not None:
            self.breadcrumb_template = breadcrumb_template
        if separator_template is not None:
            self.separator_template = separator_template

    @property
    def path(self) -> str | None:
        """The path field in a Data Feed View Type component to show in the form of templates."""
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path.setter
    def path(self, target: str | SyncFieldList[primitives.String] | None) -> None:
        """Set the Path reference by target ID or SyncFieldList[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, SyncFieldList) else target  # type: ignore[assignment]
        member = self.get_member("Path")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Path",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncFieldList<string>'),
            )

    @property
    def ui_root(self) -> str | None:
        """The place to put Breadcrumb path items in."""
        member = self.get_member("UI_Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ui_root.setter
    def ui_root(self, target: str | Slot | None) -> None:
        """Set the UI_Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("UI_Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UI_Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def breadcrumb_template(self) -> str | None:
        """The template to duplicate in order to create UI."""
        member = self.get_member("BreadcrumbTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @breadcrumb_template.setter
    def breadcrumb_template(self, target: str | BreadcrumbInterface | None) -> None:
        """Set the BreadcrumbTemplate reference by target ID or BreadcrumbInterface instance."""
        target_id: str | None = target.id if isinstance(target, BreadcrumbInterface) else target  # type: ignore[assignment]
        member = self.get_member("BreadcrumbTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BreadcrumbTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BreadcrumbInterface'),
            )

    @property
    def separator_template(self) -> str | None:
        """The slot to duplicate and place between elements to make them have slashes or commas between them."""
        member = self.get_member("SeparatorTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @separator_template.setter
    def separator_template(self, target: str | Slot | None) -> None:
        """Set the SeparatorTemplate reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SeparatorTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SeparatorTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    async def set_depth(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, depth: primitives.Int, debug: bool = False) -> dict:
        """Takes a number beside a button that when pressed will set the depth of the path.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            depth: The depth parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetDepth", {"button": button, "eventData": event_data, "depth": depth}, debug,
        )

    async def set_depth_1(self, resolink: protocols.ResoniteLinkClient, depth: primitives.Int, debug: bool = False) -> dict:
        """Takes a number beside a button that when pressed will set the depth of the path.

        Args:
            resolink: Connected ResoniteLink client.
            depth: The depth parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetDepth", {"depth": depth}, debug,
        )

