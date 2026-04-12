"""Generated component: ProtoFluxOutputProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_output import INodeOutput
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxOutputProxy(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProtoFluxOutputProxy component is used to manage the output sockets of protoflux nodes, making components become the actual visuals the user uses to interact with protoflux with. Otherwise, users would have to use purely the developer tool.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxOutputProxy"

    def __init__(self, node: str | ProtoFluxNode | None = None, element_name: primitives.String | None = None, is_dynamic: primitives.Bool | None = None, index: primitives.Int | None = None, connect_point: str | Slot | None = None, node_output: str | INodeOutput | None = None, output_type: Type | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            element_name: Initial value for ElementName.
            is_dynamic: Initial value for IsDynamic.
            index: Initial value for Index.
            connect_point: Initial value for ConnectPoint.
            node_output: Initial value for NodeOutput.
            output_type: Initial value for OutputType.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if element_name is not None:
            self.element_name = element_name
        if is_dynamic is not None:
            self.is_dynamic = is_dynamic
        if index is not None:
            self.index = index
        if connect_point is not None:
            self.connect_point = connect_point
        if node_output is not None:
            self.node_output = node_output
        if output_type is not None:
            self.output_type = output_type

    @property
    def node(self) -> str | None:
        """The ProtoFlux component whose output you wish to proxy."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | ProtoFluxNode | None) -> None:
        """Set the Node reference by target ID or ProtoFluxNode instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxNode) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNode'),
            )

    @property
    def element_name(self) -> primitives.String | None:
        """The name that appears when you hover this output with a Flux Tool."""
        member = self.get_member("ElementName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @element_name.setter
    def element_name(self, value: primitives.String) -> None:
        """Set the ElementName field value."""
        member = self.get_member("ElementName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ElementName", fields.FieldString(value=value)
            )

    @property
    def is_dynamic(self) -> primitives.Bool | None:
        """Whether this output can be converted by inputting a different type."""
        member = self.get_member("IsDynamic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_dynamic.setter
    def is_dynamic(self, value: primitives.Bool) -> None:
        """Set the IsDynamic field value."""
        member = self.get_member("IsDynamic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsDynamic", fields.FieldBool(value=value)
            )

    @property
    def index(self) -> primitives.Int | None:
        """The index in a list if this points to a list of outputs."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def connect_point(self) -> str | None:
        """What Slot a wire visual parents itself under."""
        member = self.get_member("ConnectPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @connect_point.setter
    def connect_point(self, target: str | Slot | None) -> None:
        """Set the ConnectPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ConnectPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConnectPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def node_output(self) -> str | None:
        """The field on a protoflux node Component this connector is being used as a way to connect to."""
        member = self.get_member("NodeOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node_output.setter
    def node_output(self, target: str | INodeOutput | None) -> None:
        """Set the NodeOutput reference by target ID or INodeOutput instance."""
        target_id: str | None = target.id if isinstance(target, INodeOutput) else target  # type: ignore[assignment]
        member = self.get_member("NodeOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NodeOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOutput'),
            )

    @property
    def output_type(self) -> Type | None:
        """The type of the output this proxy is for."""
        member = self.get_member("OutputType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @output_type.setter
    def output_type(self, value: Type | str) -> None:
        """Set OutputType. The type of the output this proxy is for."""
        member = self.get_member("OutputType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OutputType",
                members.FieldEnum(value=str(value)),
            )

