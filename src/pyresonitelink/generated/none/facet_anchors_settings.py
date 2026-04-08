"""Generated component: FacetAnchorsSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class FacetAnchorsSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.FacetAnchorsSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FacetAnchorsSettings"

    def __init__(self, use_facet_anchors: primitives.Bool | None = None, animation_speed: primitives.Float | None = None, show_container_background: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_facet_anchors: Initial value for UseFacetAnchors.
            animation_speed: Initial value for AnimationSpeed.
            show_container_background: Initial value for ShowContainerBackground.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_facet_anchors is not None:
            self.use_facet_anchors = use_facet_anchors
        if animation_speed is not None:
            self.animation_speed = animation_speed
        if show_container_background is not None:
            self.show_container_background = show_container_background

    @property
    def use_facet_anchors(self) -> primitives.Bool | None:
        """The UseFacetAnchors field value."""
        member = self.get_member("UseFacetAnchors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_facet_anchors.setter
    def use_facet_anchors(self, value: primitives.Bool) -> None:
        """Set the UseFacetAnchors field value."""
        member = self.get_member("UseFacetAnchors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFacetAnchors", fields.FieldBool(value=value)
            )

    @property
    def facet_anchor_toggle(self) -> members.FieldEnum | None:
        """The FacetAnchorToggle member."""
        member = self.get_member("FacetAnchorToggle")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @facet_anchor_toggle.setter
    def facet_anchor_toggle(self, value: members.FieldEnum) -> None:
        """Set the FacetAnchorToggle member."""
        self.set_member("FacetAnchorToggle", value)

    @property
    def animation_speed(self) -> primitives.Float | None:
        """The AnimationSpeed field value."""
        member = self.get_member("AnimationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_speed.setter
    def animation_speed(self, value: primitives.Float) -> None:
        """Set the AnimationSpeed field value."""
        member = self.get_member("AnimationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def show_container_background(self) -> primitives.Bool | None:
        """The ShowContainerBackground field value."""
        member = self.get_member("ShowContainerBackground")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_container_background.setter
    def show_container_background(self, value: primitives.Bool) -> None:
        """Set the ShowContainerBackground field value."""
        member = self.get_member("ShowContainerBackground")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowContainerBackground", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

