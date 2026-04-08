"""Generated component: ProtoFluxImpulseProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.proto_flux_wire_manager import ProtoFluxWireManager
from pyresonitelink.generated._types.isync_ref import ISyncRef


class ProtoFluxImpulseProxy(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxImpulseProxy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxImpulseProxy"

    def __init__(self, node: str | ProtoFluxNode | None = None, element_name: primitives.String | None = None, is_dynamic: primitives.Bool | None = None, index: primitives.Int | None = None, connect_point: str | Slot | None = None, wire: str | ProtoFluxWireManager | None = None, node_impulse: str | ISyncRef | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            element_name: Initial value for ElementName.
            is_dynamic: Initial value for IsDynamic.
            index: Initial value for Index.
            connect_point: Initial value for ConnectPoint.
            wire: Initial value for Wire.
            node_impulse: Initial value for NodeImpulse.
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
        if wire is not None:
            self.wire = wire
        if node_impulse is not None:
            self.node_impulse = node_impulse

    @property
    def node(self) -> str | None:
        """Target ID of the Node reference (targets ProtoFluxNode)."""
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
        """The ElementName field value."""
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
        """The IsDynamic field value."""
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
        """The Index field value."""
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
        """Target ID of the ConnectPoint reference (targets Slot)."""
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
    def wire(self) -> str | None:
        """Target ID of the Wire reference (targets ProtoFluxWireManager)."""
        member = self.get_member("Wire")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @wire.setter
    def wire(self, target: str | ProtoFluxWireManager | None) -> None:
        """Set the Wire reference by target ID or ProtoFluxWireManager instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxWireManager) else target  # type: ignore[assignment]
        member = self.get_member("Wire")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Wire",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxWireManager'),
            )

    @property
    def node_impulse(self) -> str | None:
        """Target ID of the NodeImpulse reference (targets ISyncRef)."""
        member = self.get_member("NodeImpulse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node_impulse.setter
    def node_impulse(self, target: str | ISyncRef | None) -> None:
        """Set the NodeImpulse reference by target ID or ISyncRef instance."""
        target_id: str | None = target.id if isinstance(target, ISyncRef) else target  # type: ignore[assignment]
        member = self.get_member("NodeImpulse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NodeImpulse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncRef'),
            )

    @property
    def impulse_type(self) -> members.FieldEnum | None:
        """The ImpulseType member."""
        member = self.get_member("ImpulseType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @impulse_type.setter
    def impulse_type(self, value: members.FieldEnum) -> None:
        """Set the ImpulseType member."""
        self.set_member("ImpulseType", value)

