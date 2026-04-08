"""Generated component: BrowserItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.browser_dialog import BrowserDialog
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BrowserItem(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BrowserItem.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BrowserItem"

    def __init__(self, browser: str | BrowserDialog | None = None, selected_color: primitives.ColorX | None = None, selected_text: primitives.ColorX | None = None, normal_color: primitives.ColorX | None = None, normal_text: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            browser: Initial value for Browser.
            selected_color: Initial value for SelectedColor.
            selected_text: Initial value for SelectedText.
            normal_color: Initial value for NormalColor.
            normal_text: Initial value for NormalText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if browser is not None:
            self.browser = browser
        if selected_color is not None:
            self.selected_color = selected_color
        if selected_text is not None:
            self.selected_text = selected_text
        if normal_color is not None:
            self.normal_color = normal_color
        if normal_text is not None:
            self.normal_text = normal_text

    @property
    def browser(self) -> str | None:
        """Target ID of the Browser reference (targets BrowserDialog)."""
        member = self.get_member("Browser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @browser.setter
    def browser(self, target: str | BrowserDialog | None) -> None:
        """Set the Browser reference by target ID or BrowserDialog instance."""
        target_id: str | None = target.id if isinstance(target, BrowserDialog) else target  # type: ignore[assignment]
        member = self.get_member("Browser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Browser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BrowserDialog'),
            )

    @property
    def selected_color(self) -> primitives.ColorX | None:
        """The SelectedColor field value."""
        member = self.get_member("SelectedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_color.setter
    def selected_color(self, value: primitives.ColorX) -> None:
        """Set the SelectedColor field value."""
        member = self.get_member("SelectedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedColor", fields.FieldColorX(value=value)
            )

    @property
    def selected_text(self) -> primitives.ColorX | None:
        """The SelectedText field value."""
        member = self.get_member("SelectedText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_text.setter
    def selected_text(self, value: primitives.ColorX) -> None:
        """Set the SelectedText field value."""
        member = self.get_member("SelectedText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedText", fields.FieldColorX(value=value)
            )

    @property
    def normal_color(self) -> primitives.ColorX | None:
        """The NormalColor field value."""
        member = self.get_member("NormalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_color.setter
    def normal_color(self, value: primitives.ColorX) -> None:
        """Set the NormalColor field value."""
        member = self.get_member("NormalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalColor", fields.FieldColorX(value=value)
            )

    @property
    def normal_text(self) -> primitives.ColorX | None:
        """The NormalText field value."""
        member = self.get_member("NormalText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_text.setter
    def normal_text(self, value: primitives.ColorX) -> None:
        """Set the NormalText field value."""
        member = self.get_member("NormalText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalText", fields.FieldColorX(value=value)
            )

