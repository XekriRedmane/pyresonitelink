"""Generated type: ContainerWorker."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.component_base import ComponentBase

C = TypeVar('C')


class ContainerWorker(Worker, Generic[C]):
    """Abstract class: [FrooxEngine]FrooxEngine.ContainerWorker<>."""

