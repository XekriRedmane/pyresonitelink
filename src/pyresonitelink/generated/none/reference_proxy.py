"""Generated component: ReferenceProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.ireference_source import IReferenceSource
from pyresonitelink.generated._types.itrigger_action_receiver import ITriggerActionReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceProxy(GeneratedComponent, IReferenceSource, ITriggerActionReceiver, IWorldEventReceiver):
    """The ReferenceProxy component is used to make a grabbed item this is on act as the reference this refers to. This is also generated when a reference in an Scene Inspector is grabbed in the form of a block of text showing the reference and its id.

    Attach to a slot with an IGrabbable to make the grabbable act as the
    reference value itself.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceProxy"

    def __init__(self, reference: str | IWorldElement | None = None, spawn_instance_on_trigger: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """The reference this component should point to for grabbable objects, making them like inspector grab cards."""
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
    def spawn_instance_on_trigger(self) -> primitives.Bool | None:
        """Whether to spawn an inspector when clicking primary with the grabbable this is on is being held."""
        member = self.get_member("SpawnInstanceOnTrigger")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_instance_on_trigger.setter
    def spawn_instance_on_trigger(self, value: primitives.Bool) -> None:
        """Set the SpawnInstanceOnTrigger field value."""
        member = self.get_member("SpawnInstanceOnTrigger")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnInstanceOnTrigger", fields.FieldBool(value=value)
            )

