"""Generated component: RectTransformComputedProperties."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectTransformComputedProperties(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RectTransformComputedProperties component is used to get the real size of a UIX element that is contained in a slot that has a RectTransform. It takes in the RectTransform reference, and then returns a ``LocalComputerRect``, which is the local bounds of the element, and returns the ``BoundingRect``, which is the bounding rect itself (which can be larger than the local elements from within). Most of the time, both values would be the same, except for some situations.

}}

    Category: Debug

    This is used to get the size of the bounds of whatever is inside the
    RectTransform.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectTransformComputedProperties"

    def __init__(self, rect: str | RectTransform | None = None, local_compute_rect: primitives.Rect | None = None, bounding_rect: primitives.Rect | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rect: Initial value for Rect.
            local_compute_rect: Initial value for LocalComputeRect.
            bounding_rect: Initial value for BoundingRect.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rect is not None:
            self.rect = rect
        if local_compute_rect is not None:
            self.local_compute_rect = local_compute_rect
        if bounding_rect is not None:
            self.bounding_rect = bounding_rect

    @property
    def rect(self) -> str | None:
        """The rect transform component to reference from"""
        member = self.get_member("Rect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rect.setter
    def rect(self, target: str | RectTransform | None) -> None:
        """Set the Rect reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("Rect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def local_compute_rect(self) -> primitives.Rect | None:
        """The local bounds of the element"""
        member = self.get_member("LocalComputeRect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_compute_rect.setter
    def local_compute_rect(self, value: primitives.Rect) -> None:
        """Set the LocalComputeRect field value."""
        member = self.get_member("LocalComputeRect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalComputeRect", fields.FieldRect(value=value)
            )

    @property
    def bounding_rect(self) -> primitives.Rect | None:
        """The bounding rect itself"""
        member = self.get_member("BoundingRect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bounding_rect.setter
    def bounding_rect(self, value: primitives.Rect) -> None:
        """Set the BoundingRect field value."""
        member = self.get_member("BoundingRect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoundingRect", fields.FieldRect(value=value)
            )

