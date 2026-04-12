"""Generated enum: HostAccessScope."""

from enum import StrEnum


class HostAccessScope(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.HostAccessScope."""

    everything = "Everything"
    http = "HTTP"
    websocket = "Websocket"
    osc_sender = "OSC_Sender"
    osc_receiver = "OSC_Receiver"

