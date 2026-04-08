"""Generated component: DestroyProxy."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idestroyable import IDestroyable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyProxy(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DestroyProxy.

    Category: Transform/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyProxy"

    def __init__(self, destroy_target: str | IDestroyable | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            destroy_target: Initial value for DestroyTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if destroy_target is not None:
            self.destroy_target = destroy_target

    @property
    def destroy_target(self) -> str | None:
        """Target ID of the DestroyTarget reference (targets IDestroyable)."""
        member = self.get_member("DestroyTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @destroy_target.setter
    def destroy_target(self, target: str | IDestroyable | None) -> None:
        """Set the DestroyTarget reference by target ID or IDestroyable instance."""
        target_id: str | None = target.id if isinstance(target, IDestroyable) else target  # type: ignore[assignment]
        member = self.get_member("DestroyTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DestroyTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IDestroyable'),
            )

