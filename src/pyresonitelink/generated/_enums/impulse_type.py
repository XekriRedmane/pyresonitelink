"""Generated enum: ImpulseType."""

from enum import StrEnum


class ImpulseType(StrEnum):
    """Enum: [ProtoFlux.Core]ProtoFlux.Core.ImpulseType."""

    continuation = "Continuation"
    call = "Call"
    async_call = "AsyncCall"
    sync_resumption = "SyncResumption"
    async_resumption = "AsyncResumption"

