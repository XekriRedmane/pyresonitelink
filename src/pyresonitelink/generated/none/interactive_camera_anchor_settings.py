"""Generated component: InteractiveCameraAnchorSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraAnchorSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraAnchorSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraAnchorSettings"

    def __init__(self, interpolate_between_anchors: primitives.Bool | None = None, anchor_interpolation_speed: primitives.Float | None = None, use_linear_interpolation: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interpolate_between_anchors: Initial value for InterpolateBetweenAnchors.
            anchor_interpolation_speed: Initial value for AnchorInterpolationSpeed.
            use_linear_interpolation: Initial value for UseLinearInterpolation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interpolate_between_anchors is not None:
            self.interpolate_between_anchors = interpolate_between_anchors
        if anchor_interpolation_speed is not None:
            self.anchor_interpolation_speed = anchor_interpolation_speed
        if use_linear_interpolation is not None:
            self.use_linear_interpolation = use_linear_interpolation

    @property
    def interpolate_between_anchors(self) -> primitives.Bool | None:
        """The InterpolateBetweenAnchors field value."""
        member = self.get_member("InterpolateBetweenAnchors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interpolate_between_anchors.setter
    def interpolate_between_anchors(self, value: primitives.Bool) -> None:
        """Set the InterpolateBetweenAnchors field value."""
        member = self.get_member("InterpolateBetweenAnchors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterpolateBetweenAnchors", fields.FieldBool(value=value)
            )

    @property
    def anchor_interpolation_speed(self) -> primitives.Float | None:
        """The AnchorInterpolationSpeed field value."""
        member = self.get_member("AnchorInterpolationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_interpolation_speed.setter
    def anchor_interpolation_speed(self, value: primitives.Float) -> None:
        """Set the AnchorInterpolationSpeed field value."""
        member = self.get_member("AnchorInterpolationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorInterpolationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def use_linear_interpolation(self) -> primitives.Bool | None:
        """The UseLinearInterpolation field value."""
        member = self.get_member("UseLinearInterpolation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_linear_interpolation.setter
    def use_linear_interpolation(self, value: primitives.Bool) -> None:
        """Set the UseLinearInterpolation field value."""
        member = self.get_member("UseLinearInterpolation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLinearInterpolation", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

