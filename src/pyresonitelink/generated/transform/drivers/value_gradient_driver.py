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
    """The ValueGradientDriver component changes the value of the field defined in ``Target`` based on the items in the ``Points`` list and their ``Position`` in relation to the ``Progress`` value.

    Category: Transform/Drivers

    Each point in the ``Points`` list has a ``Position`` field and ``Value``
    field. The ``Position`` field is used for comparison with the
    component's ``Progress`` field, while the ``Value`` field is the value
    used for driving the field in ``Target``. When ``Interpolate`` is
    checked, the value stored in ``Target`` is linearly interpolated between
    the ``Value``s of the two points surrounding the current ``Progress``.
    When unchecked, the output value is simply set to the ``Value`` of the
    closest point before the current ``Progress``. The only exception to
    this is when no point exists before the current ``Progress``, in which
    case the first point after the current ``Progress`` is used. If two
    points have the same ``Position``, then the point of greatest index
    takes priority if the value is not interpolated or if the positions are
    exactly equal to the current ``Progress``. During interpolation,
    however, the point of least index takes priority.

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
        """Controls which items from the ``Points`` list will be used to drive the value of ``Target``"""
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
        """The field that this component will drive the value of"""
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
        """Controls whether or not this component will interpolate (or blend) between the nearest two ``Points`` to the current ``Progress`` value."""
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
        """A list of items indicating their ``Position`` (in relation to ``Progress``), and a ``Value``"""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set Points. A list of items indicating their ``Position`` (in relation to ``Progress``), and a ``Value``"""
        self.set_member("Points", value)

