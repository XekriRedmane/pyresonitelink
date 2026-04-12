"""Generated component: UserspaceFacetAnchor."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.facet_anchor_point import FacetAnchorPoint
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.ui_unlit_material import UI_UnlitMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceFacetAnchor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserspaceFacetAnchor component is used to control the user facet anchors on the head, hands, and arms of the user in user space.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceFacetAnchor"

    def __init__(self, point: FacetAnchorPoint | str | None = None, background_image: str | Image | None = None, background_material: str | UI_UnlitMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point: Initial value for Point.
            background_image: Initial value for BackgroundImage.
            background_material: Initial value for BackgroundMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point is not None:
            self.point = point
        if background_image is not None:
            self.background_image = background_image
        if background_material is not None:
            self.background_material = background_material

    @property
    def point(self) -> FacetAnchorPoint | None:
        """The facet anchor point to follow."""
        member = self.get_member("Point")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return FacetAnchorPoint(member.value)
        return None

    @point.setter
    def point(self, value: FacetAnchorPoint | str) -> None:
        """Set Point. The facet anchor point to follow."""
        member = self.get_member("Point")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Point",
                members.FieldEnum(value=str(value)),
            )

    @property
    def background_image(self) -> str | None:
        """The image used for the canvas background."""
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
        """The material used for the canvas background."""
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

