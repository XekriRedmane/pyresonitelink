"""Generated component: UniverseStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UniverseStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UniverseStatus component provides information on the current universe.

    Category: Cloud/Indicators

    Attach to a slot and it will start giving data on the current universe.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UniverseStatus"

    def __init__(self, universe_id: primitives.String | None = None, universe_name: primitives.String | None = None, primary_group_id: primitives.String | None = None, in_universe: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            universe_id: Initial value for UniverseId.
            universe_name: Initial value for UniverseName.
            primary_group_id: Initial value for PrimaryGroupId.
            in_universe: Initial value for InUniverse.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if universe_id is not None:
            self.universe_id = universe_id
        if universe_name is not None:
            self.universe_name = universe_name
        if primary_group_id is not None:
            self.primary_group_id = primary_group_id
        if in_universe is not None:
            self.in_universe = in_universe

    @property
    def universe_id(self) -> primitives.String | None:
        """The ID of the universe current Universe."""
        member = self.get_member("UniverseId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @universe_id.setter
    def universe_id(self, value: primitives.String) -> None:
        """Set the UniverseId field value."""
        member = self.get_member("UniverseId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UniverseId", fields.FieldString(value=value)
            )

    @property
    def universe_name(self) -> primitives.String | None:
        """The universe's name."""
        member = self.get_member("UniverseName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @universe_name.setter
    def universe_name(self, value: primitives.String) -> None:
        """Set the UniverseName field value."""
        member = self.get_member("UniverseName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UniverseName", fields.FieldString(value=value)
            )

    @property
    def primary_group_id(self) -> primitives.String | None:
        """The ID of the primary group of the universe."""
        member = self.get_member("PrimaryGroupId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @primary_group_id.setter
    def primary_group_id(self, value: primitives.String) -> None:
        """Set the PrimaryGroupId field value."""
        member = self.get_member("PrimaryGroupId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PrimaryGroupId", fields.FieldString(value=value)
            )

    @property
    def in_universe(self) -> primitives.Bool | None:
        """Whether we are in a universe or not."""
        member = self.get_member("InUniverse")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @in_universe.setter
    def in_universe(self, value: primitives.Bool) -> None:
        """Set the InUniverse field value."""
        member = self.get_member("InUniverse")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InUniverse", fields.FieldBool(value=value)
            )

