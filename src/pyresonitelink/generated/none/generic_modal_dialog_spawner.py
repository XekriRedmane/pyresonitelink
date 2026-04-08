"""Generated component: GenericModalDialogSpawner."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GenericModalDialogSpawner(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GenericModalDialogSpawner<>.

    Parameterize with a value type::

        GenericModalDialogSpawner[np.float32]
        GenericModalDialogSpawner[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GenericModalDialogSpawner<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.GenericModalDialogSpawner<>"

    def __init__(self, size: primitives.Float2 | None = None, close_on_click: bool | None = None, close_on_context_menu: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            size: Initial value for Size.
            close_on_click: Initial value for CloseOnClick.
            close_on_context_menu: Initial value for CloseOnContextMenu.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if size is not None:
            self.size = size
        if close_on_click is not None:
            self.close_on_click = close_on_click
        if close_on_context_menu is not None:
            self.close_on_context_menu = close_on_context_menu

    @property
    def size(self) -> primitives.Float2 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float2) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat2(value=value)
            )

    @property
    def close_on_click(self) -> bool | None:
        """The CloseOnClick field value."""
        member = self.get_member("CloseOnClick")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_on_click.setter
    def close_on_click(self, value: bool) -> None:
        """Set the CloseOnClick field value."""
        member = self.get_member("CloseOnClick")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseOnClick", fields.FieldBool(value=value)
            )

    @property
    def close_on_context_menu(self) -> bool | None:
        """The CloseOnContextMenu field value."""
        member = self.get_member("CloseOnContextMenu")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_on_context_menu.setter
    def close_on_context_menu(self, value: bool) -> None:
        """Set the CloseOnContextMenu field value."""
        member = self.get_member("CloseOnContextMenu")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseOnContextMenu", fields.FieldBool(value=value)
            )

