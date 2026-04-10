"""Generated type: IAssetProvider."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iasset import IAsset

A = TypeVar('A')


class IAssetProvider(Generic[A]):
    """Interface: [FrooxEngine]FrooxEngine.IAssetProvider<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.IAssetProvider<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

