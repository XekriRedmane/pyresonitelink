"""Generated component: ReferenceMultiDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceMultiDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceMultiDriver<>.

    Category: Relations

    Parameterize with a value type::

        ReferenceMultiDriver[primitives.Float]
        ReferenceMultiDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceMultiDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceMultiDriver<>"

    def __init__(self, reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Reference reference (targets T)."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | T | None) -> None:
        """Set the Reference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def drives(self) -> members.SyncList | None:
        """The Drives member."""
        member = self.get_member("Drives")
        if isinstance(member, members.SyncList):
            return member
        return None

    @drives.setter
    def drives(self, value: members.SyncList) -> None:
        """Set the Drives member."""
        self.set_member("Drives", value)

