"""Generated component: DynamicBoneSphereCollider."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idynamic_bone_collider import IDynamicBoneCollider
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBoneSphereCollider(GeneratedComponent, IDynamicBoneCollider, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicBoneSphereCollider.

    Category: Physics/Dynamic Bones
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBoneSphereCollider"

    def __init__(self, radius: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius

    @property
    def radius(self) -> primitives.Float | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

