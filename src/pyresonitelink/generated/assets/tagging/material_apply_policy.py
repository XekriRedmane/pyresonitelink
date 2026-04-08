"""Generated component: MaterialApplyPolicy."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialApplyPolicy(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MaterialApplyPolicy.

    Category: Assets/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialApplyPolicy"

    def __init__(self, can_apply: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            can_apply: Initial value for CanApply.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if can_apply is not None:
            self.can_apply = can_apply

    @property
    def can_apply(self) -> primitives.Bool | None:
        """The CanApply field value."""
        member = self.get_member("CanApply")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_apply.setter
    def can_apply(self, value: primitives.Bool) -> None:
        """Set the CanApply field value."""
        member = self.get_member("CanApply")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CanApply", fields.FieldBool(value=value)
            )

