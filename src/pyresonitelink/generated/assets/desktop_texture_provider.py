"""Generated component: DesktopTextureProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopTextureProvider(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """The DesktopTextureProvider component only works in user space. This component is an ITexture2D and can be used as a texture. This texture is able to display what is on any particular monitor on a user's machine. This component is commonly used in the desktop tab on a user's Dash.

    Category: Assets

    This should not be used by the user, but it could be used to make a
    special facet. Insert the component into a texture field on a material
    to display it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopTextureProvider"

    def __init__(self, display_index: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            display_index: Initial value for DisplayIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if display_index is not None:
            self.display_index = display_index

    @property
    def display_index(self) -> primitives.Int | None:
        """What monitor to get image data for."""
        member = self.get_member("DisplayIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_index.setter
    def display_index(self, value: primitives.Int) -> None:
        """Set the DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayIndex", fields.FieldInt(value=value)
            )

