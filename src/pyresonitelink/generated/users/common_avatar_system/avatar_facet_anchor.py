"""Generated component: AvatarFacetAnchor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.facet_anchor_point import FacetAnchorPoint
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarFacetAnchor(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Avatar Facet Anchor is a component that is used to position a userspace facet anchor to the slot this is on.

    Category: Users/Common Avatar System

    Will not work if the component's active user is not the local user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarFacetAnchor"

    def __init__(self, facet_anchor_point: FacetAnchorPoint | str | None = None, override_state: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            facet_anchor_point: Initial value for FacetAnchorPoint.
            override_state: Initial value for OverrideState.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if facet_anchor_point is not None:
            self.facet_anchor_point = facet_anchor_point
        if override_state is not None:
            self.override_state = override_state

    @property
    def facet_anchor_point(self) -> FacetAnchorPoint | None:
        """Which facet anchor should be positioned at the slot this component is on."""
        member = self.get_member("FacetAnchorPoint")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return FacetAnchorPoint(member.value)
        return None

    @facet_anchor_point.setter
    def facet_anchor_point(self, value: FacetAnchorPoint | str) -> None:
        """Set FacetAnchorPoint. Which facet anchor should be positioned at the slot this component is on."""
        member = self.get_member("FacetAnchorPoint")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "FacetAnchorPoint",
                members.FieldEnum(value=str(value)),
            )

    @property
    def override_state(self) -> primitives.Bool | None:
        """Whether to force this anchor to stay on or off."""
        member = self.get_member("OverrideState")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_state.setter
    def override_state(self, value: primitives.Bool) -> None:
        """Set the OverrideState field value."""
        member = self.get_member("OverrideState")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideState", fields.FieldNullableBool(value=value)
            )

