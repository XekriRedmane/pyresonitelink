"""Generated component: GenericValueDisplay."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iproto_flux_node_pack_unpack_listener import IProtoFluxNodePackUnpackListener
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericValueDisplay(GenericComponent[T], IProtoFluxNodePackUnpackListener, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core

    Parameterize with a value type::

        GenericValueDisplay[primitives.Float]
        GenericValueDisplay[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<>"

    def __init__(self, input_: str | INodeValueOutput[T] | None = None, display_text: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            input_: Initial value for Input.
            display_text: Initial value for _displayText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if input_ is not None:
            self.input_ = input_
        if display_text is not None:
            self.display_text = display_text

    @property
    def input_(self) -> str | None:
        """Target ID of the Input reference (targets INodeValueOutput[T])."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Input reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def display_text(self) -> str | None:
        """Target ID of the _displayText reference (targets IField[primitives.String])."""
        member = self.get_member("_displayText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_text.setter
    def display_text(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _displayText reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_displayText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_displayText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

