"""Generated type: IEngineAssetVariantDescriptor."""

from typing import Generic, TypeVar

D = TypeVar('D')


class IEngineAssetVariantDescriptor(Generic[D]):
    """Interface: [FrooxEngine]FrooxEngine.IEngineAssetVariantDescriptor<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.IEngineAssetVariantDescriptor<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

