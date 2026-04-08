"""Generated component: CallbackRefArgument."""

from typing import Any

A = Any
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CallbackRefArgument(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CallbackRefArgument<>.

    Parameterize with a value type::

        CallbackRefArgument[primitives.Float]
        CallbackRefArgument[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CallbackRefArgument<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CallbackRefArgument<>"

    def __init__(self, reference: str | A | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets A)."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | A | None) -> None:
        """Set the Reference reference by target ID or A instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='A'),
            )

    async def call(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Call sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Call", {}, debug,
        )

    async def call_and_destroy(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the CallAndDestroy sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "CallAndDestroy", {}, debug,
        )

