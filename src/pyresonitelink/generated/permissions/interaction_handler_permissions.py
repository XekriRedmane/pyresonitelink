"""Generated component: InteractionHandlerPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractionHandlerPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractionHandlerPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractionHandlerPermissions"

    def __init__(self, allow_only_whitelisted_tools: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_only_whitelisted_tools: Initial value for AllowOnlyWhitelistedTools.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_only_whitelisted_tools is not None:
            self.allow_only_whitelisted_tools = allow_only_whitelisted_tools

    @property
    def allow_only_whitelisted_tools(self) -> primitives.Bool | None:
        """The AllowOnlyWhitelistedTools field value."""
        member = self.get_member("AllowOnlyWhitelistedTools")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_only_whitelisted_tools.setter
    def allow_only_whitelisted_tools(self, value: primitives.Bool) -> None:
        """Set the AllowOnlyWhitelistedTools field value."""
        member = self.get_member("AllowOnlyWhitelistedTools")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowOnlyWhitelistedTools", fields.FieldBool(value=value)
            )

    @property
    def tool_rules(self) -> members.SyncList | None:
        """The ToolRules member."""
        member = self.get_member("ToolRules")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tool_rules.setter
    def tool_rules(self, value: members.SyncList) -> None:
        """Set the ToolRules member."""
        self.set_member("ToolRules", value)

