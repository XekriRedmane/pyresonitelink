"""Generated type: IQuantitySI."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iquantity import IQuantity

T = TypeVar('T')


class IQuantitySI(Generic[T]):
    """Interface: IQuantitySI<>."""

    RESONITE_TYPE: str = "IQuantitySI<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

