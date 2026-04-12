"""Generated component: AnimationTrack."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ianimation_track import IAnimationTrack
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AnimationTrack(GenericComponent[T], IAnimationTrack, IWorldEventReceiver):
    """Animation track seems to be a placeholder for future content and is unused. It does not fit into anything in the game internally and it's methods go unused (According to DNSpy 07/26/2024 (mm/dd/yyyy))

    Category: Rendering

    Parameterize with a value type::

        AnimationTrack[primitives.Float]
        AnimationTrack[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AnimationTrack<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.AnimationTrack<>"

    def __init__(self, node: primitives.String | None = None, component_: primitives.String | None = None, property: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for _node.
            component_: Initial value for _component.
            property: Initial value for _property.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if component_ is not None:
            self.component_ = component_
        if property is not None:
            self.property = property

    @property
    def node(self) -> primitives.String | None:
        """Designed to be used to specify the object being controlled by the animation. Can be used with the Find Animation Track Index ProtoFlux node."""
        member = self.get_member("_node")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @node.setter
    def node(self, value: primitives.String) -> None:
        """Set the _node field value."""
        member = self.get_member("_node")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_node", fields.FieldString(value=value)
            )

    @property
    def component_(self) -> primitives.String | None:
        """Designed to be used to specify the field of the object that is being controlled by the animation. Can be used with the Find Animation Track Index ProtoFlux node."""
        member = self.get_member("_component")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @component_.setter
    def component_(self, value: primitives.String) -> None:
        """Set the _component field value."""
        member = self.get_member("_component")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_component", fields.FieldString(value=value)
            )

    @property
    def property(self) -> primitives.String | None:
        """The property on an animation asset"""
        member = self.get_member("_property")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @property.setter
    def property(self, value: primitives.String) -> None:
        """Set the _property field value."""
        member = self.get_member("_property")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_property", fields.FieldString(value=value)
            )

    @property
    def data(self) -> members.Member | None:
        """A list of values at specific time intervals to determine what the whole track's value should be at specific times."""
        member = self.get_member("Data")
        if isinstance(member, members.Member):
            return member
        return None

    @data.setter
    def data(self, value: members.Member) -> None:
        """Set Data. A list of values at specific time intervals to determine what the whole track's value should be at specific times."""
        self.set_member("Data", value)

