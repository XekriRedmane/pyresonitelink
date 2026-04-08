"""Generated component: ProtoFluxOperationProxy."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxOperationProxy(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxOperationProxy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxOperationProxy"

    def __init__(self, node: str | ProtoFluxNode | None = None, element_name: str | None = None, is_dynamic: bool | None = None, index: np.int32 | None = None, connect_point: str | Slot | None = None, node_operation: str | INodeOperation | None = None, is_async: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            element_name: Initial value for ElementName.
            is_dynamic: Initial value for IsDynamic.
            index: Initial value for Index.
            connect_point: Initial value for ConnectPoint.
            node_operation: Initial value for NodeOperation.
            is_async: Initial value for IsAsync.
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
        if node_operation is not None:
            self.node_operation = node_operation
        if is_async is not None:
            self.is_async = is_async

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
    def element_name(self) -> str | None:
        """The ElementName field value."""
        member = self.get_member("ElementName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @element_name.setter
    def element_name(self, value: str) -> None:
        """Set the ElementName field value."""
        member = self.get_member("ElementName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ElementName", fields.FieldString(value=value)
            )

    @property
    def is_dynamic(self) -> bool | None:
        """The IsDynamic field value."""
        member = self.get_member("IsDynamic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_dynamic.setter
    def is_dynamic(self, value: bool) -> None:
        """Set the IsDynamic field value."""
        member = self.get_member("IsDynamic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsDynamic", fields.FieldBool(value=value)
            )

    @property
    def index(self) -> np.int32 | None:
        """The Index field value."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: np.int32) -> None:
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
    def node_operation(self) -> str | None:
        """Target ID of the NodeOperation reference (targets INodeOperation)."""
        member = self.get_member("NodeOperation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node_operation.setter
    def node_operation(self, target: str | INodeOperation | None) -> None:
        """Set the NodeOperation reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("NodeOperation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NodeOperation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def is_async(self) -> bool | None:
        """The IsAsync field value."""
        member = self.get_member("IsAsync")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_async.setter
    def is_async(self, value: bool) -> None:
        """Set the IsAsync field value."""
        member = self.get_member("IsAsync")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsAsync", fields.FieldBool(value=value)
            )

