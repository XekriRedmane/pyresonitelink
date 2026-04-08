"""Generated component: Facet."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Facet(GeneratedComponent, IGrabEventReceiver, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Facet.

    Category: Radiant UI
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Facet"

    def __init__(self, min_width: np.float32 | None = None, max_width: np.float32 | None = None, min_height: np.float32 | None = None, max_height: np.float32 | None = None, last_placed_size: primitives.Float2 | None = None, is_standalone: bool | None = None, canvas: str | Canvas | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_width: Initial value for MinWidth.
            max_width: Initial value for MaxWidth.
            min_height: Initial value for MinHeight.
            max_height: Initial value for MaxHeight.
            last_placed_size: Initial value for LastPlacedSize.
            is_standalone: Initial value for IsStandalone.
            canvas: Initial value for Canvas.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_width is not None:
            self.min_width = min_width
        if max_width is not None:
            self.max_width = max_width
        if min_height is not None:
            self.min_height = min_height
        if max_height is not None:
            self.max_height = max_height
        if last_placed_size is not None:
            self.last_placed_size = last_placed_size
        if is_standalone is not None:
            self.is_standalone = is_standalone
        if canvas is not None:
            self.canvas = canvas

    @property
    def min_width(self) -> np.float32 | None:
        """The MinWidth field value."""
        member = self.get_member("MinWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_width.setter
    def min_width(self, value: np.float32) -> None:
        """Set the MinWidth field value."""
        member = self.get_member("MinWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinWidth", fields.FieldFloat(value=value)
            )

    @property
    def max_width(self) -> np.float32 | None:
        """The MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_width.setter
    def max_width(self, value: np.float32) -> None:
        """Set the MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxWidth", fields.FieldFloat(value=value)
            )

    @property
    def min_height(self) -> np.float32 | None:
        """The MinHeight field value."""
        member = self.get_member("MinHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_height.setter
    def min_height(self, value: np.float32) -> None:
        """Set the MinHeight field value."""
        member = self.get_member("MinHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinHeight", fields.FieldFloat(value=value)
            )

    @property
    def max_height(self) -> np.float32 | None:
        """The MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_height.setter
    def max_height(self, value: np.float32) -> None:
        """Set the MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxHeight", fields.FieldFloat(value=value)
            )

    @property
    def last_placed_size(self) -> primitives.Float2 | None:
        """The LastPlacedSize field value."""
        member = self.get_member("LastPlacedSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_placed_size.setter
    def last_placed_size(self, value: primitives.Float2) -> None:
        """Set the LastPlacedSize field value."""
        member = self.get_member("LastPlacedSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastPlacedSize", fields.FieldNullableFloat2(value=value)
            )

    @property
    def preferred_sizes(self) -> members.SyncList | None:
        """The PreferredSizes member."""
        member = self.get_member("PreferredSizes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @preferred_sizes.setter
    def preferred_sizes(self, value: members.SyncList) -> None:
        """Set the PreferredSizes member."""
        self.set_member("PreferredSizes", value)

    @property
    def allowed_aspect_ratios(self) -> members.SyncList | None:
        """The AllowedAspectRatios member."""
        member = self.get_member("AllowedAspectRatios")
        if isinstance(member, members.SyncList):
            return member
        return None

    @allowed_aspect_ratios.setter
    def allowed_aspect_ratios(self, value: members.SyncList) -> None:
        """Set the AllowedAspectRatios member."""
        self.set_member("AllowedAspectRatios", value)

    @property
    def is_standalone(self) -> bool | None:
        """The IsStandalone field value."""
        member = self.get_member("IsStandalone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_standalone.setter
    def is_standalone(self, value: bool) -> None:
        """Set the IsStandalone field value."""
        member = self.get_member("IsStandalone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsStandalone", fields.FieldBool(value=value)
            )

    @property
    def canvas(self) -> str | None:
        """Target ID of the Canvas reference (targets Canvas)."""
        member = self.get_member("Canvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas.setter
    def canvas(self, target: str | Canvas | None) -> None:
        """Set the Canvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("Canvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Canvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

