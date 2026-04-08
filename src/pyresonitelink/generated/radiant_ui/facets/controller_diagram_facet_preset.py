"""Generated component: ControllerDiagramFacetPreset."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.static_texture_2d import StaticTexture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ControllerDiagramFacetPreset(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ControllerDiagramFacetPreset.

    Category: Radiant UI/Facets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ControllerDiagramFacetPreset"

    def __init__(self, texture: str | StaticTexture2D | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for _texture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture

    @property
    def texture(self) -> str | None:
        """Target ID of the _texture reference (targets StaticTexture2D)."""
        member = self.get_member("_texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | StaticTexture2D | None) -> None:
        """Set the _texture reference by target ID or StaticTexture2D instance."""
        target_id: str | None = target.id if isinstance(target, StaticTexture2D) else target  # type: ignore[assignment]
        member = self.get_member("_texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StaticTexture2D'),
            )

