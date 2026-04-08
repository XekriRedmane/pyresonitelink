"""Generated component: RandomObjectSpawner."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RandomObjectSpawner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RandomObjectSpawner.

    Category: Transform
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RandomObjectSpawner"

    @property
    def templates(self) -> members.SyncList | None:
        """The Templates member."""
        member = self.get_member("Templates")
        if isinstance(member, members.SyncList):
            return member
        return None

    @templates.setter
    def templates(self, value: members.SyncList) -> None:
        """Set the Templates member."""
        self.set_member("Templates", value)

    @property
    def spawn_space(self) -> members.SyncObject | None:
        """The SpawnSpace member."""
        member = self.get_member("SpawnSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @spawn_space.setter
    def spawn_space(self, value: members.SyncObject) -> None:
        """Set the SpawnSpace member."""
        self.set_member("SpawnSpace", value)

    async def spawn(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Spawn sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Spawn", {}, debug,
        )

    async def spawn_at_point(self, resolink: protocols.ResoniteLinkClient, point: primitives.Float3, debug: bool = False) -> dict:
        """Call the SpawnAtPoint sync method.

        Args:
            resolink: Connected ResoniteLink client.
            point: The point parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SpawnAtPoint", {"point": point}, debug,
        )

