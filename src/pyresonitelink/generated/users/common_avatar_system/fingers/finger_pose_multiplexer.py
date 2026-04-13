"""Generated component: FingerPoseMultiplexer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifinger_pose_source_component import IFingerPoseSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FingerPoseMultiplexer(GeneratedComponent, IFingerPoseSourceComponent, IWorldEventReceiver):
    """The FingerPoseMultiplexer component can be used to get data from multiple finger pose sources and make that data its own finger pose source data. This component in itself is a IFingerPoseSourceComponent.

For more information on finger pose sources, please see Finger Posing System.

    Category: Users/Common Avatar System/Fingers

    Add items to the list of ``Sources`` to transition between and get data
    from. The data gotten is copied and becomes the data of this component.
    Can be used in the ways outlined in Finger Posing System.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FingerPoseMultiplexer"

    def __init__(self, index_: primitives.Int | None = None, interpolation_speed: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            index_: Initial value for Index.
            interpolation_speed: Initial value for InterpolationSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if index_ is not None:
            self.index_ = index_
        if interpolation_speed is not None:
            self.interpolation_speed = interpolation_speed

    @property
    def index_(self) -> primitives.Int | None:
        """What Component in ``Sources`` to copy data from for the finger pose data for this component."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index_.setter
    def index_(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def interpolation_speed(self) -> primitives.Float | None:
        """How fast the Multiplexer transitions what data this component is copying for this component's finger pose data."""
        member = self.get_member("InterpolationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interpolation_speed.setter
    def interpolation_speed(self, value: primitives.Float) -> None:
        """Set the InterpolationSpeed field value."""
        member = self.get_member("InterpolationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterpolationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def sources(self) -> members.SyncList | None:
        """The list if Finger pose sources to copy data from for the data for this component's Finger pose data."""
        member = self.get_member("Sources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sources.setter
    def sources(self, value: members.SyncList) -> None:
        """Set Sources. The list if Finger pose sources to copy data from for the data for this component's Finger pose data."""
        self.set_member("Sources", value)

