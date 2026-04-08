"""Generated component: ValueGradientDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueGradientDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueGradientDriver<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        ValueGradientDriver[primitives.Float]
        ValueGradientDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueGradientDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueGradientDriver<>"

    def __init__(self, progress: primitives.Float | None = None, target: str | IField[T] | None = None, interpolate: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            progress: Initial value for Progress.
            target: Initial value for Target.
            interpolate: Initial value for Interpolate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if progress is not None:
            self.progress = progress
        if target is not None:
            self.target = target
        if interpolate is not None:
            self.interpolate = interpolate

    @property
    def progress(self) -> primitives.Float | None:
        """The Progress field value."""
        member = self.get_member("Progress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @progress.setter
    def progress(self, value: primitives.Float) -> None:
        """Set the Progress field value."""
        member = self.get_member("Progress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Progress", fields.FieldFloat(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[T] | None) -> None:
        """Set the Target reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def interpolate(self) -> primitives.Bool | None:
        """The Interpolate field value."""
        member = self.get_member("Interpolate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interpolate.setter
    def interpolate(self, value: primitives.Bool) -> None:
        """Set the Interpolate field value."""
        member = self.get_member("Interpolate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Interpolate", fields.FieldBool(value=value)
            )

    @property
    def points(self) -> members.SyncList | None:
        """The Points member."""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set the Points member."""
        self.set_member("Points", value)

