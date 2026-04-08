"""Generated component: GrabbableReparentBlock."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableReparentBlock(GeneratedComponent, IGrabbableReparentBlock, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbableReparentBlock.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableReparentBlock"

    def __init__(self, dont_reparent: bool | None = None, max_depth: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dont_reparent: Initial value for DontReparent.
            max_depth: Initial value for MaxDepth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dont_reparent is not None:
            self.dont_reparent = dont_reparent
        if max_depth is not None:
            self.max_depth = max_depth

    @property
    def dont_reparent(self) -> bool | None:
        """The DontReparent field value."""
        member = self.get_member("DontReparent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dont_reparent.setter
    def dont_reparent(self, value: bool) -> None:
        """Set the DontReparent field value."""
        member = self.get_member("DontReparent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DontReparent", fields.FieldBool(value=value)
            )

    @property
    def max_depth(self) -> np.int32 | None:
        """The MaxDepth field value."""
        member = self.get_member("MaxDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_depth.setter
    def max_depth(self, value: np.int32) -> None:
        """Set the MaxDepth field value."""
        member = self.get_member("MaxDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDepth", fields.FieldInt(value=value)
            )

