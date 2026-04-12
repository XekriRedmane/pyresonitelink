"""Generated component: GrabbableReparentBlock."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbableReparentBlock(GeneratedComponent, IGrabbableReparentBlock, IWorldEventReceiver):
    """The GrabbableReparentBlock component makes it so that, if any slot that is a descendant (up to ``MaxDepth`` levels deep) of the current one is grabbed and then let go of, it won't be reparented to this slot.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbableReparentBlock"

    def __init__(self, dont_reparent: primitives.Bool | None = None, max_depth: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
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
    def dont_reparent(self) -> primitives.Bool | None:
        """Don't allow this slot to be reparented to. Subject to the rules explained in Grabbable - Behavior"""
        member = self.get_member("DontReparent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dont_reparent.setter
    def dont_reparent(self, value: primitives.Bool) -> None:
        """Set the DontReparent field value."""
        member = self.get_member("DontReparent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DontReparent", fields.FieldBool(value=value)
            )

    @property
    def max_depth(self) -> primitives.Int | None:
        """Objects beyond this level in the hierarchy will not be effected. Set to Int MaxValue by default"""
        member = self.get_member("MaxDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_depth.setter
    def max_depth(self, value: primitives.Int) -> None:
        """Set the MaxDepth field value."""
        member = self.get_member("MaxDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDepth", fields.FieldInt(value=value)
            )

