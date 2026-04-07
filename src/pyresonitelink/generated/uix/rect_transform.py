"""Generated component: RectTransform."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectTransform(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.RectTransform.

    Category: UIX
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectTransform"

    def __init__(self, anchor_min: primitives.Float2 | None = None, anchor_max: primitives.Float2 | None = None, offset_min: primitives.Float2 | None = None, offset_max: primitives.Float2 | None = None, pivot: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor_min: Initial value for AnchorMin.
            anchor_max: Initial value for AnchorMax.
            offset_min: Initial value for OffsetMin.
            offset_max: Initial value for OffsetMax.
            pivot: Initial value for Pivot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor_min is not None:
            self.anchor_min = anchor_min
        if anchor_max is not None:
            self.anchor_max = anchor_max
        if offset_min is not None:
            self.offset_min = offset_min
        if offset_max is not None:
            self.offset_max = offset_max
        if pivot is not None:
            self.pivot = pivot

    @property
    def anchor_min(self) -> primitives.Float2 | None:
        """The AnchorMin field value."""
        member = self.get_member("AnchorMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_min.setter
    def anchor_min(self, value: primitives.Float2) -> None:
        """Set the AnchorMin field value."""
        member = self.get_member("AnchorMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorMin", fields.FieldFloat2(value=value)
            )

    @property
    def anchor_max(self) -> primitives.Float2 | None:
        """The AnchorMax field value."""
        member = self.get_member("AnchorMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_max.setter
    def anchor_max(self, value: primitives.Float2) -> None:
        """Set the AnchorMax field value."""
        member = self.get_member("AnchorMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorMax", fields.FieldFloat2(value=value)
            )

    @property
    def offset_min(self) -> primitives.Float2 | None:
        """The OffsetMin field value."""
        member = self.get_member("OffsetMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_min.setter
    def offset_min(self, value: primitives.Float2) -> None:
        """Set the OffsetMin field value."""
        member = self.get_member("OffsetMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetMin", fields.FieldFloat2(value=value)
            )

    @property
    def offset_max(self) -> primitives.Float2 | None:
        """The OffsetMax field value."""
        member = self.get_member("OffsetMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_max.setter
    def offset_max(self, value: primitives.Float2) -> None:
        """Set the OffsetMax field value."""
        member = self.get_member("OffsetMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetMax", fields.FieldFloat2(value=value)
            )

    @property
    def pivot(self) -> primitives.Float2 | None:
        """The Pivot field value."""
        member = self.get_member("Pivot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pivot.setter
    def pivot(self, value: primitives.Float2) -> None:
        """Set the Pivot field value."""
        member = self.get_member("Pivot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pivot", fields.FieldFloat2(value=value)
            )

