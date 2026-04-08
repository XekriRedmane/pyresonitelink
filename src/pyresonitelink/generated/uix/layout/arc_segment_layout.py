"""Generated component: ArcSegmentLayout."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ArcSegmentLayout(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ArcSegmentLayout.

    Category: UIX/Layout
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ArcSegmentLayout"

    def __init__(self, nested: str | RectTransform | None = None, nested_size_ratio: np.float32 | None = None, label: str | Text | None = None, label_size: primitives.Float2 | None = None, label_distance: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            nested: Initial value for Nested.
            nested_size_ratio: Initial value for NestedSizeRatio.
            label: Initial value for Label.
            label_size: Initial value for LabelSize.
            label_distance: Initial value for LabelDistance.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if nested is not None:
            self.nested = nested
        if nested_size_ratio is not None:
            self.nested_size_ratio = nested_size_ratio
        if label is not None:
            self.label = label
        if label_size is not None:
            self.label_size = label_size
        if label_distance is not None:
            self.label_distance = label_distance

    @property
    def nested(self) -> str | None:
        """Target ID of the Nested reference (targets RectTransform)."""
        member = self.get_member("Nested")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @nested.setter
    def nested(self, target: str | RectTransform | None) -> None:
        """Set the Nested reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("Nested")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Nested",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def nested_size_ratio(self) -> np.float32 | None:
        """The NestedSizeRatio field value."""
        member = self.get_member("NestedSizeRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @nested_size_ratio.setter
    def nested_size_ratio(self, value: np.float32) -> None:
        """Set the NestedSizeRatio field value."""
        member = self.get_member("NestedSizeRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NestedSizeRatio", fields.FieldFloat(value=value)
            )

    @property
    def label(self) -> str | None:
        """Target ID of the Label reference (targets Text)."""
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | Text | None) -> None:
        """Set the Label reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Label",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def label_size(self) -> primitives.Float2 | None:
        """The LabelSize field value."""
        member = self.get_member("LabelSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_size.setter
    def label_size(self, value: primitives.Float2) -> None:
        """Set the LabelSize field value."""
        member = self.get_member("LabelSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelSize", fields.FieldFloat2(value=value)
            )

    @property
    def label_distance(self) -> np.float32 | None:
        """The LabelDistance field value."""
        member = self.get_member("LabelDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_distance.setter
    def label_distance(self, value: np.float32) -> None:
        """Set the LabelDistance field value."""
        member = self.get_member("LabelDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelDistance", fields.FieldFloat(value=value)
            )

