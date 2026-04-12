"""Generated component: FootstepEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.ifootstep_event_relay import IFootstepEventRelay
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Footstep Events node takes in the global source of a FootstepEventRelay or SelfFootstepEventRelay component, and returns the values from this user's footstep. The footstep event counts when any proxy on a slot detects the collision and raycast from a user's feet onto that ICollider, as long as that collider does not have the ``No Collision`` setting on, and also does not have the ``Ignore Raycasts`` setting on.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Locomotion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.FootstepEvents"

    def __init__(self, source: str | IGlobalValueProxy[IFootstepEventRelay] | None = None, footstep: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            footstep: Initial value for Footstep.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if footstep is not None:
            self.footstep = footstep

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IGlobalValueProxy[IFootstepEventRelay])."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IGlobalValueProxy[IFootstepEventRelay] | None) -> None:
        """Set the Source reference by target ID or IGlobalValueProxy[IFootstepEventRelay] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.IFootstepEventRelay>'),
            )

    @property
    def footstep(self) -> str | None:
        """Fires when a footstep event happens from a FootstepEventRelay or SelfFootstepEventRelay component."""
        member = self.get_member("Footstep")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @footstep.setter
    def footstep(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Footstep reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Footstep")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Footstep",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def side(self) -> members.EmptyElement | None:
        """Returns the side of that footstep."""
        member = self.get_member("Side")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @side.setter
    def side(self, value: members.EmptyElement) -> None:
        """Set Side. Returns the side of that footstep."""
        self.set_member("Side", value)

    @property
    def position(self) -> members.EmptyElement | None:
        """Returns the position of that footstep."""
        member = self.get_member("Position")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @position.setter
    def position(self, value: members.EmptyElement) -> None:
        """Set Position. Returns the position of that footstep."""
        self.set_member("Position", value)

    @property
    def rotation(self) -> members.EmptyElement | None:
        """Returns the rotation of that footstep."""
        member = self.get_member("Rotation")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @rotation.setter
    def rotation(self, value: members.EmptyElement) -> None:
        """Set Rotation. Returns the rotation of that footstep."""
        self.set_member("Rotation", value)

    @property
    def impact_velocity(self) -> members.EmptyElement | None:
        """Returns the impact velocity of that footstep."""
        member = self.get_member("ImpactVelocity")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @impact_velocity.setter
    def impact_velocity(self, value: members.EmptyElement) -> None:
        """Set ImpactVelocity. Returns the impact velocity of that footstep."""
        self.set_member("ImpactVelocity", value)

    @property
    def has_landed(self) -> members.EmptyElement | None:
        """Returns if this footstep has landed."""
        member = self.get_member("HasLanded")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_landed.setter
    def has_landed(self, value: members.EmptyElement) -> None:
        """Set HasLanded. Returns if this footstep has landed."""
        self.set_member("HasLanded", value)

    @property
    def hit_collider(self) -> members.EmptyElement | None:
        """Returns the collider that this footstep has collided with."""
        member = self.get_member("HitCollider")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_collider.setter
    def hit_collider(self, value: members.EmptyElement) -> None:
        """Set HitCollider. Returns the collider that this footstep has collided with."""
        self.set_member("HitCollider", value)

    @property
    def hit_triangle_index(self) -> members.EmptyElement | None:
        """Returns the particular triangle of where this footstep has collided with."""
        member = self.get_member("HitTriangleIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_triangle_index.setter
    def hit_triangle_index(self, value: members.EmptyElement) -> None:
        """Set HitTriangleIndex. Returns the particular triangle of where this footstep has collided with."""
        self.set_member("HitTriangleIndex", value)

