"""Generated component: Facet."""

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
    """The Facet Component is the component that drives every user made facet in the game. This component specifically handles the sizes in which a facet can/can't, and prefers to be placed. It also reports the last size a facet was placed, the aspect ratio sizes it can be placed, and the Canvas that makes up the facet's contents.

When being placed into a spot, this facet finds the closest one of ``PreferredSizes`` that can be used while still fitting and automatically makes it the size when dropped in that spot. This only triggers if the user is just dropping it on their dash, as opposed to drag clicking the facet in.

    Category: Radiant UI
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Facet"

    def __init__(self, min_width: primitives.Float | None = None, max_width: primitives.Float | None = None, min_height: primitives.Float | None = None, max_height: primitives.Float | None = None, last_placed_size: primitives.Float2 | None = None, is_standalone: primitives.Bool | None = None, canvas: str | Canvas | None = None, *, component: workers.Component | None = None) -> None:
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
    def min_width(self) -> primitives.Float | None:
        """The minimum width this facet can be."""
        member = self.get_member("MinWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_width.setter
    def min_width(self, value: primitives.Float) -> None:
        """Set the MinWidth field value."""
        member = self.get_member("MinWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinWidth", fields.FieldFloat(value=value)
            )

    @property
    def max_width(self) -> primitives.Float | None:
        """The maximum width this facet can be."""
        member = self.get_member("MaxWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_width.setter
    def max_width(self, value: primitives.Float) -> None:
        """Set the MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxWidth", fields.FieldFloat(value=value)
            )

    @property
    def min_height(self) -> primitives.Float | None:
        """The minimum height this facet can be."""
        member = self.get_member("MinHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_height.setter
    def min_height(self, value: primitives.Float) -> None:
        """Set the MinHeight field value."""
        member = self.get_member("MinHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinHeight", fields.FieldFloat(value=value)
            )

    @property
    def max_height(self) -> primitives.Float | None:
        """The maximum height this facet can be."""
        member = self.get_member("MaxHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_height.setter
    def max_height(self, value: primitives.Float) -> None:
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
        """The last size that this Facet was placed as."""
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
        """A list of sizes this canvas prefers to be placed when being dropped onto a facet holder."""
        member = self.get_member("PreferredSizes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @preferred_sizes.setter
    def preferred_sizes(self, value: members.SyncList) -> None:
        """Set PreferredSizes. A list of sizes this canvas prefers to be placed when being dropped onto a facet holder."""
        self.set_member("PreferredSizes", value)

    @property
    def allowed_aspect_ratios(self) -> members.SyncList | None:
        """A list of allowed ratios between width and height this facet allows when being placed, lest the placement guide turns red and prevents placement."""
        member = self.get_member("AllowedAspectRatios")
        if isinstance(member, members.SyncList):
            return member
        return None

    @allowed_aspect_ratios.setter
    def allowed_aspect_ratios(self, value: members.SyncList) -> None:
        """Set AllowedAspectRatios. A list of allowed ratios between width and height this facet allows when being placed, lest the placement guide turns red and prevents placement."""
        self.set_member("AllowedAspectRatios", value)

    @property
    def is_standalone(self) -> primitives.Bool | None:
        """Whether this facet has not been placed in a dash or otherwise and is out in free form space."""
        member = self.get_member("IsStandalone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_standalone.setter
    def is_standalone(self, value: primitives.Bool) -> None:
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
        """The canvas being used for the visuals of this Facet."""
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

