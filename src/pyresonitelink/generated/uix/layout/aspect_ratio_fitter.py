"""Generated component: AspectRatioFitter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AspectRatioFitter(GeneratedComponent, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.AspectRatioFitter.

    Category: UIX/Layout
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.AspectRatioFitter"

    def __init__(self, aspect_ratio: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            aspect_ratio: Initial value for AspectRatio.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio

    @property
    def aspect_ratio(self) -> np.float32 | None:
        """The AspectRatio field value."""
        member = self.get_member("AspectRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aspect_ratio.setter
    def aspect_ratio(self, value: np.float32) -> None:
        """Set the AspectRatio field value."""
        member = self.get_member("AspectRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AspectRatio", fields.FieldFloat(value=value)
            )

