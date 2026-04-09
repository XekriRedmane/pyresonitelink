"""Protocol interfaces for breaking circular imports.

This module defines Protocol classes that describe the interfaces
used by generated components to communicate with the server. The
actual ``Client`` class implements these protocols, but generated
code depends only on the protocol — not on the concrete class.
"""

from typing import Protocol

from . import codec
from . import messages
from . import responses
from . import workers


class ResoniteLinkClient(Protocol):
    """Protocol describing the client interface used by generated components.

    The concrete ``pyresonitelink.client.Client`` class satisfies this
    protocol.  Generated component code (``_base.py``, generated method
    wrappers) depends only on this protocol, avoiding circular imports.
    """

    async def get_slot(
        self,
        slot: str | workers.Slot,
        depth: int = 0,
        includeComponentData: bool = False,
        debug: bool = False,
    ) -> responses.SlotData: ...

    async def add_component(
        self,
        containerSlotId: str | workers.Slot,
        *,
        data: workers.Component | None = None,
        componentType: str | None = None,
        references: dict[str, str] | None = None,
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

    async def request_json(
        self,
        message: messages.Message,
        debug: bool = False,
    ) -> dict[str, codec.JsonValue]: ...
