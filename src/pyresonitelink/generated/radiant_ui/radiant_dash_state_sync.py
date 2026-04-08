"""Generated component: RadiantDashStateSync."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadiantDashStateSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RadiantDashStateSync.

    Category: Radiant UI
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadiantDashStateSync"

    def __init__(self, is_freeform: bool | None = None, is_open: bool | None = None, curvature: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_freeform: Initial value for IsFreeform.
            is_open: Initial value for IsOpen.
            curvature: Initial value for Curvature.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_freeform is not None:
            self.is_freeform = is_freeform
        if is_open is not None:
            self.is_open = is_open
        if curvature is not None:
            self.curvature = curvature

    @property
    def is_freeform(self) -> bool | None:
        """The IsFreeform field value."""
        member = self.get_member("IsFreeform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_freeform.setter
    def is_freeform(self, value: bool) -> None:
        """Set the IsFreeform field value."""
        member = self.get_member("IsFreeform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsFreeform", fields.FieldBool(value=value)
            )

    @property
    def is_open(self) -> bool | None:
        """The IsOpen field value."""
        member = self.get_member("IsOpen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_open.setter
    def is_open(self, value: bool) -> None:
        """Set the IsOpen field value."""
        member = self.get_member("IsOpen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsOpen", fields.FieldBool(value=value)
            )

    @property
    def curvature(self) -> np.float32 | None:
        """The Curvature field value."""
        member = self.get_member("Curvature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @curvature.setter
    def curvature(self, value: np.float32) -> None:
        """Set the Curvature field value."""
        member = self.get_member("Curvature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Curvature", fields.FieldFloat(value=value)
            )

