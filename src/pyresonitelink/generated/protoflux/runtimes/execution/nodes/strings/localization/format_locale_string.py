"""Generated component: FormatLocaleString."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.locale_resource import LocaleResource
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FormatLocaleString(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Format Locale String`` node takes in a locale asset (or repository) and a key and it returns the translated string for the user's culture.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Localization
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.FormatLocaleString"

    def __init__(self, locale: str | INodeObjectOutput[LocaleResource] | None = None, key: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            locale: Initial value for Locale.
            key: Initial value for Key.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if locale is not None:
            self.locale = locale
        if key is not None:
            self.key = key

    @property
    def locale(self) -> str | None:
        """The list of translatable strings (the repository or collection of strings)."""
        member = self.get_member("Locale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locale.setter
    def locale(self, target: str | INodeObjectOutput[LocaleResource] | None) -> None:
        """Set the Locale reference by target ID or INodeObjectOutput[LocaleResource] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Locale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Locale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.LocaleResource>'),
            )

    @property
    def key(self) -> str | None:
        """The key to search for in the locale resource."""
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @key.setter
    def key(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Key reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Key",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

