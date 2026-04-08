"""Generated component: ConvertibleIntDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConvertibleIntDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ConvertibleIntDriver<>.

    Parameterize with a value type::

        ConvertibleIntDriver[primitives.Float]
        ConvertibleIntDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ConvertibleIntDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ConvertibleIntDriver<>"

    def __init__(self, source: str | IField[T] | None = None, target: str | IField[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IField[T])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[T] | None) -> None:
        """Set the Source reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Int])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

