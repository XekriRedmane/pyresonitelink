"""Generated component: Int3ToInt2SwizzleDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Int3ToInt2SwizzleDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Int 3To Int 2Swizzle Driver component.

    Category: Relations/Swizzle Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Int3ToInt2SwizzleDriver"

    def __init__(self, source: str | IField[primitives.Int3] | None = None, target: str | IField[primitives.Int2] | None = None, x: primitives.Int | None = None, y: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            target: Initial value for Target.
            x: Initial value for X.
            y: Initial value for Y.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IField[primitives.Int3])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IField[primitives.Int3] | None) -> None:
        """Set the Source reference by target ID or IField[primitives.Int3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int3>'),
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Int2])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Int2] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Int2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int2>'),
            )

    @property
    def x(self) -> primitives.Int | None:
        """The X field value."""
        member = self.get_member("X")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @x.setter
    def x(self, value: primitives.Int) -> None:
        """Set the X field value."""
        member = self.get_member("X")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "X", fields.FieldInt(value=value)
            )

    @property
    def y(self) -> primitives.Int | None:
        """The Y field value."""
        member = self.get_member("Y")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @y.setter
    def y(self, value: primitives.Int) -> None:
        """Set the Y field value."""
        member = self.get_member("Y")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Y", fields.FieldInt(value=value)
            )

