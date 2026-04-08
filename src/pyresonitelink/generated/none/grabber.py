"""Generated component: Grabber."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.body_node import BodyNode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Grabber(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Grabber is a Component that is used in a User's hiearchy to allow the user to grab objects. This component is generated internally usually. Interacting with this component dynamically is done through Grabbable ProtoFlux Nodes.

    This component can be triggered to grab things by the user. However,
    this requires a TrackedHand to be attached under the user, or be part of
    an avatar spawned onto them. The tracked hand then auto generates this
    component. However, the component only will grab things when that
    tracked hand component detects that the user associated with it is
    trying to grab using the hand side it is assigned to. This does allow
    for multiple grabbers on the same hand however.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Grabber"

    def __init__(self, auto_update_user: str | User | None = None, release_check_radius: primitives.Float | None = None, corresponding_body_node: BodyNode | str | None = None, scale_reference: str | Grabber | None = None, base_scale: primitives.Float3 | None = None, base_distance: primitives.Float | None = None, holder_slot: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_update_user: Initial value for AutoUpdateUser.
            release_check_radius: Initial value for ReleaseCheckRadius.
            corresponding_body_node: Initial value for CorrespondingBodyNode.
            scale_reference: Initial value for _scaleReference.
            base_scale: Initial value for _baseScale.
            base_distance: Initial value for _baseDistance.
            holder_slot: Initial value for _holderSlot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_update_user is not None:
            self.auto_update_user = auto_update_user
        if release_check_radius is not None:
            self.release_check_radius = release_check_radius
        if corresponding_body_node is not None:
            self.corresponding_body_node = corresponding_body_node
        if scale_reference is not None:
            self.scale_reference = scale_reference
        if base_scale is not None:
            self.base_scale = base_scale
        if base_distance is not None:
            self.base_distance = base_distance
        if holder_slot is not None:
            self.holder_slot = holder_slot

    @property
    def auto_update_user(self) -> str | None:
        """The user handling updates for this Grabber."""
        member = self.get_member("AutoUpdateUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_update_user.setter
    def auto_update_user(self, target: str | User | None) -> None:
        """Set the AutoUpdateUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("AutoUpdateUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AutoUpdateUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def release_check_radius(self) -> primitives.Float | None:
        """How far to check before releasing a grabbable from the ``_baseDistance``. Usually used for dynamic bones."""
        member = self.get_member("ReleaseCheckRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_check_radius.setter
    def release_check_radius(self, value: primitives.Float) -> None:
        """Set the ReleaseCheckRadius field value."""
        member = self.get_member("ReleaseCheckRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReleaseCheckRadius", fields.FieldFloat(value=value)
            )

    @property
    def corresponding_body_node(self) -> BodyNode | None:
        """The node this hand is associated with."""
        member = self.get_member("CorrespondingBodyNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BodyNode(member.value)
        return None

    @corresponding_body_node.setter
    def corresponding_body_node(self, value: BodyNode | str) -> None:
        """Set CorrespondingBodyNode. The node this hand is associated with."""
        member = self.get_member("CorrespondingBodyNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CorrespondingBodyNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def scale_reference(self) -> str | None:
        """The grabber used as a scale reference, like the opposite hand."""
        member = self.get_member("_scaleReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_reference.setter
    def scale_reference(self, target: str | Grabber | None) -> None:
        """Set the _scaleReference reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_scaleReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def base_scale(self) -> primitives.Float3 | None:
        """The default scale for the grabber."""
        member = self.get_member("_baseScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_scale.setter
    def base_scale(self, value: primitives.Float3) -> None:
        """Set the _baseScale field value."""
        member = self.get_member("_baseScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_baseScale", fields.FieldFloat3(value=value)
            )

    @property
    def base_distance(self) -> primitives.Float | None:
        """The default distance for the grabber."""
        member = self.get_member("_baseDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_distance.setter
    def base_distance(self, value: primitives.Float) -> None:
        """Set the _baseDistance field value."""
        member = self.get_member("_baseDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_baseDistance", fields.FieldFloat(value=value)
            )

    @property
    def holder_slot(self) -> str | None:
        """The slot used to store objects being grabbed by the user."""
        member = self.get_member("_holderSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @holder_slot.setter
    def holder_slot(self, target: str | Slot | None) -> None:
        """Set the _holderSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_holderSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_holderSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

