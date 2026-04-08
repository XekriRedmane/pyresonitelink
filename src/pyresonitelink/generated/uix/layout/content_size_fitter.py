"""Generated component: ContentSizeFitter."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContentSizeFitter(GeneratedComponent, ILayoutElement, IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ContentSizeFitter.

    Category: UIX/Layout
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ContentSizeFitter"

    @property
    def horizontal_fit(self) -> members.FieldEnum | None:
        """The HorizontalFit member."""
        member = self.get_member("HorizontalFit")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @horizontal_fit.setter
    def horizontal_fit(self, value: members.FieldEnum) -> None:
        """Set the HorizontalFit member."""
        self.set_member("HorizontalFit", value)

    @property
    def vertical_fit(self) -> members.FieldEnum | None:
        """The VerticalFit member."""
        member = self.get_member("VerticalFit")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertical_fit.setter
    def vertical_fit(self, value: members.FieldEnum) -> None:
        """Set the VerticalFit member."""
        self.set_member("VerticalFit", value)

