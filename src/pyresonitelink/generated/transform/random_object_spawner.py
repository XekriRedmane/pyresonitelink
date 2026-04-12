"""Generated component: RandomObjectSpawner."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RandomObjectSpawner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RandomObjectSpawner component selects a slot from the ``Templates`` list, and spawns it either at this component's parent (in the case of ``Spawn()``), or at the point specified in an argument (in the case of ``SpawnAtPoint()``)

    Category: Transform

    **Behavior**: When triggered by any event source that accepts an Action (for ``Spawn()``), or Action (for ``SpawnAtPoint()``, this component will spawn a random slot from ``Templates``

Prior to Build 2020.11.8.605, this component would duplicate a random slot from ``Templates`` in-place, without changing its location.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RandomObjectSpawner"

    @property
    def templates(self) -> members.SyncList | None:
        """List of slots to be selected from, when a Trigger is invoked"""
        member = self.get_member("Templates")
        if isinstance(member, members.SyncList):
            return member
        return None

    @templates.setter
    def templates(self, value: members.SyncList) -> None:
        """Set Templates. List of slots to be selected from, when a Trigger is invoked"""
        self.set_member("Templates", value)

    @property
    def spawn_space(self) -> members.SyncObject | None:
        """The coordinate space in which the template item will be spawned."""
        member = self.get_member("SpawnSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @spawn_space.setter
    def spawn_space(self, value: members.SyncObject) -> None:
        """Set SpawnSpace. The coordinate space in which the template item will be spawned."""
        self.set_member("SpawnSpace", value)

    async def spawn(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Spawns a slot randomly selected from ``Templates``, located at the origin of this component's parent slot.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Spawn", {}, debug,
        )

    async def spawn_at_point(self, resolink: protocols.ResoniteLinkClient, point: primitives.Float3, debug: bool = False) -> dict:
        """Spawns a slot randomly selected from ``Templates``, located at the provided point.

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

