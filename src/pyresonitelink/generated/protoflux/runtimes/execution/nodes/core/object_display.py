"""Generated component: ObjectDisplay."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iproto_flux_node_pack_unpack_listener import IProtoFluxNodePackUnpackListener
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectDisplay(GenericComponent[T], IProtoFluxNodePackUnpackListener, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Display node takes in an input, but unlike the Input Display node, it will not display out a value onto the node UI, instead this is most likely used for internal use in FrooxEngine.

It is theorized that the wording "External" (found in the node browser after entering that selection) could be in reference to something that allows FrooxEngine to display the value that was inputted outside of the client/engine. Possibly for a console or receiver that is listening outside the application for debugging purposes. (Sources needed please!)

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core

    Parameterize with a value type::

        ObjectDisplay[primitives.Float]
        ObjectDisplay[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ObjectDisplay<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ObjectDisplay<>"

    def __init__(self, input_: str | INodeObjectOutput[T] | None = None, display_text: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Input reference (targets INodeObjectOutput[T])."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the Input reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
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

