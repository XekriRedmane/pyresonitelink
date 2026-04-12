"""Generated component: ObjectFieldHook."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectFieldHook(GenericComponent[T], IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Field Hook node takes in a target field and the source field value, then returns if this field is driving, as well as allowing the user to start and stop driving this field. This node gives the user more control to programmatically drive fields directly using ProtoFlux. This node hooks the given field, so whenever something external tries to write to it, it will receive a pulse from OnHook as well as the value it tried to write from HookedValue.

Manually unlinking the drive in an inspector behaves the same as triggering StopDrive.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core

    Parameterize with a value type::

        ObjectFieldHook[primitives.Float]
        ObjectFieldHook[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.ObjectFieldHook<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.ObjectFieldHook<>"

    def __init__(self, target: str | INodeObjectOutput[IField[T]] | None = None, on_start_drive: str | INodeOperation | None = None, on_stop_drive: str | INodeOperation | None = None, on_hook: str | ISyncNodeOperation | None = None, source: str | INodeObjectOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            on_start_drive: Initial value for OnStartDrive.
            on_stop_drive: Initial value for OnStopDrive.
            on_hook: Initial value for OnHook.
            source: Initial value for Source.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if on_start_drive is not None:
            self.on_start_drive = on_start_drive
        if on_stop_drive is not None:
            self.on_stop_drive = on_stop_drive
        if on_hook is not None:
            self.on_hook = on_hook
        if source is not None:
            self.source = source

    @property
    def target(self) -> str | None:
        """The target field to drive."""
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
    def is_driving(self) -> members.EmptyElement | None:
        """Returns if the target field is being driven."""
        member = self.get_member("IsDriving")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_driving.setter
    def is_driving(self, value: members.EmptyElement) -> None:
        """Set IsDriving. Returns if the target field is being driven."""
        self.set_member("IsDriving", value)

    @property
    def start_drive(self) -> members.EmptyElement | None:
        """Calls an impulse to start driving the target (hooking into it)."""
        member = self.get_member("StartDrive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @start_drive.setter
    def start_drive(self, value: members.EmptyElement) -> None:
        """Set StartDrive. Calls an impulse to start driving the target (hooking into it)."""
        self.set_member("StartDrive", value)

    @property
    def stop_drive(self) -> members.EmptyElement | None:
        """Calls an impulse to stop driving the target (unhooking it)."""
        member = self.get_member("StopDrive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @stop_drive.setter
    def stop_drive(self, value: members.EmptyElement) -> None:
        """Set StopDrive. Calls an impulse to stop driving the target (unhooking it)."""
        self.set_member("StopDrive", value)

    @property
    def on_start_drive(self) -> str | None:
        """Fires when we started driving the target field."""
        member = self.get_member("OnStartDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_start_drive.setter
    def on_start_drive(self, target: str | INodeOperation | None) -> None:
        """Set the OnStartDrive reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStartDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStartDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_stop_drive(self) -> str | None:
        """Fires when we stopped driving the target field."""
        member = self.get_member("OnStopDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_stop_drive.setter
    def on_stop_drive(self, target: str | INodeOperation | None) -> None:
        """Set the OnStopDrive reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnStopDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnStopDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_hook(self) -> str | None:
        """Fires when something writes to the target field while it is being driven by this node."""
        member = self.get_member("OnHook")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_hook.setter
    def on_hook(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnHook reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnHook")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnHook",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def source(self) -> str | None:
        """The source to drive Target from. While active this acts like any other drive."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the Source reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

    @property
    def hooked_value(self) -> members.EmptyElement | None:
        """Returns the value that was written by the OnHook call."""
        member = self.get_member("HookedValue")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hooked_value.setter
    def hooked_value(self, value: members.EmptyElement) -> None:
        """Set HookedValue. Returns the value that was written by the OnHook call."""
        self.set_member("HookedValue", value)

