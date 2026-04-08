"""Generated component: UserspaceFacetAnchor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.ui_unlit_material import UI_UnlitMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceFacetAnchor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserspaceFacetAnchor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceFacetAnchor"

    def __init__(self, background_image: str | Image | None = None, background_material: str | UI_UnlitMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            background_image: Initial value for BackgroundImage.
            background_material: Initial value for BackgroundMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if background_image is not None:
            self.background_image = background_image
        if background_material is not None:
            self.background_material = background_material

    @property
    def point(self) -> members.FieldEnum | None:
        """The Point member."""
        member = self.get_member("Point")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @point.setter
    def point(self, value: members.FieldEnum) -> None:
        """Set the Point member."""
        self.set_member("Point", value)

    @property
    def background_image(self) -> str | None:
        """Target ID of the BackgroundImage reference (targets Image)."""
        member = self.get_member("BackgroundImage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @background_image.setter
    def background_image(self, target: str | Image | None) -> None:
        """Set the BackgroundImage reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("BackgroundImage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BackgroundImage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def background_material(self) -> str | None:
        """Target ID of the BackgroundMaterial reference (targets UI_UnlitMaterial)."""
        member = self.get_member("BackgroundMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @background_material.setter
    def background_material(self, target: str | UI_UnlitMaterial | None) -> None:
        """Set the BackgroundMaterial reference by target ID or UI_UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UI_UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("BackgroundMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BackgroundMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_UnlitMaterial'),
            )

