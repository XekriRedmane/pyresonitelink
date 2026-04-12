"""Generated component: ProtoFluxNodeDebugInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxNodeDebugInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProtoFluxNodeDebugInfo component is used to gather Debug Info on a particular ProtoFlux node and it's group.

    Category: ProtoFlux/Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNodeDebugInfo"

    def __init__(self, node: str | ProtoFluxNode | None = None, is_built: primitives.Bool | None = None, index_in_group: primitives.Int | None = None, allocation_index: primitives.Int | None = None, group_name: primitives.String | None = None, group_is_valid: primitives.Bool | None = None, group_node_count: primitives.Int | None = None, node_instance_hash: primitives.Int | None = None, group_registered_for_continuous_changes: primitives.Bool | None = None, group_registered_for_updates: primitives.Bool | None = None, node_continuously_changing: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            is_built: Initial value for IsBuilt.
            index_in_group: Initial value for IndexInGroup.
            allocation_index: Initial value for AllocationIndex.
            group_name: Initial value for GroupName.
            group_is_valid: Initial value for GroupIsValid.
            group_node_count: Initial value for GroupNodeCount.
            node_instance_hash: Initial value for NodeInstanceHash.
            group_registered_for_continuous_changes: Initial value for GroupRegisteredForContinuousChanges.
            group_registered_for_updates: Initial value for GroupRegisteredForUpdates.
            node_continuously_changing: Initial value for NodeContinuouslyChanging.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if is_built is not None:
            self.is_built = is_built
        if index_in_group is not None:
            self.index_in_group = index_in_group
        if allocation_index is not None:
            self.allocation_index = allocation_index
        if group_name is not None:
            self.group_name = group_name
        if group_is_valid is not None:
            self.group_is_valid = group_is_valid
        if group_node_count is not None:
            self.group_node_count = group_node_count
        if node_instance_hash is not None:
            self.node_instance_hash = node_instance_hash
        if group_registered_for_continuous_changes is not None:
            self.group_registered_for_continuous_changes = group_registered_for_continuous_changes
        if group_registered_for_updates is not None:
            self.group_registered_for_updates = group_registered_for_updates
        if node_continuously_changing is not None:
            self.node_continuously_changing = node_continuously_changing

    @property
    def node(self) -> str | None:
        """The ProtoFlux node to get Debug Info on."""
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
    def is_built(self) -> primitives.Bool | None:
        """Whether the protoflux node group this is in is built."""
        member = self.get_member("IsBuilt")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_built.setter
    def is_built(self, value: primitives.Bool) -> None:
        """Set the IsBuilt field value."""
        member = self.get_member("IsBuilt")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsBuilt", fields.FieldBool(value=value)
            )

    @property
    def index_in_group(self) -> primitives.Int | None:
        """The node's position in its group."""
        member = self.get_member("IndexInGroup")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index_in_group.setter
    def index_in_group(self, value: primitives.Int) -> None:
        """Set the IndexInGroup field value."""
        member = self.get_member("IndexInGroup")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IndexInGroup", fields.FieldInt(value=value)
            )

    @property
    def allocation_index(self) -> primitives.Int | None:
        """The allocation index of this node in its group."""
        member = self.get_member("AllocationIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allocation_index.setter
    def allocation_index(self, value: primitives.Int) -> None:
        """Set the AllocationIndex field value."""
        member = self.get_member("AllocationIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllocationIndex", fields.FieldInt(value=value)
            )

    @property
    def group_name(self) -> primitives.String | None:
        """The autogenerated name of the node group."""
        member = self.get_member("GroupName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_name.setter
    def group_name(self, value: primitives.String) -> None:
        """Set the GroupName field value."""
        member = self.get_member("GroupName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupName", fields.FieldString(value=value)
            )

    @property
    def group_is_valid(self) -> primitives.Bool | None:
        """Whether the group this node is a part of is valid."""
        member = self.get_member("GroupIsValid")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_is_valid.setter
    def group_is_valid(self, value: primitives.Bool) -> None:
        """Set the GroupIsValid field value."""
        member = self.get_member("GroupIsValid")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupIsValid", fields.FieldBool(value=value)
            )

    @property
    def group_node_count(self) -> primitives.Int | None:
        """The number of nodes in the group this node is a part of."""
        member = self.get_member("GroupNodeCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_node_count.setter
    def group_node_count(self, value: primitives.Int) -> None:
        """Set the GroupNodeCount field value."""
        member = self.get_member("GroupNodeCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupNodeCount", fields.FieldInt(value=value)
            )

    @property
    def node_instance_hash(self) -> primitives.Int | None:
        """The hash of this node instance."""
        member = self.get_member("NodeInstanceHash")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @node_instance_hash.setter
    def node_instance_hash(self, value: primitives.Int) -> None:
        """Set the NodeInstanceHash field value."""
        member = self.get_member("NodeInstanceHash")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NodeInstanceHash", fields.FieldInt(value=value)
            )

    @property
    def group_registered_for_continuous_changes(self) -> primitives.Bool | None:
        """Whether the group this node is a part of is registered for continuous changes. See ContinuouslyChanging"""
        member = self.get_member("GroupRegisteredForContinuousChanges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_registered_for_continuous_changes.setter
    def group_registered_for_continuous_changes(self, value: primitives.Bool) -> None:
        """Set the GroupRegisteredForContinuousChanges field value."""
        member = self.get_member("GroupRegisteredForContinuousChanges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupRegisteredForContinuousChanges", fields.FieldBool(value=value)
            )

    @property
    def group_registered_for_updates(self) -> primitives.Bool | None:
        """Whether this group is registered for updates."""
        member = self.get_member("GroupRegisteredForUpdates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_registered_for_updates.setter
    def group_registered_for_updates(self, value: primitives.Bool) -> None:
        """Set the GroupRegisteredForUpdates field value."""
        member = self.get_member("GroupRegisteredForUpdates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupRegisteredForUpdates", fields.FieldBool(value=value)
            )

    @property
    def node_continuously_changing(self) -> primitives.Bool | None:
        """Whether the node this component is debugging is continously changing itself. See ContinuouslyChanging."""
        member = self.get_member("NodeContinuouslyChanging")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @node_continuously_changing.setter
    def node_continuously_changing(self, value: primitives.Bool) -> None:
        """Set the NodeContinuouslyChanging field value."""
        member = self.get_member("NodeContinuouslyChanging")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NodeContinuouslyChanging", fields.FieldBool(value=value)
            )

