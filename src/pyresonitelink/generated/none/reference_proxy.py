"""Generated component: ReferenceProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.ireference_source import IReferenceSource
from pyresonitelink.generated._types.itrigger_action_receiver import ITriggerActionReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceProxy(GeneratedComponent, IReferenceSource, ITriggerActionReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceProxy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceProxy"

    def __init__(self, reference: str | IWorldElement | None = None, spawn_instance_on_trigger: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            spawn_instance_on_trigger: Initial value for SpawnInstanceOnTrigger.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference
        if spawn_instance_on_trigger is not None:
            self.spawn_instance_on_trigger = spawn_instance_on_trigger

    @property
    def reference(self) -> str | None:
        """Target ID of the Reference reference (targets IWorldElement)."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | IWorldElement | None) -> None:
        """Set the Reference reference by target ID or IWorldElement instance."""
        target_id: str | None = target.id if isinstance(target, IWorldElement) else target  # type: ignore[assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldElement'),
            )

    @property
    def spawn_instance_on_trigger(self) -> bool | None:
        """The SpawnInstanceOnTrigger field value."""
        member = self.get_member("SpawnInstanceOnTrigger")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_instance_on_trigger.setter
    def spawn_instance_on_trigger(self, value: bool) -> None:
        """Set the SpawnInstanceOnTrigger field value."""
        member = self.get_member("SpawnInstanceOnTrigger")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnInstanceOnTrigger", fields.FieldBool(value=value)
            )

