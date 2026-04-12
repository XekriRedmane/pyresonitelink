"""Generated component: ScaleElement."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.scale_group import ScaleGroup
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleElement(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The ScaleElement component scales itself up or down depending on if it is the selected scale element in a Scale Group..

    Category: Transform/Interaction

    Used along with a Scale Group to make a list of selectable items via
    touching them.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleElement"

    def __init__(self, group: str | ScaleGroup | None = None, respond_to_physical_touch: primitives.Bool | None = None, respond_to_remote_touch: primitives.Bool | None = None, scale_target: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            group: Initial value for Group.
            respond_to_physical_touch: Initial value for RespondToPhysicalTouch.
            respond_to_remote_touch: Initial value for RespondToRemoteTouch.
            scale_target: Initial value for _scaleTarget.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if group is not None:
            self.group = group
        if respond_to_physical_touch is not None:
            self.respond_to_physical_touch = respond_to_physical_touch
        if respond_to_remote_touch is not None:
            self.respond_to_remote_touch = respond_to_remote_touch
        if scale_target is not None:
            self.scale_target = scale_target

    @property
    def group(self) -> str | None:
        """The group this belongs to. If there is a group in this component's parents, the group is auto filled into this field on attach."""
        member = self.get_member("Group")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group.setter
    def group(self, target: str | ScaleGroup | None) -> None:
        """Set the Group reference by target ID or ScaleGroup instance."""
        target_id: str | None = target.id if isinstance(target, ScaleGroup) else target  # type: ignore[assignment]
        member = self.get_member("Group")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Group",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScaleGroup'),
            )

    @property
    def respond_to_physical_touch(self) -> primitives.Bool | None:
        """Whether to make this item selected upon physical touch."""
        member = self.get_member("RespondToPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @respond_to_physical_touch.setter
    def respond_to_physical_touch(self, value: primitives.Bool) -> None:
        """Set the RespondToPhysicalTouch field value."""
        member = self.get_member("RespondToPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RespondToPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def respond_to_remote_touch(self) -> primitives.Bool | None:
        """Whether to make this item selected upon clicking via laser."""
        member = self.get_member("RespondToRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @respond_to_remote_touch.setter
    def respond_to_remote_touch(self, value: primitives.Bool) -> None:
        """Set the RespondToRemoteTouch field value."""
        member = self.get_member("RespondToRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RespondToRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def scale_target(self) -> str | None:
        """The field to drive in order to influence the scale of this slot when selecting/deselecting."""
        member = self.get_member("_scaleTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_target.setter
    def scale_target(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scaleTarget reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scaleTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scaleTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

