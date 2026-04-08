"""Generated component: ReferenceCast."""

from typing import Any

I = Any
O = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceCast(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceCast<,>.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceCast<,>"

    def __init__(self, source: str | I | None = None, target: str | SyncRef[O] | None = None, write_back: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            target: Initial value for Target.
            write_back: Initial value for WriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if write_back is not None:
            self.write_back = write_back

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets I)."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | I | None) -> None:
        """Set the Source reference by target ID or I instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='I'),
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncRef[O])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncRef[O] | None) -> None:
        """Set the Target reference by target ID or SyncRef[O] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<O>'),
            )

    @property
    def write_back(self) -> primitives.Bool | None:
        """The WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

