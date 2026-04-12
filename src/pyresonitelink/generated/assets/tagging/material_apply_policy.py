"""Generated component: MaterialApplyPolicy."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialApplyPolicy(GeneratedComponent, IMaterialApplyPolicy, IWorldEventReceiver):
    """The MaterialApplyPolicy component allows for controlling whether a Material Tool is able to apply a material to the slot hierarchy tagged with this component onto its SkinnedMeshRenderer/MeshRenderer components.

    Category: Assets/Tagging

    **<translate> Usage</translate>**: When this component is added to a Slot with a SkinnedMeshRenderer or MeshRenderer attached, it allows one to limit the effects of the Material Tool.

    **<translate> Examples</translate>**: On an avatar, you can try adding this component to the root of the avatar, making sure the avatar has a ObjectRoot, and set ``CanApply`` to false. Doing this will ensure that the avatar's material cannot be changed by the Material Tool.

Adding this component to the Slot of a MeshRender and setting ``CanApply`` to true can allow one to explicitly change the material in specific places on small objects.

    **<translate> See Also</translate>**: * MeshRenderer
* SkinnedMeshRenderer
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
        """Setting this to false will prevent the Material Tool from applying materials to any SkinnedMeshRenderer/MeshRenderer components in the slot or child slots."""
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

