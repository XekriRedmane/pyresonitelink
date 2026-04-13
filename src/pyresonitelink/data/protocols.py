"""Protocol definitions for ResoniteLink client components."""

from __future__ import annotations

from typing import Any, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from pyresonitelink.data import codec
    from pyresonitelink.data import messages
    from pyresonitelink.data import responses
    from pyresonitelink.data import workers
    from pyresonitelink.data import members


class ResoniteLinkClient(Protocol):
    """Protocol for a ResoniteLink client."""

    async def get_slot(
        self,
        slot: str | workers.Slot,
        depth: int = 0,
        debug: bool = False,
    ) -> responses.SlotData: ...

    async def find_slot(
        self,
        parent: str | workers.Slot,
        name: str,
        debug: bool = False,
    ) -> workers.Slot | None: ...

    async def remove_slot(
        self,
        slot: str | workers.Slot,
        debug: bool = False,
    ) -> responses.Response: ...

    async def get_slot_data(
        self,
        slotId: str,
        debug: bool = False,
    ) -> responses.SlotData: ...

    async def add_slot(self, **kwargs: Any) -> workers.Slot: ...

    async def add_component(
        self,
        containerSlotId: str,
        componentType: str | None = None,
        references: dict[str, str | members.Reference] | None = None,
        debug: bool = False,
    ) -> responses.NewEntityId: ...

    async def get_component(
        self,
        componentId: str,
        debug: bool = False,
    ) -> responses.ComponentData: ...

    async def update_component(
        self,
        data: workers.Component,
        debug: bool = False,
    ) -> responses.Response: ...

    async def update_references(
        self,
        componentId: str,
        references: dict[str, str | members.Reference],
        debug: bool = False,
    ) -> responses.Response: ...

    async def request_json(
        self,
        message: messages.Message,
        debug: bool = False,
    ) -> dict[str, codec.JsonValue]: ...
