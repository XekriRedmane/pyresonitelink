"""Generated component: TweenValue."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.curve_preset import CurvePreset
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TweenValue(GenericComponent[T], IAsyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Tween Value is a node that allows you to change a Target (Numeric or Enum IField`1) over a Duration (float) from a starting point to an ending point. The different curve presets determine the interpolation used, and when applicable will smoothly change using non whole numbers.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Actions

    Parameterize with a value type::

        TweenValue[primitives.Float]
        TweenValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<>"

    def __init__(self, to: str | INodeValueOutput[T] | None = None, from_: str | INodeValueOutput[T] | None = None, duration: str | INodeValueOutput[primitives.Float] | None = None, curve: str | INodeValueOutput[CurvePreset] | None = None, proportional_duration: str | INodeValueOutput[primitives.Bool] | None = None, target: str | INodeObjectOutput[IField[T]] | None = None, on_started: str | INodeOperation | None = None, on_done: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            to: Initial value for To.
            from_: Initial value for From.
            duration: Initial value for Duration.
            curve: Initial value for Curve.
            proportional_duration: Initial value for ProportionalDuration.
            target: Initial value for Target.
            on_started: Initial value for OnStarted.
            on_done: Initial value for OnDone.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if to is not None:
            self.to = to
        if from_ is not None:
            self.from_ = from_
        if duration is not None:
            self.duration = duration
        if curve is not None:
            self.curve = curve
        if proportional_duration is not None:
            self.proportional_duration = proportional_duration
        if target is not None:
            self.target = target
        if on_started is not None:
            self.on_started = on_started
        if on_done is not None:
            self.on_done = on_done

    @property
    def to(self) -> str | None:
        """Target ID of the To reference (targets INodeValueOutput[T])."""
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @to.setter
    def to(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the To reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "To",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def from_(self) -> str | None:
        """Target ID of the From reference (targets INodeValueOutput[T])."""
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @from_.setter
    def from_(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the From reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "From",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def duration(self) -> str | None:
        """Target ID of the Duration reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @duration.setter
    def duration(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Duration reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Duration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def curve(self) -> str | None:
        """Target ID of the Curve reference (targets INodeValueOutput[CurvePreset])."""
        member = self.get_member("Curve")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @curve.setter
    def curve(self, target: str | INodeValueOutput[CurvePreset] | None) -> None:
        """Set the Curve reference by target ID or INodeValueOutput[CurvePreset] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Curve")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Curve",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.CurvePreset>'),
            )

    @property
    def proportional_duration(self) -> str | None:
        """Target ID of the ProportionalDuration reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ProportionalDuration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @proportional_duration.setter
    def proportional_duration(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ProportionalDuration reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ProportionalDuration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProportionalDuration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets INodeObjectOutput[IField[T]])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[IField[T]] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[IField[T]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IField<T>>'),
            )

    @property
    def on_started(self) -> str | None:
        """Target ID of the OnStarted reference (targets INodeOperation)."""
        member = self.get_member("OnStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_started.setter
    def on_started(self, target: str | INodeOperation | None) -> None:
        """Set the OnStarted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_done(self) -> str | None:
        """Target ID of the OnDone reference (targets INodeOperation)."""
        member = self.get_member("OnDone")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_done.setter
    def on_done(self, target: str | INodeOperation | None) -> None:
        """Set the OnDone reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnDone")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDone",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

