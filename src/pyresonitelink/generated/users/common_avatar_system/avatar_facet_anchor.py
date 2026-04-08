"""Generated component: AvatarFacetAnchor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarFacetAnchor(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AvatarFacetAnchor.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarFacetAnchor"

    def __init__(self, override_state: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            override_state: Initial value for OverrideState.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if override_state is not None:
            self.override_state = override_state

    @property
    def facet_anchor_point(self) -> members.FieldEnum | None:
        """The FacetAnchorPoint member."""
        member = self.get_member("FacetAnchorPoint")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @facet_anchor_point.setter
    def facet_anchor_point(self, value: members.FieldEnum) -> None:
        """Set the FacetAnchorPoint member."""
        self.set_member("FacetAnchorPoint", value)

    @property
    def override_state(self) -> primitives.Bool | None:
        """The OverrideState field value."""
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

